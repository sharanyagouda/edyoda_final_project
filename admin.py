class Admin_details:

    def __init__(self,admin_full_name,admin_phone_number,admin_email,admin_address,admin_password):
        self.admin_full_name=admin_full_name
        self.admin_phone_number=admin_phone_number
        self.admin_email=admin_email
        self.admin_address=admin_address
        self.admin_password=admin_password

    def __str__(self):
        return f"FULL NAME:{self.admin_full_name}\nPHONE NUMBER:{self.admin_phone_number}\nEMAIL:{self.admin_email}\nADDRESS:{self.admin_address}\nPASSWORD:{self.admin_password}"


    def get_admin_full_name(self): 
        return self.admin_full_name

    def set_admin_full_name(self,admin_full_name):
        self.admin_full_name=admin_full_name

    def get_admin_phone_number(self):
        return self.admin_phone_number

    def set_admin_phone_number(self,admin_phone_number):
        self.admin_phone_number=admin_phone_number

    def get_admin_email(self):
        return self.admin_email

    def set_admin_email(self,admin_email):
        self.admin_email=admin_email

    def get_admin_address(self):
        return self.admin_address

    def set_admin_address(self,admin_address):
        self.admin_address=admin_address

    def get_password(self):
        return self.admin_password

    def set_password(self,admin_password):
        self.admin_password=admin_password    

class User_details:

    def __init__(self,user_full_name,user_phone_number,user_email,user_address,user_password):
        self.user_full_name=user_full_name
        self.user_phone_number=user_phone_number
        self.user_email=user_email
        self.user_address=user_address
        self.user_password=user_password

    def __str__(self):
        return f"FULL NAME:{self.user_full_name}\nPHONE NUMBER:{self.user_phone_number}\nEMAIL:{self.user_email}\nADDRESS:{self.user_address}\nPASSWORD:{self.user_password}"                  

    def get_user_full_name(self):
        return self.user_full_name

    def set_user_full_name(self,user_full_name):
        self.user_full_name=user_full_name

    def get_user_phone_number(self):
        return self.user_phone_number

    def set_user_phone_number(self,user_phone_number):
        self.user_phone_number=user_phone_number

    def get_user_email(self):
        return self.user_email

    def set_user_email(self,user_email):
        self.user_email=user_email

    def get_user_address(self):
        return self.user_address

    def set_user_address(self,user_address):
        self.user_address=user_address

    def get_user_password(self):
        return self.user_password  

    def set_user_password(self,user_password):
        self.user_password=user_password                                