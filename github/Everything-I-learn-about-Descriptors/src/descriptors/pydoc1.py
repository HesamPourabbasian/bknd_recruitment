import os


class DirectorySize:

    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))


class Directory:
    size = DirectorySize()  # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname  # Regular instance attribute


s = Directory('songs')
g = Directory('games')
s.size  # The songs directory has twenty files

g.size  # The games directory has three files

os.remove('games/chess')  # Delete a game
g.size  # File count is automatically updated
