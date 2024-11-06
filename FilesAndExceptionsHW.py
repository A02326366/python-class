def main():
    #define local variables
    line = ''
    total = 0
    average = 0

    #open the numbers.txt file to read
    infile = open('numbers.txt', 'r')

    #read the data
    line = infile.readline()

    
    while line != '':
        #strip the line feed
        line  = line.rstrip('\n')
        #add up the numbers
        total = total + int(line)
        #restart line
        line = infile.readline()


    #print total
    print('The sum of the numbers is ' , total)
    #close the file
    infile.close()

    #print contents
    print(contents)

main()
