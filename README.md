Traceback (most recent call last):
  File "/home/lekshmanan/lax.py", line 86, in <module>
    main()
  File "/home/lekshmanan/lax.py", line 77, in main
    applications = get_project_type_from_repo(args.repo_name, args.branch)
  File "/home/lekshmanan/lax.py", line 48, in get_project_type_from_repo
    items = git_client.get_items(
  File "/home/lekshmanan/.local/lib/python3.9/site-packages/azure/devops/v7_0/git/git_client_base.py", line 927, in get_items
    if version_descriptor.version_type is not None:
AttributeError: 'dict' object has no attribute 'version_type'
