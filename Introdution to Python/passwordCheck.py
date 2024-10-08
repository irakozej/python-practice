def is_valid(username, password):
    if username == "admin":
        return True
    elif username == "user" and password == "qweasd":
        return True
    else:
        return False
    
if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    if is_valid(username, password):
        print("Access granted")
    else:
        print("Access denied")