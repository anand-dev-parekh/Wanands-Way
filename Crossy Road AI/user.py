import pymongo
from urllib.parse import quote_plus
from stage import Stage

class User:

    def __init__(self):

        password = quote_plus("DAPASSWORD")
        cluster = pymongo.MongoClient(f"mongodb+srv://Onion8:{password}@cluster0.tbrc1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = cluster["WanandsWay"]
        self.collection = db["wanandData"]


        self.__user_name = ""
        self.__password = ""
        self.__mode = 0 #Which textbox user is clicked on
        #0 represents nothing, 1 represents username, 2 represents password
        self.__error_message = ""

    
    def change_mode(self, mode):
        self.__mode = mode
    
    def edit_active(self, char):
            
        if self.__mode == 1:
            if char == "\b":
                self.__user_name = self.__user_name[:-1]
            else: 
                self.__user_name += char

        elif self.__mode == 2:
            if char == "\b":
                self.__password = self.__password[:-1]
            else:
                self.__password += char


    def connect_account(self, stage):
        acc = self.collection.find_one({"name": self.__user_name})

        if stage is Stage.RPASSWORD:

            if acc == None:
                self.collection.insert({"name": self.__user_name})
                self.collection.update_one({"name": self.__user_name}, {"$set": {"password": self.__password, "score": 0}})
                return True

            else:
                self.__error_message = "User already exists"

        elif stage is Stage.LPASSWORD:
            if acc == None:
                self.__error_message = "Account does not exist"

            else:
                if acc["password"] == self.__password:
                    return True
                self.__error_message = "Wrong Password"
        
        return False


    #****GETTERS****
    def get_user_name(self):
        return self.__user_name

    def get_password(self):
        return self.__password
    
    def get_error_message(self):
        return self.__error_message