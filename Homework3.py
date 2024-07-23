
class Words_Finder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        result = {}
        for file in self.file_names:
            with open(file) as f:
                content = f.read()
                words = content.split()
                result[file] = words
        return result

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for key, value in all_words.items():
            index = value.index(word)
            result[key] = index
            return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for key, value in all_words.items():
            result[key] = value.count(word)
        return result

finder2 = Words_Finder('test.txt')
print(finder2.get_all_words())
print(finder2.find('is'))
print(finder2.count('it'))