import random           #IMPORT SHUFFELING

"""
SET INITIAL VALUES
"""

userhand = "yes"        #KEEP PLAYING?
userdeal = ""           #HIT/STAY
p = 0                   #PLAYER VALUE IF ACE = 11
p1 = 0                  #PLAYER VALUE IF ACE = 1
d = 0                   #DEALER VALUE IF ACE = 11
d1 = 0                  #DEALER VALUE IF ACE = 1
dd = 0                  #DRAW STATS
dw = 0                  #DEALER WIN STATS
pw = 0                  #PLAYER WIN STATS

deck = ["2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC","AC",
        "2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD","AD",
        "2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH","AH",
        "2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS","AS"]
random.shuffle(deck)

"""
FUNCTIONS FOR DEALING
"""

def dealPlayer ():
        player.append(deck[0])
        del deck[0]
def dealDealer ():
        dealer.append(deck[0])
        del deck[0]

"""
TEST IF PLAYER WANTS TO PLAY
"""

while userhand == "yes":

        """
        RESET VALUES AND HANDS
        """

        p = 0
        d = 0

        dealer = []
        player = []

        """
        FUNCTION FOR COUNTING
        """

        def countDeal ():
                global d,d1
                d = 0
                d1 = 0
                for i in range(len(dealer)):
                        if "2" in dealer[i]:
                                d += 2
                                d1 += 2
                        elif "3" in dealer[i]:
                                d += 3
                                d1 += 3
                        elif "4" in dealer[i]:
                                d += 4
                                d1 += 4
                        elif "5" in dealer[i]:
                                d += 5
                                d1 += 5
                        elif "6" in dealer[i]:
                                d += 6
                                d1 += 6
                        elif "7" in dealer[i]:
                                d += 7
                                d1 += 7
                        elif "8" in dealer[i]:
                                d += 8
                                d1 += 8
                        elif "9" in dealer[i]:
                                d += 9
                                d1 += 9
                        elif "10" in dealer[i]:
                                d += 10
                                d1 += 10
                        elif "J" in dealer[i]:
                                d += 10
                                d1 += 10
                        elif "Q" in dealer[i]:
                                d += 10
                                d1 += 10
                        elif "K" in dealer[i]:
                                d += 10
                                d1 += 10
                        elif "A" in dealer[i]:
                                d += 11
                                d1 += 1
                                
                return d,d1
        def countPlay ():
                global p,p1
                p = 0
                p1 = 0
                for i in range(0,len(player)):
                        if "2" in player[i]:
                                p += 2
                                p1 += 2
                        elif "3" in player[i]:
                                p += 3
                                p1 += 3
                        elif "4" in player[i]:
                                p += 4
                                p1 += 4
                        elif "5" in player[i]:
                                p += 5
                                p1 += 5
                        elif "6" in player[i]:
                                p += 6
                                p1 += 6
                        elif "7" in player[i]:
                                p += 7
                                p1 += 7
                        elif "8" in player[i]:
                                p += 8
                                p1 += 8
                        elif "9" in player[i]:
                                p += 9
                                p1 += 9
                        elif "10" in player[i]:
                                p += 10
                                p1 += 10
                        elif "J" in player[i]:
                                p += 10
                                p1 += 10
                        elif "Q" in player[i]:
                                p += 10
                                p1 += 10
                        elif "K" in player[i]:
                                p += 10
                                p1 += 10
                        elif "A" in player[i]:
                                p += 11
                                p1 += 1
                return p,p1

        """
        DEAL AND PRINT OUT INITIAL CARDS
        """

        dealPlayer ()
        dealDealer ()
        dealPlayer ()
        dealDealer ()

        print("Dealer: [*] " +  str(dealer[1]))
        print("Player: " + str(player))

        """
        COUNT AND PRINT OUT INITIAL VALUE
        """
        
        countPlay()

        if p == 21:
                print ("Nice! 21!")   
        elif p1 != p and p < 21:
                print ("Currently at: " + str(p) + " or " + str(p1))
        elif p < 22:
                print ("Currently at: " + str(p))
        elif p1 < 22:
                print ("Currently at: " + str(p1))

        """
        CONDITION: IF NOT BJ
        """
  
        if p != 21 or p1 != 21:
                userdeal = input("stay/hit")

                """
                IF HIT, DEAL CARD AND COUNT IT, IS STAY, BREAK LOOP
                """

                while userdeal == "hit":
                        dealPlayer ()
                        print("Play" + str(player))
                        countPlay ()
                        if p > 21 and p1 > 21:
                                print ("BUST!")
                                print ("Dealer won!")
                                dw += 1
                                break
                        elif p == 21 or p1 == 21:
                                print ("Nice! 21!")
                                break
                        elif p1 != p and p < 21:
                                print ("Currently at: " + str(p) + " or " + str(p1))
                        elif p < 22:
                                print ("Currently at: " + str(p))
                        elif p1 < 22:
                                print ("Currently at: " + str(p1))
                        userdeal = input("stay/hit")
                        continue

        """
        CONDITION: SKIP IF BUST
        """

        if p < 22 or p1 < 22:
                countPlay ()
                countDeal ()
                while d < 17 or d1 < 17:
                        dealDealer ()
                        countDeal ()
                        continue

                """
                SELECT BETTER COMBINATION
                """

                if p > 21:
                        p = p1
                elif p < 22 and p1 < 22 and p!= p1:
                        if p1 > p:
                                p = p1

                if d > 21:
                        d = d1
                elif d < 22 and d1 < 22 and d!= d1:
                        if d1 > d:
                                d = d1

                """
                PRINT OUT COUNT AND CARDS
                """
                
                print ("Dealer: " + str(d))
                print ("Player: " + str(p))

                print("Deal" + str(dealer))
                print("Play" + str(player))

                """
                SEE WHO WON
                """

                if d > 21 and d1 > 21:
                        pw += 1
                elif p < 22 and d < 22:
                        if (d-p) < (p-d):
                                pw += 1
                        elif (d-p) > (p-d):
                                dw += 1
                        else:
                                dd += 1
        
        """
        PRINT WIN/LOSS STATS
        """

        print("dw: " + str(dw) + "_pw: " + str(pw) + "_dd: " + str(dd))
        print(str(deck))

        """
        RESHUFFLE IF AT HALF DECK
        """

        if len(deck) <=  26:
                deck = ["2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC","AC",
                        "2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD","AD",
                        "2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH","AH",
                        "2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS","AS"]
                random.shuffle(deck)

        userhand = input("Deal another hand?")


        """
        NO PROBABILITY/AUTOMATION FOR PLAYER
                OBSERVE DEALER UPCARD?
                NO-BUST STRATEGY?
        NO REGARD OF INSURANCE ETC. PURE WIN/LOSS
        WIN = + 1x bet
        LOSS = - 1x bet
        DRAW =  0
        """