import smtplib
from email.message import EmailMessage

# Email content setup
msg = EmailMessage()
msg['Subject'] = "🎁 MyAI Plus Free for 3 Months!"
msg['From'] = "support@openai-access.com"  # Spoofed sender
msg['To'] = "mahajankalash9@gmail.com"         # Replace with your test email

# Replace with your ngrok link or localhost for testing
link = "https://e560-103-186-246-114.ngrok-free.app"

msg.set_content(f"""\
Hi there,

You have been selected to try MyAI Plus FREE for 3 months.

🎁 Claim your offer here: {link}

Offer expires in 24 hours!

- The ChatGPT Team
""")

# Send using Gmail SMTP
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login("mahajankalash8@gmail.com", "beao enzv wwot jmot")  # App Password
    smtp.send_message(msg)

print("✅ Email sent successfully.")
