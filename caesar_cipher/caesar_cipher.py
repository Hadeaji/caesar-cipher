import Corpus
import nltk
import string

def encrypt(string_,x):
    letters = [char for char in string.ascii_lowercase]
    list_ = [char for char in string_]
    mod = []

    for i in list_:
        hold = False
        if i == i.upper():
            i = i.lower()
            hold = True
        if i in letters:
            j = letters.index(i)
            j += x
            if j > 25:
                j= (j%25) -(j//25)
                
            if hold == True:
                mod.append(letters[j].upper())
            else:
                mod.append(letters[j])
        else:
            mod.append(i)

    result = ''.join(mod)
    return result

def decrypt(string_,x):
    letters = [char for char in string.ascii_lowercase]
    list_ = [char for char in string_]
    mod = []

    for i in list_:
        hold = False
        if i == i.upper():
            i = i.lower()
            hold = True
        if i in letters:
            j = letters.index(i)
            if x > 25:
                x= (x%25) -(x//25)
            j -= x

            if hold == True:
                mod.append(letters[j].upper())
            else:
                mod.append(letters[j])
        else:
            mod.append(i)

    result = ''.join(mod)
    return result

def force(string_):
    nltk.download('words')
    eng_words = nltk.corpus.words.words()
    letters = [char for char in string.ascii_lowercase]

    list_w = string_.split()
    list_ = [char for char in string_]
    mod = []

    perC = len(list_w)
    count = 0
    x = 1
    times = 1

    while times < 26:

        for i in list_w:
            if i.lower() in eng_words:
                count +=1

        if count > perC * 0.7:
            count = 0

            for i in list_w:
                mod.append(i)
                mod.append(' ')
            mod.pop(-1)
            result = ''.join(mod)
            return result

        elif count < perC * 0.7:
            count = 0
            pre_mod = []

            for i in list_w:
                word = []

                for f in i:
                    hold = False
                    if f == f.upper():
                        f = f.lower()
                        hold = True
                    if f in letters:
                        j = letters.index(f)
                        if x > 25:
                            x= (x%25) -(x//25)
                        j -= x

                        if hold == True:
                            word.append(letters[j].upper())
                        else:
                            word.append(letters[j])
                    elif f not in letters:
                        word.append(f)
                pre_mod.append(''.join(word))
            list_w = pre_mod
        times +=1

print(encrypt('It was the best of times, it was the worst of times.',2))
print(decrypt('Kv ycu vjg dguv qh vkogu, kv ycu vjg yqtuv qh vkogu.',2))
print(force('Kv ycu vjg dguv qh vkogu, kv ycu vjg yqtuv qh vkogu.'))