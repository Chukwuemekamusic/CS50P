import emoji
import sys

text = ":"
text += sys.argv[1]
text += ":"
#text = ":thumbs_up:"
#print(emoji.emojize('Python is fun :thumbs_up:'))
print(emoji.emojize(f'{text}'))

