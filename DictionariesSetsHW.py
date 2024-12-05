def main():
    try:
        # Prompt the user for the file path
        print('Enter the name of a text file to see how many unique words exist')
        print(' ')
        file_name = input("Enter the name of the text file: ")

        # Call the function to get unique words
        unique_words(file_name)

    except ValueError:
        print('No file was specified. Please try again.')

def unique_words(file_name):

    try:
        #Open file
        with open(file_name, 'r') as file:
            # Read contents of file
            content = file.read()

            #If the file is empty
            if not content.strip():
                print("The file is empty. Please try again")
                return

            # Convert content to lowercase and remove punctuation
            # I looked up a more efficient way to remove non-alpha characters
            content = content.lower()
            translator = str.maketrans('', '', string.punctuation)
            content = content.translate(translator)
             
            
            # Create empty set to store unique words
            unique_words = set()

            # Split content into words and add to set
            words = content.split()
            unique_words.update(words)


        # Display unique words 
        print("Unique words found in the file:")
        for word in unique_words:
            print(word)

    except FileNotFoundError:
        print(f"The file named '{file_name}' was not found. Please check the file and try again.")


# Call the main function
if __name__ == "__main__":
    main()
