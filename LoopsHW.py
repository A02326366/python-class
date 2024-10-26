#set the inventory
muffins = 10
cupcakes = 10

#get input from customer
while True:
    item = input("Enter the desired item ('muffin' or 'cupcake') or '0' to finish: ")

    if item == '0':
        break

    elif item == 'muffin':
        if muffins > 0:
            muffins -= 1
            print("Muffin sold.")

        else:
            print("Out of stock!")

    elif item == 'cupcake':
        if cupcakes > 0:
            cupcakes -= 1
            print("Cupcake sold.")

        else:
            print("Out of stock!")

    else:
        print("Invalid input. Please try again!")


#print the remaining items

print(f"Muffins: {muffins} Cupcakes: {cupcakes}")
