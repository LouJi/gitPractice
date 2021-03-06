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
    sent_from = googleUser
    to=  reciever
    subject = 'gitPractice Test'
    body = str(f'Sent to you on {dateToday}.\n' + str(getMsg()))
    

    email_text = email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, to, subject, body)# Replace 'to' with '",".join(to)' for multiple persons

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(googleUser, googlePassword)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong. Could not send email.')

def time5m():
    time = 5 * 60 #5 minutes in seconds
    ti= "5 minutes"
    return time, ti

def time15m():
    time= 15* 60 # 15 minmutes in seconds
    ti= "15 minutes"
    return time, ti

def time1h():
    time= 60 *60 # 1 hour in seconds
    ti = "1 hour"
    return time, ti

def time24h():
    time= (60*60)*24 #24 hours in seconds
    ti= "24 hours"
    return time, ti

def timeSwitch():
    timeSelect= input('Please select a time interval (use the corresponding letter as input): \n a) 5 minutes \n b) 15 minutes \n c) 1 hour \n d) 24 hours \n')
    switch = { 'a': time5m(), 'b': time15m(), 'c': time1h(), 'd': time24h()}
    timeInterval, displayTime= switch.get(timeSelect, "Not a Valid Entry")
    print(displayTime)
    if displayTime == "Not a Valid Entry":
        timeSwitch()
    return timeInterval
        
def GetTimeLimit():
    timeLtd= input('Select a time limit:\n a) 1 hour \n b) 1 day\n c) 2 days\n')
    if timeLtd == 'a':
        timeLmt= 3600 # string change to int and an hour in seconds
    elif timeLtd == 'b':
        timeLmt= 86400
    elif timeLtd == 'c':
        timeLmt= 172800
    else:
        print('Invalid Entry')
        GetTimeLimit()
    return timeLmt


#MAIN starts here
print('This program will send you an email notice after a certain time has elapsed for 2 days.')
#perform a check for an integer.

timeInterval= timeSwitch()
print(timeInterval)
timeLimit= GetTimeLimit()
if timeInterval > timeLimit:
    print('Please select a time limit greater than your time interval.')
    timeLimit= GetTimeLimit()
#timeLimit= 172800 # hard coded for now with be one of 3 option user selected
Exit= 0

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
reciever= [input('Who are you notifying. Enter the full email addresss: ')]
t0 =  int(time.time())
print(t0) #for debugging
lastTimeChecked = int(time.time() - t0)
print(f'last {lastTimeChecked}') #for debugging

                      
while (Exit == 0):
    Exit = CheckTime(lastTimeChecked)
    print(f'Exit is {Exit}') #for debugging
#clock()
print('End of Program')


"""
Can add when merged with master branchaiput for uses to enter email credentials before entering the while loop. or  use default email. 
Keep in mind you will need to search email addresses for service provider and adjust smtp ports.
Look at aol,  gmail, msn, outlook, yahoo, etc. Google search popular email providers.
"""
