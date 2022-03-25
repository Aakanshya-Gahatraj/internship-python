def calculator(a,operator,b):
    if operator=='+':
        return a+b
    elif operator=='-':
        return a-b
    elif operator=='*':
        return a*b
    else:
        return int(a/b)


while True:
    a= int(input("Number 1: "))
    operator= input("Operator: ")
    b= int(input("Number 2: "))
    ans= calculator(a,operator,b)
    print("Ans: " f"{ans}")
    exit= input("Exit? (y/n): ")
    if exit=='y':
        break

