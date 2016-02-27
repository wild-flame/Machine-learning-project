import pickle
import sys
from bag_of_words import Vector
import json
import random

def dot_product(values, weights):
    return sum(value * weight for value, weight in zip(values, weights))

def random_list(a_list):
    random.shuffle(a_list)
    return a_list
def gradient_decent(training_set):
    threshold = 1
    learning_rate = 1
    bias = 0 # Drop bias for the moment
    weights = [0] * len(training_set[0][0])
    weights_cached = weights
    training_set = training_set
    iter_count = 0
    R_sum_cached = float("inf")
    while True and iter_count < 20:
        iter_count = iter_count + 1 # counter
        print '\r'+ '-' * 30 + str(iter_count) + '-' * 30
        R_sum = float(0)
        for i in random_list(range(len(training_set))):
            input_vector = training_set[i][0] 
            desired_output = training_set[i][1]
            result = dot_product(input_vector, weights) * desired_output
            # print weights,result
            if result > 1:
                R_sum = R_sum
            elif result <= 1:
                loss = 1 - result
                print "\r>>loss is {0}".format(loss),
                sys.stdout.flush()
                R_sum += loss
                for index, value in enumerate(input_vector):
                    weights[index] = weights[index] + learning_rate * desired_output * value
            else:
                raise BaseException("Undefined case. Unkown Exception. REFNUM: 001")
        if R_sum < R_sum_cached:
            R_sum_cached = R_sum
            weights_cached = weights
        print R_sum, R_sum_cached
    print R_sum_cached

    # print weights_cached, R_sum_cached
    return weights_cached, bias

list = []

# ======================================= #
# ================ MAIN ================= #
# ======================================= #

if __name__ == "__main__":
    from bag_of_words import Vector

    def read_data(filename):
        #TODO: load the data as json instead of object.

        f = open(filename,"r")
        object_data = pickle.load(f)
        f.close()
        return object_data


    def classify(vectors_test,percp_weights, bias):
        true_count = 0
        error_count = 0
        for vector in vectors_test:
            result = dot_product(vector.vec,percp_weights) + bias
            if result > 0:
                true_count += 1
            else:
                error_count += 1
        print "TEST RESULT: {0} is Atheism while {1} is Sports".format(true_count,error_count)

    vectors_atheism = read_data("atheism.vector.data")
    vectors_sports =read_data("sports.vector.data")
    training_vector = []

    for vector in vectors_atheism:
        training_vector.append((vector.vec,1))

    for vector in vectors_sports: 
        training_vector.append((vector.vec,-1))

    # percp_weights,bias = perceptro(training_vector)
    # percp_weights,bias = averaged_perceptro(training_vector)
    percp_weights, bias = gradient_decent(training_vector)

    f = open("gradient_weights.json",'w')
    json.dump((percp_weights,bias),f)
    f.close()

    vectors_atheism_test = read_data("atheism_test.vector.data")
    vectors_sports_test = read_data("sports_test.vector.data")

    classify(vectors_atheism,percp_weights,bias)
    classify(vectors_sports,percp_weights,bias)

    classify(vectors_atheism_test,percp_weights,bias)
    classify(vectors_sports_test,percp_weights,bias)
