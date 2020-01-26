obj = []
def inputs():
    global obj
    data=''
    while data!='stop' and data!='end':
        data=input('Type in data ')
        if data!='stop' and data!='end':
            obj.append(data)

print('''Type in data to add up to your list,
type in 'end' or 'stop' to print the results in alphabetical order.''')
print()
inputs()
print()
for a in sorted(obj):
    print('-',a)
