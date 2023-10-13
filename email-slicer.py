# Project_2: email-slicer

def get_mail():
    while True:
        print("--Email Slicer--")
        email = input("Enter email: ")    
        if "@" not in email or "." not in email: # checking the correct format
            print("Invalid email format. Try again!")
            continue
        else:
            return email

def email_split(email): # split into two parts
    return email.split("@")

def main():
    email = get_mail()
    username, domain = email_split(email)
    print("----")
    print(f"Email: {email}")
    print(f"Username: {username}")
    print(f"Domain: {domain}")

if __name__ == "__main__":
    main()


