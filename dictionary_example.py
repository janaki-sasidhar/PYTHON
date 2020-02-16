def fuck(lyrics):
    mydict={}
    for word in lyrics:
        if word in mydict:
            mydict[word]+=1
        else:
            mydict[word]=1
    return mydict
fuckoff=['fuck','fuck','of','of','the','mu','a','dfa']
#fuck(fuckoff)
