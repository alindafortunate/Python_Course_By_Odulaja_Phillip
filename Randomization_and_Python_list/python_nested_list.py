# Accessing items in a nested python list.

sequence = [True, "John", [56, 78], "Chris", [True, ["Jonan", "Lucky", 78], 90.66]]

length_of_sequence = len(sequence)
last_item = sequence[-1]

# length_of_last_item=len(last_item)

nested_last_item = last_item[1]

last_item_of_nested = nested_last_item[-1]

# print(length_of_sequence)
print(last_item)
print(nested_last_item)
print("The last item of the nested item is ", last_item_of_nested)
print("The last item of the nested item using method 2 is ", sequence[-1][1][-1])
