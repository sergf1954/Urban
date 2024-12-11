import threading
import time

def task(file, num):
    print("Поток запущен", file)

def write_words(word_count,file_name):
    with open(file_name, 'w', encoding= 'utf-8') as file:

        for i in range(word_count):
            file.write(((lambda x:'Какое-то слово № ' + str(i+1) + '\n')(i)))
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


file = 'example'
txt = '.txt'
num = (10,30,200,100)
current_time_start = time.time()

[threading.Thread(target=write_words(num[i-1],file+str(i)+txt)) for i in range(1,len(num)+1)]

current_time_end = time.time()
print(f"Работа потоков ({current_time_end - current_time_start}) ")


current_time_start = time.time()

t1 = threading.Thread(target=write_words, args=(10,'example5.txt'))
t2 = threading.Thread(target=write_words, args=(30,'example6.txt'))
t3 = threading.Thread(target=write_words, args=(200,'example7.txt'))
t4 = threading.Thread(target=write_words, args=(100,'example8.txt'))


t1.start()
t1.join()
t2.start()
t3.start()
t4.start()

while True:
    if  not t1.is_alive() and not t2.is_alive() and not t3.is_alive() and not t4.is_alive():
        current_time_end = time.time()
        print(f"Работа потоков ({current_time_end - current_time_start}) ")
        break
    else:
        pass