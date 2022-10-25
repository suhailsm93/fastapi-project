from passlib.context import CryptContext

pwd_context= CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password:str):#converts password to hash from to store in db
    return pwd_context.hash(password)

def verify(plain_password,hash_password):#converts plain_password to hash form then compare both user enter
    #password and password from database
    return pwd_context.verify(plain_password,hash_password)