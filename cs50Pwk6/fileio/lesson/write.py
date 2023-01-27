# with open('echo.txt', 'a') as f:
#     f.write('\nEncapsulation')

with open('/home/joseph/workspace/oop/lesson/oop.txt') as file:
    content =  file.read()
    with open('copy.txt', 'a') as f:
        f.write(content)
        f.write('\n\nkeep learning!!!')
