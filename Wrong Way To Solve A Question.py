lis = ["00000"]
for i in range(99999):
    a = str(i + 1)
    for k in range(5 - len(a)):
        a = "0" + a
    lis.append(a)
numb = [0, "00000"]
say = False
print(len(lis))
for i in lis[1:]:
    for k in numb[1:]:
        ced = 0
        say = True
        for c, z in enumerate(k):
            if i[c] == z:
                ced += 1
        if ced >= 4:
            say = False
            break
    if say:
        numb[0] += 1
        numb.append(i)
    if int(i) % 1000 == 0:
        print(i)

f = open("Q1Answers.txt", "w")
for i in numb:
    f.write(str(i)+"\n")
f.close()