def swapFileData():
    file1 = input("your first file: ")
    file2 = input("your second file: ")

    a = open(file1, "r")
    b = open(file2, "r")
    data_a = a.read()
    data_b = b.read()

    a = open(file1, "w")
    b = open(file2, "w")
    a.write(data_b)
    b.write(data_a)

swapFileData()