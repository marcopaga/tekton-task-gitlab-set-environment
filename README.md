# tekton-task-gitlab-set-environment

This python code is intended to be used within a tekton task.  Check out the implementation at[codecentric/tekton-catalog/tree/main/task/gitlab-set-environment/0.1](https://github.com/codecentric/tekton-catalog/tree/main/task/gitlab-set-environment/0.1).
The code can be configured using environment variables which are listed below.

## Environment Parameters

| Environment Key | Description                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------|
|GITLAB_HOST_URL  | Full URL to the gitlab instance e.g. https://gitlab.marco-paga.eu                                |
|REPO_FULL_NAME   | group-name/project-name                                                                          |
|GITLAB_TOKEN     | The access token for the gitlab instance (currently on PAT supported here)                       |
|ENVIRONMENT_NAME | The short name of the environment. This could be simply the branch name                          |
|ENVIRONMENT_URL  | Full URL to the environment that can be navigated. e.g. https://feature-branch.dev.marco-paga.eu |

## Development

This task uses [python-gitlab](https://python-gitlab.readthedocs.io/en/stable/#) to connect to the gitlab api and run the intended actions.
The code is placed in the `main.py` and versions are managed by [Pipfile](https://github.com/pypa/pipfile).

Renovate is active for this repository and keeps the versions updated.