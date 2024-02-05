from random import randint

class NaiveRandomNamesIterable():
    """Iterable on random Cyrillic "names"  """

    def __init__(self, name_count, min_length, max_length):
        self.name_count = name_count
        self.min_length = min_length
        self.max_length = max_length
        self.count = 0

        self.vowels = ["а","о","е","и","ю","я"]

    def __generate_random_consonant(self):
        # we need only consonant, so loop until one is found
        while True:
            # code 1072 in unicode is for 'a' (CYRILLIC SMALL LETTER A)
            letter = chr(randint(1072, 1103))

            if letter not in self.vowels:
                return letter

    def __get_random_vowel(self):
        vowels_last_index = len(self.vowels)-1

        return self.vowels[randint(0,vowels_last_index)]

    def __create_random_name(self):
        """Create random "name", between min_length and max_length letters long.
                The "name" letters are alternating random generated vowels/consonants

            Returns:
                [string] - the generated random name with first letter capitalized
        """
        self.name_length = randint(self.min_length,self.max_length)
        self.name = ""

        should_generate_vowel = False
        for i in range(self.name_length):
            if should_generate_vowel:
                l = self.__get_random_vowel()
            else:
                l = self.__generate_random_consonant()

            should_generate_vowel = not should_generate_vowel

            self.name += l

        return self.name.capitalize()

    def __iter__(self):
        return self

    def __next__(self):
        name = self.__create_random_name()

        if ( self.count < self.name_count):
            self.count += 1
            return name
        else:
            raise StopIteration

# generate 10 Cyrillic "names":
names = NaiveRandomNamesIterable(name_count=10, min_length = 3, max_length = 8)

for name in names:
    print(name, end=",")


# Зечящ,Эяб,Люьийа,Синемеыю,Бацеци,Эячи,Гемяфодо,Лоыяэюч,Бяъющ,Ъюметосю,