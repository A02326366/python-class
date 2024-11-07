def main():
    #define local variables
    line = ''
    total = 0
    average = 0
    count = 0

    try:
        fileName = input('Enter the name of the file: ')
        #open the numbers.txt file to read
        infile = open(fileName, 'r')

        #read the data
        line = infile.readline()
        count = 1

    
        while line != '':
            try:
                #strip the line feed
                line  = line.rstrip('\n')
                
                #add up the numbers
                total = total + int(line)

                #print the line to see the contents
                print(line)
                
                #restart line
                line = infile.readline()

                #add to counter when line is read
                count += 1

                #find the average
                average = int(total / count)
    
            except ValueError:
                print(f"ERROR: Could not convert '{line}' to a number.")

            #if there is an error, skip to next line
            line = infile.readline()

    except IOError:
        print('ERROR: Could not open or read the file')

    except FileNotFoundError:
        print('ERROR: The specified file could not be found')

    
    #print total
    print('The sum of the numbers is' , total)
    print('The average of the numbers is' , average)
    
    #close the file
    infile.close()

main()
