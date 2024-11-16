class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = []
        for file_name in file_names:
            if isinstance(file_name, list):
                self.file_names.extend(file_name)
            else:
                self.file_names.append(file_name)
        self.all_words = {}

    def get_all_words(self):
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            words_list = []
            with open(file_name, encoding='utf-8') as f:
                for line in f:
                    words = line.lower().split()
                    words = [''.join(char for char in word if char not in punctuation) for word in words]
                    words_list.extend(words)
                    self.all_words[file_name] = words_list
        return self.all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result


if __name__ == '__main__':
    # Пример выполнения программы:
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
    print()
    # Другой пример выполнения программы
    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                          'Rudyard Kipling - If.txt',
                          'Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.find('the'))
    print(finder1.count('the'))
