import os

from niklibrary.git.GitlabManager import GitLabManager
from dotenv import load_dotenv

load_dotenv()
# print(Assets.get("apktool_2.10.0.jar"))
gitlab_manager = GitLabManager(private_token=os.environ.get('GITLAB_TOKEN', ''))
gitlab_manager.get_oem_project("caiman", 15)