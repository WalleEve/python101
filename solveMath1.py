s = [[3, -1, 7],
    [-5, 2, -4],
    [2, -1, -3] ]


abs_no = 0;
neg_no = 0;
for i in s:
    print(i)
    for x in i:
        if int(x) >= 1:
            abs_no += int(x)
            print(abs_no)
        else:
            neg_no += int(x)
            print(neg_no)
if abs_no + neg_no == 0:
    print("Yes")
else:
    print("No")


x = ['python', 'coder', 'is', 'Awesome' ]
print(x[1][-3:])
