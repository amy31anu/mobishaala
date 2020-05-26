import base64

class insta_user():
    '''
        This class is defined for a insta_user
    '''
    def __init__(self):
        #constructor
        self.username = None
        self.__password = None
        self.login = False
        self.myposts = []
        self.followers = []
        self.following = []
        self.feed = []

    def create_new_user(self, username, password):
        #This method creates a new user
        self.username = username
        self.__password = password
        
    def login_user(self, username, password):
        #This method logs in a user and the boolean value of login becomes True
        self.login = True
        
class insta_post(insta_user):
    def __init__(self):
        self.uname = None
        self.post_name = None
        self.liked = False
        self.likes = []
        
    def add_post(self,Username,post_name):
        #This method creats a new post
        self.post_name = post_name
        self.uname = Username
        
print("Enter your choice:\n1) Create an account\n2) Login\n3) Add a post \n4) Like a post \n5) Search Profile \n6) Follow someone \n7) View Feed")
obj_list=[]
while True:
    ip=input("\nChoice:   ")
    if ip=="1":
        #Takes in UserName and Password and creates an object "obj" and adds it to obj_list
        #Here obj_list keeps track of the list of all the instagram users
        username=input("Enter UserName: ")
        password=input("Enter Password: ")
        obj=insta_user()
        obj.create_new_user(username,password)
        obj_list.append(obj)
        
    elif ip=="2":
        #Takes in UserName and Password if that matches with any user in obj_list, it initiates their login value to True
        #If user not found it prints a message
        done=0
        Username=input("Enter UserName: ")
        Password=input("Enter Password: ")
        num_of_users=len(obj_list)
        for i in range(num_of_users):
            if obj_list[i].username==Username and obj_list[i]._insta_user__password==Password:
                obj_list[i].login=True
                done += 1
        if done==0:
            print("Login failed.Please try again!!")
                
    elif ip=="3":
        #Takes in Username and Post_name
        #If user is logged in then it saves the post to user's profile, user's feed and his followers feed(stack).
        #Else it prints error message.
        done=0
        Username=input("Enter UserName: ")
        Post_name=input("Enter Postname: ")
        num_of_users=len(obj_list)
        for i in range(num_of_users):
            if obj_list[i].username==Username:
                done += 1
                if obj_list[i].login==True:
                    post=insta_post()
                    post.add_post(Username,Post_name)
                    obj_list[i].myposts.append(post)
                    obj_list[i].feed.append(post)
                    for z in obj_list[i].followers:
                        for z1 in range(num_of_users):
                            if obj_list[z1].username==z:
                                break
                        obj_list[z1].feed.append(post)
                else:
                    print("Please login...")
        if done==0:
            print("User not found")
            
    elif ip=="4":
        #Takes in YourUsnm(The person who opened instagram to see it)
        #Takes in pstUsnm(The name of the person who posted the post)
        #Takes in Post_name
        #If the user with YourUsnm is logged in it serches for a person with pstUsnm and a post with Post_name belonging to pstUsnm
        #If it is found, then YourUsnm likes the the post(Post_name) of pstUsnm and YourUsnm is added to the likes[] of that post.
        #Else it prints error message.
        getme=0
        getpu=0
        getp=0
        YourUsnm=input("Enter your UserName: ")
        pstUsnm=input("Enter UserName of the person who owns the post: ")
        Post_name=input("Enter Postname: ")
        for i in range(num_of_users):
            if obj_list[i].username==YourUsnm:
                getme += 1
                if obj_list[i].login==False:
                    print("please login...")
                else:
                    for index, item in enumerate(obj_list):
                        if item.username == pstUsnm:
                            getpu += 1
                            break
                    if getpu == 1:
                        for p in obj_list[index].myposts:
                            if p.post_name==Post_name:
                                getp += 1
                                #p.like_post(YourUsnm,pstUsnm,Post_name)
                                if YourUsnm not in p.likes:
                                    p.likes.append(YourUsnm)
                                else:
                                    now=p.likes.index(YourUsnm)
                                    del p.likes[now]
                        if getp==0:
                            print("No such posts available")
                    else:
                        print("No such kind of username")
        if getme==0:
            print("your username is wrong.Please try again")
            
    elif ip=="5":
        #Takes in User1 and User2 as input
        #If User1 is logged in then if User2 is present in obj_list then User1 can view the profile of User2
        #Here the profile consists of Name, list of followers, list of following members and its posts showing whether User1 liked a post or not along with the total number of likes.
        #Else it prints an error message
        u1p=0
        u2p=0
        User1=input("Enter your UserName: ")
        User2=input("Enter UserName of the person whose profile you wanna open: ")
        for index, item in enumerate(obj_list):
            if item.username == User1 and item.login==True:
                u1p += 1
                break
        if u1p==1:
            for index1, item in enumerate(obj_list):
                if item.username == User2:
                    u2p += 1
                    break
            if u2p==1:
                print("----------------------------------------------------------------------------")
                print("Name: ",obj_list[index1].username)
                l1=len(obj_list[index1].followers)
                l2=len(obj_list[index1].following)
                print("Followers:  ",l1)
                print(obj_list[index1].followers)
                print("Following:  ",l2)
                print(obj_list[index1].following)
                print("Posts: ")
                for i in obj_list[index1].myposts:
                    if User1 in i.likes:
                        print(i.post_name,"                    liked: Yes    total likes: ",len(i.likes))
                    else:
                        print(i.post_name,"                    liked: No     total likes: ",len(i.likes))
                print("----------------------------------------------------------------------------")
            else:
                print("No such user exists...")
        else:
            print("Please login with correct details..")
    
    elif ip=='6':
        #Takes in User1 and User2
        #If User1 is logged in and User2 is an valid account then User1 follows User2
        #The above is indicated by adding User1 to follower list of User2
        #and also adds User2 to the following list of User1
        #Else it prints error message.
        u1p=0
        u2p=0
        User1=input("Enter your UserName: ")
        User2=input("Enter UserName of the person whom you wanna follow: ")
        for index, item in enumerate(obj_list):
            if item.username == User1 and item.login==True:
                u1p += 1
                break
        if u1p==1:
            for index1, item in enumerate(obj_list):
                if item.username == User2:
                    u2p += 1
                    break
            if u2p==1:
                obj_list[index].following.append(User2)
                obj_list[index1].followers.append(User1)
            else:
                print("No such user exists to follow...")  
        else:
            print("Please login with correct details..")
                    
    elif ip=="7":
        #Takes in User1 as input and if he is logged in it presents the feed of User1 and clears the feed(stack)
        #This greatly optimizes the space and time and he can view any posts of a person using choice value as 5.
        #Else it prints error message.
        u1p=0
        User1=input("Enter your UserName: ")
        for index, item in enumerate(obj_list):
            if item.username == User1 and item.login==True:
                u1p += 1
                break
        if u1p==1:
            for i in range(len(obj_list[index].feed)):
                fp=obj_list[index].feed.pop()
                if User1 in fp.likes:
                    print("UserName: ",fp.uname,"    PostName: ",fp.post_name,"      liked: Yes    total likes: ",len(fp.likes))
                else:
                    print("UserName: ",fp.uname,"    PostName: ",fp.post_name,"      liked: No     total likes: ",len(fp.likes))
        else:
            print("Please login with correct details")
        
    else:
        break
