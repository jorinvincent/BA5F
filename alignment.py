
pam = open("PAM250.txt")
reader = open("input", "r")
writer = open("output", "w")


twod = []
first = pam.readline().strip().split()
first.insert(0, ' ')
twod.append(first)
for line in pam:
    l = line.strip().split()
    twod.append(l)

pam_dictionary = {}
for i in range(1, 21):
    r = twod[i][0]
    for j in range(1, 21):
        c = twod[0][j]
        pam_dictionary[(r, c)] = twod[i][j]

top_string = "-" + reader.readline().strip()
bottom_string = "-" + reader.readline().strip()

indel = -5
score = [[0 for j in range(0, len(bottom_string))] for i in range(0, len(top_string))]
path = [["" for j in range(0, len(bottom_string))] for i in range(0, len(top_string))]

for j in range(0, len(bottom_string)):
    score[0][j] = indel * j
    path[0][j] = "del"

for i in range(0, len(top_string)):
    score[i][0] = indel * i
    path[i][0] = "ins"

for i in range(1, len(top_string)):
    for j in range(1, len(bottom_string)):
        temp = (bottom_string[j], top_string[i])

        match = score[i - 1][j - 1] + int(pam_dictionary[temp])
        insert = score[i - 1][j] + indel
        delete = score[i][j - 1] + indel

        score[i][j] = max(match, insert, delete)

        if (score[i][j] == match):
            path[i][j] = "mch"
        elif (score[i][j] == insert):
            path[i][j] = "ins"
        elif (score[i][j] == delete):
            path[i][j] = "del"

max_score = 0
start_i = -1
start_j = -1
for i in range(0, len(top_string)):
    for j in range(0, len(bottom_string)):
        if (score[i][j] > max_score):
            max_score = score[i][j]
            start_i = i
            start_j = j

i = start_i
j = start_j
top_align = ""
bottom_align = ""

while (i != 0 or j != 0):
    direction = path[i][j]
    if (direction == "mch"):
        top_align += top_string[i]
        bottom_align += bottom_string[j]
        i -= 1
        j -= 1
    elif (direction == "ins"):
        top_align += top_string[i]
        bottom_align += "-"
        i -= 1
    elif (direction == "del"):
        top_align += "-"
        bottom_align += bottom_string[j]
        j -= 1

top_align = top_align[::-1]
bottom_align = bottom_align[::-1]

writer.write(str(max_score) + "\n" + top_align + "\n" + bottom_align)


pam.close()
reader.close()
writer.close()
