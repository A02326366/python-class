#Design a program that lets user enter rainfall for each month into list

def main():
    #Get the list with values
    numbers = get_values()

    #variable for total
    total = 0.0

    #Calc and Display the total rainfall
    for value in numbers:
        total += value

    print(' ')
    print('The total amount of rainfall for 12 months is' , total)

    #Calc and Display the average
    average = total / len(numbers)
    print(' ')
    print('The average amount of rainfall is' , average)

    #Calc and Display the Min and Max rainfall
    print(' ')
    print('The lowest amount of rainfall is' , min(numbers) , 'inches')
    print(' ')
    print('The highest amount of rainfall is' , max(numbers) , 'inches')

#Function for getting the values
def get_values():

    #create the list
    values = []

    #create a variable to record the month
    month = 1

    #provide a starting prompt for user to add additional information
    print('Please provide the total rainfall in inches for each month')
    print('in a twelve month period.')
    print(' ')
    print('Each entry will need to be only the numerical value with the')
    print('precise decimal amount of rainfall.')
    print(' ')
    
    #get values from user and add to list
    while month <= 12:

        #get number and append to list
        num = float(input(f'Enter the total rainfall for month {month}: '))
        values.append(num)
        month += 1

    #return the list
    return values




#call the main function.
if __name__ == '__main__':
    main()
