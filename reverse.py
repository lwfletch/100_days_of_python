def reverse_string(string):
    str = ""
    for s in string:
        str = s + str
    print(str)
reverse_string("Hello World")