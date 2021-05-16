#리스트 실습
li = [3, 1, "배가", 4, "고파요", 5, 1]

#리스트 인덱싱
print(li[2])

#리스트 슬라이싱
print(li[2:5])

#1_리스트 길이를 구해주는 내장함수 : len(리스트 변수명)
print(len(li))

#2_리스트를 오름차순으로 정렬해주는 내장함수 : 리스트변수명.sort()
li2 = [3, 1, 4, 5, 2]
li2.sort() #여기서 정렬 이미 끝남
print(li2)

#sorted()
print(sorted(li2)) #새로운 리스트를 만들어서 출력
print(li2)

#깜짝퀴즈 : 구글링을 해서 sort()로 내림차순 하는 법을 알아보도록 하자(보너스 과제)
li2.sort(reverse=True)
print(li2)

#3_리스트 내의 특정 원소 인덱스를 반환하는 함수 : 리스트변수.index()
print(li.index("배가"))

#4_리스트 내의 특정 원소의 갯수를 세어주는 함수 : 리스트변수.count(요소)
print(li.count(1))