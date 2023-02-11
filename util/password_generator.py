import random, string

def rp_rand(): 
    password = ""
    for _ in range(8):
        match random.randint(1,2): 
            case 1: password += str(random.randint(1,9))
            case 2: password += random.choice((string.ascii_letters).upper())
    return(password)

    