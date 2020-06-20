import bcrypt
from pymongo import MongoClient
class RegisterModel:
    def __init__(self):
        print("Object being created")
        self.client = MongoClient()
        self.db = self.client["vishal"]
        self.collection = self.db["users"]
    def insertUser(self, data_username, data_password):
        print("Inserting user", data_username)
        user1 = {"username":data_username, "password":bcrypt.hashpw(data_password.encode(), bcrypt.gensalt())}
        user_id = self.collection.insert_one(user1)
        print("USER ID OF INSERTED",user_id)
    def login(self, data_username, data_password):
        print("Login func called")
        user_to_be_searched = {"username" : data_username}
        user_found = self.collection.find_one(user_to_be_searched)
        print(user_found)
        if user_found is not None:
            if bcrypt.checkpw(data_password.encode(), user_found["password"]):
                print("CORRECT PASSWORD")
                return 1
            else:
                return 0
        else:
            return 0
    def findPost(self, name):
        posts_collection = self.db["posts"]
        post_found = posts_collection.find_one({"name":name})
        print(post_found)
        if post_found:
            return post_found
        else:
            return False