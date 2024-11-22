#Write a program that reads a string from the user containing a list of names
#separated by commas and spaces. The program should then parse the string and
#print the names in the format "Last Name, First Name" in alphabetical order.

#For example, if the user inputs the string: "John Doe, Mary Jane",
#program should print:
#Doe, John
#Jane, Mary



def main():


    #Get user input for name
    print("Enter a list of names. Include both first and last names and seperate them by a comma and a space.")
    my_string = input('Enter names: ')
    print(" ")

    #Capitalize the values in the string for personal preference
    #I did look this up online as I could not find it in previous PowerPoints
    my_string = my_string.title()

    #split the string into individual name pairs by the commas and spaces
    names = my_string.split(", ")

    #define list to put the name pairs into
    name_pair = []

    #organize by last, first

    for name in names:
        try:
            #split the names
            first, last = name.split(" ")

            #make the names last, first
            name_pair.append((last, first))

        except ValueError:
            print(f"ERROR: '{name}' is in an invalid format.")
            print(" ")

    #alphabetize
    name_pair.sort()

    #Print the results

    for last, first in name_pair:
        print(f"{last}, {first}")

if __name__ == "__main__":
    main()

    
