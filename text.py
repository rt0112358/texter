import credentials 
import smtplib
import time
#########################################
# Automated Text Machine
# 
# Sends texts via email or simply emails 
#########################################

def init_server():
    host_server = 'smtp.gmail.com'
    setup = smtplib.SMTP_SSL(host_server, 465)
    return setup

def sign_in(email, password):
    host = init_server()
    host.login(email, password)
    return host

def send_message(destination):
    email = credentials.username()
    pssword = credentials.password()
    
    server = sign_in(email, pssword)
    
    num_messages = 10 
    for i in range(num_messages):
        # time.sleep(0.5) # Uncomment to ensure chronological order 
        server.sendmail(email, destination, "Hello " + str(i))

def main():
    dest = credentials.default_destination()
    send_message(dest)

main()