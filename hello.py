from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Path to the service account key file
SERVICE_ACCOUNT_FILE = r"C:\Users\anany\Downloads\attendify-414918-ab19dbf77161.json"


# The ID of the folder you want to share
FOLDER_ID = '10RPfdbCSgYM3X367v7C2X0mbUO7DBcmR'

# The email address of the service account
SERVICE_ACCOUNT_EMAIL = 'attendify@attendify-414918.iam.gserviceaccount.com'

# The role to grant (e.g., 'reader', 'writer', 'commenter')
ROLE = 'reader'

# Authenticate and create a service object
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=['https://www.googleapis.com/auth/drive'])
service = build('drive', 'v3', credentials=credentials)

# Create the permission
permission = {
    'type': 'user',
    'role': ROLE,
    'emailAddress': SERVICE_ACCOUNT_EMAIL
}

# Share the folder
try:
    result = service.permissions().create(
        fileId=FOLDER_ID,
        body=permission,
        fields='id'
    ).execute()

    print(f'Successfully shared folder with {SERVICE_ACCOUNT_EMAIL}')
except HttpError as error:
    print(f'An error occurred: {error}')
