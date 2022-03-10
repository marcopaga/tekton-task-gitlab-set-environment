# tekton-task-gitlab-set-environment

This python code is intended to be used within a tekton task.
The code can be configured using environment variables.

## Environment Parameters

| Environment Key | Description                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------|
|GITLAB_HOST_URL  | Full URL to the gitlab instance e.g. https://gitlab.marco-paga.eu                                |
|REPO_FULL_NAME   | group-name/project-name                                                                          |
|GITLAB_TOKEN     | The access token for the gitlab instance (currently on PAT supported here)                       |
|ENVIRONMENT_NAME | The short name of the environment. This could be simply the branch name                          |
|ENVIRONMENT_URL  | Full URL to the environment that can be navigated. e.g. https://feature-branch.dev.marco-paga.eu |