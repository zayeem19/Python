command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("car started!")
    elif command == "stop":
        print("car stopped")
    elif command == "help":
        print("""
Start - To start car
Stop - To stop car
quit - To end game
    """)
    elif command == "quit":
        break
    else:
        print("i dont understand you")
