from string import punctuation


def pig_it(text):
    pig_latin = []
    for word in text.split():
        if word in punctuation:
            pig_latin.append(word)
        else:
            pig_latin.append(word[1:]+word[0]+'ay')
    return ' '.join(pig_latin)
