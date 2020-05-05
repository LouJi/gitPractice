import time
import smtplib
from datetime import datetime

def wasteTime():
    for i in range (99999999):
        k=1+0
    print('end Waste Time')

def NewTimeRecord(newTimestamp):
    with open('TimestampLog.txt', 'a') as f:
              f.write('\n')
              f.write(newTimestamp) # add line IDs with "line + ")\t" +" add tothis statment.

def LastTimestamp():                #fix to read last line only.
    with open('TimestampLog.txt', 'r') as f:
        return (list(f)[-1])        

def CheckTime(lastTimeChecked):
    time.sleep(1.0)
    timeCheckNow = int(time.time() - t0)
    compareTime = timeCheckNow - lastTimeChecked
    print(f'Now = {timeCheckNow} | Last = {lastTimeChecked}') #for debugging
    lastTimeChecked = timeCheckNow
    if (compareTime % timeInterval == 0):
        Email()
        #print('Sent Email')  #for debugging
        if (timeCheckNow >= timeLimit):
            return 1
        return 0
    else:
        if (timeCheckNow >= timeLimit):
            return 1
        return 0

def getMsg():
    with open('EmailBody.txt') as msg:
        return(msg.read())

def Email():
    #5ent_from = googleUser
    #to = ['ddotdasilva@gmail.com']
    subject = 'gitPractice Test'
    body = str(f'Sent to you on {dateToday}.\n' + getMsg())
    #print(gmail_password)

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (googleUser, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(googleUser, googlePassword)
        server.sendmail(googleUser, to, email_text)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong. Could not send email.')
"""    
def  pro():
    time.sleep(2.5)
 #Only for Winndows right now.   
def clock():
    pro()
    print (time.time() - t0, "seconds wall time")
    pro()
    print (time.time() - t0, "seconds wall time")
    pro()
    pro()
    print (time.time() - t0, "seconds wall time")
"""
timeLimit= 22 # hard coded for now with be one of 3 option user selected
Exit= 0
timeInterval= 5
a = str (LastTimestamp())
print('Welcome to the Git Practice')
print('Program will continue, error is corrected. ')
print ("The last timestamp is at " + a)  #fix to read last line only
b= str(datetime.now())
print('The new timestamp is at ' + b)
NewTimeRecord(b)
#DateTime format
dateToday = str(datetime.now().strftime("%A %B %d, %Y"))
print(f'Today is {dateToday}')
googleUser= input('Enter your google username: ') #+'@gmail.com'
googlePassword= input('Enter your password: ')
to= [input('Who are you notifying. Enter the full email addresss: ')]
t0 =  int(time.time())
print(t0) #for debugging
lastTimeChecked = int(time.time() - t0)
print(f'last{lastTimeChecked}') #for debugging

                      
while (Exit == 0):
    Exit = CheckTime(lastTimeChecked)
    print(f'Exit is {Exit}') #for debugging
#clock()
print('End of Program')
