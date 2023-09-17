import csv

# List of names and phone numbers
contacts = [
    {"Name": "John Smith", "Phone": "(518) 625-9017"},
    {"Name": "David Jones", "Phone": "(860) 293-0292"},
    {"Name": "Michael Johnson", "Phone": "(719) 421-7400"},
    {"Name": "Chris Lee", "Phone": "(857) 273-3103"},
    {"Name": "Mike Brown", "Phone": "(919) 767-8175"},
    {"Name": "Mark Williams", "Phone": "(310) 549-9319"},
    {"Name": "Paul Rodriguez", "Phone": "(770) 359-8588"},
    {"Name": "Eric Ferguson", "Phone": "(626) 672-9887"},
]

# Specify the CSV file path
csv_file = "contacts.csv"

# Write contacts to the CSV file
with open(csv_file, mode="w", newline="") as file:
    fieldnames = ["Name", "Phone"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for contact in contacts:
        writer.writerow(contact)

print(f"Contacts saved to {csv_file}")
