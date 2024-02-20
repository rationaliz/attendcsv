from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to the service account key file
SERVICE_ACCOUNT_FILE = r"C:\Users\anany\Downloads\attendify-414918-ab19dbf77161.json"

# Authenticate and create a service object
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=['https://www.googleapis.com/auth/drive'])
service = build('drive', 'v3', credentials=credentials)

# The name of the folder you want to find
FOLDER_NAME = 'ATTENDIFY'

# Query to search for the folder by name
query = f"name='{FOLDER_NAME}' and mimeType='application/vnd.google-apps.folder' and trashed = false"

# Use the service object to find the folder
results = service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
items = results.get('files', [])

if not items:
    print(f"No folder named '{FOLDER_NAME}' found.")
else:
    print(f"Folder named '{FOLDER_NAME}' found:")
    for item in items:
        print(f"{item['name']} ({item['id']})")
