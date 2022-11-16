import KeyPair
import Signature

# A class for managing a wallet, creating operations and data signing.
global accountID, wallet, balance

class Account:
    
    #  constructor calls the genAccount method which in turn creates an address and ID 
    def __init__(self) -> None:
        self.genAccount()

    # a function that allows you to create an account. It returns an object of the Account class. The first key pair is generated and assigned to the account.
    def genAccount(self):
        keyPair = KeyPair()
        self.wallet = []
        self.balance = 0
        self.wallet.append(keyPair.genKeyPair())  # Adds the keys to the initially empty wallet.
        self.accountID = self.wallet[0]  # Gets the privKey, accessing it via index
        # print(self.wallet)
        print(self.accountID)
        return self.wallet, self.accountID
        

    # a function that allows you to add a new key pair to the wallet and use it in the future to sign operations initiated from this account. It does not return anything  
    def addKeyPairToWallet(self):
        self.wallets.append(Account.genKeyPair())  # 

    #a function that allows to update the state of the user's balance. It takes an integer value as input, and does not return anything.
    def updateBalance(self, coins):
        self.balance = coins                # Integer input is the token, in this case coins

    #a function that allows to create a payment operation on behalf of this account to the recipient. Accepts the account object as input to which the payment will be made, the transfer amount and the key index in the wallet.
    def createPaymentOp(self, accountID, amount, walletIndex):
        self.accountID = accountID
        self.amount = amount
        self.walletIndex = self.wallet[walletIndex]
            

    # a function that allows to get the state of the user's balance. It returns an integer value.    
    def getBalance(self):
        return self.balance        
    
    # a function that allows to display the state of the user's balance. It does not return anything.
    def printBalance(self):
        return self.balance

    # a function that allows the user to sign random data. It accepts a message and an index of the key pair in the wallet as input. Returns the value of the signature
    def signData(self, data, index):
        signature = Signature.signData()
        key = self.wallet[self.walletIndex][0]
        return self.wallet, self.accountID
    