# Discord Email Checker 

This tool checks whether a list of email addresses are **registered on Discord** by attempting to register them via Discord's public `/auth/register` endpoint.  
It helps identify which emails are already used for Discord accounts.

> ⚠️ **Disclaimer:** This tool is intended for educational and testing purposes only. Misuse of this script can result in violations of Discord’s Terms of Service.

---

## 📦 Features

- Detect if an email is registered on Discord.
- Automatically handles rate-limiting (`429 Too Many Requests`).
- Outputs results to:
  - `livehesap.txt` – Emails registered on Discord.

---

## 📂 File Structure

- `emails.txt` → Input file. One email per line.
- `livehesap.txt` → Output file for emails registered on Discord.
---

## 🚀 How to Use

1. Install required packages:
   ```bash
   pip install requests colorama

- Coded By: DARK KENZ
[Discord](https://discord.com/users/787475535483633684)
