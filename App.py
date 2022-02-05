# -*- coding: utf-8 -*-
"""
black Jack game, Created on Sun Jan 29 2022
"""
import random


card =[["S",1],["S",2],["S",3],["S",4],["S",5],["S",6],
           ["S",7],["S",8],["S",9],["S",10],["S",11],["S",12,],["S",13,],
           ["H",1],["H",2],["H",3],["H",4],["H",5],["H",6],
           ["H",7],["H",8],["H",9],["H",10],["H",11],["H",12,],["H",13,],
           ["C",1],["C",2],["C",3],["C",4],["C",5],["C",6],
           ["C",7],["C",8],["C",9],["C",10],["C",11],["C",12,],["C",13,],
           ["D",1],["D",2],["D",3],["D",4],["D",5],["D",6],
           ["D",7],["D",8],["D",9],["D",10],["D",11],["D",12,],["D",13,]]


def initialize():
    global x_counter
    x_counter = 0
    #data0-4 for player, data5 for dealer
    data0 = []
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    global data 
    data = [data0,data1,data2,data3,data4,data5]
    
    
def add_new_card(i):
    global x_counter        
    data[i].append(x[x_counter+i])    
    x_counter += 1
    return data

def first_card():
    initialize()
    #First, shuffle 48 sheets, arrange them in a row, and store them in x. (It is more consistent than shuffling and cutting out individually later)
    global x
    x = random.sample(card, 48)  
    
    for i in range (6) :
        add_new_card(i)

#Place to store the numbers in each player's hand # 0-4 for players, # 5 for dealers
global sum_2
sum_2 = [0,0,0,0,0,0]

def initialize_number():
    data0_number=[]
    data1_number=[]
    data2_number=[]
    data3_number=[]
    data4_number=[]
    data5_number=[]
    global data_number
    data_number=[data0_number,data1_number,data2_number,data3_number,data4_number,data5_number]

#Players 1-5, store only the numbers in the dealer's hand in another list
def number_seperate():
    initialize_number()
    for i in range(6):
        card_qty = len(data[i])
        for k in range(card_qty):
            data_number[i].append(data[i][k][1]) # data [i] shows the i-th hand. [0] [1] is the first number
    return data_number

#Sort the cards in each position in ascending order of number
def sort():
    for i in range(6):
        data_number[i] = sorted(data_number[i]) 
    return data_number

#Function that returns the number of cards at card position k (k: 0-5)
def card_quantity(k):
    card_quantity = len(data[k])
    return card_quantity


#Function that returns the total value of card position j (j: 0-5)
def card_check(j):
    #Sort the cards in ascending order of numbers
    sort()
    #Count the number of cards
    qty = card_quantity(j)
    #Initialize the sum of the numerical values of position j
    sum_2[j] = 0
    #If there is a picture card, set the number to 10 and add up the numbers on the two cards to store the data.
    for i in range (qty):
         if data_number[j][i] == 11 or data_number[j][i] == 12 or data_number[j][i] == 13 :
             data_number[j][i] = 10
         sum_2[j] = sum_2[j]  + data_number[j][i]
         
    #in the case of black jack    
    if data_number[j][0] == 1 and data_number[j][1] == 10:
            sum_2[j] = 21 
    #if there is Ace in card　and sum_2 is less than 10, add 10 to sum_2    
    if data_number[j][0] == 1 and sum_2[j] <= 11:
           sum_2[j] = sum_2[j] + 10
    #if there is Ace in card　and sum_2 is more than 11, use Ace as 1     
    if data_number[j][0] == 1 and sum_2[j] > 11:
           sum_2[j] = sum_2[j]
           
def check_process(i):
    number_seperate() 
    card_check(i)
   
        
def judgment_against_dealer(player_position):
    if sum_2[player_position] > 21 :
        message ='too bad'
    if sum_2[player_position] == 21: 
        message ='Black Jack　おめでとう'
    elif sum_2[player_position] <= 21 and sum_2[5] > 21:
        message ='あなたの勝ち！　'
    elif sum_2[player_position] <= 21 and sum_2[player_position] > sum_2[5]:
        message ='あなたの勝ち！　さすが！'
    elif sum_2[player_position] <= 21 and sum_2[player_position] == sum_2[5]:
        message ='even'
    else:
        message ='too bad (あなたの負けで～す)'
         
    return message
        




########################################################################
########################################################################
            #Implementing functions for browsers from here #
########################################################################
########################################################################

from flask import Flask, render_template, request
app = Flask(__name__)


#Used in HTML image overlay class
global children
children = ['children1','children2','children3','children4','children5']

@app.route('/')
def index():
    initialize_card_image()
    global data
    data = []
    card_display = display()  
    mode = 'auto_operation'
    return render_template('index.html',
                           card_display = card_display,
                           children = children,
                           mode = mode
                           )

