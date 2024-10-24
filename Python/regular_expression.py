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

print(re.search(r"Py.*n", "Pygmalion")) # . là bất kỳ ký tự nào, * là 0 hoặc nhiều lần
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming")) 
print(re.search(r"Py[a-z]*n", "Pyn")) # vì n là chữ cái thường nên vẫn tìm thấy kết quả

print(re.search(r"o+l+", "goldfish")) # + là 1 hoặc nhiều lần
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil")) #lí do không tìm được vì sau o không có l

print(re.search(r"p?each", "To each their own")) #? là 0 hoặc 1 lần
print(re.search(r"p?each", "I like peaches"))

print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome")) #\ là escape character, tức là không xem . là ký tự đặc biệt
print(re.search(r"\.com", "mydomain.com\homepage"))

print(re.search(r"\w*", "This is an example")) #\w là ký tự chữ hoặc số, * là 0 hoặc nhiều lần
print(re.search(r"\w*", "And_this_is_another"))

print(re.search(r"p?each", "I like peaches"))

print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome")) # \ is an escape character, meaning . is not treated as a special character
print(re.search(r"\.com", "mydomain.com\homepage"))

print(re.search(r"\w*", "This is an example")) # \w is a word character (alphanumeric + underscore), * means 0 or more times
print(re.search(r"\w*", "And_this_is_another"))

def check_web_address(text):
    pattern = r"^[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}$"
    result = re.search(pattern, text)
    return result is not None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

import re
def check_time(text):
  pattern = r"\d{2}:\d{2}"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
print(check_time("6:02 am")) # True
print(check_time("6:02km")) # False

import re
def contains_acronym(text):
  pattern = r"\([A-Za-z0-9]*\)"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
"{} {}".format(result[2], result[1])

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Lovelace, Ada")
