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
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.MyPost()
        elif user_input == "4":
            self.msg()
        else:
            exit()
            
    def signup(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        
        self.user_name = email
        self.password = password
        
        print(f"Signup successful! Welcome, {self.user_name}!")
        print("/n")
        self.menu()
        
    def signin(self):
        if self.user_name == "" and self.password == "":
            print("No user found. Please sign up first.")
        else:
            input_email = input("Enter your email: ")
            input_password = input("Enter your password: ")
            
            if input_email == self.user_name and input_password == self.password:
                print(f"Signin successful! Welcome back, {self.user_name}!")
                self.logged_in = True
            else:
                print("Invalid email or password. Please try again.")
        
        print("/n")
        self.menu()
    
    def MyPost(self):
        if self.logged_in:
            post_content = input("Enter your post content: ")
            print(f"Post created: {post_content}")
        else:
            print("You need to sign in first to create a post.")
        
        print("/n")
        self.menu()                   
               
               
    def msg(self):
        if self.logged_in:
            friend_name = input("Enter your friend's name: ")
            message_content = input("Enter your message: ")
            print(f"Message sent to {friend_name}: {message_content}")
        else:
            print("You need to sign in first to send messages.")
        
        print("/n")
        self.menu()           
               
#obj = Chatbook()            
            