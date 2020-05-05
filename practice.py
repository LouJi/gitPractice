import time
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

a = str (LastTimestamp())
print('Welcome to the Git Practice')
print('Program will continue, error is corrected. ')
print ("The last timestamp is at " + a)  #fix to read last line only
b= str(datetime.now())
print('The new timestamp is at ' + b)
NewTimeRecord(b)
#DateTime format 
print(f'Today is {datetime.now().strftime("%A %B %d, %Y")}')
t0 = time.time()
clock()
print('End of Program')
