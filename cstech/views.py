
from django.shortcuts import render
from cstech.gameController import *

def index(request): #Bu fonksiyon on yuz ile algoritma arasindaki penceredir.
    global game, computerGuess, gamedict #Tum requestler icerisinden erisilebilir degiskenler.
    if request.method == 'GET': # Get methodunu kontrol ederek gerekli ilk islemlerin yapilmasi.
        gamedict = {
            "comp_guess_list": [],
            "comp_score_list": [],
            "user_guess_list": [],
            "user_score_list": []
        }
        game = gameController()
        computerNumber = game.newGame()
        print(computerNumber,"Computer number......")
        computerGuess = game.guessNewNumber()
        gamedict['comp_guess_list'].append(computerGuess)
        return render(request,'index.html',{'dict':gamedict})
    if request.method == 'POST':
        isGameEnded = False
        compScore = request.POST['comp_score']
        userGuess = request.POST.get('user_guess')
        isValid = game.inputValidator(compScore,userGuess)
        print("USER GUES : ",userGuess)
        if isValid != True:
            return render(request,'index.html',{'intent':True,'dict':gamedict,'info': isValid})
        else:
            gamedict['comp_score_list'].append(compScore)
            gamedict['user_guess_list'].append(userGuess)
            userScore = game.calculateUserScore(userGuess)
            if userScore == "True":
                info ="Sen Kazandin! Benim numaram : "+str(userGuess)
                return render(request, 'index.html',
                              {'isGameEnded': True, 'intent': True, 'dict': gamedict, 'info': info})

            isWinner = game.checkNewPossibleList(compScore,computerGuess)
            if isWinner == "True":
                gamedict['user_score_list'].append(",".join(userScore))
                computerGuess = game.guessNewNumber()
                print("LENGHT......: ",len(computerGuess))
                gamedict['comp_guess_list'].append(computerGuess)
                print(gamedict['comp_guess_list'][0])
                return render(request, 'index.html', {'intent': False, 'dict': gamedict})
            else:
                return render(request, 'index.html',
                              {'isGameEnded': True, 'intent': True, 'dict': gamedict, 'info': isWinner})
