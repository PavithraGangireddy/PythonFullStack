# writing a file
file = open("data.txt", "w")
file.write("Hello Python")
file.close()

#write multiple lines to a file
file = open("students.txt", "w")
file.write("Pavithra\n")
file.write("Rahul\n")
file.write("Anjali\n")
file.close()
print("Student names added")

#checking file exist or not
import os
if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File does not exist")


#sending  welcome email 
import smtplib
sender = "your_email@gmail.com"
receiver = "receiver@gmail.com"
password = "your_app_password"
subject = "Welcome to Python Course"
body = """Hello,
Welcome to the Python course.
We are happy to have you with us.
Thank you."""
message = f"Subject: {subject}\n\n{body}"
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
print("Welcome email sent")

#sending mail with user input
import smtplib
sender = "your_email@gmail.com"
receiver = "receiver@gmail.com"
password = "your_app_password"
name = input("Enter your name: ")
subject = input("Enter email subject: ")
body = input("Enter email message: ")
message = f"Subject: {subject}\n\nHello {name},\n\n{body}"
with smtplib.SMTP("smtp.@gmail.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
print("Email sent successfully")

