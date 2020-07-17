import requests
import json
#------------------------------------------------------------------------
username = ""
token = ""
license_template = ""
t_owner = ""
t_repo = ""
wh_events = ["push","pull_request"]
wh_url = ""
organization = ""
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
        print(p.status_code)
        continue
    tfrparams = {}
    tfrparams['new_owner'] = organization
    p = requests.post(url + 'repos/' + username + '/' + name + '/transfer', data=json.dumps(tfrparams), headers=headers)
    if p.status_code != 202:
        print("Error! Repository could not be transferred to the organization.")
        continue
    print("Success! {} has been created successfully.".format(name))