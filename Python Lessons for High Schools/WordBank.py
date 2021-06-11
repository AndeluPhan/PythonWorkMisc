import requests

def MostAmazingParser():
    word_site = "http://www.desiquintans.com/downloads/nounlist/nounlist.txt"

    response = requests.get(word_site)
    WORDS = response.content.splitlines()

    Vocab = list()
    for i in WORDS:
        j = str(i).replace("b'","'")
        k = str(j).replace("'","")
        c = str(k).replace('b"',"")
        d = str(c).replace('"',"")
        Vocab.append(d)

    for val in Vocab: #gets rid of any word less than 3 characters.
        count = 0
        for letter in val:
            count += 1
        if count < 3:
            Vocab.remove(val)

    return Vocab

