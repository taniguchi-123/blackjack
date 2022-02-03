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
    #最初に48枚をシャッフルして1列に並べてxに格納しておく。（あとで個別にシャッフルして切り出すよりも整合性がよい） 
    global x
    x = random.sample(card, 48)  
    
    #手持ちデータをdataに格納
    for i in range (6) :
        add_new_card(i)

#各プレーヤーの手札の数値を格納する場所　#0～4がプレーヤー、#5がディーラー
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

#プレーヤー1～5、ディーラーの手札の数字のみを別のリストに格納する
def number_seperate():
    initialize_number()
    for i in range(6):
        card_qty = len(data[i])
        for k in range(card_qty):
            data_number[i].append(data[i][k][1]) #data[i]までがi番目の手札をしめす。　[0][1]は1枚目の数字
    #print(data_number)
    return data_number


#各ポジションのカードを番号の小さい順にソート
def sort():
    for i in range(6):
        data_number[i] = sorted(data_number[i]) 
    return data_number

#カードポジションk(k:0～5)のカード枚数を返す関数
def card_quantity(k):
    card_quantity = len(data[k])
    return card_quantity


#特定のカードのみを判定する（カード情報の合計を計算）　
#カードポジションj(j:0～5)の合計値を返す関数
def card_check(j):
    #手持ちカードを数字の低い順に並べ替える
    sort()
    #手持ちカード枚数を数える    
    qty = card_quantity(j)
    #ポジションｊの数値の合計を初期化する    
    sum_2[j] = 0
    #絵札がある場合は数字を10にして2枚のカードの数字を合計してデータを格納する                
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
   
#プレーヤーの選んだポジションを処理するフロー (コンソール上での動作)
def select_position():
    s = input('希望のカードを入力してください\n1番目(1)／2番目(2)／3番目(3)／4番目(4)／5番目(5)】')
    player_position = int(s)   #make a list for replace card 
    if player_position >0 and player_position <= 5:
        return player_position
    else:
        print('1から5の数値を入力してください')

#コンソール上でプレイするときのコマンド        
def player_operation(i):
    #3枚目のカードをもらうかどうか
    s = input('番号を押してください。\n【カードをもらう(1)／そのままにする(2)】')
    player_decision = int(s)   #1 or 2 
    if player_decision == 1:
        card_provide_to_player(i)
        
        #4枚目のカードをもらうかどうか
        s = input('番号を押してください。\n【カードをもらう(1)／そのままにする(2)】')
        player_decision = int(s)   #1 or 2 
        if player_decision == 1:
            card_provide_to_player(i)
            
    elif player_decision == 2:
        check_process(i)
        print(data[i],sum_2[i])

#コンソール上でプレイするときのコマンド    
def card_provide_to_player(i):
    add_new_card(i)
    check_process(i)
    print(data[i],sum_2[i])
        
#コンソール上でプレイするときのコマンド    
def play():
    first_card()
    print(data)
    player_position = select_position() - 1  #プレーヤの選んだポジション。ループ状は0からなので-1しておく
    
    for i in range(6):
        if i == player_position:
            card_provide_to_player(i)
            player_operation(i)
            continue
      
        #2枚目のカードを加えて合計処理
        check_process(i)
        if sum_2[i] <=16:
            add_new_card(i)
        #3枚目のカードを加えて再度合計処理
        check_process(i)
        if sum_2[i] <=16:
            add_new_card(i)
        #4枚目のカードを加えて再度合計処理
        check_process(i)
        if sum_2[i] <=16:
            add_new_card(i)
        #5枚目のカードを加えて再度合計処理
        check_process(i)
        
        #デバッグ用と出力確認用）        
        print(data[i],sum_2[i])
        judgment_against_dealer(player_position)
        
def judgment_against_dealer(player_position):
    if sum_2[player_position] > 21 :
        print('too bad')
        message ='too bad'
    if sum_2[player_position] == 21: 
        print('you win')
        message ='Black Jack　おめでとう'
    elif sum_2[player_position] <= 21 and sum_2[5] > 21:
        print('you win')
        message ='あなたの勝ち！　'
    elif sum_2[player_position] <= 21 and sum_2[player_position] > sum_2[5]:
        print('you win')
        message ='あなたの勝ち！　さすが！'
    elif sum_2[player_position] <= 21 and sum_2[player_position] == sum_2[5]:
        print('even')
        message ='even'
    else:
        message ='too bad (あなたの負けで～す)'
         
    return message
        
#コンソール上で動作させる場合は下記を実行（現在は#でエスケープ）    
#play()



########################################################################
########################################################################
                       #ここからブラウザ用に機能実装#
