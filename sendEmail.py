import smtplib
# setup the connection
connection =smtplib.SMTP_SSL('smtp.gmail.com', 465)
# start the connection
# connection.ehlo()
# start the tls connection
# connection.starttls
# next login 

# send the email
connection.sendmail('jrforbes24@gmail.com', 'cindymacq@gmail.com', 'Subject: Sent from Python.\n\n Hello my love.')