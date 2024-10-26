#Get input for average speed, speed limit, and distance traveled

avg_speed = int(input('What is your average speed for the trip?: '))
spd_lmt = int(input('What is the speed limit for the duration of the trip?: '))
distance = int(input('How many miles did you travel in this trip?: '))

#Now we need to calculate how long the trip would take going the speed limit
#To get this into minutes, we will multiply it by 60

avg_time = int(60*(distance / spd_lmt))


#Now figure out the actual time spent

real_time = int(60*(distance / avg_speed))

#Now we get the time saved

time_saved = real_time - avg_time

#Finally the results. I put the -1 in the calculation to make sure the results
#were positive

if time_saved < 0:
    print(f'You saved {time_saved * -1} minutes!')
elif time_saved > 0:
    print(f'You lost {time_saved * -1} minutes!')
else:
    print('You did not save any time!')
