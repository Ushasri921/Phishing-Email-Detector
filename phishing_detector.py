emails = [
    "Congratulations! You won a free iPhone",
    "Your bank account has been blocked",
    "Meeting scheduled at 5 PM",
    "Update your password immediately",
]

phishing_keywords = [
    "won",
    "free",
    "bank",
    "blocked",
    "password",
    "urgent",
]

for email in emails:
    is_phishing = False

    for word in phishing_keywords:
        if word.lower() in email.lower():
            is_phishing = True
            break

    if is_phishing:
        print(f"PHISHING EMAIL: {email}")
    else:
        print(f"SAFE EMAIL: {email}")