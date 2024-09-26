"""With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program"""

n = int(input())
d = dict()
for i in range(1,n+1):
    d[i] = i * i
print(d)

#Using for loop
n = int(input())
ans = {}
for i in range (1,n+1):
    ans[i] = i * i
print(ans)

#Using dictionary comprehension

n = int(input())
ans={i : i*i for i in range(1,n+1)}
print(ans)

