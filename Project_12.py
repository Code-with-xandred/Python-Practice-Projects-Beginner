#12. Email Slicer Programme

email = input("Enter Your Email: ")

index = email.index("@")

username = email[:index]
domain = email[index + 1:]

print(f"your Username Is {username} And Domain Is {domain}")

# __________________________________________________________________________________

# Second Method

email = input("Enter Your Email: ")

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(f"Your Username Is {username} and Domain Is {domain}")