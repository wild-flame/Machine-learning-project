import os
import nltk
import collections
import pickle

counter = 0

class Vector(object):
    """vector is where the vector was used in machine learning(svm)"""
    def __init__(self, filename, bow):
        """Initialization: Called to build vector from Document with bag_of_words"""
        self.desired_output = None
        self.output = None
        self.words = self._read(filename)
        self.bow = bow
        self.vec = tuple(self._cal_vector(self.words,self.bow))

    def _read(self,filename):
        """read the files in to tokens, currently the function relys on the nltk library"""
        text = open(filename, 'r').read()
        try:
            text = unicode(text, 'utf-8')
        except UnicodeError:
            text = unicode(text, 'latin-1')
        return nltk.word_tokenize(text)

    def _cal_vector(self,words,bow):
        global counter
        vec_list = []
        for word in bow:
            vec_list.append(words.count(word))
        counter = counter + 1
        print counter
        return vec_list

class Document(object):
    def __init__(self, srcpath):
        self.srcpath = srcpath
        self.pathnames = []
        self.numdocs = 0
        self.words = []

    def get_filenames(self,*srcpath):
        """Get all the filenames under the srcpath"""
        if (len(srcpath) == 0 ):
            srcpath = self.srcpath
        else:
            self.srcpath = srcpath
        for root, dirs, files in os.walk(srcpath):
            for file in files:
                self.pathnames[len(self.pathnames):] = [os.path.join(root, file)]

    def read_dir(self,*srcpath): 
        """Read the files in an directory"""
        self.get_filenames()
        self._read_dir_file()

    def _read_dir_file(self):
        """read the file in the Doucment"""
        for filename in self.pathnames:
            text = open(filename, 'r').read()
            self.words += self._read(filename, text)

    def _read(self,filename,text):
        "read the files in to tokens using lirary"
        try:
            text = unicode(text, 'utf-8')
        except UnicodeError:
            text = unicode(text, 'latin-1')
        self.numdocs += 1
        return nltk.word_tokenize(text)

    "TODO:def write_csv:"
    "TODO:def read_csv:"

    def get_vectors(self):
        for filename in self.filenams:
            vec = Vector()

class BOW(object):
    """This is the bag-of-word object"""
    def __init__(self, *words_list):
        self._bows = set()
        for words in words_list:
            self._bows |= set(words)

# INITAILIZING TO BUILD THE INPUT

if __name__ == "__main__":

    vectors_atheism = []
    vectors_sports = []

    Atheism = Document("data/train/atheism") # The srcpath can be write in when create the instance
    Atheism.read_dir()

    print("{0} file is loaded from {1}".format(len(Atheism.pathnames),Atheism.srcpath))
  
    Sports = Document("data/train/sports")
    Sports.read_dir()
    print("{0} file is loaded from {1}".format(len(Sports.pathnames),Sports.srcpath))

    # LIST OF THE WORDS IN A DICT: for each file read, check the words in the dictionary or not.
    dictionary = BOW(Atheism.words, Sports.words)
    bow = dictionary._bows

    # Building the vector through document.
    for filename in Atheism.pathnames:
        vectors_atheism = vectors_atheism.append(Vector(filename,bow))

    for filename in Sports.pathnames:
        vectors_sports = vectors_sports.append(Vector(filename,bow))

    # The peceptro algorithm
    f = file.open("atheism.vector.data","w")
    pickel.dump(vectors_atheism.f)
    f.close()
    f = file.open("sports.vector.data","w")
    pickel.dump(sports_atheism.f)
    f.close()

def dot_product(values, weights):
    return sum(value * weight for value, weight in zip(values, weights))

def perceptro(training_set):
    threshold = 0
    learning_rate = 0.1
    weights = [1, 0, 0]
    training_set = [((1, 0, 0), 1), ((1, 0 , 1), 1), ((1, 1, 0), 1), ((1, 1, 1), -1)]
    while True:
        print('-' * 60)
        error_count = 0
        for input_vector, desired_output in training_set:
            print(weights)
            result = dot_product(input_vector, weights) > threshold
            if result == True:
                output = 1
            else:
                output = -1
            print "result is {0}, output is {1}, desired_output is {2} ".format(result,output, desired_output)
            if output != desired_output:
                error_count += 1
                print('**updating weight**')
                for index, value in enumerate(input_vector):
                    weights[index] = weights[index] + desired_output * value
        if error_count == 0:
            break

# perceptro(training_set)

# print weights

# TODO: write the unit test: 1. Atheism should not be empty



Atheism = Document("data/train/atheism") # The srcpath can be write in when create the instance
Atheism.read_dir()

print("{0} file is loaded from {1}".format(len(Atheism.pathnames),Atheism.srcpath))

Sports = Document("data/train/sports")
Sports.read_dir()
print("{0} file is loaded from {1}".format(len(Sports.pathnames),Sports.srcpath))

# LIST OF THE WORDS IN A DICT: for each file read, check the words in the dictionary or not.
dictionary = BOW(Atheism.words, Sports.words)
bow = dictionary._bows

vectors_atheism = []
vectors_sports = []

# Building the vector through document.
for filename in Atheism.pathnames:
    vectors_atheism.append(Vector(filename,bow))

for filename in Sports.pathnames:
    vectors_sports.append(Vector(filename,bow))
