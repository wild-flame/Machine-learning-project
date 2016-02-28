import os
import nltk
import collections
import pickle
import sys

counter = 0 # GOLABLE VARIABLES !!! 


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
        print  '\r>> You have finished {0} )'.format(counter),
        counter = counter + 1
        sys.stdout.flush()
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

    "
    def get_vectors(self):
        for filename in self.filenams:
            vec = Vector()
    "

class BOW(object):
    """This is the bag-of-word object"""
    def __init__(self, *words_list):
        self._bows = set()
        for words in words_list:
            self._bows |= set(words)

# ======================================= #
# ================ MAIN ================= #
# ======================================= #

# INITAILIZING TO BUILD THE INPUT

if __name__ == "__main__":

    DATA_PATH = "../data"

    def dump_data(object,filename):
       #TODO: Export the data as json instead of object.
        f = open(filename,"w")
        pickle.dump(object,f)
        f.close()

    vectors_atheism = []
    vectors_sports = []

    Atheism = Document(DATA_PATH + "data/train/atheism") # The srcpath can be write in when create the instance
    Atheism.read_dir()

    print("{0} file is loading from {1}".format(len(Atheism.pathnames),Atheism.srcpath))

    Sports = Document(DATA_PATH + "data/train/sports")
    Sports.read_dir()
    print("{0} file is loading from {1}".format(len(Sports.pathnames),Sports.srcpath))

    # LIST OF THE WORDS IN A DICT: for each file read, check the words in the dictionary or not.
    dictionary = BOW(Atheism.words, Sports.words)
    bow = dictionary._bows

    # Building the vector through document.
    for filename in Atheism.pathnames:
        vectors_atheism.append(Vector(filename,bow))

    for filename in Sports.pathnames:
        vectors_sports.append(Vector(filename,bow))

    print("dumping data in progress")
    dump_data(vectors_atheism,DATA_PATH + "atheism.vector.data")
    dump_data(vectors_sports,DATA_PATH + "sports.vector.data")

    def convert_testdata_to_vector(pathname,bow):
        vector_l = []
        doc = Document(pathname)
        doc.read_dir()
        print("{0} file is loading from {1}".format(len(doc.pathnames),doc.srcpath))
        for filename in doc.pathnames:
            vector_l.append(Vector(filename,bow))
        return vector_l

    vectors_atheism_test = convert_testdata_to_vector(DATA_PATH + "data/test/atheism",bow)
    vectors_sports_test = convert_testdata_to_vector(DATA_PATH + "data/test/sports",bow)

    dump_data(vectors_atheism_test, DATA_PATH + "atheism_test.vector.data")
    dump_data(vectors_sports_test, DATA_PATH + "sports_test.vector.data")
