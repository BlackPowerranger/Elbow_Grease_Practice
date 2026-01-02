import sys
import os
import subprocess

if "launched_new_window" not in sys.argv:
    script_path = os.path.abspath(__file__)
    # Use 'start' to open a new separate command window. 
    # /c closes the window after the script ends.
    subprocess.run(f'start cmd /c python "{script_path}" launched_new_window', shell=True)
    sys.exit()


# Loop for restarting the game
while True:
    os.system('cls') # Clear the screen (Windows)

    def showInstructions():
        #print a main menu and the commands
        print('''
              RPG Game
              ========
              Commands:
              go [direction]
              get [item]
              GOAL: ESCAPE THE HOUSE AND GET TO THE GARDEN 
              ''')

    def showStatus():
        #print the player's current status
        print('---------------------------')
        print('You are in the ' + currentRoom)
        #print the current inventory
        print('Inventory : ' + str(inventory))
        #print an item if there is one
        if "item" in rooms[currentRoom]:
            print('You see a ' + rooms[currentRoom]['item'])
        if "monster" in rooms[currentRoom]:
            print("There is a monster here guarding the key! You can 'get closer'.")
        #print the relative position of other rooms
        for direction in rooms[currentRoom]:
            if direction != 'item' and direction != 'monster':
                print('The ' + rooms[currentRoom][direction] + ' is ' + direction)

        print("---------------------------")

    #an inventory, which is initially empty
    inventory = []

    #a dictionary linking a room to other rooms
    rooms = {
        'Hall' : {
            'south' : 'Kitchen',
            'east' : 'Dining Room',
        },
        'Kitchen' : {
            'north' : 'Hall',
            'monster' : True,
            'item' : 'key'
        },
        'Dining Room' : {
            'west' : 'Hall',
            'south' : 'Garden',
            'item' : 'potion'
        },
        'Garden' : {
            'north' : 'Dining Room' }
    }

    #start the player in the Hall
    currentRoom = 'Hall'

    showInstructions()

    #loop forever
    game_over = False
    while True:

        showStatus()

        #get the player's next 'move'
        #.split() breaks it up into a list array
        #e.g. typing 'go east' would give the list:
        #['go','east']
        move = ''
        while move == '':
            move = input('>')

        move = move.lower().split()

        #if they type 'go' first
        if move[0] == 'go':
            #check that they are allowed wherever they want to go
            if len(move) > 1 and move[1] in rooms[currentRoom]:
                #set the current room to the new room
                if rooms[currentRoom][move[1]] == 'Garden' and 'key' not in inventory:
                    print('DOOR LOCKED')
                else:
                    currentRoom = rooms[currentRoom][move[1]]
            #there is no door (link) to the new room
            else:
                print('You can\'t go that way!')

        #if they type 'get' first
        elif move[0] == 'get' :
            if len(move) > 1 and currentRoom == 'Kitchen' and move[1] == 'closer':
                if 'potion' in inventory:
                    print('The monster sees the potion, becomes timid, and retreats.')
                    del rooms['Kitchen']['monster']
                else:
                    print('The monster attacks! You died.')
                    game_over = True
                    break
            #if the room contains an item, and the item is the one they want to get
            elif len(move) > 1 and "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                #special check for key in Kitchen
                if currentRoom == 'Kitchen' and 'monster' in rooms['Kitchen']:
                    print('MONSTER GROWLS! It is guarding a key. You can "get closer" to inspect it.')
                else:
                    #add the item to their inventory
                    inventory += [move[1]]
                    #display a helpful message
                    print(move[1] + ' got!')
                    #delete the item from the room
                    del rooms[currentRoom]['item']
            #otherwise, if the item isn't there to get
            else:
                #tell them they can't get it
                item_name = move[1] if len(move) > 1 else "nothing"
                print('Can\'t get ' + item_name + '!')
            
        # Invalid command catch-all
        else:
            print("\nInvalid command!")
            print("Available commands in this room:")
            # List valid directions
            for direction in rooms[currentRoom]:
                if direction != 'item' and direction != 'monster':
                    print(f"  - go {direction}")
            # List valid items
            if "item" in rooms[currentRoom]:
                print(f"  - get {rooms[currentRoom]['item']}")
            # List special interactions
            if "monster" in rooms[currentRoom]:
                print("  - get closer")
            
            input("\nPress Enter to continue...")


        if currentRoom== 'Garden' and 'key' in inventory:
            print("You escaped the house... You won!")
            game_over = True
            break
            
    if game_over:
        while True:
            choice = input("\nPlay again? (y/n): ").lower()
            if choice == 'y':
                break # Break inner loop, continue outer loop (restart)
            elif choice == 'n':
                sys.exit() # Exit script (closes window)
            else:
                print("Please enter 'y' or 'n'.")
