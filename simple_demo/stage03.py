with open("artifacts.txt", mode="a") as f:
    f.write("Adding some extra lines")

with open("artifacts.txt", mode="r") as f:
    text = f.read()

print(text)
print("Stage3 is done")