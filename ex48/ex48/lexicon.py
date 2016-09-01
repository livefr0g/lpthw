""" Lexicon module scans user input and attempts to match words to known types """
directions = ('north', 'south', 'east', 'west', 'down',
                'up', 'left', 'right', 'back')
verbs = ('go', 'stop', 'kill', 'eat')
stops = ('the', 'in', 'of', 'from', 'at', 'it')
nouns = ('door', 'bear', 'princess', 'cabinet')


def scan(input):
    words = input.lower().split(' ')
    sentence = []

    for w in words:
        if w in directions:
            sentence.append(('direction', w))
        elif w in verbs:
            sentence.append(('verb', w))
        elif w in stops:
            sentence.append(('stop', w))
        elif w in nouns:
            sentence.append(('noun', w))
        else:
            try:
                sentence.append(('number', int(w)))
            except ValueError:
                sentence.append(('error', w))

    return sentence
