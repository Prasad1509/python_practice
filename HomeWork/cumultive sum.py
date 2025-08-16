l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
cm=[sum(l[:i+1])for i in range(len(l))]
print(cm)