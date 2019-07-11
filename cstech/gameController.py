from itertools import permutations
from random import shuffle
global computerNumber
global allPossibleList

class gameController:
    def __init__(self):#Initial degiskenlerimizi olusturduk.
        self.computerNumber = []
        self.allPossibleList = []
        self.allNumbers = []

    def newGame(self):#Yeni bir oyuna baslamamiz gerektiginde
        self.findAllProbabilities()#tum olasi degerleri hesapladik ve bilgisayar icin bir sayi tuttuk
        self.computerNumber = self.guessNewNumber()
        print("compuerNumber  : "+ str(self.computerNumber))
        return self.computerNumber

    def findAllProbabilities(self):
        self.allPossibleList = []                           #Bu fonksiyon, verilen '0123456789' stringinin ve 4 degerinin
        allList = list(permutations('0123456789', 4))       #once stringin teker teker elemanlarina gore 4'lu kombinasyonunu
        for i in allList:                                   #alip daha, sonra bu kombinasyonlarin permutasyonunu almaktadir.
            if i[0] != '0':
                self.allPossibleList.append(i)
        self.allNumbers = [list(value) for value in self.allPossibleList]

    def guessNewNumber(self):#Bu fonksiyon tum olasi degerler arasindan bir secim yapmaktadir.
        shuffle(self.allPossibleList)
        return self.allPossibleList[0]

    def inputValidator(self,compScore,userGuess): #Bu fonksiyon input datalarin uygunlugunu kontrol ediyor.
        comp_score = []
        score = self.parse_score(compScore)
        userGuess = [value for value in userGuess]
        if len(score) != 2:
            return "Lutfen skor degerini kontrol ederek oynayiniz."
        for value in score:
            for i in range(5):
                if str(i) == value:
                    comp_score.append(i)
        if comp_score == [] or len(comp_score) != 2:
            return "Lutfen skor degerini kontrol ederek oynayiniz."
        if userGuess not in self.allNumbers:
            print(userGuess)
            return "Lutfen 1000 - 9999 arasinda bir sayi giriniz."
        else:
            return True


    def compCalc(self, usr_value, comp_value):#Bu fonksiyon bizim tahminimizin scorunu hesapliyor.
        plus = minus = 0
        for x in range(len(usr_value)):
            if usr_value[x] == comp_value[x]:
                plus += 1
            elif usr_value[x] in comp_value:
                minus += 1
        return [str(plus),str(minus)]

    def calculateUserScore(self, userGuess):#compCalc icin bir header fonksiyon. Uygun durumda hesaplama yapiyoruz.
        if userGuess != "".join(self.computerNumber):
            return self.compCalc(userGuess, self.computerNumber)
        else:
            return "True"


    def parse_score(self, score):
        score = score.strip().split(',')
        return score


    def checkNewPossibleList(self, compScore, compGuess):#Bilgisayarin bizim tuttugumuz sayiyi score'ler yardimiyla
        newPossibleList = []                             #Tahmin etmesini saglayan fonksiyon. Tum degerler arasindan
        for x in self.allPossibleList:                   #Score'lere gore uygunsuz degerleri siler.
            score_calculator = self.compCalc(x,compGuess)
            if self.parse_score(compScore) == score_calculator:
                newPossibleList.append(x)
        if len(newPossibleList) > 1:
            self.allPossibleList = newPossibleList
            self.guessNewNumber()
            return "True"
        elif not newPossibleList:
            return "Skor'da bir sorun var. Lutfen kontrol edip tekrar dene!."
        else:
            return "Malesef oyunu kaybettin. Ben Kazandim. Bilmen gereken sayi : " + "".join(
                self.computerNumber) + " Tuttugun sayi : " + "".join(
                newPossibleList[0])


