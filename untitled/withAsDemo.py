print("With as write start")
with open("withas.txt", "w") as my_write:
    my_write.write(str("write contents"))

print("write complete")
with open("withas.txt", "r") as my_read:
    print(str(my_read.read()))

print("read complete")