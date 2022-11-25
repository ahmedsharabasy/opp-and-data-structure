def finalword(word):
    if len(word)==1:
        return word

    if word[0]==word[1]:
        return finalword(word[1:])
    return word[0]+finalword(word[1:]) 


print(finalword('aaaaaaahhhhhhhmmmmmeeeeeeddd'))