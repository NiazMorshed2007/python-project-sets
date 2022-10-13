rounds = int(input("Number of commands: "))
d = []
for _ in range(rounds+1):
    command = input("Enter your command: ")
    if command == "print":
        print(d)
    elif command == "sort":
        sorted(d)
    elif command == "pop":
        d.pop()
    elif command == "reverse":
        d.reverse()
    else:
        sc = command.split()
        mc = sc[0]
        print(mc)
        if mc == "append":
            d.append(int(sc[1]))
        elif mc == "remove":
            d.remove(int(sc[1]))
        elif mc == "insert":
            d.insert(int(sc[1]), int(sc[2]))
