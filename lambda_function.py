import json
import requests
import base64
from resources import *
from modules import GitHub

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])

        jira_request = data["fields"]["issuetype"]["name"].strip().lower().replace(' ', '-')
        print(solicitud)

        github = GitHub()

        if jira_request == 'THE_NAME_OF_YOUR_JIRA_REQUEST':
            jira_key = data.get("key")
            jira_field_display_name = data["fields"].get("customfield_XXXXX")
            new_branch_from_jira = "{}-{}".format(jira_key, jira_field_display_name) if jira_key and jira_field_display_name else None

            client_name = data["fields"].get("customfield_XXXXX")
            client_display_name =  data["fields"].get("customfield_XXXXX")
            
            if github.create_commit(new_branch_from_jira, client_name, client_display_name, solicitud, data):
                if github.create_pull_request(new_branch_from_jira, client_name):
                    return {
                        'statusCode': 200,
                        'body': json.dumps('Commit y Pull Request created successfully!')
                    }
                else:
                    return {
                        'statusCode': 400,
                        'body': json.dumps('Error creaeting Pull Request')
                    }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Error creating Commit')
                }
      
        else:
            return {
                'statusCode': 400,
                'body': json.dumps(f'Unknown request: {data["fields"]["issuetype"]["name"]}')
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Internal Server Error: {str(e)}')
        }
