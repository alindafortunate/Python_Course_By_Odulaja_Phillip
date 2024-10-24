def count_words(sentence: str, *args):

    # working on the string to make it a list of items.
    separated_sentence = sentence.split(" ")
    # print(separated_string)

    # Tracing similar words and counting word occurences
    #  in the list of separated items and create the dictionary.
    result = dict()
    for arg in args:
        arg_count = separated_sentence.count(arg)
        result[arg] = arg_count

    # for separate_items in separated_sentence:

    #     count_of_item_occurency = separated_sentence.count(separate_items)

    #     for arg in args:
    #         if arg == separate_items:
    #             result[arg] = count_of_item_occurency
    #             # result[arg] = separated_string.count(separate_items)
    #             # The above works fine too.

    #         else:
    #             pass

    return result


sentence = "Senior Python Developer with experience with Python and Django framework"
print(count_words(sentence, "Python", "Senior", "with", "experience"))
