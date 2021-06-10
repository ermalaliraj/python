# A concordancer is a tool for exploring textual data. Given a corpus of text data and a word, it extracts the occurrences
# of this word as well as the left and right contexts in which this word appears.
# For example, if given the preceding paragraph and the word "a", it would display the following result:
#                            a    concordancer is a to...
# a concordancer is          a    tool for exploring t...
# ... textual data. given    a    corpus of text data ...
# ...pus of text data and    a    word, it extracts th...

class Concordancier:
    def __init__(self, file_name):
        file = open(file_name) # save the text as a list of lines
        self.text = file.readlines()

    def display(self, word, context_length=20):
        for line in self.text:
            line = " " + line.strip().lower() + " " # add spaces: tip to search for whole words
            match = line.find(" " + word.lower() + " ")
            while match >= 0: # if find
                # determine the beginning and the end of word
                beginning = match + 1
                end = match + len(word) + 2

                # determine the beginning and the end of context
                beginning_context = max(0, match-context_length)
                end_context = min(end+context_length, len(line)) # extract the contexts of the line
                context_left = line[beginning_context:match]
                context_right = line[end:end_context]

                # format the contexts
                s = "{0:>{width}} {1} {2:<{width}}".format(context_left, word.upper(), context_right, width=context_length)
                print(s)

                match = line.find(" " + word.lower() + " ", end) # look for the next occurrence

c = Concordancier("austen.txt")
c.display("emma")