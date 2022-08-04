#Write a python function to sum all the numbers in a list.

sample_List=(8, 2, 3, 0, 7)
def sum(*a):
    sum=0
    for i in a:
        sum=sum+i
    return sum

result=sum(8, 2, 3, 0, 7)
print(result)