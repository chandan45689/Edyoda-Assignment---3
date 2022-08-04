#Write a Python Function that accepts a string and calculate the number of upper case letters and lower case letters.

sample_string="The quick Brow Fox"
def count(string):
    lower=0
    upper=0
    for i in string:
        if i.islower():
            lower=lower+1
        elif i.isupper():
            upper=upper+1
    print("Number of lower characters:", lower) 
    print("Number of upper characters:", upper)
count("The quick Brow Fox")


