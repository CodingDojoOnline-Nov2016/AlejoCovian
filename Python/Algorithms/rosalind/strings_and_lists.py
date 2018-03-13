def strings_and_lists(string, a, b, c, d):
    thing = ""
    thing2 = ""
    for i in range(a, b+1):
        thing += string[i]
    for j in range(c, d+1):
        thing2 += string[j]
    print thing + " " + thing2

strings_and_lists('Tbp30jBZQMzbiE1EBXT5yTTINwxqDAFyJP5DOvis9Tt71RZIGwAy5AhIY7M4pQY33AdLFRKWaGSGKzQ60QVbQulgjilMSNAnroctBlwgH7oF5Ez80cluwgdQ2YEXX5SNFEiId2hPj2J3JRBMIs9DkpsDdactylisonansZbgAZVqzIcClmY9Hh18Ri0VxvDAwTN',
36, 39, 152, 164)
