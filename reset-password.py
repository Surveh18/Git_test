username: str = input("Enter username: ")
password: int = int(input("Enter password: "))

if username == "Admin" and password == "Admin":
    print("U can Reset")
else:
    print("U cannot Reset")
