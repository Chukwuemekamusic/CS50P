count = 0
due = 0
while True:
    no = int(input("pay: "))
    cost = 50

    # 25 10 and 5 coin

    if no == 25 or no == 10 or no == 5:
        if count == 0:
            due = cost - no
        else:
            due = due - no
            if due <= 0:
                print("Change owed: " + str(due * (-1)))
                break

    else:
        if count == 0:
            due = cost
        else:
            due = due

    print(f"Amount due: {due}")

    count += 1
