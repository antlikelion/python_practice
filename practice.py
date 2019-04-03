if __name__ == '__main__':
    list_student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_student.append([name, score])

min_score = list_student[0][1]
index = 0

for i in range(len(list_student)):
    if list_student[i][1] < min_score:
        min_score = list_student[i][1]

for i in list_student:
    if min_score == i[1]:
        del i

new_list = []

min_score = list_student[0][1]

for j in range(len(list_student)):
    if list_student[j][1] < min_score:
        min_score = list_student[j][1]

for k in range(len(list_student)):
    if list_student[k][1] == min_score:
        new_list.append(list_student[k][0])

new_list.sort()

for a in range(len(new_list)):
    print(new_list[a])
