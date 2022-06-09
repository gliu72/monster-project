'''
Name: George Liu
Current Date: 4/20/18

'''
from Monster import *
from RockMonster import *
from ScissorMonster import *

class PaperMonster(Monster):
    def __init__(self,n='georgeP',t='Paper',hp=100,l=20,w=20):
    #Initializes name,type,hp,length,and width. 
        Monster.__init__(self,n,t,hp)
        self._length=l
        self._width=w
    def setLength(self,l):
        self._length=l
    def getLength(self):
        return self._length
    def setWidth(self,w):
        self._width=w
    def getWidth(self):
        return self._width
    def attack(self,monsterObj):
    #allows combat/damage with other monster objects
        damage=self._width*self._length
        return monsterObj.takeDamage(damage)
    def __str__(self):
    #allows printing/display of the information of each object
        s=Monster.__str__(self)
        s+='Length: '+str(self._length)+'\n'+'Width: '+str(self._width)+'\n'
        return s
if __name__=="__main__":
    m1=Monster('george','rock',100)
    s1=ScissorMonster('georgeS','scissor',100,40)
    r1=RockMonster('georgeR','Rock',100,20,20)
    
    p1=PaperMonster('george','p',99,19,19)
    p1.setName('georgeP')
    print p1.getName()
    p1.setType('paper')
    print p1.getType()
    p1.setHP(100)
    print p1.getHP()
    p1.setLength(20)
    print p1.getLength()
    p1.setWidth(20)
    print p1.getWidth()

    print p1.attack(m1)
    print p1.attack(s1)
    print p1.attack(r1)
    print s1.attack(p1)
    print r1.attack(p1)
    
    print PaperMonster()
