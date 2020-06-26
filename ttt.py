import random
box = ['-','-','-',
      '-','-','-',
      '-','-','-']
new_list = ['x', 'o']
player = random.choice(new_list)
def display():
    print(box[0]+' . '+box[1]+' . '+box[2]+'\n'+
         box[3]+' . '+box[4]+' . '+box[5]+'\n'+
         box[6]+' . '+box[7]+' . '+box[8])
def win():
    global player
    for i in range(0,3):
        if box[i] == box[i+3] == box[i+6] and box[i]!= '-':
            print(player + " Wins")
            exit()
    for i in range(0,9,3):
        if box[i] == box[i+1] == box[i+2] and box[i]!='-':
            print(player + " Wins")
            exit()
    if (box[0] == box[4] == box[8] and box[0]!= '-') or (box[2] == box[4] == box[6] and box[2]!= '-'):
            print(player + " Wins")
            exit()
def tie():
    if '-' not in box:
        print("It's a tie.")
        exit()
def play():
    global player
    if player == 'x':
        player = 'o'
    elif player == 'o':
        player = 'x'
    print(player + '\'s Turn')
    a = input("Choose a place from 1-9")
    while a not in['1','2','3','4','5','6','7','8','9'] or box[int(a)-1]!='-':
        a = input("Cannot do this. Please Enter a choice between 1-9:")
    box[int(a)-1] = player
    display()
    win()
    tie()
while True:
    play()
