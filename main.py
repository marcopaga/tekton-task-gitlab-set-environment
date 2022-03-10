#         - name: "GITLAB_HOST_URL"
#           value: "$(params.GITLAB_HOST)"
#         - name: "REPO_FULL_NAME"
#           value: "$(params.REPO_PATH_ONLY)"
#         - name: "GITLAB_TOKEN_SECRET_NAME"
#           value: "gitlab-api-secret"
#         - name: "GITLAB_TOKEN_SECRET_KEY"
#           value: "token"
#
import sys
import os
import gitlab

GITLAB_HOST_URL = os.getenv("GITLAB_HOST_URL")
REPO_FULL_NAME = os.getenv("REPO_FULL_NAME")
GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")
ENVIRONMENT_NAME = os.getenv("ENVIRONMENT_NAME")
ENVIRONMENT_URL = os.getenv("ENVIRONMENT_URL")

gl = gitlab.Gitlab(GITLAB_HOST_URL, private_token=GITLAB_TOKEN)

try:
    gl.projects.get(REPO_FULL_NAME)
except:
    sys.exit('Supplied project "{0}" could not be found.'.format(REPO_FULL_NAME))

environments = gl.projects.get(REPO_FULL_NAME).environments

exists_environment = [env for env in environments.list() if (env.name == ENVIRONMENT_NAME)]
if(exists_environment):
    print('🚀 Existing environment {0} modified'.format(ENVIRONMENT_NAME))
    environment = exists_environment[0]
    environment.external_url = ENVIRONMENT_URL
    environment.save()
else:
    print('🚀 New environment {0} created'.format(ENVIRONMENT_NAME))
    new_environment = environments.create({'name':ENVIRONMENT_NAME})
    new_environment.external_url= ENVIRONMENT_URL
    new_environment.save()