def to_seconds(hours, minutes, seconds):
    return hours*3600+minutes*60+seconds

print("Welcome to this time converter")

cont = "y"
while(cont.lower() == "y"):
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
    print()
    cont = input("Do you want to do another conversion? [y to continue] ")
    
print("Goodbye!")

# cat streams.py
#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
print("Now we generate an error to STDERR: " + data + 1)
"""./streams.py 
This will come from STDIN: Python Rocks!
Now we write it to STDOUT: Python Rocks!

cat greeting.txt 
Well hello there, STDOUT

cat greeting.txt 
Well hello there, STDOUT

ls -z
"""

"""
echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
cat variables.py
#!/usr/bin/env python3
"""
import os
print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))
"""
./variables.py 
export FRUIT=Pineapple
./variables.py 
"""
#cat parameters.py 
#!/usr/bin/env python3
import sys
print(sys.argv)
"""
./parameters.py
['./parameters.py'] 

./parameters.py one two three
['./parameters.py', 'one', 'two', 'three']


wc variables.py
7 19 174 variables.py 	
echo $?
0

wc notpresent.sh
wc: notpresent.sh: No such file or directory
echo $?
1

"""

#!/usr/bin/env python3

import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)
"""
./create_file.py example
echo $?
0

cat example 
New file created
./create_file.py example
Error, the file example already exists!
echo $?
1
"""
my_number = input('Please Enter a Number: \n')
#Please Enter a Number: 
#123 + 1
print(my_number)
#123 + 1
type(my_number)
#<class 'str'>
eval(my_number)
#124