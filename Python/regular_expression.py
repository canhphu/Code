import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
print(log[index+1:index+6]) #lay ra so 12345

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]" #cach hoat dong: tim kiem dau ngoac vuong, sau do lay ra so, \d+ la so bat ky, r la raw string
result = re.search(regex, log) #tim kiem regex trong log
print(result[1]) #lay ra so 12345

result = re.search(r"aza", "plaza")
print(result)

print(re.search(r"^x", "xenon")) #tim kiem x o dau chuoi
print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "sponge")) 
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE)) #ignore case là không phân biệt chữ hoa chữ thường
print(re.search(r"[Pp]ython", "Python")) #tim kiem Python hoac python
print(re.search(r"[a-z]way", "The end of the highway")) #tim kiem chuoi bat dau bang chu thuong va ket thuc bang way
print(re.search(r"[a-z]way", "What a way to go")) # lí do không tìm được vì trước chữ way là dấu cách
print(re.search("cloud[a-zA-Z0-9]", "cloudy")) #tim kiem chu cloud va sau do la chu hoac so
print(re.search("cloud[a-zA-Z0-9]", "cloud9")) 
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))