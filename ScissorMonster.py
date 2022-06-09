'''
Name: George Liu
'''
from Monster import *
from RockMonster import *
from PaperMonster import *
class ScissorMonster(Monster):
    def __init__(self,n='georgeS',t='paper',hp=100,sharp=40):
        #Initializes name,type,hp, and sharpness
        Monster.__init__(self,n,t,hp)
        self._sharpness=sharp
    def setSharpness(self,sharp):
        self._sharpness=sharp
    def getSharpness(self):
        return self._sharpness
    def attack(self,monsterObj):
    #allows combat/damage to other monster objects
        damage=self._sharpness
        return monsterObj.takeDamage(damage)
    def __str__(self):
    #allows print/display of information of each object. 
        s=Monster.__str__(self)
        s+='Sharpness: '+str(self._sharpness)+'\n'
        return s
    
if __name__=="__main__":
    m1=Monster('george','rock',100)
    s1=ScissorMonster('george','paper',99,39)
    s1.setName('georgeS')
    print s1.getName()
    s1.setType('scissor')
    print s1.getType()
    s1.setHP(100)
    print s1.getHP()
    s1.setSharpness(40)
    print s1.getSharpness()
    print s1.attack(m1)

    s2=ScissorMonster()
    s2.setName('nameWorks')
    print s2.getName()
    s2.setType('typeWorks')
    print s2.getType()
    s2.setHP('hp works')
    print s2.getHP()
    s2.setSharpness('sharpness works')
    print s2.getSharpness()
    print s2
