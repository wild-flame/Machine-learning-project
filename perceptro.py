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
