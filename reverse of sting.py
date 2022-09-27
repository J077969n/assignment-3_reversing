s = "1234abcd"

def text(s):
    reversed_string = ""
    for i in s:
        reversed_string = i + reversed_string
    print("reverse string is:",reversed_string)

text(s)

