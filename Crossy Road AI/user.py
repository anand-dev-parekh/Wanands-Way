import pymongo
from urllib.parse import quote_plus
from stage import Stage

class User:

    def __init__(self):

        password = quote_plus("PASSWORDHERE")
        cluster = pymongo.MongoClient(f"mongodb+srv://Onion8:{password}@cluster0.tbrc1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = cluster["WanandsWay"]
        self.collection = db["wanandData"]
        
        self.__mode = 0 #Which textbox user is clicked on
        #0 represents nothing, 1 represents username, 2 represents password

        self.__user_name = ""
        self.__password = ""
        self.__error_message = ""

        self.__leaderboard = None
        self.__interval = 1

    
    def edit_active(self, char):
        """
        Adds character to the active textbox
        :param char: char OR String
        """
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
        """
        Checks to see if user's attributes are valid to LOGIN or to REGISTER
        :param stage: Stage 
        """
        acc = self.collection.find_one({"name": self.__user_name})

        if stage is Stage.RPASSWORD:
            
            if acc == None:
                self.collection.insert_one({"name": self.__user_name, "password": self.__password, "score": 0})
                return True

            else: #if account is not None then it already exists
                self.__error_message = "User already exists"

        elif stage is Stage.LPASSWORD:
            if acc == None: #if account is None, then doesn't exist
                self.__error_message = "Account does not exist"

            else:
                if acc["password"] == self.__password: 
                    return True
                self.__error_message = "Wrong Password"
        
        return False

    def update_score(self, score):
        """
        Updates users max score if it is greater than current max
        :param score: int
        """
        acc = self.collection.find_one({"name": self.__user_name})
        if score > acc["score"]:
            self.collection.update_one({"name": self.__user_name}, {"$set":{"score": score}})
    

    def update_leaderboard(self):
        """
        Updates leaderboard with request to mongoDB server
        """
        top_li = []
        for user in self.collection.find():
            top_li.append((user["name"], user["score"]))
        top_li.sort(key = lambda x: -1 * x[1])
        self.__leaderboard =  top_li
            
    def change_leaderboard_display(self, change):
        if self.__interval + change == 0 or ((self.__interval + change) * 10) - len(self.__leaderboard) >= 10:
            return

        self.__interval += change

    def logout(self):
        self.__mode = 0
        self.__user_name = ""
        self.__password = ""
        self.__error_message = ""
        self.__leaderboard = None
        self.__interval = 1


        
    #****GETTERS****
    def get_leaderboard(self):
        return self.__leaderboard


    def get_user_name(self):
        return self.__user_name

    def get_password(self):
        return self.__password
    
    def get_error_message(self):
        return self.__error_message    

    def get_interval(self):
        return self.__interval
    
    #****SETTERS****
    def set_mode(self, mode):
        self.__mode = mode



if __name__ == "__main__":
    pass