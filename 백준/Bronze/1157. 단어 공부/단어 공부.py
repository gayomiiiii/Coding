word = input().upper() # 대문자로 입력받기
word_list = list(set(word))
cnt = []

for i in word_list:
    cnt.append(word.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(word_list[cnt.index(max(cnt))]) # cnt가 가장 높은 인덱스의 word_list 추출