#match - match the exact sequence
import re
# o/p match object - matched sequence and span() - start and end index
#checks for a match only at the beginning of the string
#returns a match object if found else NO
text = "hello world"
result = re.match("hello", text)
print(result)

#using Pattern
test_str = "123566778abcghhhjhjabcABC"
pattern = re.compile("123")
#re.finditer() finds all non-overlapping matches of the pattern in a string and
#return an iterator of match objects (not a list)
matches = pattern.finditer(test_str)
for match in matches:
    print(match)

#search operation searches the entire string
#return the first occurence
text = "python is powerful math powerful"
result =re.search("powerful",text)
print(result)
#search -- search the entire string -  find the occurances
#raw string for including the special character
a=r"\tHello"
print(a)

#match ()-determine if RE matches at the beginning of the string.
#search() - scan through a string, looking for any location where this RE matches
#finditer() - find all substrings where theRE matches , and returns then as an integer
#findall() - find all the string where the re matches and return a list

#findall()
my_string = "abc123ABC123abc"
pattern = re.compile(r'123')
matches = pattern.findall(my_string)
for match in matches:
    print(match)

#method on match
#group() - return the string matched ny the RE
#start() -  return the starting position of the match
#end() - return the ending position of the match
#span() - return a tuple contaning the(start,end) positions of the match
test_string = "123abc456789abc123ABC"
pattern = re.compile(r'abc')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
    print(match.span(),match.start(),match.end())
    print(match.group()) #return the substring that was matched by the Re

#special character
#meta character
#regular expressions
#pattern meaning
#[abc] a orb or c
#[a-z] lowercase letters
#[0-9] digits
#'a b'
# any single character

# abc matches exact text
text = " I like abc and abcde"
result = re.findall("abc",text)
print(result)

#matcg exact  "abc" wherever it is appearing
#[a-z]lowercase letter
ext = " I like abc and ABCFHJHJH"
result = re.findall("[a-z]",text)
print(result)

#[abc] a 0r b  or c - matches any one  of the character
#matches  single character:a or b or c
text = " apple banana cat"
result = re.findall("[abc]",text)
print(result)

#[0-9]
text = " I like abc and 123455ABCGHJHJH"
result = re.findall("[0-9]",text)
print(result)


#matches either "cat" or "bat"
text = " cat bat cat"
result = re.findall("c.t",text)
print(result)

#special character
'''
special sequence begins with a backslash \.
sequence meaning example
\d Digit (0-9) \d\d
\D non-digit \D
\w Word char (a-z,A-Z,0-9,_)\w
\W Non- Word char \W
\s Whitespace \s
\S Non-Whitespace \S
\b word boundry \bcat\b
\B Not a word boundry \Bcat'''

#\d Digit (0-9) \d\d
print(re.findall(r"\d","Order 123 costs 450"))
#\D non-digit \D

print(re.findall(r"\D","Order 123 costs 450"))
#\w Word char (a-z,A-Z,0-9,_)\w
text = "Python_3 version!"
result = re.findall(r"\w",text)
print(result)
#\W Non- Word char \W
text = "Hello@123!"
result = re.findall(r"\W",text)
print(result)
#\s Whitespace \s spaces , tabs and new line
text = "Hello World\nPython"
result = re.findall(r"\s",text)
print(result)
#\S Non-Whitespace \S matches position at start or end of a word
text = "Hi There"
result = re.findall(r"\S",text)
print(result)

#\b word boundry \bcat\b matches position at stat or end of a word
text = " cat scatter catalog"
result = re.findall(r"\bcat\b",text)
print(result)

#matches only full word "cat"
#\B Not a word boundry \Bcat - matches  when pattern is NOT at word boundry.
text = " cat scatter catlog"
result = re.findall(r"cat\B",text)
print(result)

'''Meta-characters have special meaning in regex.
Meta-characte Meaning
. Any character
^ Start of string
$ End of string
* 0 or more
+ 1 or more
? 0 or 1
{n} Exactly n times
{n,} n or more
{n,m} Between n and m
[] Character set
() Grouping
'''


#^ start of string
text="Python is easy"
print(re.findall(r"Python",text))
#$ End of the string
text="Python is easy"
print(re.findall(r"easy$",text))
#* 0 or more
text="ab abb abbb a n "
print(re.findall(r"ab*",text))

#+ 1 or more
text="ab abb abbb a"
print(re.findall(r"ab+",text))

#? 0 or 1
text="color colour colr"
print(re.findall(r"colou?r",text))

#{n} Exactly n times
text="111 22 3333 68777"
print(re.findall(r"\d{3}",text))

#{n,} n or more
text="1 22 333 4444"
print(re.findall(r"\d{3,}",text))
#{n,m} Between n and m
text="111 22 333 444"
print(re.findall(r"\d{2,3}",text))

#[] character set
text="apple banana cat"
print(re.findall(r"[abc]",text))

#() Grouping
text="2026-02-11"
print(re.findall(r"(\d{4})-(\d{2})-(\d{2})",text))

#regular expression modifiers
'''

 `re.I`  re.IGNORECASE  Case-insensitive      
 `re.M`  re.MULTILINE   ^ and $ work per line 
 `re.S`  re.DOTALL      Dot matches newline   
 `re.X`  re.VERBOSE     Write readable regex  
 `re.A`  re.ASCII       ASCII-only matching 
  re.DEBUG    —  Debug pattern  
'''

#re.IGNORECASE re.I case-insenitive matching
text="Python"
print(re.search("python",text,re.I))
#re.MULTILINE re.M ^ and $ match each line
text="Hello\nPython"
print(re.search("^Python",text,re.M))

#re.DOTALL re.S - matches new line
text="Hello\nWorld"
print(re.search("Hello.*World",text,re.S))

#re.VERBOSE re.X write readable regex with comments - make it more readable

import re
pattern = re.compile(r"""
7879hbgjklksdgskl..%^^&89""",re.X)
print(pattern)

#re.ASCII re.A ASCII -only matching
print(re.findall(r"\w+",text,re.A))

#re.DEBUG -Debug pattern

pattern = re.compile(r"""7879hbgjklksdgskl..%^^&89""",re.DEBUG)
print(pattern)

#assertitions - validating the output or checking certain condition
'''
^ → Start of string
$ → End of string
\b → Word boundary
\B → Not word boundary
(?=...) → Positive Lookahead
(?!...) → Negative Lookahead
(?<=...) → Positive Lookbehind
(?<!...) → Negative Lookbehind
'''

text="user1 admin2 test"
print(re.findall(r"\w+(?=\d)",text))
#(?!...)  negative lookahead
text="user1 admin2 test2"
print(re.findall(r"\w+(?!\d)",text))
#(?<=...) positive lookbehind - match only preceeded by something
text="Price ₹500"
print(re.findall(r"(?<=₹)\d+",text))

#(?<!..) negative lookbehind
text="500 ₹300"
print(re.findall(r"(?<!₹)\d+",text))





