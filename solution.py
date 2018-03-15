
file = open("original_string.txt","r")
s = file.read()
file.close()


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)


""" Get position of all opening and closing tags """
opening_tag, closing_tag, corrector = list(find_all(s, '<'))[1:],  list(find_all(s, '>')), 0
""" Solution 1: Truncate string """
content = [s[:closing_tag[0]+1]] #  first tag
for iterator in range(len(closing_tag)-1):
    content.append(s[closing_tag[iterator]+1:opening_tag[iterator]]) #  appending words
    content.append(s[opening_tag[iterator]:closing_tag[iterator+1]+1]) #  appending htmls tag

content[-2] = content[-2] + ' ...'
print(content)

file = open("truncated_string.txt","w")
for string in content:
    file.write(string + '\n')
file.close()

""" Solution 2: Add ellipsis not using truncated string """
for indx in opening_tag:
    s = s[:indx+corrector] + '...' + s[indx+corrector:]
    corrector = corrector + 3

print(s)
file = open("string_with_ellipsis.txt","w")
file.write(s)
file.close()
