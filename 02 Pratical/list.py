a = ["Yuvraj", "singh", 23 ,3, 34]
b = ["vibhav", "magrare", 105, 114]
print("1 for multi by 3 \n2 for add \n3 for index 4 \n4 for index to end \n5 for multi of 4 \n6 for index till 2")
want = int(input("from: \tmulti,\n\taddition of a & b,\n\tindex to 4,\n\tindex to end,\n\tmulti of 4,\n\tindex till 2,\n your choice: "))
print("hii how are you your answer is ")
if want == 1:
    print(a*3)
elif want == 2:
    print(a + b)

elif want == 3:
    print(a[:4])
elif want == 4:
    print(a[0:])

elif want == 5:
    print(b*4)
elif want == 6:
    print(b[0:3])