class Chatbook:
    def __init__(self):
        self.user_name = ""
        self.password = ""
        self.logged_in = False
        self.menu()
        
    def menu(self):
        user_input = input(""""welcome to chatbook, how would you like to proceed? 
                           \n 1. press 1 to Signup
                           \n 2. press 2 to Signin
                           \n 3. press 3 to Write a post 
                           \n 4. press 4 to msg to freinds
                           \n 5. press 5 to Logout""")    
        
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
            
            
obj = Chatbook()            
            