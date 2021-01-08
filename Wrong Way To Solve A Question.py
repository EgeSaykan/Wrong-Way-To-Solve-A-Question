
# A list contains all numbers from 00000 to 99999
lis = ["00000"]
for i in range(99999):
    a = str(i + 1)
    for k in range(5 - len(a)):
        a = "0" + a
    lis.append(a)

# A list with an integer indicating number of how many students there are and strings to represent students' numbers
numb = [0, "00000"]

say = False

# A loop to check any number from 00001 to 99999
for i in lis[1:]:
    # A loop to check numbers in numb list (students' numbers)
    for k in numb[1:]:
        ced = 0
        say = True
        for c, z in enumerate(k):
            if i[c] == z:
                ced += 1
        # Stop if a contradicting number is found
        if ced >= 4:
            say = False
            break
    # Update numb list
    if say:
        numb[0] += 1
        numb.append(i)
    # Print where the loop is every 1000 numbers checked
    if int(i) % 1000 == 0:
        print(i)

# Create/Write to Q1Answers.txt file.
f = open("Q1Answers.txt", "w")
for i in numb:
    f.write(str(i)+"\n")
f.close()
