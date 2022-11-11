import random

def deposit():
    while True:
        print("="*25+" CASH DEPOSIT "+"="*25)
        print("❗️❗️please deposit at least 100$",)
        amount = input("Deposit cash to your account (enter amount of cash) : ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                if amount < 100:
                    print("amount should be more 100❗️")
                else:
                    print("-"*64)
                    print("\n")
                    break
            elif amount < 0 :
                print("amount should not be less than zero❗️")
            else:
                print("amount must not be 0❗️")
        else:
            print("please enter a number❗️")
    return amount


def get_bet():
    while True:
        print("="*25+" ROUND BETTING "+"="*25)
        print("❗️❗️betting shound be more then 20$ per round.")
        amount_bet = input("how much would you like to bet on this game per round: ")

        if amount_bet.isdigit():
             amount_bet = int(amount_bet)
             if amount_bet <= 20:
                 print("-"*65)
                 print("\n")
                 break 
             else:
                 print("amout should less than 20$ per round❗️")
        else: 
            print("please enter a number.❗️")
    return amount_bet

#rock paper scissors game
def game_RPS(balance,bet):
    def win(result1,result2):
        print("=================","YOU WIN🎉","=================")
        print("you selected ",result1)
        print("computer selected ",result2)
        print("you got cash +",bet,"$")
        print("your balacne is remaining",balance,"$")  
        print("-"*43) 
        print("\n")

    def lose(result1,result2):
        print("=================","YOU LOSE😱","=================")
        print("you selected ",result1)
        print("computer selected ",result2)
        print("you got cash -",bet,"$")
        print("your balacne is remaining",balance,"$")  
        print("-"*43) 
        print("\n")
        
    def tie(result1,result2):
        print("=================","TIE😮‍💨","=================")
        print("you selected ",result1)
        print("computer selected ",result2)
        print("you got cash ","0","$")
        print("your balacne is remaining",balance,"$") 
        print("-"*43) 
        print("\n")
    choices = ["rock","paper","scissors"]
    user_point= 0
    computer_point=0
    print("============= ROCK - PAPER - SCISSORS GAME ============")
    while True:
        if balance > bet:
            choose = input("type rock paper scissors or q to quit this game : ")
            if choose == "q":
                break
            elif choose not in choices:
                continue
            #randint()
            computer_choose = choices[random.randint(0,2)]
            
            if choose == "rock" and computer_choose == "scissors":
                user_point += 1
                balance += bet
                win("✊","✌️")
            elif choose == "paper" and computer_choose == "rock":
                user_point += 1
                balance += bet
                win("✋","✊")
            elif choose == "scissors" and computer_choose =="paper":
                user_point += 1
                balance += bet
                win("✌️","✋")
            elif choose=="rock" and computer_choose =="rock":
                tie("✊","✊")
            elif choose=="paper" and computer_choose =="paper":
                tie("✋","✋")
            elif choose=="scissors" and computer_choose =="scissors":
                tie("✌️","✌️")
            elif choose == "scissors" and computer_choose == "rock":
                computer_point += 1
                balance -= bet
                lose("✌️","✊")
            elif choose == "rock" and computer_choose == "paper":
                computer_point += 1
                balance -= bet
                lose("✊","✋")
            elif choose == "paper" and computer_choose =="scissors":
                computer_point += 1
                balance -= bet
                lose("✋","✌️")

        else:
            print("your money is not enough to play next round")
        
    print("=================== RESULT ===================")
    print("you win: "+str(user_point)+ "   " +"computer win: "+str(computer_point))
    print("Your balance is remaining "+str(balance)+"$")
    print("-"*43)
    return balance
    
#rock paper scissors game end
#quiz game
qusetions1 = ["How many hours are in a week?","What does IOT stand for?","Who is the most richest person in the world?","What does AI stand for?"]
qusetions2 = ["What does CPU stand for?","What does RAM stand for?","What does gpu stand for?","how many seconds in an hour?"]
qusetions3 = ["Who is the creator of Python?","Who is the father of computer?","Who discovered America first?","how many seconds in one year?"]

solution_list1 = ["168","internet of things","elon musk","artificial intelligence"]
solution_list2 =["central processing unit","random access memory","graphics processing unit","3600"]
solution_list3=["guido van rossum","charles babbage","christopher columbus","31,536,000"]


def levelofquiz():
    while True:
        print("================ DIFFICULTY LEVEL ================")
        print('''
1) select 1 to answer easy questions.
(get betting per round * 1 if you win)

2) select 2 to answer medium questions.
(get betting per round * 2 if you win)

3) select 3 to answer hard questions.
(get betting per round * 3 if you win)
        ''')
        select = input("Enter the level of questions: ")
        print("-"*40)
        print("\n")
        
        if select.isdigit():
            select = int(select)
            if select == 1 :
                pre_balance = quiz(qusetions1,solution_list1,balance,bet,1) 
                print(pre_balance)
                break       
            elif select == 2 :
                pre_balance=quiz(qusetions2,solution_list2,balance,bet,2)
                break
            elif select == 3:
                pre_balance=quiz(qusetions3,solution_list3,balance,bet,3)
                print("Do you want to play another game?")
                nextGame_select = input("(yes or no) :").lower()
                if nextGame_select == "yes":
                    game_RPS(pre_balance,bet)
                elif nextGame_select == "no":
                    print("========== thank you =========")
                    print("Thank for playing our game🙏🙏")
                else:
                    print("something went wrong")
            elif select > 3:
                print("please enter number (1 or 2)")
            elif select < 0:
                print("please enter number (1 or 2)")
            
        else:
            print("please enter number ")
    return pre_balance       

def quiz(questions,solve,balance,bet,leverage):
        if balance > bet:
            point = 0
            amount_q = len(questions)
            print("=============== QUIZ ===============")
            for i in range(amount_q) :
                print(questions[i])
                answer = input("enter your answer: ").lower()
                print("\n")
                if answer == solve[i] :
                    point += 1
                    balance += (bet * leverage)
                    print("======= Your answer is CORRECT✅ =======")
                    print("you got cash +",(bet*leverage),"$")
                    print("your balacne is remaining",balance,"$")  
                    print("-"*38) 
                    print("\n")
                
                else:
                    balance -= bet
                    print("====== Your answer is WRONG❌======")
                    print("you got cash -",bet,"$")
                    print("your balacne is remaining",balance,"$")
                    print("-"*38) 
                    print("\n")
            print("=================== RESULT ===================")
            print("you answer correctly: "+str(point) )
            print("Score percentage :" + str(point*100/4)+"%")
            print("Your balance is remaining "+str(balance)+"$")
            print("-"*43)
            return balance
        else:print("your money is not enough to play next round")
                   
# end of quiz game function
while True:
    print("Do you have an account?")
    account = input("(yes or no) :").lower()
    if account == "yes":
        print("="*15+" login "+"="*15)
        username_login = input("enter your username : ")
        pass_login = input("enter your password : ")
        file_username = open("username.txt","r")
        file_pass = open("password.txt","r")
        data_username= file_username.read().splitlines()
        data_pass= file_pass.read().splitlines()
        if username_login in data_username and pass_login in data_pass:
            print("login successful")
            print("-"*37)
            print("\n")
            break
        else:
            print("your email or your password was incorrect plaeas try again❗️❗️")
            print("-"*40)
            print("\n")
            
    elif account == "no":
        print("="*15+" register "+"="*15)
        file_username = open("username.txt","a")
        file_pass = open("password.txt","a")
        file_username_r = open("username.txt","r")

        input_username = input("enter your username : ")
        input_pass = input("enter your password : ")
        if len(input_username) < 7 and len(input_pass) < 7:
            print("password must have at least 8 characters❗️❗️")
            print("Please, attempt to register again.")
            print("\n")
        else:
            data = file_username_r.read().split()
            if input_username in data:
                print("this username is already exist!!")
                print("-"*40)
                print("\n")
            else:
                file_username.writelines(input_username+"\n")
                file_pass.write(input_pass+"\n")
                print("register success fully😁")
                print("-"*40)
                print("\n")
        
    else:
        print("something went wrong please try again❗️❗️")
        print("\n")

while True:
    print('''================ select game ===============
1) select 1 to play rock,paper,scissors game
2) select 2 to play quiz game
''')
    game_select=input("select your game (1 and 2) : ")
    print("\n")
    if game_select.isdigit():
        game_select = int(game_select)
        balance = deposit()
        balance_first = balance
        bet=get_bet()
        if game_select == 1:
           pre_balanca=game_RPS(balance,bet)
           while True:
                print("do you want to play quiz game?")
                select_quiz = input("(yes/no)")
                if select_quiz == "yes":
                            balance = pre_balanca
                            levelofquiz()
                            break  
                elif select_quiz == "no":
                            print("========== thank you for playing ==========")
                            print("\n")
                            break       
                else: 
                            print("You didn't enter yes or no!!!")
           break           
                
        elif game_select == 2:
            pre_balance=levelofquiz()    
            print("Do you want to play rock,paper,scissors game?")
            while True:
                nextGame_select = input("(yes or no) :").lower()
                
                if nextGame_select == "yes":
                    game_RPS(pre_balance,bet)
                    break
                elif nextGame_select == "no":
                    print("========== thank you =========")
                    print("Thank for playing our game🙏🙏")
                    break
                else:
                    print("something went wrong")
            break
        else:
            print("❗️❗️please enter number❗️❗️")
        
    






