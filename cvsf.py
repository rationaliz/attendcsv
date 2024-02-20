import csv
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Path to the service account key file
SERVICE_ACCOUNT_FILE = r"C:\Users\anany\Downloads\attendify-414918-ab19dbf77161.json"

# The ID of the folder you want to share
FOLDER_ID = '10RPfdbCSgYM3X367v7C2X0mbUO7DBcmR'

# The role to grant (e.g., 'reader', 'writer', 'commenter')
ROLE = 'reader'

# Authenticate and create a service object
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=['https://www.googleapis.com/auth/drive'])
service = build('drive', 'v3', credentials=credentials)

# Function to read the CSV file and extract email addresses
def read_email_addresses(csv_file):
    email_addresses = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Assuming the email is in the first column
            email = row[0]
            email_addresses.append(email)
    return email_addresses

# Path to the CSV file containing the list of email addresses
CSV_FILE = r"C:\Users\anany\Downloads\attendify_nirmaan.csv"

# Read the email addresses from the CSV file
email_addresses = read_email_addresses(CSV_FILE)

# Iterate over the email addresses and share the folder with each email address
for email in email_addresses:
    try:
        # Create the permission
        permission = {
            'type': 'user',
            'role': ROLE,
            'emailAddress': email
        }

        # Share the folder
        result = service.permissions().create(
            fileId=FOLDER_ID,
            body=permission,
            fields='id'
        ).execute()

        print(f'Successfully shared folder with {email}')
    except HttpError as error:
        print(f'An error occurred: {error}')
