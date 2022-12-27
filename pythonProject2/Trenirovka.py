
with open("C:\\Users\\bagbe\\Downloads\\dataset_3363_2 (1).txt") as file:
    s1 = file.readline()

count = '0'
letter = ''
temp_out = ''
for i in s1:
    if i.isalpha():
        temp_out += letter * int(count)
        letter = i
        count = '0'
    elif i.isdigit():
        count += i
temp_out += letter * int(count)

with open('text.txt', 'w') as file2:
    file2.write(temp_out)

# Comments