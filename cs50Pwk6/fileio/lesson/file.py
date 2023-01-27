import os

# read line by line
with open('/home/joseph/workspace/oop/lesson/oop.txt') as file:
    lines =  file.readlines()
    for line in lines:
        ...#print(line, end='')
#print()

# read everything
with open('/home/joseph/workspace/oop/lesson/oop.txt') as file:
    content =  file.read()
    #print(content)

    #sets back the pointer to the begninning
    file.seek(0)

    content1 = file.read(10)
    #print(content1)

files = os.listdir('/home/joseph/workspace/oop/lesson')
print(files)


