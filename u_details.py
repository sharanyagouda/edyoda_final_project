
from admin import User_details


order_list=[]
food_info={"dict1":{"food name":"tandoori",
                    "food price":"240rs",
                    "food quantity":"5 pieces"
},
                    "dict2":{"food name":"vegan burger",
                    "food price":"120rs",
                    "food quantity":"1 piece"

}


}
food_list={}
user_list=[]
class UserFunction:

    user_list=[]
    def add_user(self):
        print("***********ADDING USER DETAILS**********")
        user_full_name=input("enter user full name")
        user_phone_number=int(input("enter user phone number"))
        user_email=input("enter user email")
        user_address=input("enter user address")
        user_password=input("enter user password")
        user_obj=User_details(user_full_name,user_phone_number,user_email,user_address,user_password)
        self.user_list.append(user_obj)

    def update_profile(self):
        print("************UPDATE PROFILE************")
        update_username=input("enter username")
        print("select option")
        print("1.update user phone number")
        print("2.update  user email")
        print("3.update user address")
        print("4.update user password")
        option=int(input("enter option"))
        if option==1:
            for i in self.user_list:
                print(i.user_full_name)
                if i.user_full_name == update_username:
                    i.user_phone_number=int(input("enter phone number"))
                    print("user phone number update successfully")
                    
        elif option==2:
            for i in self.user_list:
                if i.user_full_name == update_username:
                    i.user_email=input("enter email id")
                    print("user email updated succeccfully")
                    

        elif option ==3:
            for i in self.user_list:
                if i.user_full_name==update_username:
                    i.user_address=input("enter address")
                    print("user address updated successfully")
                    

        elif option ==4:
            for i in self.user_list:
                if i.user_full_name==update_username:
                    i.user_password=input("enter password")
                    print("user passsword updated successfully")
                    

        else:
            print("invalid option")        
            
    def place_new_order(self):
        print("***********NEW ORDER**********")
        for j in range(len(food_info)):
            print("select food item\n1.dict1\n2.dict2\n3.press 3 to quit")
            choice=int(input("enter choice"))
            if choice==1:
                print(food_info["dict1"])
                order_list.append(food_info["dict1"])
                
            elif choice==2:
                print(food_info["dict2"])
                order_list.append(food_info["dict2"])
                
            else:
                
                break        
        print("TOTAL_ORDER:",order_list)



        
    def order_history(self):
        print("***********ORDER HISTORY********")
        print(order_list)    

            
        



    




                  



        





