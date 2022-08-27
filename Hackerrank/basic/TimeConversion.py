'''
step 1: split the copy of string last 2 index values It will br PM or AM
step 2: also split hours from the string and all the scene will be play with this one only
step 3: In the mibble minutes and seconds seperate them store it in another string

step 4: check if it is Pm or Am
step 5: if it is PM check if the hours is 12 or not, if 12 then return it with min and sec (actual answer), 
        if it is not 12 means less than 12 add 12 + hours to it.
step 6: if it is AM and if it is 12 and reset hours to  00 and append it to the min and sec return it(actual answer)
        if it is less than 12 return the same input to the o/p 
'''

def time_conversion(s):
    format = s[-2] + s[-1]  # extracting the period from the time
    hours,min, sec  = list(map(str, s.split(':')))  # taking hours , min , sec from the string
    
    # checking if the format there in sec or not and removing from the sec
    if format in sec:
        sec = sec.removesuffix(format)  # suffix will check at end and removes
    if format == 'AM':
        if hours == '12':
            hours = '00'
            return "{0}:{1}:{2}".format(hours, min, sec)
        else:
            return "{0}:{1}:{2}".format(hours, min, sec)
    else:
        if hours == '12':
            return "{0}:{1}:{2}".format(hours, min, sec)
        else:
            actual_hours = int(hours)
            actual_hours+=12
            return "{0}:{1}:{2}".format(actual_hours, min, sec)

print(time_conversion("07:41:00PM"))
