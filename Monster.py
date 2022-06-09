'''
Name: George Liu
Current Date: 4/20/18
'''
class Monster():
    def __init__(self,n='default',t='rock',hp=100):
    #Intializes name,type,and hp for all monster objects
        self._name=n
        self._type=t
        self._hitpoints=int(hp)
        
    def setName(self,n):
        self._name=n
    def getName(self):
        return self._name
    def setType(self,t):
        self._type=t
    def getType(self):
        return self._type
    def setHP(self,hp):
        self._hitpoints=hp
    def getHP(self):
        return self._hitpoints

    def takeDamage(self,dmg):
    #Allows every monster object to take damage and reduce in hitpoints.
    #Also signals when a monster is dead when their hp falls at or below 0.
        self._hitpoints=self._hitpoints-dmg
        if self._hitpoints>=0:
            return False
        else:
            return True
    def __str__(self):
    #Allows display of the information of each monster object
        return ('Name: '+str(self._name)+'\n'+'Type: '+str(self._type)+'\n'
                +'Hitpoints: '+str(self._hitpoints)+'\n')
                
        
if __name__=="__main__":
    m1=Monster('george','paper',99)
    m1.setName('george1')
    print m1.getName()
    m1.setType('monster')
    print m1.getType()
    m1.setHP(100)
    print m1.getHP()
    print m1.takeDamage(80)
    print m1.getHP()
    print m1.takeDamage(100)
    print m1
    
    
