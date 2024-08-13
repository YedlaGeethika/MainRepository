def countofvowelsinstring(string):
    count = 0
    string = string.lower()
    vowels = "aeiou"
    for x in string:
        if x in vowels:
            count+=1

    return count 

string = "GeethikaLovesAarushi"
print (countofvowelsinstring(string))