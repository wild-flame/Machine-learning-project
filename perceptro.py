import pickle
import sys
from bag_of_words import Vector

def dot_product(values, weights):
    return sum(value * weight for value, weight in zip(values, weights))

def perceptro(training_set):
    threshold = 0
    learning_rate = 0.1
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
                print "\r>>error_count is {0}, **updating weight**".format(error_count),
                sys.stdout.flush()

        if error_count == 0:
            break
    return weights

def averaged_perceptro(training_set):
    while 

# ======================================= #
# ================ MAIN ================= #
# ======================================= #

if __name__ == "__main__":
    from bag_of_words import Vector

    def read_data(filename):
        #TODO: Export the data as json instead of object.
        f = open(filename,"r")
        object_data = pickle.load(f)
        f.close()
        return object_data

    vectors_atheism = read_data("atheism.vector.data")
    vectors_sports =read_data("sports.vector.data")
    training_vector = []

    for vector in vectors_atheism:
        training_vector.append((vector.vec,1))

    for vector in vectors_sports: 
        training_vector.append((vector.vec,-1))

    percp_weights = perceptro(training_vector)
    percp_weights = averaged_perceptro(training_vector)

    print percp_weights
    f = open("percp_weights.json",'w')
    json.dump(percp_weights,f)
    f.close()

    vectors_atheism_test = read_data("atheism_test.vector.data")
    vectors_sports_test = read_data("sports_test.vector.data")

def classify(vectors_test,percp_weights):
    true_count = 0
    error_count = 0
    for vector in vectors_test:
        result = dot_product(vector.vec,percp_weights)
        if result > 0:
            true_count += 1
        else:
            error_count += 1
    print "TEST RESULT: {0} is Atheism while {1} is Sports".format(true_count,error_count)

    classify(vectors_atheism_test,percp_weights)
    classify(vectors_sports_test,percp_weights)
