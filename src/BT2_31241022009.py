# Python String 113 exercises1.
# 1. Write a Python program to calculate the length of a string.
str_1 = input("1) Enter a string: ")
print(f"Length of the string: {len(str_1)}")
# 2. Write a Python program to count the number of characters (character frequency) in a string.
str_2 = input("2) Enter a string: ")
freq = {} #gọi từ điển
for char in str_2: #for, if,.. phải có :
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(f"Number of character in the string: {freq}")
#3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
# If the string length is less than 2, return the empty string instead.
str_3 = input("3) Enter a string: ")
def f2l2_str(str_3):    #tạo 1 hàm bất kì
    if len(str_3) < 2:
        return "Empty string" #trả về giá trị
    return str_3[:2] + str_3[-2:]
print(f"Result: {f2l2_str(str_3)}")
#4. Write a Python program to get a string from a given string where all occurrences
# of its firstchar have been changed to '$', except the first char itself.
str_4 = input("4) Enter a string: ")
def changed_str(str_4):
    first_char = str_4[0]
    result = first_char + str_4[1:].replace(first_char, '$')
    return result
print(f"Result: {changed_str(str_4)}")
#5. Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
str_5_1, str_5_2 = input("5) Enter 2 strings: ").split()
new_1 = str_5_2[:2]+str_5_1[2:]
new_2 = str_5_1[:2]+str_5_2[2:]
print(f"Result: {new_1} {new_2}")
#6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing', add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged
str_6 = input("6) Enter a string: ")
def str_ing(str_6):
    if len(str_6) > 3:
        if str_6[-3:] == "ing": #dấu = trong đây là ==
            return str_6 + "ly"
        return str_6 + "ing"
    return str_6
print(f"Result: {str_ing(str_6)}")
#7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
# If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return there sulting string.
str_7 = input("7) Enter a string: ")
def new_7(str_7):
    no_not = str_7.find("not")
    no_poor = str_7.find("poor")
    if "not" and "poor" in str_7:
        return str_7[:no_not] + "good" + str_7[no_poor+4:] #poor 4 ô là nhảy 4 ô
    return str_7
print(f"Result: {new_7(str_7)}")
#8. Write a Python function that takes a list of words and return the longest word
# and the length of the longest one.
str_8 = input("8) Enter a list: ").split()
longest = str_8[0]
for i in range(len(str_8)):
    if len(str_8[i]) > len(longest):
        longest = str_8[i]
print(f"Longest word: {longest}")
print(f"Length of the longest word: {len(longest)}")
#9. Write a Python program to remove the nth index character from a nonempty string.
#(nhập 1 chuỗi, nhập 1 số n bất kì. viết ct để nó xóa cái kí tự ở thứ tự n đó)
str_9 = input("9) Enter a string: ")
n = int(input("Enter nth index: "))
def del_n(str_9):
    if str_9 == "":
        return "Empty string"
    return str_9[:n] + str_9[n+1:]
print(f"Result: {del_n(str_9)}")
#10. Write a Python program to change a given string to a newly string where
# the first and last chars have been exchanged.
str_10 = input("10) Enter a string: ")
last = str_10[-1]
m = len(str_10) - 1
print(f"Newly string: {last + str_10[1:m] + str_10[:1]}")
#11. Write a Python program to remove characters that have odd index values in a given string.
str_11 = input("11) Enter a string: ") #có tính số 0 là số chẵn
print(f"Result: {str_11[1::2]}")
#12. Write a Python program to count the occurrences of each word in a given sentence.
str_12 = input("12) Enter a sentence: ")
words = str_12.split() #tách từ trong câu ra
freq_12 = {}
for word in words: #xét từng từ đã tách
    if word in freq_12:
        freq_12[word] += 1
    else:
        freq_12[word] = 1
print(f"Occurrences of each word in the sentence: {freq_12}")
#13. Write a Python script that takes input from the user and
# displays that input back in upper and lower cases.
str_13 = input("13) Enter a string: ")
print(f"Upper string: {str_13.upper()}")
print(f"Lower string: {str_13.lower()}")
#14. Write a Python program that accepts a comma-separated sequence of words as input
# and prints the distinct words in sorted form (alphanumerically).
str_14 = input("14) Enter a string: ")
words = str_14.split("," or " ")
distinct = set(words)
sort = sorted(distinct)
print(f"Result: {sort}")
#15. Write a Python function to create an HTML string with tags around the word(s).
def HTML(tag, word):
    return f"<{tag}>{word}</{tag}>" #tạo hàm trước
tag_inp = input("15) Enter a tag: ")
word_inp = input("Enter a word: ")
print(f"Result: {HTML(tag_inp, word_inp)}") #gắn cái input dô hàm
#16. Write a Python function to insert a string in the middle of a string.
str_16 = input("16) Enter a string: ")
str_16mid = input("Enter a middle string: ")
def mid_str(str_16, str_16mid):
    mid = len(str_16mid) // 2
    return f"{str_16mid[:mid]}{str_16}{str_16mid[mid:]}"
