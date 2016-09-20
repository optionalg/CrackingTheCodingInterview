#You have a basketball hoop and someone says that you can play one of two games.
#Game 1: You get one shot to make the hoop.
#Game 2: You get three shots and you have to make two of three shots.
#If p is the probability of making a particular shot, for which values of p should
#you pick one game or the other?
def whichGame():
    p=-1
    while p<0 or p>100:
        p=int(raw_input("Enter the probability of a particular shot(number between 1 and 100: "))
    game1=p/100.0
    print game1
    game2=(3*((p/100.0)*(p/100.0)*((100-p)/100.0)))+((p/100.0)*(p/100.0)*(p/100.0))
    print game2
    if game1>game2:
        print "Game1!"
    elif game2>game1:
        print "Game2!"
    else:
        print "They both have equal probability!"