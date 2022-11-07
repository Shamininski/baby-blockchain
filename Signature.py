from KeyPair import KeyPair, privateKey, publicKey
import hashlib 
from ecdsa.util import sigencode_der
from ecdsa.util import sigdecode_der
from ecdsa import BadSignatureError
# from pathlib import Path


# privateKey = KeyPair.genKeyPair()
privateKey = KeyPair.privateKey       # Having trouble importing this two properties from KeyPair class. Still working on them
publicKey = KeyPair.publicKey          
hash_func = hashlib.sha256()
data = "Some test data"

def signData(self, data, privateKey):
    self.data = data
    self.privateKey = privateKey
    sig = privateKey.sign_deterministic(
        data,
        hash_func,
        sigencode=sigencode_der
        ) 
        
    with open("data.sig", "wb") as f:
        f.write(sig)
    return 

def verifySignature(self, data):
    self.data = data
    with open("data.sig", "rb") as f:
        sig = f.read()
        
    try:
        ret = publicKey.verify(sig, data, hash_func, sigdecode=sigdecode_der)
        assert ret
        print("Valid signature")
    except BadSignatureError:
        print("Incorrect signature")
        
def toString():
    pass


# signData(data, priv_key.pem)
# verifySignature(dat)
signData()