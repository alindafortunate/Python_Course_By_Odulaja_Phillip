# 
with open('intro.txt', 'r') as file:
    print(file.read())

#Using the write() method
with open('intro.txt', 'w') as new_file :
    new_file.write('I will not only be developing softwares but also tutoring software development concepts.') 
    # The above method replaces whatever was in the file.

#Using the append() method.
#Remember we use this method together with the write() to add the desired contents to the file.
with open('intro.txt','a') as updated_file:
    updated_file.write('\nI am Alinda Fortunate \nA Software Developer \nI am 28 years.')