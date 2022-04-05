n = int(input("Enter the row number: "))

list1 = []
for i in range(n):
    tem_list = []
    for j in range(i+1):
        if j == 0 or j == i:
            tem_list.append(1)
        else:
            tem_list.append(list1[i-1][j-1] + list1[i-1][j])
        
    # appending temp list to list1
    list1.append(tem_list)

for i in range(n):
    for j in range(n-i-1):
        print(format(" ", "<2"), end = "") # we took 2 place for single space
    for j in range(i+1):
        print(format(list1[i][j], "<4"), end = "") 
    print()