import requests
import time
from colorama import Fore, init

init(autoreset=True)

print(f"""{Fore.LIGHTBLUE_EX}
██████╗  █████╗ ██████╗ ██╗  ██╗     ██████╗ ██████╗ ██████╗ ███████╗██████╗ ███████╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝
██║  ██║███████║██████╔╝█████╔╝     ██║     ██║   ██║██║  ██║█████╗  ██████╔╝███████╗
██║  ██║██╔══██║██╔══██╗██╔═██╗     ██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗╚════██║
██████╔╝██║  ██║██║  ██║██║  ██╗    ╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║███████║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝
                                                                                                                                                                                                                                                                  
                                                                                                        
{Fore.LIGHTBLUE_EX}Coded By: DARK KENZ {Fore.LIGHTCYAN_EX}
{Fore.LIGHTBLUE_EX}Discord: {Fore.LIGHTCYAN_EX} https://discord.gg/Qywpa9hwcq """) 
print("")
print(Fore.RED + f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("")

def register_discord_email(email):
    url = 'https://discord.com/api/v9/auth/register'
    payload = {
        "email": email,
        "password": "darkcoders63123!",
        "username": "bydarkkenz",
        "invite": None,
        "consent": True,
        "date_of_birth": "1942-07-17"  # Stalingrad o/
    }
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        json_response = response.json()

        if response.status_code == 200:
            return f"{email} Registration for is successful."
        elif response.status_code == 400:
            if 'captcha-required' in json_response.get('message', '').lower() or 'captcha_sitekey' in json_response:
                if json_response.get('mfa_enabled', False):  # 2FA Checker
                    return Fore.GREEN + f"{email} Registered on Discord. (2FA Enabled)"
                return Fore.GREEN + f"{email} Registered discord"
            elif json_response.get('code') == 50035:
                return Fore.RED + f"{email} Not registered Discord."
            return f"{email} Registration failed for: {json_response}"
        elif response.status_code == 429:
            retry_after = json_response.get('retry_after', 10)
            time.sleep(retry_after)
            return f"{email} Request limit exceeded. Try again in {retry_after} seconds."
        else:
            return f"{email} An unknown error occurred for . Status code: {response.status_code}, Response: {json_response}"
    except requests.exceptions.RequestException as e:
        return f"{email} An error occurred sending a request for: {e}"

def check_emails_from_file(email_filename, live_filename, mfa_filename):
    try:
        with open(email_filename, 'r') as file:
            emails = [email.strip() for email in file if email.strip()]
    except FileNotFoundError:
        print(f"{email_filename} file not found.")
        return []

    for email in emails:
        result = register_discord_email(email)
        print(result)

        if "Registered Discord." in result:
            with open(live_filename, 'a') as live_file:
                live_file.write(email + "\n")
        if "(2FA Active)" in result:
            with open(mfa_filename, 'a') as mfa_file:
                mfa_file.write(email + "\n")

        # Speed ​​ratio if you change that you gotta be a motherfucker man
        time.sleep(1)

# Kullanım
email_dosya_adi = "emails.txt"  # File containing email addresses to check
live_dosya_adi = "livemails.txt"  # File that will only save email addresses that are "registered with Discord"
mfa_dosya_adi = "2fa_emails.txt"  # [Soon, NOT WORKING]
check_emails_from_file(email_dosya_adi, live_dosya_adi, mfa_dosya_adi)

input("The process is completed. Press Enter to close the console...")
