from KeyPair import KeyPair, privateKey, publicKey
import hashlib 
from ecdsa.util import sigencode_der
from ecdsa.util import sigdecode_der
from ecdsa import BadSignatureError
# from pathlib import Path

class Signature: 
    
       
    # privateKey = KeyPair.genKeyPair()
    # privateKey = KeyPair.privateKey       # Having trouble importing this two properties from KeyPair class. Still working on them
    # publicKey = KeyPair.publicKey          
    # hash_func = hashlib.sha256()
    # data = "Some test data"
    
    def __init__(self) -> None:
        self.privateKey = KeyPair.privateKey       # Having trouble importing this two properties from KeyPair class. Still working on them
        self.publicKey = KeyPair.publicKey          
        # self.hash_func = hashlib.sha256()
        self.data = "Some test data"
    

    def signData(self, data, privateKey):
        self.data = data
        self.privateKey = privateKey
        hash_func = hashlib.sha256()
        sig = privateKey.sign_deterministic(
            data,
            hash_func,
            sigencode=sigencode_der
            ) 
            
        with open("data.sig", "wb") as f:
            f.write(sig)
        return 

    def verifySignature(self, data, publicKey):
        self.data = data
        self.publicKey = publicKey
        hash_func = hashlib.sha256()
        with open("data.sig", "rb") as f:
            sig = f.read()
            
        try:
            ret = self.publicKey.verify(sig, data, hash_func, sigdecode=sigdecode_der)
            assert ret
            print("Valid signature")
        except BadSignatureError:
            print("Incorrect signature")
            
    def toString():
        pass


    # signData(data, priv_key.pem)
    # verifySignature(dat)
    # signData()