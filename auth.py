import bcrypt
import jwt
import datetime

SECRET_KEY = "supersecretkey"  # for demo only

users_db = {}

def register_user(username, password, role="user"):
    if username in users_db:
        return False, "User already exists"

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users_db[username] = {
        "password": hashed,
        "role": role
    }
    return True, "User registered successfully"

def login_user(username, password):
    user = users_db.get(username)
    if not user:
        return False, "Invalid credentials"

    if not bcrypt.checkpw(password.encode(), user["password"]):
        return False, "Invalid credentials"

    payload = {
        "username": username,
        "role": user["role"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return True, token
