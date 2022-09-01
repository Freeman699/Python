#10.1
class FileReader():
    '''Simple file read-print class'''

    def __init__(self,file_path):
        '''Initializing file_path'''
        self.file_path = file_path

    def all_file_read(self):
        '''Full file read method'''
        with open(self.file_path) as file:
            contents = file.read()
        print(contents.rstrip())

    def line_by_line_read(self):
        '''Line by line file read method'''
        with open(self.file_path) as file:
            for line in file:
                print(line.rstrip())

    def lines_into_list(self):
        '''Writing strings to a list and moving them out of a block with'''
        with open(self.file_path) as file:
            lines = file.readlines()
        for line in lines:
            print(line.strip())


my_file = 'learning_python.txt'
reader = FileReader(my_file)

print('#1')
reader.all_file_read()

print('#2')
reader.line_by_line_read()

print('#3')
reader.lines_into_list()



print()
#10.2
class WordReplacer():
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_content = []
        self.file_read()

    def file_read(self):
        '''Writing strings to a list'''
        with open(self.file_path) as file:
            lines = file.readlines()
        self.file_content = lines

    def get_file_content(self):
        return self.file_content
    
    def word_replacer(self, old_word, new_word):
        '''Replacing given word with new one in saved file content. Returning new content list'''
        new_file_content = []
        for line in self.file_content:
            new_line = line.replace(old_word, new_word)
            new_file_content.append(new_line)
        return new_file_content



my_file = 'learning_python.txt'
new_replacer = WordReplacer(my_file)
replaced_word_content = new_replacer.word_replacer('Python', 'C++')
for line in replaced_word_content:
    print(line.strip())