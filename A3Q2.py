#Write a python program to reverse a string

sample_string="1234abcd"
def reverse(word):
    b=""
    for i in word:
        if i.isalnum():
            b=i+b
    return b
result=reverse("1234abcd")
print(result)
