
from bag_of_words import *

Atheism = Document("data/train/atheism")
Atheism.read_dir()
bow = BOW(Atheism.words)
bow = bow._bows
words = ["a","b","c"]
vec = Vector(words,bow)
words = vec._read(Atheism.pathnames[2])
tuples = {}

for word in bow:
    tuples.update({word:words.count(word)})

