from Signature import Signature
import Account

# A class that allows to create a payment operation.
class Operations:
    
    # constructor
    def __init__(self, sender, receiver, amount=0, signature=b''):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature
        
      
    # return true/false depending on the checking of the results of sender's amount balance
    def verifyOperation(self, sig):
        if self.amount < self.sender.balance:
            self.verifySignature(self.data, self.sig)
        else: 
            print("Sender has insufficient funds")
        
    # Creates an operation by accessing the publicKey from memory and use it to sign the data
    # then it returns an operation object with its necessary members.
    # Most likely not optimal as it should separate purpose of the funct. Will definitely need refactoring 
    # to produce 2 functions - one for signature work and the other to solely create the operation.   
    def createOperation(self):    
        publicKey = open("pub_key.pem", "rb")
        self.data = "test data"
        self.sig = Signature.verifySignature(self.data, publicKey.read().decode(encoding="utf-8"))
        # return 
        return self.sender.accountID, self.receiver.AccountID, self.amount, self.sig
        

    # 
    def toString():
        pass

    # 
    def printKeyPair():
        pass



