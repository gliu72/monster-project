'''
Name: George Liu
Current Date: 4/20/18
'''
from Monster import *
from ScissorMonster import *
from PaperMonster import *

class RockMonster(Monster): 
    def __init__(self,n='georgeR',t='Rock',hp=100,m=20,v=20):
        #Initializes name, type, hp, mass, and velocity
        Monster.__init__(self,n,t,hp)
        self._mass=int(m)
        self._velocity=int(v)
    def setMass(self,m):
        self._mass=m
    def getMass(self):
        return self._mass
    def setVelocity(self,v):
        self._velocity=v
    def getVelocity(self):
        return self._velocity
    def attack(self,monsterObj):
    #attack method that does damage on another monsterobj based on mass/velocity
        damage=self._mass*self._velocity*self._velocity
        return monsterObj.takeDamage(damage)
    def __str__(self):
    #allows print/display of the information of each object
        s=Monster.__str__(self)
        s+='Mass: '+str(self._mass)+'\n'+'Velocity: '+str(self._velocity)+'\n'
        return s
if __name__=="__main__":
    m1=Monster('george','rock',100)
    s1=ScissorMonster('georgeS','scissor',100,40)
    
    r1=RockMonster('george','paper',99,19,19)
    r1.setName('georgeR')
    print r1.getName()
    r1.setType('rock')
    print r1.getType()
    r1.setHP(100)
    print r1.getHP()
    r1.setMass(20)
    print r1.getMass()
    r1.setVelocity(20)
    print r1.getVelocity()

    print r1.attack(m1)
    print r1.attack(s1)
    print s1.attack(r1)

    print RockMonster()
    
