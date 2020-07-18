# Repo-Generator
Create repositories quickly with these Python scripts. <br>
`repos.py` creates repositories individually. <br>
`bulk_repos.py` creates repositories in bulk with the requirements set beforehand (using a template repository).

## Features
- Create personal or organization repositories.
- Create a fresh repository or a repository through a template.
- Add descriptions for the repositories.
- Add licenses and READMEs.
- Add webhooks.

## Requirements
Clone this repository and navigate to this folder.
The scripts use the `requests` and the `python-dotenv` libraries, so run this command. <br>
```pip install requests python-dotenv```

## Setup
Create a personal access token as specified [here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).
Give the following permissions:
```
repo
admin:org
admin:repo_hook
admin:org_hook
delete_repo
```
Fill the variables in the `.env` file with your credentials.
```
GITHUB_USERNAME = "Your GitHub username"
GITHUB_TOKEN = "Youe GitHub personal access token"
LICENSE = "License template, as given in licenses.txt"
T_OWNER = "Template repository's owner"
T_REPO = "Template repository"
WH_EVENTS = "Webhook permissions, ["push","pull_request"] is the default"
WH_URL = "Webhook URL"
ORGANIZATION = "Organization's username"
```
Check `licenses.txt` out for license keywords, if you want to add a license.
