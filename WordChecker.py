class WordChecker:
    def __init__(self):
        self.dict = self.get_word_dict()

    def get_word_dict(self):
        """Makes a dict out of valid words for checking"""
        returning_dict = {}
        file_stream = open("Collins Scrabble Words (2019) with definitions.txt", "r")
        for line in file_stream:
            temp = line.split("\t")[0]
            returning_dict[temp] = temp

        return returning_dict