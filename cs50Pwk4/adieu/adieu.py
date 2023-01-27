import inflect as i
import sys

p = i.engine()
no = 104
myList = p.join(sys.argv[1:], final_sep="")
print("Adieu, adieu, to " + myList)
print(p.number_to_words(no))


# names
# for name in sys.argv[1:]:
#     names 