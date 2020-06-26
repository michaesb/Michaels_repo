import numpy as np
import matplotlib.pyplot as plt



def file_read(doc):
    with open(doc, 'r') as values:
        first_line = values.readline()
        info = first_line.split()
        length = int(info[0])
        number_of_arrays = int(info[1])
        format = info[2]
        table_array = np.zeros((number_of_arrays,length))
        i = 0
        for line in values:
            if line[0] !='#':
                list = line.split()
                list = np.array(list)
                table_array[i,:] = list
                i +=1
    return table_array

a,b,c = file_read('c++_text_reader_tutorial.txt')
plt.plot(b,c,'*')
plt.show()
