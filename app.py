def login(username, password):
    if username == "admin" and password == "password123":
        return "Login successful"
    return "Login failed"

print(login("admin", "password123"))
