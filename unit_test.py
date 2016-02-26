import unittest
import perceptron
# from bag_of_words import *

# Atheism = Document("data/train/atheism")
# Atheism.read_dir()
# bow = BOW(Atheism.words)
# bow = bow._bows
# words = ["a","b","c"]
# vec = Vector(words,bow)
# words = vec._read(Atheism.pathnames[2])
# tuples = {}
#
# for word in bow:
#     tuples.update({word:words.count(word)})

class TestPerceptroMethod(unittest.TestCase):

    def test_perceptron(self):
        print("==============test_perceptron=========")
        weights = [0,0,0]
        training_set = [((1, 0, 0), 1), ((1, 0, 1), 1), ((1, 1, 0), 1), ((1, 1, 1), -1)]
        weights, bias = perceptron.perceptro(training_set)
        print weights, bias
        self.assertIsInstance(weights, list)
        self.assertIsInstance(bias, int)

    def test_perceptron_average(self):
        print("==============test_perceptron_average=========")
        weights = [0,0,0]
        training_set = [((1, 0, 0), 1), ((1, 0, 1), 1), ((1, 1, 0), 1), ((1, 1, 1), -1)]
        weights, bias = perceptron.averaged_perceptro(training_set)
        print weights, bias
        self.assertIsInstance(weights, list)
        self.assertIsInstance(bias, int)

if __name__ == '__main__':
    unittest.main()