#Need to store image file information to display the card on the screen
def initialize_card_image():
    #card_info0-4 for player, card_info5 for dealer
    card_info0 = []
    card_info1 = []
    card_info2 = []
    card_info3 = []
    card_info4 = []
    card_info5 = []
    global card_info 
    card_info = [card_info0,card_info1,card_info2,card_info3,card_info4,card_info5]
    
    #card_display0-4 for player, card_info5 for dealer
    card_display0 = []
    card_display1 = []
    card_display2 = []
    card_display3 = []
    card_display4 = []
    card_display5 = []
    global card_display 
    card_display = [card_display0,card_display1,card_display2,card_display3,card_display4,card_display5]


#diplay card image (until the first card is distributed)
def display():
    if not data: 
        for i in range(6):
            card_display[i].append('static/card/cover.bmp')       
    else:
        #When the player does not intervene, all the cards are automatically distributed, and when the player intervenes, only the first card is actually stored.
        for i in range(6):
            qty = card_quantity(i)
            for k in range(qty):
                mark = data[i][k][0]   #data [i] shows the i-th position. [0] [0] is the first number
                number = data[i][k][1]
                card_info[i].append(str(mark)+str(number))
                card_display[i].append('static/card/' + str(card_info[i][k]) + '.bmp')

    return card_display,card_info
  
#update card_info after each card destribustion
#Position i-th k-th card information is stored in card_info
def update_card_info(i,k):
    mark = data[i][k][0]  #data [i] shows the position i-th hand. [K] [0] is the first number
    number = data[i][k][1]
    card_info[i].append(str(mark)+str(number))
    card_display[i].append('static/card/' + str(card_info[i][k]) + '.bmp')
    return card_info, card_display

@app.route('/gamestart' , methods=['POST'])
def gamestart():
    play_step1()
    display()  
    mode = 'select_position'
    
    return render_template(
        'index.html',
        data = data,
        mode = mode,
        card_display = card_display,
        children = children) 

#From the start of the game to the point where the first card is dealt
def play_step1():
    initialize_card_image()
    sum_clear()
    first_card()
   
def sum_clear():
    for j in range(6):
        sum_2[j] = 0    
        

#Selection of position to play, until the providing the second card to the selected position
@app.route('/play_step2' , methods=['POST'])
def play_step2():
    global player_position
    player_position = request.form.get("position")
    player_position = int(player_position) - 1  #To match the actual position -1
    mode = 'player_operation'
    for i in range(player_position):
        # Add the second card and process the total
        add_new_card(i)
        update_card_info(i,1)
        check_process(i)
        if sum_2[i] <16:
            add_new_card(i)
            update_card_info(i,2)
        # Add the third card and process the total again
        check_process(i)
        if sum_2[i] <16:
            add_new_card(i)
            update_card_info(i,3)
        # Add the 4th card and process the total again
        check_process(i)
        if sum_2[i] <16:
            add_new_card(i)
            update_card_info(i,4)
        # Add the 5th card and process the total again
        check_process(i)
        
    # Deal a second card to the player's position
    add_new_card(player_position)
    update_card_info(player_position,1)
    check_process(player_position)

    
    return render_template(
        'index.html',
        data = data,
        mode = mode,
        sum_2 = sum_2,
        player_position = player_position,
        card_display = card_display,
        children = children) 


# Behavior in the player's selected position
@app.route('/play_step3' , methods=['POST'])
def play_step3():
    mode = 'player_operation'
    player_select = request.form.get("player_select")
    
    #Count the number of cards the player has
    global player_position
    qty = card_quantity(player_position)
    message =''

    # In case of '1', a card will be provided
    if player_select == '1':
        add_new_card(player_position)
        update_card_info(player_position,qty)
        check_process(player_position)

        #Automatic processing when the total number exceeds 21
        if sum_2[player_position] > 21:
            mode = 'auto_operation' 
            play_step4(player_position)
            message = judgment_against_dealer(player_position)    
        
    #In the case of  '2', the player-operation is finished. Perform the rest of the process           
    if player_select == '2':
        mode = 'auto_operation' 
        play_step4(player_position)
        message = judgment_against_dealer(player_position)
    
    return render_template(
        'index.html',
        data = data,
        mode = mode,
        sum_2 = sum_2,
        message = message,
        card_display = card_display,
        player_position = player_position,
        children = children) 
            
#After dealing cards to positions after the player's selected position, until the end of the game
def play_step4(player_position):    
    for i in range(player_position+1, 6):
        #Add a second card after the player's next position to process the total
        add_new_card(i)
        update_card_info(i,1)
        check_process(i)
        if sum_2[i] <16:
            add_new_card(i)
            update_card_info(i,2)
        # Add the third card and process the total again
        check_process(i)
        if sum_2[i] <16:
            add_new_card(i)
            update_card_info(i,3)
        # Add the 4th card and process the total again
        check_process(i)
        if sum_2[i] <16:
            add_new_card(i)
            update_card_info(i,4)
        # Add the 5th card and process the total again
        check_process(i)    
    
    
#Run
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
