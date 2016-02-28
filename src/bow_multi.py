from bag_of_words import Document, Vector, BOW
import json

if __name__ == "__main__":

    DATA_PATH = "../data"

    def dump_vector(object,filename):
        "dump_the_vector into json file, throw the other infomation away"
        f = open(filename,"w")
        json.dump(object,f)
        f.close()

    def load_Document(pathname):
        instance = Document(pathname)
        instance.read_dir()
        print "{0} file is loading from {1}".format(len(instance.pathnames),instance.srcpath)
        return instance 

    def create_vectors(Document):
        vectors = []
        for filename in Document.pathnames:
            vectors = vectors.append(Vector(filename,bow).vec)
        return vectors

    Atheism = load_Document(DATA_PATH + "data/train/atheism")
    Sports = load_Document(DATA_PATH + "data/train/sports")
    Politics = load_Document(DATA_PATH + "data/train/politics")
    Science = load_Document(DATA_PATH + "data/train/Science")

    # LIST OF THE WORDS IN A DICT: for each file read, check the words in the dictionary or not.
    dictionary = BOW(Atheism.words, Sports.words, Politics.words, Science.words)
    bow = dictionary._bows

    # Building the vector through document.
    vectors_atheism = create_vectors(Atheism)
    vectors_sports = create_vectors(Sports)
    vectors_politics = create_vectors(Politics)
    vectors_science = create_vectors(Science)

    print("dumping data in progress")
    dump_vector(vectors_atheism, DATA_PATH + "atheism.vector.json")
    dump_vector(vectors_sports, DATA_PATH + "sports.vector.json")
    dump_vector(vectors_politics, DATA_PATH + "politics.vector.json")
    dump_vector(vectors_science, DATA_PATH + "science.vector.json")

    def convert_testdata_to_vector(pathname,bow):
        vector_l = []
        doc = Document(pathname)
        doc.read_dir()
        print("{0} file is loading from {1}".format(len(doc.pathnames),doc.srcpath))
        for filename in doc.pathnames:
            vector_l.append(Vector(filename,bow).vec)
        return vector_l

    vectors_atheism_test = convert_testdata_to_vector( DATA_PATH + "data/test/atheism",bow)
    vectors_sports_test = convert_testdata_to_vector( DATA_PATH + "data/test/sports",bow)
    vectors_politics_test = convert_testdata_to_vector( DATA_PATH + "data/test/politics",bow)
    vectors_science_test = convert_testdata_to_vector( DATA_PATH + "data/test/science",bow)

    dump_vector(vectors_atheism_test, DATA_PATH + "atheism_test.vector.json")
    dump_vector(vectors_sports_test, DATA_PATH + "sports_test.vector.json")
    dump_vector(vectors_politics_test, DATA_PATH + "politics_test.vector.json")
    dump_vector(vectors_science_test, DATA_PATH + "science_test.vector.json")
