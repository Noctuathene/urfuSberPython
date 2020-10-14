def flatten(input_list):
    result = []
    for elem in input_list:
        if(type(elem) is list):
            result.extend(flatten(elem))
        else:
            result.append(elem)
    return result
