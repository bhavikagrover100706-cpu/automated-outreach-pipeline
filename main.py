from prospeo import get_contacts, get_email
from brevo import send_email

domain = input("Enter the company domain: ")

contacts = get_contacts(domain)

for contact in contacts[:3]:
    person_id = contact["person"]["person_id"]

    email = get_email(person_id)

    if email:
        print(email)
        send_email(email)
    else:
        print("No email available for this contact")