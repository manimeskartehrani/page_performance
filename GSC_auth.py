import argparse
import httplib2
from googleapiclient.discovery import build
from oauth2client import client
from oauth2client import file
from oauth2client import tools

def authorize_creds(creds, site_short_name):
    print('Authorizing Creds')
    # Variable parameter that controls the set of resources that the access token permits.
    SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly'] 

    # Path to client_secrets.json file

    CLIENT_SECRETS_PATH = creds

# Create a parser to be able to open browser for Authorization
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[tools.argparser])
    flags = parser.parse_args([])

# Creates an authorization flow from a clientsecrets file.
# Will raise InvalidClientSecretsError for unknown types of Flows.
    
    flow = client.flow_from_clientsecrets(
        CLIENT_SECRETS_PATH, scope = SCOPES,
        message = tools.message_if_missing(CLIENT_SECRETS_PATH))

# Prepare credentials and authorize HTTP
# If they exist, get them from the storage object
# credentials will get written back to the 'authorizedcreds.dat' file.
    storage = file.Storage('./credential/GSC/authorizedcreds_'+f'{site_short_name}.dat')
    credential = storage.get()
    
    if credential is None or credential.invalid:
        credential = tools.run_flow(flow, storage, flags) 

    # Take the credentials and authorize them using httplib2   
    http = httplib2.Http()                                      # Creates an HTTP client object to make the http request
    http = credential.authorize(http=http)                     # Sign each request from the HTTP client with the OAuth 2.0 access token
    webmasters_service = build('searchconsole', 'v1', http=http)   # Construct a Resource to interact with the API using the Authorized HTTP Client.

    print('Auth Successful')
    return webmasters_service