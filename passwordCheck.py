def is_valid(username, password):
    if username == "admin":
        return True
    elif username == "user" and password == "qweasd":
        return True
    else:
        return False