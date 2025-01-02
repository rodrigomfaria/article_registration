from passlib.context import CryptContext

CRYPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

def check_password(password: str, password_hash: str) -> bool:
    return CRYPTO.verify(password, password_hash)

def generate_pass_hash(password: str) -> str:
    return CRYPTO.hash(password)