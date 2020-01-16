import random
from datetime import datetime as dt
rule ='''**RULES***
*You can enter t to get your remaining time
*You can enter space key to show an alphabet
*You can enter (quit game) to exit'''
print rule
#function to get random word from the file
def get_random_word(file):
    line = next(file) #each line is a word
    for num,aline in enumerate(file,2):
        if random.randrange(num): continue
        line = aline
    return line.strip() #strip() removes extra spaces from start and end


def StartGame(players):
    print ("***************************************GAME STARTED***************************************************")
    playersScore = {} #dictionary to store player with their scores
    for player in players:
        print ("\n ----------------------------Player "+ str(player)+" is playing----------------------------------\n")
        #getting word from file
        answer = get_random_word(open("words.txt"))
        #which alphabet to show in start, picking it randomly
        alphabetToShowList = [answer[random.randrange(len(answer))]]
        noOfAsterics = 0 #no of hidden alphabets
        #printing the word
        print "The word is: ",
        for alphabet in answer:
            if alphabet in alphabetToShowList:
                print alphabet,
            else:
                noOfAsterics += 1
                print "*",
        #countdown timer randomly chosing from 10 to 15
        countDownTime = random.randrange(10, 15)
        start = dt.now()
        #now starting the game
        while (True):
            if (noOfAsterics == 0): #if user has guessed everything
                print ("\n You Won! Your score: " + str(round(countDownTime - (dt.now() - start).total_seconds())))
                playersScore[player] = round(countDownTime - (dt.now() - start).total_seconds())
                break
            if ((countDownTime - (dt.now() - start).total_seconds()) <= 0): # countdown over
                print ("\nYour Loose. The bomb exploded BOOOOOOOOOOO....")
                print("The answer was: "+answer)
                playersScore[player] = round(countDownTime - (dt.now() - start).total_seconds())
                break
            print ("\n You have {} seconds".format(round(countDownTime - (dt.now() - start).total_seconds())))
            input = raw_input("Guess any alphabet: ")
            if input in answer: #if the alphabet is in the answer word
                alphabetToShowList.append(input)
                noOfAsterics = 0
                print "The word is: ",
                for alphabet in answer:
                    if alphabet in alphabetToShowList:
                        print alphabet,
                    else:
                        noOfAsterics += 1
                        print "*",
            elif input == " ":
                countDownTime -= 1
                while (True):
                    randomAlphabet = answer[random.randrange(len(answer))]
                    if randomAlphabet not in alphabetToShowList:
                        alphabetToShowList.append(randomAlphabet)
                        break
                noOfAsterics = 0
                print "The word is: ",
                for alphabet in answer:
                    if alphabet in alphabetToShowList:
                        print alphabet,
                    else:
                        noOfAsterics += 1
                        print "*",
            elif input == "time":
                print ("You have {} seconds".format(round(countDownTime - (dt.now() - start).total_seconds())))
            elif input=="quit game":
                print ("You score is 0")
                exit(0)
            else:
                countDownTime -= 1
                print "wrong!"
                noOfAsterics = 0
                print "The word is: ",
                for alphabet in answer:
                    if alphabet in alphabetToShowList:
                        print alphabet,
                    else:
                        noOfAsterics += 1
                        print "*",
    print ("*******************************FINAL RESULTS*********************************************")
    for x in playersScore:
        print x,
        print playersScore[x]
    print ("*******************************GAME OVER*************************************************")

players = []
while(True):
    player = raw_input("Type player names. type end to finish :")
    if player != "end":
        players.append(player)
    else:
        break
StartGame(players)




