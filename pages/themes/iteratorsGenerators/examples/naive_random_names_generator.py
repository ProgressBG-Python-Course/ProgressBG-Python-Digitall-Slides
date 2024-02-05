from random import randint

def cyrillic_names_generator(count=5, min_length = 3, max_length = 8 ):
    def _gen_random_vowel():
        idx = randint(0, len(vowels)-1)
        return vowels[idx]

    def _gen_random_consonant():
        # we need only consonant, so loop until one is found
        while True:
            # code 1072 in unicode is for 'a' (CYRILLIC SMALL LETTER A)
            letter = chr(randint(1072, 1103))

            if letter not in vowels:
                return letter

    def _gen_random_name():
        name_length = randint(min_length, max_length)
        # generate list of alternating vowels and consonants
        name_letters = [
            _gen_random_vowel() if i%2 else _gen_random_consonant()
                for i in range(name_length)
        ]
        return "".join(name_letters).capitalize()

    vowels = ["а","о","е","и","ю","я"]

    # print(_gen_random_vowel())
    # print(_gen_random_consonant())
    # print(_gen_random_name())

    for c in range(count):
        yield _gen_random_name()


# generate 10 Cyrillic "names":
for name in cyrillic_names_generator(count=10):
    print(name, end=",")

# Сеьехиц,Пюмедяц,Ыодя,Чосюдапю,Ряцаые,Щитисюфю,Жех,Вефел,Щит,Уюбежя,