print(f"Result: {mid_str(str_16, str_16mid)}")
#17. Write a Python function to get a string made of 4 copies of
# the last two characters of a specified string (length must be at least 2).
str_17 = input("17) Enter a string: ")
def new17(str_17):
    if len(str_17) < 2:
        return f"Empty string"
    return str_17[-2:]*4
print(f"Result: {new17(str_17)}")
#18. Write a Python function to get a string made of the first three characters of a specified string.
# If the length of the string is less than 3, return the original string.
str_18 = input("18) Enter a string: ")
def new18(str_18):
    if len(str_18) < 3:
        return str_18
    return str_18[:3]
print(f"Result: {new18(str_18)}")
#19. Write a Python program to get the last part of a string before a specified character.
#(nhập cái chuỗi, nhập 1 kí tự nào đó có trong chuỗi, lấy phần chuỗi nằm bên trái kí tự đó)
str_19 = input("19) Enter a string: ")
char = input("Enter a character: ")
parts = str_19.split(char,1)
print(f"Result: {parts[0]}")
#20. Write a Python function to reverse a string if its length is a multiple of 4.
str_20 = input("20) Enter a string: ")
def multi_of_4(str_20):
    if len(str_20) % 4 != 0:
        return str_20
    return str_20[::-1]
print(f"Result: {multi_of_4(str_20)}")
#21. Write a Python function to convert a given string to all uppercase
#if it contains at least 2uppercase characters in the first 4 characters.
str_21 = input("21) Enter a string: ")
def upper(str_21):
    count = 0
    for char in str_21[:4]:
        if char.isupper() == True: #isupper để ktra kí tự có in hoa hay ko
            count += 1 #ngược lại cũng có islower
    if count >= 2:
        return str_21.upper()
    return str_21
print(f"Result: {upper(str_21)}")
#22.Write a Python program to sort a string lexicographically.
#(nhập string rồi sort theo a->z)
str_22 = input("22) Enter a string: ")
result_22 = "".join(sorted(str_22)) #join: gộp kí tự lại thành 1 string
print(f"Result: {result_22}")
#23. Write a Python program to remove a newline in Python.
#(cái này: \n (newline) sẽ làm chuỗi xuống dòng => xóa nó)
str_23 = "hello\nworld"   #do input ko nhập được \n nên phải tự lấy ví dụ sẵn chuỗi
no_newline = str_23.replace("\n", "")
print(f"Result: {no_newline}")
#24. Write a Python program to check whether a string starts with specified characters.
#(nhập chuỗi dô kiểm tra chuỗi đó có bắt đầu bằng kí tự chỉ định hay ko)
str_24 = input("24) Enter a string: ")
spe_char = input("Enter specified character: ")
def check(str_24, spe_char):
    return str_24[:1] == spe_char
print(f"Result: {check(str_24, spe_char)}")
#**25. Write a Python program to create a Caesar encryption.
str_25 = input("25) Enter a string: ")
shift = int(input("Enter shift number: "))
def caesar(str_25, shift):
    result_25 = ""
    for char in str_25:
        if char.isalpha(): #nếu nhập dô là chữ in hoa => thì nó là ord(A)
            start = ord('A') if char.isupper() else ord('a')
            result_25 += chr((ord(char) - start + shift) % 26 + start)
        else: #((mã số của char đó - A/a + số bước) chia lấy dư cho 26 + A/a)
            result_25 += char
    return result_25
print(f"Result: {caesar(str_25, shift)}")
#26. Write a Python program to display formatted text (width=50) as output.
str_26 = input("26) Enter a string: ")
import textwrap #dùng textwrap.fill để tách dòng
print(f"{textwrap.fill(str_26, width = 50)}")
#27. Write a Python program to remove existing indentation from all of the lines in a given text.
#(xóa thụt lề các đoạn)
str_27 ="""
        27)Hello World
        This is Python
        Caesar Cipher Example
"""
import textwrap #textwrap.dedent xóa đầu dòng mỗi đoạn
print(f"{textwrap.dedent(str_27)}")
#28. Write a Python program to add prefix text to all of the lines in a string.
#(thêm tiền tố mỗi đoạn giống bullet)
str_28 = """Hello World
This is Python
Caesar Cipher Example
"""
prefix = input("28) Add a prefix: ")
import textwrap
print(f"{textwrap.indent(str_28, prefix)}")
#29. Write a Python program to set the indentation of the first line.
str_29 = input("29) Add a prefix: ")
line = str_28.splitlines() #tách từng dòng ra
line[0] = str_29 + line[0]
print(f"{"\n".join(line)}")
#30. Write a Python program to print the following numbers up to 2 decimal places.
#(nhập số thực in ra số làm tròn 2 chữ số thập phân)
str_30 = float(input("30) Enter a number: "))
print(f"Result: {str_30:.2f}")
#31. Write a Python program to print the following numbers up to 2 decimal places with a sign.
str_31 = float(input("31) Enter a number: "))
print(f"Result: {str_31:+.2f}") #hiện dấu
#32. Write a Python program to print the following positive and negative numbers with no decimal places.
str_32 = float(input("32) Enter a number: "))
print(f"Result: {str_32:.0f}")
#33. Write a Python program to print the following integers with zeros to the left of the specified width.
str_33 = input("33) Enter numbers: ").split()
w_33 = int(input("Enter the width: "))
for z in str_33:
    print(f"{z:0>{w_33}}")
