def getdate():
    import datetime
    return datetime.datetime.now()
def client_data_entry():
    
    client_name_data=int(input("Write Your client name\n 1.Harry\n 2.Rohan\n 3.Hammad\n"))
    client_work_data=int(input("which One you want??\n 1.FOOD\n 2.Exercise\n"))
    if client_name_data==1 and client_work_data==1:
        client_foods_name=input("Enter foods Name")
        food_list=open("harryFood.txt","a")
        date=str(getdate())
        food_list.write(date)
        food_list.write(" : ")
        food_list.write(client_foods_name)
        food_list.write("\n")
        food_list=open("harryFood.txt","r")
        print(": ")
        content=food_list.read()
        print(content)
        print("Written Succesfully !!")
        food_list.close()
    elif client_name_data==2 and client_work_data==1:
        client_foods_name=input("Enter foods Name")
        food_list=open("rohanFood.txt","a")
        date=str(getdate())
        food_list.write(date)
        food_list.write(" : ")
        food_list.write(client_foods_name)
        food_list.write("\n")
        food_list=open("rohanFood.txt","r")
        print(": ")
        content=food_list.read()
        print(content)
        print("Written Succesfully !!")
        food_list.close()
    elif client_name_data==3 and client_work_data==1:
        client_foods_name=input("Enter foods Name")
        food_list=open("hammadFood.txt","a")
        date=str(getdate())
        food_list.write(date)
        food_list.write(" : ")
        food_list.write(client_foods_name)
        food_list.write("\n")
        food_list=open("hammadFood.txt","r")
        print(": ")
        content=food_list.read()
        print(content)
        print("Written Succesfully !!")
        food_list.close()
        
   #-------------- For Exercising-----------
   
    elif client_name_data==1 and client_work_data==2:
        client_foods_name=input("Enter foods Name")
        food_list=open("harryEx.txt","a")
        date=str(getdate())
        food_list.write(date)
        food_list.write(" : ")
        food_list.write(client_foods_name)
        food_list.write("\n")
        food_list=open("harryEx.txt","r")
        print(": ")
        content=food_list.read()
        print(content)
        print("Written Succesfully !!")
        food_list.close()
    elif client_name_data==2 and client_work_data==2:
        client_foods_name=input("Enter foods Name")
        food_list=open("rohanEx.txt","a")
        date=str(getdate())
        food_list.write(date)
        food_list.write(" : ")
        food_list.write(client_foods_name)
        food_list.write("\n")
        food_list=open("rohanEx.txt","r")
        print(": ")
        content=food_list.read()
        print(content)
        print("Written Succesfully !!")
        food_list.close()
    elif client_name_data==3 and client_work_data==2:
        client_foods_name=input("Enter foods Name")
        food_list=open("hammadEx.txt","a")
        date=str(getdate())
        food_list.write(date)
        food_list.write(" : ")
        food_list.write(client_foods_name)
        food_list.write("\n")
        food_list=open("hammadEx.txt","r")
        print(": ")
        content=food_list.read()
        print(content)
        print("Written Succesfully !!")
        food_list.close()
    else:
        print("Please for Name Enter 1 to 3 And Work 1 to 2 \n Thanks")
  
    # -----------  Printing data On Your device-------------- 
def client_data_read():
    client_name_data=int(input("Write Your client name\n 1.Harry\n 2.Rohan\n 3.Hammad\n"))
    client_work_data=int(input("which One you want??\n 1.FOOD\n 2.Exercise\n"))
    if client_name_data==1 and client_work_data==1:
        food_list=open("harryFood.txt","r")
        show_list=food_list.read()
        print(show_list)
    elif client_name_data==2 and client_work_data==1:
        food_list=open("rohanFood.txt","r")
        show_list=food_list.read()
        print(show_list)
    elif client_name_data==3 and client_work_data==1:
        food_list=open("hammadFood.txt","r")
        show_list=food_list.read()
        print(show_list)
    elif client_name_data==1 and client_work_data==2:
        food_list=open("harryEx.txt","r")
        show_list=food_list.read()
        print(show_list)
    elif client_name_data==2 and client_work_data==2:
        food_list=open("rohanEx.txt","r")
        show_list=food_list.read()
        print(show_list)
    elif client_name_data==3 and client_work_data==2:
        food_list=open("hammadEx.txt","r")
        show_list=food_list.read()
        print(show_list)
    else:
        print("Please for Name Enter 1 to 3 And Work 1 to 2 \n Thanks")
        


print("----------Welcome to Daily Healh ManageMent----------\n")

print("Which Mode You want to Open\n 1. Entry data \n 2.Print Data\n")
client_choose=int(input())
if client_choose==1:
    client_data_entry()
else:
    client_data_read()
    