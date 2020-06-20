def has_no_e(word):
    if 'e' not in word.lower(): 
        return True
    return False


# reading files: https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
cossword_file = open('Crossword-Testing.txt', 'r')
words = []
found = 0

while True:
    line = cossword_file.readline()
    words.append(line.strip())  # use strip to remove \n charector
    if not line:
        break


for word in words:
    if(has_no_e(word) ==True):
        found += 1

cossword_file.close()
percentage = "{:.2f}".format((found/len(words)) * 100) # format to two decimal places: https://stackoverflow.com/questions/14540143/python-3-float-decimal-points-precision
print(f"{percentage}%")
