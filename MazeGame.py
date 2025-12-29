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
    #print the relative position of other rooms
    for direction in rooms[currentRoom]:
        if direction != 'item':
            print('The ' + rooms[currentRoom][direction] + ' is ' + direction)

    print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {
    'Hall' : {
        'south' : 'Kitchen',
        'east' : 'Dining Room',
        'item' : 'key'

    },
    'Kitchen' : {
        'north' : 'Hall',
        'item' : 'monster'
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
while True:

    showStatus()

    if currentRoom == 'Kitchen' and 'item' in rooms['Kitchen'] and rooms['Kitchen']['item'] == 'monster':
        print('MONSTER GROWLS! You can "get closer"')

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
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            if rooms[currentRoom][move[1]] == 'Garden' and 'key' not in inventory:
                print('DOOR LOCKED')
            else:
                currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        if currentRoom == 'Kitchen' and move[1] == 'closer':
            if 'potion' in inventory:
                print('The monster sees the potion, becomes timid, and retreats.')
                del rooms['Kitchen']['item']
            else:
                print('The monster attacks! You died.')
                break
        #if the room contains an item, and the item is the one they want to get
        elif "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    if currentRoom== 'Garden' and 'key' in inventory and 'potion' in inventory:
        print("You escaped the house... You won!")
        break
