import os

file = open("Python\spider.txt") #mo file
print(file.read()) #doc file
print(file.readline()) #doc tung dong
file.close() #dong file

with open("Python\spider.txt") as file:
    print(file.readline())
    
with open("Python\spider.txt") as file:
    for line in file:
        print(line.strip().upper()) #strip() loai bo khoang trang, upper() viet hoa
        
file = open("Python\spider.txt")
lines = file.readlines() #doc tat ca dong va tra ve list
file.close()
lines.sort()
print(lines)

with open("Python\spider.txt", "w") as file: #ghi de len file
    file.write("6. s") 

    """
“r”  open for reading (default)

“w”  open for writing, truncating the file first

“x”  open for exclusive creation, failing if the file already exists

“a”  open for writing, appending to the end of the file if it exists

“+”  open for both reading and writing
    """

f = open('Python\spider.txt', 'w', encoding="utf-8") #mo file voi encoding utf-8
f.write('This is a test\n')

"""_
#Windows file directory
C:\my-directory\target-file.txtsummary_
#Windows file directory written in Python
C:/my-directory/target-file.txt.
"""

os.getcwd() #tra ve duong dan hien tai