def get_key_of_max_value(dictionary):
    max_key = ""
    max_value = 0.0
    for key, value in dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key