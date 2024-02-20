import csv

# Path to the CSV file containing the list of email addresses
CSV_FILE = r"C:\Users\anany\Downloads\attendify_nirmaan.csv"


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

# Call the function and print the extracted email addresses
email_addresses = read_email_addresses(CSV_FILE)
print("Email addresses extracted from the CSV file:")
for email in email_addresses:
    print(email)
