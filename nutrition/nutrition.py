itemDict = {}

def main():
    buildDict()
    print(itemDict)
    item = input("item: ").lower()
    if item in itemDict:
        value = itemDict[item]
        print(f"Calories: {value}")
    # else:
    #     print()



def buildDict():
    itemDict["apple"] = 130
    itemDict["avocado"] = 50
    itemDict["banana"] = 110
    itemDict["cantaloupe"] = 50
    itemDict["grapefruit"] = 60
    itemDict["grapes"] = 90
    itemDict["honeydew melon"] = 50
    itemDict["kiwifruit"] = 90
    itemDict["lemon"] = 15
    itemDict["lime"] = 20
    itemDict["nectarine"] = 60
    itemDict["orange"] = 80
    itemDict["peach"] = 60
    itemDict["pear"] = 100
    itemDict["pineapple"] = 50
    itemDict["plums"] = 70
    itemDict["strawberries"] = 50
    itemDict["sweet cherries"] = 100
    itemDict["tangerine"] = 50
    itemDict["watermelon"] = 80


main()   