start_state=True
while True:
	inputs=input(">").lower()
        if inputs=="help":
                print('''
                        start - to start the car
                        stop  - to stop the car
                        quit  - to quit the game ''')
        elif inputs=="start":
                if start_state:
                        print("car is already started")
                else:
                     	start_state=True
                        print("car started")
        elif inputs=="stop":
                if  not  start_state:
                        print("car is already stopped")
                else:
                     	start_state=False
                        print("car is  stopped now")
        elif inputs=="quit":
                print("bye")
                break
        else:
             	print("I did not understand the command")

