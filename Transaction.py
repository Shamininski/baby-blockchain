from hashlib import sha256
import collections

# A class that allows to form a transaction containing user payments
class Transaction:
    
    # global transactionID, setOfOperations, nonce
    
    def __init__(self, transaction = [], nonce = 0):
        self.transaction = transaction
        self.nonce = nonce
        self.setOfOperations = ['send', 'receive', 'endorse', 'revert']

    # Check if operation is supported
    def isOpPermissible(self, op):
        setOfOperations = ['send', 'receive', 'endorse', 'revert']
        if (self.op in setOfOperations):
            return True
        else:
            return False

    # creates an operation only if the operation is supported by the system.
    def createOperation(self, transaction, nonce):       
        tx = self.transaction, self.nonce
        tx_nature = self.isOpPermissible(tx[0]) 
        if (tx_nature):
            return collections.OrderedDict({
                'transactionId': sha256(str(tx).encode('utf-8')).digest().hex(),
                'Tansactions': transaction,
                'nonce': nonce})
        else:
            return "Transaction not supported"
            
        

    # 
    def toString():
        pass

    # 
    def printKeyPair():
        pass