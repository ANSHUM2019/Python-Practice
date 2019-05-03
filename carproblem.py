command=""
print("Write Help")
while command !="quit" :
    command=input(">").lower()
    if command=="start":
        print("The car is started")

    elif command=="stop":
        print("The car is stopped")

    elif command=="help":
        print("""
        write start=To start the car
        write stop=To stop the car
        write quit=To exit
        """)
    elif command=="quit":
        print("You are successfully exited")
        break
    else :
        print("Sorry i don't understand")
