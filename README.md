Traceback (most recent call last):
  File "/home/lekshmanan/lax.py", line 93, in <module>
    main()
  File "/home/lekshmanan/lax.py", line 84, in main
    applications = get_project_type_from_repo(args.repo_name, args.branch)
  File "/home/lekshmanan/lax.py", line 55, in get_project_type_from_repo
    items = git_client.get_items(
  File "/home/lekshmanan/.local/lib/python3.9/site-packages/azure/devops/v7_0/git/git_client_base.py", line 933, in get_items
    response = self._send(http_method='GET',
  File "/home/lekshmanan/.local/lib/python3.9/site-packages/azure/devops/client.py", line 104, in _send
    response = self._send_request(request=request, headers=headers, content=content, media_type=media_type)
  File "/home/lekshmanan/.local/lib/python3.9/site-packages/azure/devops/client.py", line 68, in _send_request
    self._handle_error(request, response)
  File "/home/lekshmanan/.local/lib/python3.9/site-packages/azure/devops/client.py", line 270, in _handle_error
    raise AzureDevOpsServiceError(wrapped_exception)
azure.devops.exceptions.AzureDevOpsServiceError: A project name is required in order to reference a Git repository by name.
