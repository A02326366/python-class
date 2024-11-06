def main():
    #define local variable
    contents = ''

    #open the numbers.txt file to read
    infile = open('numbers.txt', 'r')

    #read the data
    contents = infile.read()

    #close the file
    infile.close()

    #print contents
    print(contents)

main()
