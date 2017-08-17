# coding the matrix
# 1.1 집합
# 집합(set)은 {}로 표현
# set은 중복되는 객체는 하나의 원소로만 표기함,
a = {1,2,3,4}
b = {1,2,2,3,3,4}
c = {4,4,2,3,3,4}       # set은 알아서 순서를 오름차순으로 sorting 해줌

print(a,type(a))
print(b,type(b))
print(c,type(c))
print(a == b)

#1.2 카테시안 곱(Cartesian product)
import itertools
a = {1,2,3}
b = {3,4,5}
#원소 10 을 추가
a.add(10)
# set 중에서 원소 3제거
b.remove(3)

c = itertools.product(a,b)
print(a,b)
for i in c:
    print(i,type(i))

print(len(a)*len(b))
#print(len(c))

#합집합
union = {1,2,3} | {2,3,4}
#교집합
intersection = {1,2,3} & {2,3,4}
print(union, intersection)


a = {1,2,3}
print(a)
# 기존 set에 새로운 set를 추가함
a.update({4,5,2})
print(a)

# 기존 set에 교집합을 한 원소를
S = {1,2,3,4,5,6}
S.intersection_update({5,6,7,8,9})
print(S)
