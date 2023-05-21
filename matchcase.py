a =int(input("Enter a number: "))

match a:
    case 1:
        print("Case is 1")
    case 2:
        print("case is 2")
    case 12:
        print("case is 12")
    case 8:
        print("case is 8")
    case 10:
        print("case is 10")
    case _:
        print("No match found")
