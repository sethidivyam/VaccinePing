# 💉 VaccinePing – CoWIN Vaccine Slot Notifier

**VaccinePing** is a real-time alert system that checks COVID-19 vaccine slot availability using the CoWIN public API and notifies the user via **WhatsApp Web** and **voice alerts**.

---

## 🚀 Features

- 🔍 Check slot availability using PIN codes
- 📅 Filter by age and vaccine type (e.g., COVAXIN)
- 📢 Notifications through:
  - WhatsApp Web (prefilled alert message)
  - Voice alert using `pyttsx3`
- 🔁 Automatically refreshes every few seconds

---

## 🛠 Requirements

Install required Python packages:

```bash
pip install requests pyautogui pyttsx3
```

---

## 📂 Project Structure

```
vaccineping/
├── cowin_vaccine.py     # Main script
└── README.md            # Documentation
```

---

## ⚙️ Configuration

Open `cowin_vaccine.py` and customize the following:

```python
date_int = '3-1-2022'  # Format: DD-MM-YYYY
age = 17  # Minimum eligible age
pincode_list = [110009, 110006, 110084, 110085, 110088]  # Pincodes to monitor
phone_list = ['+919911713714']  # WhatsApp numbers to notify
```

---

## 🧠 How It Works

1. Sends GET request to CoWIN API’s `calendarByPin` endpoint.
2. Filters for sessions with:
   - Available first dose slots
   - Matching vaccine type (e.g., COVAXIN)
   - Age eligibility
3. On availability:
   - Opens WhatsApp Web with pre-filled message
   - Speaks the alert using `pyttsx3`
   - Simulates "enter" key to send message
4. Repeats the check every few seconds

---

## 🖥️ Example Output

```
Available: 15 slots
District: North Delhi
Pincode: 110009

[WhatsApp opened, voice alert triggered]
```

---

## 🧾 Disclaimer

- This project is for **educational/personal** use only.
- Do **not spam** the CoWIN API.
- Use **WhatsApp Web automation** responsibly.
- Respect CoWIN and WhatsApp terms of service.

---

## 🔮 Future Enhancements

- 📬 Email or Telegram alerts
- 🖼 GUI with Flutter/Tkinter
- 📊 Slot history and logging
- 🔐 OTP-based assisted booking (manual flow)

---

## 👨‍💻 Author

**Divyam Sethi**  
🔗 [LinkedIn](https://www.linkedin.com/in/divyam-sethi-3a5141232)  
📧 [Email](mailto:divyamsethi1804@gmail.com)

---

## ⭐️ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub and sharing it!
