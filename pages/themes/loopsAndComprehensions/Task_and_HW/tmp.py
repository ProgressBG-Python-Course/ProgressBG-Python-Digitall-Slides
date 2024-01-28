text = """apple and banana one apple one banana
a red apple and a green apple"""

words = text.split()


# words_freq = {}
# for word in words:
#     if word in words_freq:
#         words_freq[word]+=1
#     else:
#         words_freq[word] = 1


words_freq = {word:words.count(word) for word in words}
for k,v in words_freq.items():
    print(f'{k:7}- {v}')



