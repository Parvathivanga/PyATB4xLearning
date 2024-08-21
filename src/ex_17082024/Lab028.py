# Escape Sequence
print("Hello world")
print("Hello\nworld") #\n-newline
print("Hello\tworld") #\t-tabline
print("Hello\bworld") #\b-backspace

#dir='c:\pramod\n.txt' -invalid in single quote
#dir="c:\pramod\n.txt" -invalid in double quotes
# We have to use r concept.
# it is used in Automation api, wen automation, file_path.
dir=r'c:\pramod\n.txt'
dir2=r"c:\pramod\n.txt"
print(dir)
print(dir2)

name='pramod\'utta'
name2="pramod\'utta"
print(name)
print(name2)

