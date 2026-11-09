
a = int(input("Enter first number: "))
b = int(input("Enter second Number: "))
while True:
    print("+")
    print("-")
    print("*")
    print("/")
    print('%')
    print("_ (program off)")
    print("Enter Your Choice: ")
    choice = input()
    match choice:
        case "+":
            print(a+b)
            continue
        case "-":
            print(a-b)
            continue
        case "*":
            print(a*b)
            continue       
        case "/":
            print(a/b)
            continue
        case "%":
            print(a%b)
            continue
        case "_":
            break
    break



