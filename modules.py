import requests
import base64
from resources import *

class GitHub:
    def __init__(self):
        self.usuario = 'YOUR_GITHUB_USERNAME'
        self.token = 'YOUR_GITHUB_TOKEN'
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'token {self.token}'
        }

    def get_file_content(self, url):
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()  # Raise and exception for HTTP Errors
        content = response.json()['content']
        decoded_content = base64.b64decode(content).decode('utf-8')
        return decoded_content

    def create_commit(self, new_branch_from_jira, client_name, client_display_name, jira_request, data ):
        url = 'https://api.github.com/repos/YOUR_REPOSITORY_URL/contents/'
        new_file = None
        
        if jira_request == 'YOUR_JIRA_REQUEST_NAME':
            new_content = auth0_create_client_file(client_display_name, client_name)
            new_file = f'{client_name}.tf'
        else:
            raise Exception(f'Unknown request: {jira_request}')
    
    
        # Create a new file
        payload = {
            "message": "",
            "content": base64.b64encode(new_content.encode('utf-8')).decode('utf-8'),
            "path": new_file,
            "branch": new_branch_from_jira
        }
    
        try:
            response = requests.put(url + new_file, json=payload, headers=self.headers)
            response.raise_for_status()
    
            return True
        except Exception as e:
            raise Exception(f'Error while creating commit: {str(e)}')


    def create_pull_request(self, new_branch_from_jira, client_name):
        url = f'https://api.github.com/repos/YOUR_REPOSITORY_URL/pulls'

        payload = {
            'title': 'New Organization ' + client_name + ' Added.',
            'head': new_branch_from_jira,
            'base': 'develop',
            'body': 'MESSAGE_YOU_WANT_FOR_YOUR_PULL_REQUESTS',
            'auto_merge': False
        }

        try:
            response = requests.post(url, json=payload, headers=self.headers)
            response.raise_for_status()
            return True
        except Exception as e:
            raise Exception(f'Error while creating Pull Request: {str(e)}')
