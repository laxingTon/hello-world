import requests
import logging
import json
from typing import List, Tuple, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')  # Custom format to remove INFO:__main__:
logger = logging.getLogger(__name__)

# Custom exception for API errors
class APIError(Exception):
    pass

def load_config(filepath: str) -> dict:
    """Load configuration from a JSON file."""
    with open(filepath, 'r') as file:
        return json.load(file)

def fetch_targets(org_id: str, api_token: str, targets_list: List[str]) -> Optional[List[str]]:
    """Fetch matching target IDs from the Snyk API."""
    url = f"https://api.snyk.io/rest/orgs/{org_id}/targets?version=2024-09-04"
    headers = {
        "Content-Type": "application/vnd.api+json",
        "Authorization": f"token {api_token}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        logger.error(f"Error fetching targets: {response.status_code}, {response.text}")
        raise APIError("Failed to fetch targets")

    data = response.json()
    targets = [(target['id'], target['attributes']['display_name']) for target in data['data']]
    matching_target_ids = [target[0] for target in targets if target[1] in targets_list]
    return matching_target_ids

def fetch_project_info(org_id: str, project_id: str, api_token: str) -> Optional[dict]:
    """Fetch project information from the Snyk API."""
    url = f"https://api.snyk.io/rest/orgs/{org_id}/projects/{project_id}?version=2024-09-04"
    headers = {
        "Content-Type": "application/vnd.api+json",
        "Authorization": f"token {api_token}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        logger.error(f"Error fetching project info: {response.status_code}, {response.text}")
        raise APIError("Failed to fetch project info")

    data = response.json()
    project_info = {
        "project_name": data['data']['attributes']['name'],
        "target_id": data['data']['relationships']['target']['data']['id']
    }
    return project_info

def fetch_issues(org_id: str, api_token: str) -> List[Tuple[str, str, str]]:
    """Fetch issues from the Snyk API."""
    url = f"https://api.snyk.io/rest/orgs/{org_id}/issues?version=2024-09-04&effective_severity_level=critical%2Chigh"
    headers = {
        "Content-Type": "application/vnd.api+json",
        "Authorization": f"token {api_token}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        logger.error(f"Error fetching issues: {response.status_code} - {response.text}")
        raise APIError("Failed to fetch issues")

    data = response.json()
    return [(issue['id'], issue['attributes']['title'], issue['relationships']['scan_item']['data']['id'])
            for issue in data['data'] if issue['type'] == 'issue']

def check_high_critical_issues(org_id: str, api_token: str, targets_list: List[str]) -> str:
    """Check for high/critical issues in specified targets."""
    try:
        matching_target_ids = fetch_targets(org_id, api_token, targets_list)
        if not matching_target_ids:
            return "No matching targets found."

        issues = fetch_issues(org_id, api_token)
        for issue_id, title, project_id in issues:
            project_info = fetch_project_info(org_id, project_id, api_token)
            if project_info and project_info['target_id'] in matching_target_ids:
                return "High/Critical Issue found for provided targets"

        return "No high/critical issues found for provided targets"
    except APIError as e:
        return str(e)

if __name__ == "__main__":
    # Load configuration
    config = load_config('config.json')  # Replace with your config file path
    org_id = config['org_id']
    api_token = config['api_token']
    targets_list = config['targets_list']

    message = check_high_critical_issues(org_id, api_token, targets_list)
    logger.info(message)