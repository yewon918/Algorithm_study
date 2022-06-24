import json
file_path="./Steam_전처리완료.json"

with open(file_path, 'r') as file:
    data = json.load(file)

dic={}
cnt= 0
total = 0
lan_list = [x["supported_languages"] for x in data]

c_dic = {}
cate_list = [y["categories"] for y in data]

'''
ban = ['<', '&', ';', '/', '[', '\n', '#', '(', ',','  ']
ok = ['chinese', 'Chinese']

word = ''
for i in lan_list:

    total += 1
    if i[0]== ' ':
        i = i[1:]
    for j in range(len(i)):
        if i[j] in ban:
            cnt += 1
            break
        else:
            continue
    else:
        word = i

    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

print('number of weird names', cnt, '/', total)
print(len(dic), len(dic.values()), dic)
'''
for j in cate_list:

