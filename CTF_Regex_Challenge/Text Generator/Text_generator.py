import random
import string



def generate_type_1_word ():
    LMNO = ['L', 'M', 'N', 'O']
    TO = ['T','O']
    r_u = ['r','s','t','u']

    out = [] 
    out.append('@') 
    length = random.randint(0,1)
    for i in range(length):    
        random_char = random.choice(r_u)
        out.append(random_char)
    random_char = random.choice(LMNO)
    out.append(random_char)
    length = random.randint(1,6)
    for i in range(length):
        random_char = random.choice(TO)
        out.append(random_char)
    out.append('%') 
    out = "".join(out)
    return(out)


def generate_type_2_word ():
    OWRKS = ['O','W','R','K','S']
    digits = string.digits 

    out = [] 
    out.append('#') 
    length = random.randint(0,4)
    for i in range(length):    
        random_char = random.choice(digits)
        out.append(random_char)
    out.append('JH')
    length = random.randint(1,6)
    for i in range(length):
        random_char = random.choice(OWRKS)
        out.append(random_char)
    out.append('^') 
    out = "".join(out)
    return(out)

def generate_type_3_word ():
    ENDPOT = ['E', 'N', 'D', 'P', 'O', 'T']
    YPE = ['Y', 'P', 'E']

    out = []
    out.append('+') 
    has_space = random.choice([True, False])
    if has_space :
        out.append(" ")
    int = random.randint(1,2)
    out.append(str(int))
    out.append('r')
    for i in range(5):
        random_char = random.choice(ENDPOT)
        out.append(random_char)
    length = random.randint(1,6)
    for i in range(length):
        random_char = random.choice(YPE)
        out.append(random_char)
    out.append('$')     
    out = "".join(out)
    return(out)

def generate_type_4_word():
    ENDPO = ['E','N','D','P','O','e','n','d','p','o']
    SKYPE = ['S','K','Y','P','E','s','k','y','p','e','!']

    out=[]
    out.append('-')
    out.append(str(random.randint(1,5)))
    out.append('VD')    
    for i in range(4):    
        random_char = random.choice(ENDPO)
        out.append(random_char)
    length = random.randint(1,6)
    for i in range(length):
        random_char = random.choice(SKYPE)
        out.append(random_char)
    out.append('*')
    out = "".join(out)
    return(out)

def generate_random_paragraph(num_sequences):
    sequences = []
    seq_list = range(num_sequences)
    flag = ['TWljcm97ckVn','M1hfQ0FOX2','IzX0Z1Tn0KCg==']
    flag_index = random.sample(seq_list,3)
    for i in range(num_sequences):
        if i in flag_index :
            sequences.append(flag[0])
            flag = flag[1:] 
        else :
            type = random.randint(1,4)
            if type == 1:
                sequences.append(generate_type_1_word())
            elif type == 2:
                sequences.append(generate_type_2_word())
            elif type == 3:
                sequences.append(generate_type_3_word())
            else:
                sequences.append(generate_type_4_word())
    return "".join(sequences)
 
paragraph = generate_random_paragraph(1500)
#word = genrate_type_1_word()
print(paragraph)
with open('text.txt', 'w') as file:
    file.write(paragraph)

