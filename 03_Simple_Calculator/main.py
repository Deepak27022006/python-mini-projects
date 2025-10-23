
def sum(num1, num2):
     return num1+num2
 
def sub(num1, num2):
    return num1-num2 
   
def mul(num1, num2):
    return num1*num2  
  
def div(num1, num2):
    return num1/num2   
 
def modulus(num1, num2):
    return num1%num2

print("Select operators: ")
print("+")
print("-")
print("*")
print("/")
print("%")

num1= float(input("Enter number: "))
oper= input("operator: ")
num2= float(input("Enter number: "))
  
if oper=="+":
    print(f"Sum:, {sum(num1,num2)}")

elif oper=="-":
    print(f"Result: {sub(num1, num2)}")

elif oper=="*":
    print(f"Result: {mul(num1,num2)}")   

elif oper=="/":
    if num2!=0:
     print(f"Result: {div(num1, num2)}") 
    
    else:
        print("Error: Cannot divide by zero!")

elif oper=="%":
    print(f"Result: {modulus(num1,num2)}") 

else:
    print("Invalid Input ")    