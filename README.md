# VaccinePing
A smart alert system using the CoWIN API to track and notify users about COVID-19 vaccine slot availability in real time. Users can set preferences like age, pin code, or district, and receive instant alerts via email, SMS, or app notifications as soon as slots open up.


💉 CoWIN Vaccine Slot Notifier
A simple Python script that uses the official CoWIN API to check for COVID-19 vaccine slot availability and send real-time alerts via WhatsApp and voice notification when a slot is found.

🚀 Features
🔍 Checks vaccine slot availability by pincode

📅 Filters by age group and vaccine type (e.g., COVAXIN)

📢 Sends alerts via:

WhatsApp Web

Voice announcement (using pyttsx3)

🔁 Continuously checks every few seconds

🛠 Requirements
Install the following Python packages before running the script:

bash
Copy
Edit
pip install requests pyautogui pyttsx3
📂 Project Structure
bash
Copy
Edit
cowin-vaccine/
│
├── cowin_vaccine.py       # Main script
└── README.md              # Project documentation
⚙️ Configuration
Edit the following variables in cowin_vaccine.py to customize:

python
Copy
Edit
date_int = '3-1-2022'  # Date of slot checking (format: DD-MM-YYYY)
age = 17               # Minimum age of recipient
pincode_list = [110009, 110006, 110084, 110085, 110088]  # List of pincodes
phone_list = ['+919911713714']  # WhatsApp numbers to send alert to
🧠 How It Works
Sends requests to CoWIN API’s calendarByPin endpoint.

Parses the JSON response for centers with:

Available dose 1 slots

Vaccine type = "COVAXIN"

Age eligibility

If found, it:

Opens WhatsApp Web with a prefilled message

Uses pyttsx3 to give a voice alert

Waits before sending the next alert

🛑 Disclaimer
This tool is for educational and personal use only.

Do not spam the CoWIN API or misuse WhatsApp automation.

Ensure you're following CoWIN API terms.

📬 Future Enhancements
Email or Telegram alerts

GUI interface with Flutter or Tkinter

Slot history tracking

OTP-based auto-booking (with user interaction)
