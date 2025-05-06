

class User:
    organisation= "google"

    def __init__(self, username, password):
        self.username=username
        self.__password=password
    def getpassword(self):
        return self.__password
    def setpassword(self, new_password):
        self.__password=new_password
        
    def login(self,password):
        if self.__password==password:
           print("Your login has been sucessful :)")
        else:
            print("Please try again later... :(")

user1=User("Hi@43326","12345")
print(user1.organisation) 
print(user1.username) 
#print(user1.password)
print(user1.getpassword())
user1.login("abcdefgH1")
user2=User("Bye@43369","abcdefgHI")
print(user2.organisation)  
print(user2.username)
#print(user2.password)
print(user2.getpassword())
user2.setpassword("ilovepython")
user2.login("abcdefgHI")