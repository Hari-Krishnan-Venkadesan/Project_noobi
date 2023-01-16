# add function
def addition (num1,num2):
    return num1 + num2

# subtraction
def subtraction (num1,num2):
    return num1 - num2

# multiplcation
def multiplication (num1,num2):
    return num1 * num2


#division
def floordivision(num1,num2):
    return num1 // num2

print('Select the operation you want to perform:')
print('1.Addition')
print('2.Subraction')
print('3.Multiplication')
print('4.Floor Division')

choice = input("Enter your choice of operation (1/2/3/4):")
if choice in ('1','2','3','4'):
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        
        if choice == '1':
            val = addition(num1,num2)
            print(val)
        
        elif choice == '2':
            val = subtraction(num1,num2)
            print(val)
            
        elif choice == '3':
            val = multiplication (num1,num2)
            print(val)
            
        elif choice == '4':
            val = floordivision(num1,num2)
            print(val)
else:
    print("Invalid input, Please enter from 1/2/3/4")        