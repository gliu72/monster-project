class Caller:
    def __init__(self,name,address,phoneNum,emergency,PSAP):
        self._callerName=name
        self._callerAddress=address
        self._callerPhoneNum=phoneNum
        self._callerEmergency=emergency
        self._callerPSAP=PSAP
    def setName(self,name):
        self._callerName=name
    def getName(self):
        return self._callerName

    def setAddress(self,address):
        self._callerAddress=address
    def getAddress(self):
        return self._callerAddress

    def setPhoneNum(self,phoneNum):
        phoneNum=raw_input("Enter a phone number.")
        while len(str(phoneNum))!=7 or phoneNum.isdigit()==False:
            phoneNum=raw_input("Invalid number. Enter a correct number")
        self._callerPhoneNum=phoneNum
    def getPhoneNum(self):
        return self._callerPhoneNum

    def setEmergency(self,emergency):
        self._callerEmergency=emergency
    def getEmergency(self):
        return self._callerEmergency

    def setPSAP(self,psap):
        while len(str(psap))!=4 or psap.isdigit()==False:
            psap=raw_input("Invalid PSAP. Enter a correct PSAP")
        self._callerPSAP=psap
    def getPSAP(self):
        return self._callerPSAP

    def __str__(self):
        return ("Name: "+self._callerName+"\n"+"Address: "+self._callerAddress
                +"\n"+"Phone Number: "+str(self._callerPhoneNum)+"\n"+"Emergency: "
                +self._callerEmergency+"\n"+"PSAP: "+str(self._callerPSAP))
                
