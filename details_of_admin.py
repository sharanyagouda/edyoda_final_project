from admin import Admin_details
from food_items import Food

class Admin:
    admin_list=[]
    food_list=[]
    def add_details(self):
        print("*********ADDING ADMIN DETAILS***********")
        admin_full_name=input("enter admin full name")
        admin_phone_number=int(input("enter admin phone number"))
        admin_password=input("enter admin password")
        admin_address=input("enter admin address")
        admin_email=input("enter admin email")
        admin_obj=Admin_details(admin_full_name,admin_phone_number,admin_email,admin_address,admin_password)
        self.admin_list.append(admin_obj)
        print(self.admin_list)
        
    def add_food_details(self):
        print("***********ADDING FOOD DETAILS************")
        food_id=int(input("enter food id")) 
        val1=food_id
        food_name=input("enter food name")
        val2=food_name
        food_quantity=int(input("enter food quantity"))
        val3=food_quantity
        food_price=float(input("enter food price"))
        val4=food_price
        food_discount=int(input("enter food discount"))
        val5=food_discount
        food_stock=int(input("enter food stock"))
        val6=food_stock
        food_obj=Food(food_id,food_name,food_quantity,food_price,food_discount,food_stock)
        self.food_list.append(food_obj)
        keys=("FOOD ID","FOOD NAME","FOOD QUANTITY","FOOD PRICE","FOOD DISCOUNT","FOOD STOCK")
        values=(val1,val2,val3,val4,val5,val6)
        dic=dict(zip(keys,values))


        return dic

    def view_food_item(self):
        print("***************VIEW FOOD ITEMS*************")
        for i in self.food_list:
            print(i)

    def edit_food_item(self):
        print("*************EDIT FOOD ITEMS***************")
        edit_food_id=int(input("enter food id"))
        print("select option")
        print("1.edit food name")
        print("2.edit  food quantity")
        print("3.edit food price")
        print("4.edit food discount")
        print("5.edit food stock")
        choice=int(input("enter your choice"))
        
        if choice==1:
            for j in self.food_list:
                if edit_food_id==j.food_id:
                    j.food_name=input("enter food name")
                    print("food name updated successfully") 
                    print(j.food_name)   
                
        elif choice==2:
            for j in self.food_list:
                if edit_food_id==j.food_id:
                    j.food_quantity=input("enter food quantity")
                    print("food quantity updated successfully") 
                    print(j.food_quantity)
                

        elif choice==3:
            for j in self.food_list:
                if edit_food_id==j.food_id:
                    j.food_price=float(input("enter food price")) 
                    print(" food price updated successfully")
                    print("UPDATE FOOD PRICE:",j.food_price)   
                    

        elif choice==4:
            for j in self.food_list:
                if edit_food_id==j.food_id:
                    j.food_discount=int(input("enetr food discount"))
                    print("food discount updated successfully")
                    print(j.food_discount)
                    
        elif choice==5:
            for j in self.food_list:
                if edit_food_id==j.food_id:
                    j.food_stock=int(input("enter food stock"))
                    print("food stock updated successfully")   
                    

        else:
            print("invalid choice")       

    def delete_food_item(self):
        print("************DELETE FOOD ITEMS**************")
        del_food_id=int(input("enter food id"))
        for food in self.food_list:
            if del_food_id==food.food_id:
                print("food item deleted successfully")
            else:
                pass    






                



        


   