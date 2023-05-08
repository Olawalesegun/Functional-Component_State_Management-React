def remove_duplicates(email_list):
    unique_emails = []
    for email in email_list:
        if email not in unique_emails:
            unique_emails.append(email)
    return unique_emails


email_list = ["example1@example.com", "example2@example.com", "example1@example.com", "example3@example.com"]
unique_emails = remove_duplicates(email_list)
print(unique_emails) # Output: ["example1@example.com", "example2@example.com", "example3@example.com"]