########################################################################
########################################################################

from flask import Flask, render_template, request
app = Flask(__name__)



#HTMLの画像重ね表示のclassで利用
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

#カードを画面に表示するために画像ファイルの情報を格納必要
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


#diplay card image (～1枚目のカード配布まで)
def display():
    if not data: 
        for i in range(6):
            card_display[i].append('static/card/cover.bmp')       
    else:
        #プレーヤが介在しないときは全部のカードを自動で配布、プレーヤーが介在するときは実際には再世の1枚目だけを格納する
        for i in range(6):
            qty = card_quantity(i)
            for k in range(qty):
                mark = data[i][k][0]  #data[i][0][0] #data[i]までがポジションi番目の手札をしめす。　[0][0]は1枚目の数字            
                number = data[i][k][1]
                card_info[i].append(str(mark)+str(number))
                card_display[i].append('static/card/' + str(card_info[i][k]) + '.bmp')

    return card_display,card_info
  
#update card_info after each card destribustion
#ポジションi番目のk番目のカード情報をcard_infoに格納する   
def update_card_info(i,k):
    mark = data[i][k][0]  #data[i][k][0] #data[i]までがポジションi番目の手札をしめす。　[k][0]は1枚目の数字            
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
        #card_info = card_info,
        card_display = card_display,
        children = children) 

#ゲーム開始～1枚目のカードを配り終えるところまで
def play_step1():
    initialize_card_image()
    sum_clear()
    first_card()
   
def sum_clear():
    for j in range(6):
        sum_2[j] = 0    
        

#プレーするポジションの選択～プレーヤーの選択ポジションに2枚目のカードを配り終えるところまで
@app.route('/play_step2' , methods=['POST'])
def play_step2():
    global player_position
    player_position = request.form.get("position")
    player_position = int(player_position) - 1  #実際のポジションと整合させるために-1 
    mode = 'player_operation'
    for i in range(player_position):
        #2枚目のカードを加えて合計処理
        add_new_card(i)
        update_card_info(i,1)
        check_process(i)
        if sum_2[i] <16:
            add_new_card(i)
            update_card_info(i,2)
        #3枚目のカードを加えて再度合計処理
        check_process(i)
        if sum_2[i] <16:
            add_new_card(i)
            update_card_info(i,3)
        #4枚目のカードを加えて再度合計処理
        check_process(i)
        if sum_2[i] <16:
            add_new_card(i)
            update_card_info(i,4)
        #5枚目のカードを加えて再度合計処理
        check_process(i)
        
    #プレーヤのポジションに2枚目のカードを配る   
    add_new_card(player_position)
    update_card_info(player_position,1)
    check_process(player_position)

    #プレーヤのポジションに以降の合計数値を更新する処理       
    #いったんエスケープ　220130　
    #for i in range(player_position+1, 6):
    #    check_process(i)
    
    return render_template(
        'index.html',
        data = data,
        mode = mode,
        sum_2 = sum_2,
        player_position = player_position,
        card_display = card_display,
        children = children) #,player_position


#プレーするポジションの選択～プレーヤーの選択ポジションに2枚目のカードを配り終えるところまで
@app.route('/play_step3' , methods=['POST'])
def play_step3():
    mode = 'player_operation'
    player_select = request.form.get("player_select")
    
    #プレーヤーの手持ちカード枚数を数える    
    global player_position
    qty = card_quantity(player_position)
    message =''
    
    if player_select == '1':
        add_new_card(player_position)
        update_card_info(player_position,qty)
        check_process(player_position)

        
        """デバッグ中。"""
        if sum_2[player_position] > 21:
            mode = 'auto_operation' 
            play_step4(player_position)
            message = judgment_against_dealer(player_position)    
        """デバッグ中。"""
        
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
            
#プレーヤーの選択ポジション以降のポジションにカードを配り終え手ゲーム終了まで
def play_step4(player_position):    
    for i in range(player_position+1, 6):
    #for i in range(3, 6):
        #プレーヤーの次のポジション以降に2枚目のカードを加えて合計処理
        add_new_card(i)
        update_card_info(i,1)
        check_process(i)
        if sum_2[i] <16:
            add_new_card(i)
            update_card_info(i,2)
        #3枚目のカードを加えて再度合計処理
        check_process(i)
        if sum_2[i] <16:
            add_new_card(i)
            update_card_info(i,3)
        #4枚目のカードを加えて再度合計処理
        check_process(i)
        if sum_2[i] <16:
            add_new_card(i)
            update_card_info(i,4)
        #5枚目のカードを加えて再度合計処理
        check_process(i)    
    
    


#実行する
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
