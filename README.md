Traceback (most recent call last):
  File "/home/lekshmanan/chad.py", line 96, in <module>
    main()
  File "/home/lekshmanan/chad.py", line 87, in main
    applications = get_project_type_from_repo(args.project_name, args.repo_name, args.branch)
  File "/home/lekshmanan/chad.py", line 76, in get_project_type_from_repo
    yaml_content = content.decode('utf-8')
AttributeError: 'generator' object has no attribute 'decode'
