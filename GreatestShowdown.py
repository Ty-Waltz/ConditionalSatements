first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))

#calculating the biggest number
if (first_number >= second_number) and (first_number >= third_number):
   biggest = first_number
elif (second_number >= first_number) and (second_number >= third_number):
   biggest = second_number
else:
   biggest = third_number

#calculating the smallest number
if (first_number <= second_number) and (first_number <= third_number):
   smallest = first_number
elif (second_number <= first_number) and (second_number <= third_number):
   smallest = second_number
else:
   smallest = third_number

print("The biggest number is", biggest)
print("The smallest number is", smallest)