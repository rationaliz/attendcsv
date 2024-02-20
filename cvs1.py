from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to the service account key file
SERVICE_ACCOUNT_FILE = r"C:\Users\anany\Downloads\attendify-414918-ab19dbf77161.json"

# Authenticate and create a service object
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=['https://www.googleapis.com/auth/drive'])
service = build('drive', 'v3', credentials=credentials)

# Now you can use the 'service' object to interact with the Google Drive API
