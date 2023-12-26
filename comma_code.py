"""A function that takes a list of values and returns a string
separated by commas and a spacew with 'and' inserted before last item."""

def modify_comma_list(word_list):
    """Takes list and adds to string separated by a comma and space"""
    return_string = ''
    if len(word_list) == 0:
        return_string = ''
    elif len(word_list) == 1:
        return_string += word_list[0]
    else:
        for word in word_list[:-1]:
            return_string += str(word) + ', '
        return_string += word_list[-1]
    print(return_string)



def main():
    """Main function."""
    list_one = ['one', 'two', 'three']
    list_two = ['one', 2, 'three']
    list_three = []
    list_four = ['done']

    modify_comma_list(list_one)
    modify_comma_list(list_two)
    modify_comma_list(list_three)
    modify_comma_list(list_four)

if __name__ == '__main__':
    main()