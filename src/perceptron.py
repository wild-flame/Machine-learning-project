import pickle
import sys
from bag_of_words import Vector
import json

def dot_product(values, weights):
    return sum(value * weight for value, weight in zip(values, weights))

def perceptro(training_set):
    threshold = 0
    learning_rate = 0.1
    bias = 0
    weights = list(training_set[0][0])
    training_set = training_set
    counter = 0
    while True:
        counter = counter + 1 # counter
        print('-' * 60)
        error_count = 0
        for input_vector, desired_output in training_set:
            result = dot_product(input_vector, weights) > threshold
            if result == True:
                output = 1
            else:
                output = -1
            # print "result is {0}, output is {1}, desired_output is {2} ".format(result,output, desired_output)
            print  '\r>> You have finished {0} '.format(counter),
            if output != desired_output:
                error_count += 1
                for index, value in enumerate(input_vector):
                    weights[index] = weights[index] + desired_output * value
                bias = bias + desired_output
                sys.stdout.flush()
                print "\r>> error_count is {0}, **updating weight nad bias**".format(error_count),
        if error_count == 0:
            break
    return weights, bias

def averaged_perceptro(training_set):
    weights = [0.0] * len(training_set[0][0])  # initialize weights
    cached_weights = [0.0] * len(weights) # initialize cached_weights
    bias = 0.0                            # initialize bias
    cached_bias = 0.0                     # initialize cached bias
    counter = 1                         # initialize example counter to 1
    iter = 0
    while True:
        correct_count = 0
        iter = iter + 1
        print  '\r>> You have finished {0} '.format(iter)
        error_count = 0
        for input_vector, desired_output in training_set:
            result = dot_product(input_vector, weights) * desired_output
            # print weights, result
            if result > 0:
                correct_count += 1
            else:
                error_count += 1
                for index, value in enumerate(input_vector): # This is how vectors are calculated in python 
                    weights[index] = weights[index] + desired_output * value
                    cached_weights[index] = cached_weights[index] + desired_output * counter * value
                bias = bias + desired_output
                cached_bias = cached_bias + desired_output * counter
                sys.stdout.flush()
                print "\r>> error_count is {0}, ***updating weight and bias**".format(error_count),

            counter = counter + 1
        if error_count == 0:
            break
    # print weights, bias 

    for index, value in enumerate(cached_weights): # This is how vectors are calculated in python 
        weights[index] = weights[index] - value / counter
    bias = bias - cached_bias / counter 

    return weights, bias

# ======================================= #
# ================ MAIN ================= #
# ======================================= #

if __name__ == "__main__":
    from bag_of_words import Vector

    DATA_PATH = "../data"

    def read_data(filename):
        #TODO: Export the data as json instead of object.
        f = open(filename,"r")
        object_data = pickle.load(f)
        f.close()
        return object_data


    def classify(vectors_test,percp_weights,bias):
        true_count = 0
        error_count = 0
        for vector in vectors_test:
            result = dot_product(vector.vec,percp_weights) + bias
            if result > 0:
                true_count += 1
            else:
                error_count += 1
        print "TEST RESULT: {0} is Atheism while {1} is Sports".format(true_count,error_count)

    vectors_atheism = read_data(DATA_PATH + "atheism.vector.data")
    vectors_sports =read_data(DATA_PATH + "sports.vector.data")
    training_vector = []

    for vector in vectors_atheism:
        training_vector.append((vector.vec,1))

    for vector in vectors_sports: 
        training_vector.append((vector.vec,-1))

    # percp_weights,bias = perceptro(training_vector)
    percp_weights,bias = averaged_perceptro(training_vector)
    percp_weights

    f = open(DATA_PATH + "percp_weights.json",'w')
    json.dump((percp_weights,bias),f)
    f.close()

    vectors_atheism_test = read_data(DATA_PATH + "atheism_test.vector.data")
    vectors_sports_test = read_data(DATA_PATH + "sports_test.vector.data")

    classify(vectors_atheism,percp_weights,bias)
    classify(vectors_sports,percp_weights,bias)

    classify(vectors_atheism_test,percp_weights,bias)
    classify(vectors_sports_test,percp_weights,bias)
