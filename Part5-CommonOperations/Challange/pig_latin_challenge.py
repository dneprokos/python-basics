def topiglatin(sentence):
    vowels = "AEIOUaeiou"
    plwrods = []
    curwords = sentence.split(' ')

    for word in curwords:
        if vowels.find(word[0]) != -1:
            plwrods.append(word + 'way')
        else:
            for i, c in enumerate(word):
                indx = vowels.find(c)
                if indx != -1:
                    prefix = word[0:i]
                    suffix = word[i:]
                    newword = suffix + prefix + 'ay'
                    plwrods.append(newword)
                    break
    return ' '.join(plwrods)

teststr = "This is a test translation to pig latin"
print(topiglatin(teststr))