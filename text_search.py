

"""
    date
    law
    money

    DATE
        day.month.year
        12.12.2000

        12. monthnamefull 2019
        12. oct. 2019

        *spaces after the punkts



        lets just the month names
        number 1-12 months 1-31 days



"""




def printerrr (stuff):
    for i in stuff:
        for j in i:
            print(j)


def onedimension(stuffs):
    ret = []
    for z in stuffs:
        ret.extend(z)
    return ret
        

"""with open("f.txt") as f:
    word = ""
    sen = ""
    sentances =  []
    all_words = []

    for line in f: 
        for i,c in enumerate(line):
            if c in ".\n\r\t":
                if word:
                    all_words.append(word)
                    word = "" 
            else: 
                word+=c

    for w in all_words:
        sen+=w
        for ch in w:
            if ch in "?!.":
                sentances.extend(sen)"""


with open("f.txt") as f:
    all_words = []
    all_words.extend(l.split("\n") for l in f)
    all_words = onedimension(all_words)

    for st in all_words:
        st = st.strip("\n")
        st = st.strip("\'")
        st = st.strip("\"")


new_thing = []

for sdfg in all_words:
    if sdfg:
        new_thing.append(sdfg)
    

print(len(new_thing))
print(new_thing)



