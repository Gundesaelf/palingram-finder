# |---------------------------------IMPORTS---------------------------------|

import sys

# |---------------------------------FUNCTIONS---------------------------------|

def load_file():
    fname = '2of4brif.txt'

    try:
        with open(fname) as file:
            loaded_txt = file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f'\nError opening {fname}. Terminating program.')
        sys.exit(1)

def  find_palingrams():
    words = set(load_file())

    palingrams_list = []

    for word in words:
        end = len(word)
        reversed_word = word[::-1]
        
        if end > 1:
            for i in range(end):
                if word[i:] == reversed_word[:end - i] and reversed_word[end - i:] in words:
                    palingrams_list.append((word, reversed_word[end - i:]))
                if word[:i] == reversed_word[end - i:] and reversed_word[:end - i] in words:
                    palingrams_list.append((reversed_word[:end - i], word))

    return palingrams_list

palingrams = find_palingrams()
palingrams_sorted = sorted(palingrams)

for first, second in palingrams_sorted:
    print(f'First: {first}, Second: {second}')
