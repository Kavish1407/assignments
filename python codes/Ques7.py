temp=True
while(temp):
    player1=input("Player1 select your choice(Rock,Paper,Scissor) ")
    player2=input("Player2 select your choice(Rock,Paper,Scissor) ")
    if ( player1=='Rock' and player2=='Paper' ):
        print("Congratulations to player2")
    elif(player1=='Rock' and player2=='Scissor'):
        print("Congratulations to player1")
    elif(player1=='Paper' and player2=='Rock'):
        print("Congratulations to player1")
    elif(player1=='Paper' and player2=='Scissor'):
        print("Congratulations to player2")
    elif (player1 == 'Scissor' and player2== "Rock"):
        print("Congratulations to player2")
    elif (player1 == 'Scissor' and player2== "Paper"):
        print("Congratulations to player1")
    else:
        print("Its a tie!")
    x=input("Do you want to play again? y/n ")
    if(x=='y'):
        temp=True
    else:
        temp=False
