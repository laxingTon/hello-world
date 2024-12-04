Traceback (most recent call last):
  File "/home/lekshmanan/lax.py", line 97, in <module>
    main()
  File "/home/lekshmanan/lax.py", line 88, in main
    applications = get_project_type_from_repo(args.repo_name, args.branch)
  File "/home/lekshmanan/lax.py", line 52, in get_project_type_from_repo
    items = git_client.get_items(
TypeError: get_items() got an unexpected keyword argument 'continuation_token'
