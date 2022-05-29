def swapFileData():
    file1 = input("Enter First File Name:-")
    file2 = input("Enter Second File Name:-")
    with open(file1,'r') as A:
        data1=A.read()
    with open(file2,'r') as B:
        data2=B.read()
    with open(file1,'w') as A:
        A.write(data2)
    with open(file2,'w') as B:
        B.write(data1)

swapFileData()
