import re

text = ''

file = open('filelocation')
#open some file like open('C://users/a.txt')
for line in file:
    text = text + line
file.close()

#print text
result = re.findall(' to ',text)#find all word ' to ' in the file
print len(result)

a_word = re.findall('( [a][a-z][a-z] )',text)#all word start with a
A_word = re.findall('([A][a-z][a-z] )',text)#all word start with A
a_word = set(a_word)
A_word = set(A_word)
print a_word, line, A_word, line, len(a_word)+len(A_word)
'''
simpword = re.findall('( \w{3} )',text)
print set(simpword)
'''
raw_input()