#34. Write a Python program to print the following integers with '*' to the right of the specified width.
str_34 = input("34) Enter numbers: ").split()
w_34 = int(input("Enter the width: "))
for y in str_33:
    print(f"{y:*<{w_34}}")
#35. Write a Python program to display a number with a comma separator.
str_35 = input("35) Enter numbers: ").split()
print(f"Result: {",".join(str_35)}")
#36. Write a Python program to format a number with a percentage.
str_36 = float(input("36) Enter numbers: "))
print(f"Result: {str_36:.2%}")
#37. Write a Python program to display a number in left, right,
# and center aligned with a width of 10. (canh lề 3 kiểu độ rộng 10)
str_37 = input("37) Enter a number: ")
print(f"Align right: {str_37:>10}")
print(f"Align left: {str_37:<10}")
print(f"Align center: {str_37:^10}")
#38. Write a Python program to count occurrences of a substring in a string.(đếm chuỗi con)
str_38 = input("38) Enter a string: ").split()
freq38 = {}
for sub_string in str_38:
    if sub_string in freq38:
        freq38[sub_string] += 1
    else:
        freq38[sub_string] = 1
print(f"Result: {freq38}")
#39. Write a Python program to reverse a string.(đảo kí tự)
str_39 = input("39) Enter a string: ")
print(f"Result: {str_39[::-1]}")
#40. Write a Python program to reverse words in a string.(đảo từ trong chuỗi)
str_40 = input("40) Enter strings: ").split()
print(f"Result: {" ".join(str_40[::-1])}")
#41. Write a Python program to strip a set of characters from a string.
str_41 = input("41) Enter strings: ")
print(f"Result: {str_41.replace(" ","")}")
#42. Write a Python program to count repeated characters in a string.(đếm kí tự lặp)
str_42 = input("42) Enter a string: ")
freq42 = {}
for a in str_42:
    if a in freq42:
        freq42[a] += 1
    else:
        freq42[a] = 1
for i in freq42:
    if  freq42[i] > 1:
        print(f"{i} {freq42[i]}")
#43. Write a Python program to print the square and cube symbols in the area of a rectangle
# and the volume of a cylinder. (ghi đơn vị diện tích và thể tích)
print(f"43) The area of the rectangle is 1256.66 cm\u00b2")
print(f"    The volume of the cylinder is 1254.725 cm\u00b3")
#44. Write a Python program to print the index of a character in a string.
str_44 = input("44) Enter a string: ")
for char, b in enumerate(str_44):
    print(f"Current character {b} position at {char}")
#45. Write a Python program to check whether a string contains all letters of the alphabet.
str_45 = input("45) Enter a string: ")
import string #import string trc
def check(str_45):
    lowtext = str_45.lower() #đem về chữ thường cho dễ kiểm
    letter = set(lowtext)
    return set(string.ascii_lowercase).issubset(letter)
    #set(string.ascii_lowercase): tập bảng chữ cái alpha thường
    #issubset(): kiểm xem tập này có là con tập kia hay ko
print(f"Result: {check(str_45)}")
#46. Write a Python program to convert a given string into a list of words.
str_46 = input("46) Enter a string: ").split()
print(str_46)
#47. Write a Python program to lowercase the first n characters in a string.
str_47 = input("47) Enter a string: ")
n47 = int(input("Enter number n: "))
print(f"Result: {str_47[:n47].lower() + str_47[n47:]}")
#48. Write a Python program to swap commas and dots in a string.
str_48 = input("48) Enter a string: ")
print(f"Result: {str_48.replace(",","#").replace(".",",").replace("#",".")}")
    #nếu ko chuyển qua dấu trung gian nó sẽ quay lại như cũ
#49. Write a Python program to count and display vowels in text.
#(đếm và hiển thị nguyên âm: u e a o i )
str_49 = input("49) Enter a string: ")
count_49 = {}
vowels = "ueaoiUEAOI"
for ch in str_49: #với ch chạy trong str
    if ch in vowels: #nếu nó là nguyên âm
        if ch in count_49: #xét xem nó có lặp lại chưa
            count_49[ch] += 1
        else:
            count_49[ch] = 1
print(f"Vowel counts: {count_49}")
#50. Write a Python program to split a string on the last occurrence of the delimiter
#(nhập chuỗi và cắt chuỗi đó ở chỗ dấu phân cách cuối cùng)
str_50 = input("50) Enter a string: ")
d = input("Enter a delimiter: ")
print(f"Result: {str_50.rsplit(d,1)}") #cắt từ bên phải, cắt 1 lần
