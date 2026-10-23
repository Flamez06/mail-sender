<div align="center">

# GForm Mailer

Automated personalized Gmail notifications from Google Forms responses using **Python**, **smtplib**, and **CSV / .env**.

</div>

---

## Features

- Read respondent data directly from a local CSV export (`responses.csv`)
- Automated Gmail dispatch via secure SSL (`smtplib`)
- 2-Step Verification compatible using dedicated Gmail App Passwords
- Automatic status tracking to prevent duplicate emails (`Status` column updated to `Sent`)
- Dynamic, personalized message templating (`{recipient_name}`)

---

## Stack

- Python 3.8+
- smtplib & email (Built-in standard library)
- csv (Built-in standard library)
- python-dotenv

---

## Setup

```bash
git clone [https://github.com/your-username/gform-mailer.git](https://github.com/your-username/gform-mailer.git)

cd gform-mailer

python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install python-dotenv
```
---
## Configuration

Update the following values inside `send_emails.py`:

```python
CSV_FILE = "responses.csv"

EMAIL_COLUMN = "EMAIL"

NAME_COLUMN = "NAME"

STATUS_COLUMN = "Status"
```

Configure your sender credentials inside `.env`:

```env
GMAIL_USER=your_email@gmail.com

GMAIL_APP_PASSWORD=abcdefghijklmnop
```

Set the email subject and body inside `message.txt`

---
