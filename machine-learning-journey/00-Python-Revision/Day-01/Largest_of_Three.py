a=int(input("Enter 1st Number is: "))
b=int(input("Enter 2nd Number is: "))
c=int(input("Enter 3rd Number is: "))
large = a
if(large < b or large<c):
    if(b>c):
        large = b
    else :
        large = c
print("The Large Number is: ", large)