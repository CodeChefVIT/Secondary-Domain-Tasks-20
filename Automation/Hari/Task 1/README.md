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
The scripts use the `requests` library, so run this command.
```pip install requests```

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
Fill the variables in the scripts with your credentials.
```
username = "Your GitHub username"
token = "Youe GitHub personal access token"
t_owner = "Template repository's owner"
t_repo = "Template repository"
wh_events = "Webhook permissions, ["push","pull_request"] is the default"
wh_url = "Webhook URL"
organization = "Organization's username"
```
Check `licenses.txt` out for license keywords, if you want to add a license.
