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
    
a = str (LastTimestamp())
print('Welcome to the Git Practice')
print('Program will continue, error is corrected. ')
print ("The last timestamp is at " + a)  #fix to read last line only
b= str(datetime.now())
print('The new timestamp is at ' + b)
NewTimeRecord(b)
print('End of Program')
