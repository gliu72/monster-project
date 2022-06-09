'''
Name: George Liu
Current Date: 4/20/18

'''

from RockMonster import *
from ScissorMonster import *
from PaperMonster import *
from Monster import *
import random

class MonsterGame():
    def __init__(self,f='P6Input.txt'):
    #Initializes a list of monster objects(list of lists).
    #Opens up a file to be read and interpreted. Interprets every line and converts into
    #a monster object.
        self._monsterList=[]
        source=file(f)
        for line in source:
            data=line.split()
            if data[0]=='Rock':
                r1=RockMonster(data[1],data[0],int(data[2]),int(data[3]),int(data[4]))
                self._monsterList.append(r1)
            elif data[0]=='Paper':
                p1=PaperMonster(data[1],data[0],int(data[2]),int(data[3]),int(data[4]))
                self._monsterList.append(p1)
            elif data[0]=='Scissor':
                s1=ScissorMonster(data[1],data[0],int(data[2]),int(data[3]))
                self._monsterList.append(s1)
        source.close()
        
        
    def playGame(self):
    #engages the monster objects in combat/tournament. 
        while len(self._monsterList)>1:
        #if there is only one monster remaining, that is the winning monster.
            self._monsterList = random.sample(self._monsterList, len(self._monsterList))
            i=0
            while i<(len(self._monsterList)-1):
            #A counter i keeps track of the monsters and allows adjacent monsters to fight.
                while 1==1:
                #A loop that keeps monsters fighting until one of them dies. 
                    x=self._monsterList[i].attack(self._monsterList[i+1])
                    if x==True:
                    #if i+1 monster dies, it is deleted as the loser.
                        self._monsterList.pop(i+1)
                        break
                    y=self._monsterList[i+1].attack(self._monsterList[i])
                    if y==True:
                    #if i monster dies, it is deleted as the loser. 
                        self._monsterList.pop(i)
                        break
                i+=1
        winner=self._monsterList[0]
        #the winning dinosaur is the only remaining monster object in the list. 
        print 'WINNER: '
        print winner
        #displays who the winner is. 
                
        
    def __str__(self):
    #displays all monster objects in the list of monsters. 
        for i in self._monsterList:
            print i
        return ''
    

if __name__=="__main__":
    game=MonsterGame()
    print game
    game.playGame()
    
