📄 Project Documentation: MyAI Phishing Simulation (For Educational Purposes)

🧠 Project Overview
This is a simulated phishing project built for cybersecurity education and awareness training. It demonstrates how phishing emails and spoofed login pages can be used to harvest credentials, in a controlled and ethical environment.

DISCLAIMER: This project uses a fictional brand "MyAI". It must not be used to impersonate real companies or conduct unauthorized phishing.


📥File Structure :- 
app.py — Flask backend to serve pages and capture input
send_mail.py — Sends phishing email with spoofed content
credentials.txt — Stores captured email/password entries
README.md — Complete project guide

📁 templates/
index.html — ChatGPT offer page
login_google.html — Fake Google-style login form
warning.html — Page after login

📁 static/
styles.css — Shared styling for all pages


🚀 Features
| Feature                   | Description                                          |
| ------------------------- | ---------------------------------------------------- |
| 🎯 **Email Simulation**  | Sends a fake offer email with a tempting link.       |
| 🖥 **Phishing Site**      | A web page styled like a real login page.            |
| 🔐 **Credential Capture** | Captures submitted email & password (for awareness). |
| 📁 **Credential Storage** | Logs are saved in `credentials.txt`.                 |
| 🌐 **Ngrok Compatible**   | Can be hosted publicly for demo using ngrok.         |


🛠️ Technologies Used
Python 3.x
Flask for backend server
HTML/CSS for frontend UI
SMTP (smtplib) for sending emails
Ngrok for exposing localhost (during testing)


📦 Setup Instructions
1. Install Flask:
   ```bash
   pip install flask
   ```
2. Run server:
   ```bash
   python app.py
   ```
3. Expose with ngrok:
   ```bash
   ngrok http 5000
   ```
4. Update `send_mail.py` with your email, app password, and ngrok link.
5. Send email:
   ```bash
   python send_mail.py
   ```

📄 File Details
🔸 send_mail.py
Sends a spoofed email with a clickable phishing link.   
🔸 app.py
Handles route rendering and logs credentials.
🔸 credentials.txt
Logs format:- user@example.com : password123


🧪 Use Case
This simulation can be shown in:
Ethical hacking demonstrations
Red team simulations (in labs)
Cybersecurity education sessions
Awareness training for employees


🔐 Important Legal Notice
This project is for authorized training or testing purposes only. Never send phishing emails or collect data from real users without informed consent.
Unauthorized use may be illegal and unethical.

