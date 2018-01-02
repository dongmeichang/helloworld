for i in range(1, 10):
    name = "text_{}.txt".format(i)
    print("creating text_{}.txt ...".format(i))
    with open(name, "w") as f:
        f.write("hello {}".format(i))

print("Done")
