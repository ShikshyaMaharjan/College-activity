

with open("data.txt", "rb") as f:
    while True:
        cmd = input("Enter command (f=forward, b=backward, e=exit): ")

        if cmd == "f":
            n = int(input("Move forward by: "))
            f.seek(n, 1)

        elif cmd == "b":
            n = int(input("Move backward by: "))
            f.seek(-n, 1)

        elif cmd == "e":
            break

        else:
            print("Invalid command")

        print("Current position:", f.tell())