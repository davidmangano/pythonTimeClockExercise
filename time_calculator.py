def convert_time(start):
    if start[1] == ':' and start[5:] == 'AM':
        hour = "0" + str(start[0])
        minu = start[2:4]
        start_new = hour + ':' + minu
        return start_new
    else:
        if start[6:] == 'PM':
            hour = int(start[:2]) + 12
            minu = start[3:5]
            newtime = str(hour) + ':' + minu
        elif start[5:] == 'PM':
            hour = int(start[:1]) + 12
            minu = start[2:4]
            newtime = str(hour) + ':' + minu
        else:
            start = start[:5]
            return start
    return newtime

def get_duration(duration):
    dx, dy = duration.split(':',2)
    if int(dx) < 24:
        day = 0 
        hour = int(dx)
        min = int(dy)
        return day, hour, min 
    else: 
        day = int(dx)//24
        hour = int(dx)%24
        min = int(dy)
    return day, hour, min


def get_dayofweek(day,add=0):
    day_dict = {"monday":"Monday","tuesday":"Tuesday", "wednesday":"Wednesday", 
                "thursday":"Thursday", "friday":"Friday","saturday":"Saturday",
                "sunday":"Sunday"}
    for x in enumerate(day_dict):
        if x[1] == day.lower():
            daykey = x[0]
            break
        else:
            continue
            
    if daykey + add == 7:
        newday = 0
    elif daykey + add > 7 and add > 7:
        newday = daykey + (add%7)
        if newday < 7: 
            pass 
        else: 
            newday = newday-7
    elif daykey + add > 7 and add < 7:
        if daykey - abs(add-7) > 0:
            newday = daykey - abs(add-7)
        else:
            newday = 7 - abs(daykey - abs(add-7))
    else: 
        newday = daykey + add
    for x in enumerate(day_dict):
        if x[0] == newday:
            dk = x[1]
            return day_dict[dk]
        else:
            continue
        
def revert_time(time):
    if time[:2] == '00':
        hour = str(int(time[:2]) + 12 )
        return hour + time[2:] + ' AM'
    elif int(time[:2]) < 12 and int(time[:2]) < 10 :
        hour = str(int(time[:2]))
        return hour + time[2:] + ' AM'
    elif int(time[:2]) < 12:
        return time + ' AM'
    elif int(time[:2]) == 12:
        return time + ' PM'
    else: 
        hour = str(int(time[:2]) - 12)
        return hour + time[2:] + ' PM'
    

def add_time(start, duration, startday = " "):
#convert start time to 24 hr time 
    workingTime = convert_time(start)
#extract duration (days, hours, mins)
    days, hours, mins = get_duration(duration)
# add time from get duration to start time (if hour + addhours >= 24) then (hour + addhours) + 00:00 and daycount +1

# add mins
    if int(workingTime[3:]) + mins >= 60: 
        hours = hours + 1
        if 0 + ((int(workingTime[3:]) + mins) - 60) < 10:
            new_mins = '0' + str(0 + ((int(workingTime[3:]) + mins) - 60))
        else:
            new_mins = str(0 + ((int(workingTime[3:]) + mins) - 60))
    elif int(workingTime[3:]) + mins == 0:
        new_mins = '00'
    elif int(workingTime[3:]) + mins < 10:
        new_mins = '0' + str(int(workingTime[3:]) + mins)
    else: 
        new_mins = str(int(workingTime[3:]) + mins)
# add hours

    if int(workingTime[:2]) + hours >=24:
        days = days + 1
        if 0 + ((int(workingTime[:2]) + hours) - 24) < 10:
            new_hours = '0' + str(0 + ((int(workingTime[:2]) + hours) - 24))
        else:
            new_hours = str(0 + ((int(workingTime[:2]) + hours) - 24))
    elif int(workingTime[:2]) + hours == 0:
        new_hours = '00'
    elif int(workingTime[:2]) + hours < 10:
        new_hours = '0' + str(int(workingTime[:2]) + hours)
    
    else: 
        new_hours = str(int(workingTime[:2]) +  hours)
# add days
    if startday == " " and days == 0:
        dayflag = ''
    elif startday == " " and  days  == 1:
        dayflag = ''' (next day)'''
    elif startday == " " and days > 1:
        dayflag = ' (' + (f"{days} days later") + ')'
    elif startday != " " and days == 0:
        dayflag = ', '+ get_dayofweek(startday) 
    elif startday != " " and days == 1: 
        dayflag = ', ' + get_dayofweek(startday,days) +''' (next day)'''
    else: 
        dayflag = ', ' + str(get_dayofweek(startday,days)) + ' (' + str(days) + ' days later)'

# revert time funtion 
    constructed_time = revert_time(new_hours + ':' + new_mins)
 

    return constructed_time + dayflag 
 