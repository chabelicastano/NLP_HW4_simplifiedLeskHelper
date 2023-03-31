# Chabeli Castano Arango
# NLP HW4
# Helper for question 1b - Lesk Algorithm

sentence = ['got', 'money', 'bank']

# change the word depending in what senses you need
word = 'bank'

sense = ''

# characters to be deleted from the senses - to make search for overlapping easier
del_chars = ['(v)', '(', ')', '"', 's:', ',', ':', ';', '.']

file_name = word + '_senses.txt'

with open(file_name, 'r', encoding='utf8', newline='\n') as file:
    line_no = 1
    for line in file:
        count = 0
        sense = line
        sense = sense.lower()
        for ch in del_chars:
            sense = sense.replace(ch, "")
        sense = sense.split()
        for wd in sentence:
            sp_count = sense.count(wd)
            count = count + sp_count
            # print('{}  --- {}\n'.format(wd, sp_count))
        print('{} {} -----> overlap: {}\n'.format(line_no, line, count))
        line_no += 1
