
class WordsFinder:
    file_names = []              # Список файлов
    def __init__(self,*args):
        self.file_names = args

    def get_all_words(self):
        all_words = dict()        #Словарь
        for i in self.file_names:
            with open(i, encoding='utf-8')  as file:
                str_new = (file.read().translate(str.maketrans(",.=!?;:-", "        "))).split()
                all_words[i] = str_new

        return all_words

    def find_count(self, word):

        count = []
        for name, words in WordsFinder.get_all_words(self).items():
            file_name = name
            j = 0  # сколько нашли
            for i in enumerate(words):
                if word.lower() in i[1].lower():
                    j += 1
                    count.append(i[0]+1)
            if j == 0:
               return False
            else:
                return file_name,count
    def count(self, word):
        if WordsFinder.find_count(self, word):
            dictionary = dict()
            dictionary[WordsFinder.find_count(self, word)[0]]\
                = len(WordsFinder.find_count(self, word)[1])
            return dictionary
        else:
            return (' Нет такого слова')

    def find(self,word):
        if WordsFinder.find_count(self,word):
            dictionary = dict()
            dictionary[WordsFinder.find_count(self, word)[0]] \
                = WordsFinder.find_count(self, word)[1][0]
            return dictionary
        else:
            return (' Нет такого слова')


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))     # 3 слово по счёту
print(finder2.count('teXT'))    # 4 слова teXT в тексте всего
print(finder2.count('Наnйти'))

# finder2 = WordsFinder('ttt.txt')
# print(finder2.get_all_words())
# print(finder2.find('captain'))
# print(finder2.count('captain'))
#
# Результат:
#
# {'Walt Whitman - O Captain! My Captain!.txt': ['o', 'captain', 'my', 'captain', 'o', 'captain', 'my', 'captain', 'our', 'fearful', 'trip', 'is', 'done', 'the', 'ship', 'has', 'weather’d', 'every', 'rack', 'the', 'prize', 'we', 'sought', 'is', 'won', 'the', 'port', 'is', 'near', 'the', 'bells', 'i', 'hear', 'the', 'people', 'all', 'exulting', 'while', 'follow', 'eyes', 'the', 'steady', 'keel', 'the', 'vessel', 'grim', 'and', 'daring', 'but', 'o', 'heart', 'heart', 'heart', 'o', 'the', 'bleeding', 'drops', 'of', 'red', 'where', 'on', 'the', 'deck', 'my', 'captain', 'lies', 'fallen', 'cold', 'and', 'dead', 'o', 'captain', 'my', 'captain', 'rise', 'up', 'and', 'hear', 'the', 'bells', 'rise', 'up', '—', 'for', 'you', 'the', 'flag', 'is', 'flung', '—', 'for', 'you', 'the', 'bugle', 'trills', 'for', 'you', 'bouquets', 'and', 'ribbon’d', 'wreaths', '—', 'for', 'you', 'the', 'shores', 'acrowding', 'for', 'you', 'they', 'call', 'the', 'swaying', 'mass', 'their', 'eager', 'faces', 'turning', 'here', 'captain', 'dear', 'father', 'this', 'arm', 'beneath', 'your', 'head', 'it', 'is', 'some', 'dream', 'that', 'on', 'the', 'deck', 'you’ve', 'fallen', 'cold', 'and', 'dead', 'my', 'captain', 'does', 'not', 'answer', 'his', 'lips', 'are', 'pale', 'and', 'still', 'my', 'father', 'does', 'not', 'feel', 'my', 'arm', 'he', 'has', 'no', 'pulse', 'nor', 'will', 'the', 'ship', 'is', 'anchor’d', 'safe', 'and', 'sound', 'its', 'voyage', 'closed', 'and', 'done', 'from', 'fearful', 'trip', 'the', 'victor', 'ship', 'comes', 'in', 'with', 'object', 'won', 'exult', 'o', 'shores', 'and', 'ring', 'o', 'bells', 'but', 'i', 'with', 'mournful', 'tread', 'walk', 'the', 'deck', 'my', 'captain', 'lies', 'fallen', 'cold', 'and', 'dead', 'walt', 'whitman']}
# {'Walt Whitman - O Captain! My Captain!.txt': 2}
# {'Walt Whitman - O Captain! My Captain!.txt': 10}