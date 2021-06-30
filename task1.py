import docker
client = docker.from_env()

user_input='''
Press 1 to Run a container :- 
Press 2 to Run a container in the background  :- 
Press 3 to List and manage containers:- 
Press 4 to Stop all running containers:- 
Press 5 to Print the logs of a specific container :- 
Press 6 to List all images :- 
Press 7 to Pull an image :-
Press 8 to Pull an image with authentication  :-  
Press 9 to Commit a container :- 
Perss 0 to exit the program :-
'''


while True: 
    print(user_input)
    # to accept input from user 
    user_choice=input()
    # printing user input 
    #print("user has entered ",user_choice)


    if  user_choice ==  '1' :
      print(client.containers.run("alpine", ["echo", "hello", "world"]))
        
    elif  user_choice  ==  '2' :
      container = client.containers.run("bfirsh/reticulate-splines", detach=True)
      print(container.id)
       
        
    elif  user_choice  ==  '3' : 
      for container in client.containers.list():
        print(container.id)       

    elif  user_choice  ==  '4' :
        for container in client.containers.list():
          container.stop()
    elif  user_choice  ==  '5' :
        container = client.containers.get('f1064a8a4c82')
        print(container.logs()) 

    elif  user_choice  ==  '6' :
        for image in client.images.list():
          print(image.id)

    elif  user_choice  ==  '7' :
        image = client.images.pull("alpine")
        print(image.id)
    
    elif  user_choice  ==  '8' :
      image = client.images.pull("alpine")
      print(image.id)
      
    elif  user_choice  ==  '9' :
      container = client.containers.run("alpine", ["touch", "/helloworld"], detach=True)
      container.wait()
      image = container.commit("helloworld")
      print(image.id)

    elif  user_choice  ==  '0' :
        exit()

    else :
        print("opps! pressed a wrong key... try again")