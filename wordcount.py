file_name = "test.txt"

open_file = open(file_name)

def word_count(open_file):
    word_count_dict = {}
    for line in open_file: # go through each line in file_name
        words = line.split()
        print "words=", words
        for word in words:
            print "word=", word # get each word in each line
            # for word in line:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else: 
                word_count_dict[word] = 1
    for word, count in word_count_dict.items():
        print "%s %d" %(word, count)

word_count(open_file)
# need to know number of words in file_name
# return/print (word, word count)
