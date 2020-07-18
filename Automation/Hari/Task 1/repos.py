import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests
import json

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#------------------------------------------------------------------------
username = os.environ.get("GITHUB_USERNAME")
token = os.environ.get("GITHUB_TOKEN")
#------------------------------------------------------------------------

headers = {
    'Authorization': 'token ' + token,
    'Accept': 'application/vnd.github.baptiste-preview+json'
}
params = {}

url = "https://api.github.com/"

print(username)
print(token)
cf = 0
while(cf==0):
    choice = int(input('''Choose:
    1. Create a new repository
    2. Create a new repository using a template repository
    Choice: '''))
    if choice != 1 and choice !=2:
        print("Invalid choice, choose between 1 and 2.")
        cf = 0
    else:
        cf = 1

name = str(input("Name of the repository: "))
params['name'] = name 
params['description'] = str(input("Description of the repository: "))
visibility =  str(input("Is the repository 'public' or 'private': ")).lower()
if visibility == "private":
    params['private'] = True
else:
    params['private'] = False

if choice == 1:
    lic_op = str(input("Add a license? (y/N) "))
    if lic_op.lower() == "y":
        params['license_template'] = str(input("License keyword: ")).lower()
    rm_op = str(input("Initialize empty README? (y/N): "))
    if rm_op.lower() == "y":
        params['auto_init'] = True
    p = requests.post(url + 'user/repos', data=json.dumps(params), headers=headers)
    
else:
    headers['Accept'] = "application/vnd.github.baptiste-preview+json"    
    t_owner = str(input("Username of the template repository's owner: "))
    t_repo = str(input("Name of the template repository: "))
    params['owner'] = t_owner
    p = requests.post(url + 'repos/' + t_owner + '/' + t_repo + '/generate', data=json.dumps(params), headers=headers)

if p.status_code == 201:
    print("Success! The repo has been generated.")
    headers.pop("Accept")
else:
    print("Error! Repository could not be generated.")
    print("Error Code:",p.status_code)
    exit()

wh_op = str(input("Create a webhook? (y/N): "))
if wh_op.lower() == "y":
    whpar = {}
    config = {}
    whpar['events'] = [
        "push",
        "pull_request"
    ]
    config['url'] = str(input("Webhook URL:"))
    whpar['config'] = config
    p = requests.post(url + 'repos/' + username + '/' + name + '/hooks', data=json.dumps(whpar), headers=headers)
    if p.status_code == 201:
        print("Success! The hook has been created.")
    else:
        print("Error! The hook could not be created.")
        print("Error Code:",p.status_code)

tfr_op = str(input("Transfer repository to an organization? (y/N): "))
if tfr_op.lower() == "y":
    organization = str(input("Enter the name of the organization: "))
    tfrparams = {}
    tfrparams['new_owner'] = organization
    p = requests.post(url + 'repos/' + username + '/' + name + '/transfer', data=json.dumps(tfrparams), headers=headers)
    if p.status_code == 202:
        print("Success! The repository has been transferred to {}.".format(organization))
    else:
        print("Error! The repository could not be transferred.")
        print("Error Code:",p.status_code)
