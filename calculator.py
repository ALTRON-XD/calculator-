num1 = int(input("enter the 1st number : ")) #taking input from user
num2 = int(input("enter the 2nd number : ")) #taking input from user
choice = int(input("enter your choice from 1-7 : \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.sqrt\n7.squre\n")) #taking input from user

if choice == 1: #addition
    print("the addition of", num1,  "and", num2, "is", num1 + num2)
elif choice == 2: #subtraction
    print("the Subtraction of", num1,  "and", num2, "is", num1 - num2)
elif choice == 3: #multiplication
    print("the Multiplication of", num1,  "and", num2, "is", num1 * num2)
elif choice == 4: #division
    print("the Division of", num1,  "and", num2, "is", num1 / num2)
elif choice == 5: #modulus
    print("the Modulus of", num1, "and", num2, "is", num1 % num2)
elif choice == 6: #sqrt
    print("the sqrt of", num1, "is", num1**0.5)
elif choice == 7: #squre
    print("the squre of", num1,  "and", num2, "is", num1**num2)
else: #invalid choice
    print("enter a valid choice")
