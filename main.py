
#Problem 1
list=[1,2,3]#The list where numbers are placed
def multiplication(the_list):#defining my function
  product=1#Product starts at 1
  for i in the_list:#Create a for loop with the defined function
    product=product*i#The old product will be multiplied by the next number in that list
  return product#End the execution of the function
print("All the numbers in the list multiplies to:",multiplication(list))#Assuring the user what will happen to their number along with printing its sum


#Problem 2
def multiply(number):#defining my function
    result = 1#Result starts at 1
    for i in range(0, len(number)):#Create a for loop with the defined function ina range
        result *= number[i]#The old result will be multiplied by the next number in that list
    return result#End the execution of the function

print("Please input a list of numbers to multiply:")#Assuring the user what will happen to their number
print(multiply([int(s) for s in input().split()]))#For all the numbers entered, it will be split