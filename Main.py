'''This is my attempt at a student Adminstration Timetable
5 students
several subject'''

subjects= ['Maths','Art','Science','Hstory','Geography','PE','English']

username = input('enter your username')
password = input('enter your password')

if username =='Tom' and password =='Cartoon12':
    print('Welcome Tom')
    print('Your selected lessons are:')
    print(subjects[0])
    print(subjects[3])
    print(subjects[-1])
elif username =='Katie' and password =='python99':
    print('Welcome katie')
    print('Your selected lessons are:')
    print(subjects[1])
    print (subjects[-2])
    print (subjects[-3])
elif username =='Miles' and password=='Tails89':
    print('Welcome Miles')
    print('Your selected lessons are:')
    print(subjects[-4])
    print(subjects[-1])
    print(subjects[0])
elif username=='Ravi' and password=='Dance91':
    print('Welcome Ravi')
    print('Your selected lessons are:')
    print(subjects[1])
    print(subjects[0])
    print(subjects[-3])
elif username=='Fred' and password=='Buya01':
    print('Welcome Fred')
    print('Your selected lessons are:')
    print(subjects[0])
    print(subjects[-2])
    print(subjects[1])
else:
    print('invalid login')
