class crud:
    @staticmethod
    def create():
        with open("employees.csv", "a") as file:
            name=input("Enter employee name: ")
            age=input("Enter employee age: ")
            department=input("Enter employee department: ")
            file.write(f"{name},{age},{department}\n")
            print("Employee details entered successfully.")
            
    @staticmethod
    def read():
        with open("employees.csv", "r") as file:
            data=file.readlines()
            for line in data:
                print(line)

    @staticmethod
    def update():
        with open("employees.csv", "r") as file:
            data=file.readlines()
        with open("employees.csv", "w") as file:
            for line in data:
                name=input("Enter employee name to update:")
                list=line.strip().split(",")
                if list[0]==name:  
                    age=input("Enter new employee age: ")
                    department = input("Enter new employee department: ")
                    file.write(f"{name},{age},{department}\n")
                    print("Employee details updated successfully.")
                else:
                    file.write(line)


    @staticmethod
    def delete():
        with open("employees.csv", "r") as file:
                data=file.readlines()
                for line in data:
                    print(line)
        with open("employees.csv", "w") as file:
            name=input("Enter employee name to delete: ")
            if(name in [line.split(",")[0] for line in data]):
                for line in data:
                    if name not in line:
                        file.write(line)
                        print("Employee details deleted.")
            else:
                print("Employee name not found.")

            

class main(crud):
    @staticmethod
    def menu():
        with open("employees.csv", "w") as file:
                file.write("Name,Age,Department\n")
                print("employees.csv file created successfully.") 
        while True:
            print("1.Create employee entry")
            print("2.Read employee details")
            print("3.Update employee details")
            print("4.Delete employee details")
            print("5.Exit")
            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    crud.create()
                    print("\n")

                case "2":
                    crud.read()
                    print("\n")
                case "3":
                    crud.update()
                    print("\n")
                case "4":
                    crud.delete()
                    print("\n")
                case "5":
                    break
                case _:
                    print("Invalid choice.")

main.menu()
