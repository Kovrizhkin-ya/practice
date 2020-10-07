time = int(input("Enter count of minutes"))
sum = 100
if (time - 50) != 0:
    sum += 50
if (time - 100) != 0:
    sum += (time - 100) * 2
print("You must pay", str(sum))