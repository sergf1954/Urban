import threading
import random
import time


class Bank(threading.Thread):
    def __init__(self,balance=None, lock=None):   # , lock: object):
        super().__init__()
        if balance == None:
            self.balance = 0
        if lock == None:
            self.lock = threading.Lock()


    def deposit(self):             # Пополнение баланса
        self.lock.acquire()
        for i in range(100):
            time.sleep(0.001)
            random_number = random.randint(50, 500)
            balance_old = self.balance
            self.balance += random_number
            if self.balance > 500 and self.lock:
                self.balance = balance_old
            else:
                print(f'Пополнение {random_number} Баланс {self.balance}')



    def take(self):
        for i in range(100):
            time.sleep(0.001)
            random_number = random.randint(50, 500)
            print(f' Запрос {random_number}')
            if self.balance > random_number :
                self.balance -= random_number
                print(f'Снятие: {random_number}. Баланс {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                if not self.lock:
                    self.lock.release()



bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f' Итоговый баланс {bk.balance}')
print('-----------------')