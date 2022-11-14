def palind(name):
    if name == name[::-1]:
        name = "YES"
    else:
        name = "NO"
    return name
