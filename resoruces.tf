import json

def auth0_organization(client_display_name, client_name):

    org_display_name = client_display_name
    org_name = client_name #org_display_name.replace(' ', '-')
    
    organization_template = f'''
resource "auth0_organization" "{org_name}" {{
  name         = "{org_name}"
  display_name = "{org_display_name}"
  metadata = {{
    client_id = "dummyClientIDTest"
  }}
}}
  '''
    return organization_template
    
def auth0_application_m2m(client_display_name, client_name):
    application_m2m_template = '''
resource "auth0_client" "{}" {{
  name                     = "{}"
  app_type                 = "non_interactive"
  grant_types              = ["client_credentials"]
  client_metadata = {{
    client_id = "dummyClientIDTest"
  }}
}}  
'''.format(client_name, client_display_name)

    return application_m2m_template
    
def auth0_create_client_file(client_display_name, client_name):
    client_file_content = auth0_application_m2m(client_display_name, client_name)
    
    file_content = f'''
resource "auth0_organization" "{client_name}" {{
  name         = "{client_name}"
  display_name = "{client_display_name}"
}}

{client_file_content}
'''
    return file_content
    
