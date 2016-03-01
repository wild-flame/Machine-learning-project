from bag_of_words import Document, Vector, BOW
from gradient_descent import gradient_decent
from perceptron import perceptro, averaged_perceptro, dot_product
import json

def dump_vector(object,filename):
    """dump_the_vector into json file, throw the other infomation away"""
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
        vectors.append(Vector(filename,bow).vec)
    return vectors

def convert_testdata_to_vector(pathname,bow):
    vector_l = []
    doc = Document(pathname)
    doc.read_dir()
    print("{0} file is loading from {1}".format(len(doc.pathnames),doc.srcpath))
    for filename in doc.pathnames:
        vector_l.append(Vector(filename,bow).vec)
    return vector_l

def load_vector(filename):
    """
    input: ::String filename
    output: ::list vector
    Load the data from json file
    """
    f = open(filename,"r")
    vector = json.load(f)
    f.close()
    return vector

def feature_extraction():

    DATA_PATH = "../data/"

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

    vectors_atheism_test = convert_testdata_to_vector( DATA_PATH + "data/test/atheism",bow)
    vectors_sports_test = convert_testdata_to_vector( DATA_PATH + "data/test/sports",bow)
    vectors_politics_test = convert_testdata_to_vector( DATA_PATH + "data/test/politics",bow)
    vectors_science_test = convert_testdata_to_vector( DATA_PATH + "data/test/science",bow)

    dump_vector(vectors_atheism_test, DATA_PATH + "atheism_test.vector.json")
    dump_vector(vectors_sports_test, DATA_PATH + "sports_test.vector.json")
    dump_vector(vectors_politics_test, DATA_PATH + "politics_test.vector.json")
    dump_vector(vectors_science_test, DATA_PATH + "science_test.vector.json")

def classify(vectors_test,percp_weights, bias):
    true_count = 0
    error_count = 0
    for vector in vectors_test:
        result = dot_product(vector,percp_weights) + bias
        if result > 0:
            true_count += 1
        else:
            error_count += 1
    return true_count, error_count

def train(func, *vectors_list):
    params_set = []
    for i in range(len(vectors_list)):
        training_set = []
        for j in range(len(vectors_list)):
            for vector in vectors_list[j]:
                training_set.append((vector,1 if i==j else -1))
        weights,bias = func(training_set)
        params_set.append((weights,bias))
    return params_set

if __name__ == "__main__":
    # feature_extraction()

    DATA_PATH = "../data/"

    vectors_atheism = load_vector( DATA_PATH + "atheism.vector.json")
    vectors_sports = load_vector( DATA_PATH + "sports.vector.json")
    vectors_politics = load_vector( DATA_PATH + "politics.vector.json")
    vectors_science = load_vector( DATA_PATH + "science.vector.json")

    vectors_atheism_test = load_vector( DATA_PATH + "atheism_test.vector.json")
    vectors_sports_test = load_vector( DATA_PATH + "sports_test.vector.json")
    vectors_politics_test = load_vector( DATA_PATH + "politics_test.vector.json")
    vectors_science_test = load_vector(DATA_PATH + "science_test.vector.json")

    parames_set = train(gradient_decent, vectors_atheism, vectors_sports, vectors_politics, vectors_science)

    def multi_classify(vectors_test,weights):
        count = [0,0,0,0]
        result = [0,0,0,0]
        for vector in vectors_test:
            for i in range(4):
                result[i] = dot_product(vector,weights[i][0]) + weights[i][1]
            if result[0] > result[1] and result[0] > result[2] and result[0] > result[3]:
                count[0] += 1
            elif result[1] > result[2] and result[1] > result[3]:
                count[1] += 1
            elif result[2] > result[3] and result[2] > result[3]:
                count[2] += 1
            else:
                count[3] += 1
        return count

for i in range(4):
    #classify(vectors_atheism_test,parames_set[i][0],parames_set[i][1])
    #classify(vectors_sports_test,parames_set[i][0],parames_set[i][1])
    #classify(vectors_politics_test,parames_set[i][0],parames_set[i][1])
    #classify(vectors_science_test,parames_set[i][0],parames_set[i][1])

    multi_classify(vectors_atheism_test,parames_set)
    multi_classify(vectors_sports_test,parames_set)
    multi_classify(vectors_politics_test,parames_set)
    multi_classify(vectors_science_test,parames_set)

