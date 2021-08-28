import smtplib
from dictionary import email_dict


#Sender email
email = "example@gmail.com"
#Send password
pw = "examplepassword"


def sending_email(send_to, name):
    with smtplib.SMTP("smtp.gmail.com", 587) as email_connection:
        email_connection.starttls()
        email_connection.login(user=email, password=pw)
        email_connection.sendmail(from_addr=email, to_addrs=send_to,
        msg=f"""
        Subject: Hello there

        
        Hi {name},

        Nice to meet you!
        
        Best regards,
        BigFatDuck 
        """
        )

for send_name, send_email in email_dict.items():
    sending_email(send_email, send_name)

