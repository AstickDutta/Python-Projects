def email_extractor():
    email = input("Please enter your email address: ")

    if "@" in email:
        index = email.index("@")
        userName = email[:index]
        domain = email[index + 1:]

        print(f"User Name : { userName } and Domain: { domain }")
    else:
        print("Invalid email address. Please include '@' in the email.")

email_extractor()