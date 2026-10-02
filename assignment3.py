import pandas as pd

df=pd.DataFrame({'Emp ID': [],'Name': [],'Age': [],'Department': [],'Salary':[]})
def create():
    print("Enter employee details to add to database:")
    name=input("Name: ")
    age=int(input("Age: "))
    department=input("Department: ")
    salary=float(input("Salary: "))
    employee_id=len(df)+1
    df.loc[employee_id] = [employee_id, name, age, department, salary]
    print("Employee added successfully!")

def read():
    if(df.empty):
        print("No employee records found.")
    else:
        print(df)

def update():
    print("Enter employee ID to update details:")
    empid=int(input("Employee ID: "))
    print(df['Emp ID'])
    if(empid in df['Emp ID'].values):
        print("Enter new details:")
        name=input("Name: ")
        age=int(input("Age: "))
        department=input("Department: ")
        salary=float(input("Salary: "))
        df.loc[empid,'Name']=name
        df.loc[empid,'Age']=age
        df.loc[empid,'Department']=department
        df.loc[empid,'Salary']=salary
        print("Employee details updated successfully!")

def delete():
        print("Enter employee ID to delete:")
        empid=int(input("Employee ID: "))
        if(empid in df['Emp ID'].values):
            df.drop(empid, inplace=True)
            print("Employee details deleted successfully!")
        else:
            print("Employee ID not found.")

def main():
    while True:
        print("----MENU----")
        print("1.Create employee record")
        print("2.Read employee records")
        print("3.Update employee record")
        print("4.Delete employee record")
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