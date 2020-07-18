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
license_template = os.environ.get("LICENSE")
t_owner = os.environ.get("T_OWNER")
t_repo = os.environ.get("T_REPO")
wh_url = os.environ.get("WH_URL")
organization = os.environ.get("ORGANIZATION")
wh_events = json.loads(os.environ.get("WH_EVENTS"))
#------------------------------------------------------------------------

url = "https://api.github.com/"
headers = {
    'Authorization': 'token ' + token,
    'Accept': 'application/vnd.github.baptiste-preview+json'
}
num = int(input("Number of respositories to be generated: "))
for i in range(num):
    headers['Accept'] =  "application/vnd.github.baptiste-preview+json"
    params = {}
    name = str(input("Name of repository #{}: ".format(i+1)))
    params['name'] = name 
    params['description'] = str(input("Description of repository #{}: ".format(i+1)))
    p = requests.post(url + 'repos/' + t_owner + '/' + t_repo + '/generate', data=json.dumps(params), headers=headers)
    if p.status_code != 201:
        print("Error! Repository could not be created.")
        print("Error Code:",p.status_code)
        continue
    headers.pop("Accept")
    whpar = {}
    config = {}
    whpar['events'] = wh_events
    config['url'] = wh_url
    whpar['config'] = config
    p = requests.post(url + 'repos/' + username + '/' + name + '/hooks', data=json.dumps(whpar), headers=headers)
    if p.status_code != 201:
        print("Error! Webhook could not be created.")
        print("Error Code:",p.status_code)
    tfrparams = {}
    tfrparams['new_owner'] = organization
    p = requests.post(url + 'repos/' + username + '/' + name + '/transfer', data=json.dumps(tfrparams), headers=headers)
    if p.status_code != 202:
        print("Error! Repository could not be transferred to the organization.")
        print("Error Code:",p.status_code)
    print("Success! {} has been created successfully.".format(name))