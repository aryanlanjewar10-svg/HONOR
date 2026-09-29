def create():
    with open("employees.csv", "w") as file:
        print("employees.csv file created successfully.")

def read():
    with open("employees.csv", "r") as file:
        data=file.readlines()
        for line in data:
            print(line)

def update():
    with open("employees.csv", "a") as file:
        name=input("Enter employee name: ")
        age=input("Enter employee age: ")
        department=input("Enter employee department: ")
        file.write(f"{name},{age},{department}\n")
        print("Employee details updated successfully.")

def delete():
    with open("employees.csv", "r") as file:
            data=file.readlines()
            for line in data:
                print(line)
    with open("employees.csv", "w") as file:
        name=input("Enter employee name to delete: ")
        for line in data:
            if name not in line:
                file.write(line)
        print("Employee details deleted.")

def main():
    while True:
        print("1.Create employees.csv file")
        print("2.Read employee details")
        print("3.Update employee details")
        print("4.Delete employee details")
        print("5.Exit")
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                create()
                print("\n")

            case "2":
                read()
                print("\n")
            case "3":
                update()
                print("\n")
            case "4":
                delete()
                print("\n")
            case "5":
                break
            case _:
                print("Invalid choice.")

main()