from ecdsa import SigningKey, VerifyingKey, SECP256k1


class KeyPair:
        
    def __init__(self, privateKey, publicKey):
        self.privateKey = privateKey
        self.publicKey = publicKey
            
    # privateKey, publicKey = '', ''
    global privateKey, publicKey 


    def genKeyPair():            
        # Generating the key pair from a SECP256K1 elliptic curve.
        global privateKey, publicKey
        privateKey = SigningKey.generate(curve=SECP256k1)
        publicKey = privateKey.get_verifying_key()
        
        with open("priv_key.pem", "wb") as f:
            f.write(privateKey.to_pem(format="pkcs8"))
        with open("pub_key.pem", "wb") as f:
            f.write(publicKey.to_pem())   
        return privateKey, publicKey 


    def printKeyPair():    
        # print(privateKey)
        # print(privateKey, publicKey)
        with open("priv_key.pem") as f:
            pri_key_string = SigningKey.from_pem(f.read())
            print(pri_key_string)
        with open("pub_key.pem") as f:
            pub_key_string = VerifyingKey.from_pem(f.read())
            print(pub_key_string)
            
    def toString():
        with open("priv_key.pem") as f:
            pri_key_string = SigningKey.from_pem(f.read())
            print(pri_key_string)
        with open("pub_key.pem") as f:
            pub_key_string = VerifyingKey.from_pem(f.read())
            print(pub_key_string)
        return pri_key_string, pub_key_string

    # Calling functions to test their working
    printKeyPair()



