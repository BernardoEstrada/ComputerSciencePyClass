import shelve
a=input('a: ')
d = shelve.open('score.txt')
d['score'] = a
d.close()


d = shelve.open('score.txt')
print(d['score'])
d.close()
