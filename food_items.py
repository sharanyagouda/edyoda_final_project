class Food:
    def __init__(self,food_id,food_name,food_quantity,food_price,food_discount,food_stock):
        self.food_id=food_id
        self.food_name=food_name
        self.food_quantity=food_quantity
        self.food_price=food_price
        self.food_discount=food_discount
        self.food_stock=food_stock

    def __str__(self):
        return f"FOOD ID:{self.food_id}\nFOOD NAME:{self.food_name}\nFOOD QUANTITY:{self.food_quantity}\nFOOD PRICE:{self.food_price}\nFOOD DISCOUNT:{self.food_discount}\nFOOD STOCK:{self.food_stock}"

    def get_food_id(self):
        return self.food_id

    def set_food_id(self,food_id):
        self.food_id=food_id

    def get_food_name(self):
        return self.food_name

    def set_food_name(self,food_name):
        self.food_name=food_name

    def get_food_quantity(self):
        return self.food_quantity

    def set_food_quantity(self,food_quantity):
        self.food_quantity=food_quantity

    def get_food_price(self):
        return self.food_price  

    def set_food_price(self,food_price):
        self.food_price=food_price  

    def get_food_discount(self):
        return self.food_discount       

    def set_food_discount(self,food_discount):
        self.food_discount=food_discount     

    def get_food_stock(self):
        return self.food_stock

    def set_food_stock(self,food_stock):
        self.food_stock=food_stock                                
