from details_of_admin import Admin
from u_details import UserFunction


class Main:
    
    def __init__(self,admin_obj,user_obj):
        self.admin_obj=admin_obj
        self.user_obj=user_obj

    def execute(self,choice):
        if choice==1:
            print("********CREATE ADMIN ACCOUNT******")
            admin_obj=Admin()
            admin_obj.add_details()

        elif choice==2: 
            print("*********** CREATE USER ACCOUNT**********")
            user_obj=UserFunction()
            user_obj.add_user()
            
        elif  choice==3:
            print("************ADMIN LOGIN*************")
            admin_obj=Admin()
            a_name=input("enter admin name")
            a_password=input("enter password") 
            for i in Admin.admin_list:
                if a_name==i.admin_full_name and a_password==i.admin_password:
                    print("*********login successfull!********")
                    print("enter choice\n1.add food items\n2.view food items\n3.edit food items\n4.delete food item")
                    choice=int(input("enter your choice"))
                    if choice==1:
                        admin_obj=Admin()
                        admin_obj.add_food_details()
                        
                    elif choice==2:
                        admin_obj=Admin()
                        admin_obj.view_food_item()
                        
                    elif choice==3:
                        admin_obj=Admin()
                        admin_obj.edit_food_item()
                        
                    elif choice==4:
                        admin_obj=Admin()
                        admin_obj.delete_food_item()
                        
                    else:
                        break  
                else:
                    print("---------------------")
                    print("wrong credentials,please try again!")  
                    
           
        elif choice==4:
            print("**************USER LOGIN************")
            user_obj=UserFunction()     
            u_name=input("enter user name")
            u_password=input("enter user password")
            for i in UserFunction.user_list:
                if u_name==i.user_full_name and u_password == i.user_password:
                    print("**********LOGIN SUCCESSFULL!***********")
                    print("select option\n1.place new order\n2.order history\n3.update profile")
                    option=int(input("enter option"))
                    if option==1:
                        user_obj=UserFunction()
                        user_obj.place_new_order()
                        
                    elif option ==2:
                        user_obj=UserFunction()
                        user_obj.order_history()
                        
                    elif option ==3:
                        user_obj=UserFunction()
                        user_obj.update_profile()
                        
                    else:
                        print("*****invalid option*****")
                        break    
                else:
                    print("-------------------------")
                    print("wrong credential,please try again!")    
                    
        else:
            print("invalid choice")
            print(quit())        
         
if __name__=="__main__":
    admin_obj=Admin() 
    user_obj=UserFunction()    
    main=Main(admin_obj,user_obj)     

    while True:
        print("enter choice\n1.create admin account\n2.create user account\n3.admin login\n4.user login")
        choice=int(input("enter your choice"))
        main.execute(choice)    
        

