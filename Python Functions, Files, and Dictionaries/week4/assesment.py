def beginning(input_list):
    output_list = []
    index = 0
    while (index < len(input_list) and index<10):
        if input_list[index] != 'bye':
            output_list.append(input_list[index])
            index += 1
        else:
            break
    return output_list
