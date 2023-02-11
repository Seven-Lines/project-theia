import random, json

def ru_name(name): # In a func for later use (email username).
    fname, lname = name.lower().split()[0], name.lower().split()[1]
    num = str(random.randint(100, 9999))

    match random.randint(1,6): 
        case 1: return(f"{fname}{lname}{num}") # johndoe000
        case 2: return(f"{lname}{fname}{num}") # doejohn000
        case 3: return(f"{fname}_{lname}{num}") # john_doe000
        case 4: return(f"{fname[0]}{lname}{num}") # jdoe000
        case 5: return(f"{lname[0]}{fname}{num}") # djoe000
        case 6: return(f"{fname[0]}_{lname}{num}") # j_doe000

def ru_noun(name): 
    fname, lname = name.lower().split()[0], name.lower().split()[1]
    noun1, noun2 = json.load(open('./data/word_lists/username_nouns.json'))[random.randint(1, 25444)], json.load(open('./data/word_lists/username_nouns.json'))[random.randint(1, 25444)] 
    num = str(random.randint(100, 9999))
    
    match random.randint(1,6): 
        case 1: return(f"{fname}{noun1}") # johnnoun 
        case 2: return(f"{fname}{noun1}{num}") # johnnoun000
        case 3: return(f"{fname[0]}{noun1}{num}") # jnoun000
        case 4: return(f"{fname}_{noun1}") # john_noun
        case 5: return(f"{noun1}{noun2}") #nounnoun
        case 6: return(f"{noun1}{noun2}{num}") #nounnoun000