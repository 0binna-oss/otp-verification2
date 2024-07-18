import math,random 
import random 
import smtplib 

#function to generate otp 
def generateotp():
    return random.randint(100000, 999999)

def initialize():
    email = get_user_email()
    otp = generate_random_otp()
    send_mail(otp,email)
    print(f"Email has been sent to{otp}")
    get_user_otp = input("Enter OTP code:")
    if str(get_user_otp) == str(otp):
        print("OTP verification successful")
    else:
        print("OTP verification failed,Try again.")
    
def get_user_email():
    user_input = input("Welcome to OTP verification system.\nEnter your email to recieve your one time verification password:")
    return str(user_input)

def generate_random_otp():
    return str(random.randint(100000, 999999))

def send_mail(otp,user_email):
    content = f"your one time verification code is{otp}"
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.startlis()
    sender = "obinnamarvelous50@gmail.com"
    recipient = f"{user_email}"
    mail.login('')
    header = "OTP verification code\n"
    content = header + content 
    mail.sendmail(sender,recipient,content)
    mail.close()

initialize()