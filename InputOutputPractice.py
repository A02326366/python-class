#Constant slices per pizza amount
pizza_slices = 8

#Ask how many slices each persons want
person1 = int(input('How many slices would you like?: '))
person2 = int(input('How many slices would you like?: '))
person3 = int(input('How many slices would you like?: '))
person4 = int(input('How many slices would you like?: '))

#This will be the total slices that everyone wants
total_slices = person1 + person2 + person3 + person4
print('The total number of slices we need:',total_slices)

#Now we need to figure out how many pizzas we need
pizza_order = round(total_slices / pizza_slices)
print(f'We need to order this many pizzas: {pizza_order}')

#The leftover slices
leftovers = pizza_slices * pizza_order - total_slices
print(f'This means that we will have this many slices left:{leftovers}')
