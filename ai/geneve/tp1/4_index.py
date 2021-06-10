# Create a script that takes as input a file of text data and displays the list of words contained in
# that file in alphabetical order, as well as the lines in which the words appear.

index_dict = {}
line_num = 1
file = open("austen.txt", "r")

for line in file:
    words = line.split()
    for word in words:
        if word not in index_dict:
            index_dict[word] = []
        index_dict[word].append(line_num)
        line_num += 1
        
for word in sorted(index_dict):
    print(word, end="\t\t")
    for line in index_dict[word]:
        print(line, end=" ")
    print()
