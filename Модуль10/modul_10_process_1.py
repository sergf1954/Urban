
from datetime import datetime
import multiprocessing

filenames = [f'./file {number}.txt' for number in range(1, 5)]

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            else:
                all_data.append(line.strip('\n'))


# Start     Линейный вызов

start_time = datetime.now()
for i in filenames:
    read_info(i)

print((datetime.now() - start_time), ' Линейный')

# Finish     Линейный вызов


#      Start      Многопроцесcный

# if __name__ == "__main__":
#     start_time = datetime.now()
#
#     with multiprocessing.Pool(10) as pool:
#          pool.map(read_info,filenames)
#
#     print((datetime.now() - start_time), 'многопроцессный')

#      Finish      Многопроцесcный


