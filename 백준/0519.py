# ##### 1157번
# a=input().lower()
# aList = list(set(a))
# alphabetNum = []
# for i in aList:
#     # 변수. count(찾는 요소) : 문자열 내부에서 특정 문자, 혹은 문자열이 포함 되어있는지 계산해서 반환해주는 함수
#     alphabetCount=a.count
#     alphabetNum.append(alphabetCount(i))
# if alphabetNum.count(max(alphabetNum))>1:
#     print("?")
# else:
#     print(aList[(alphabetNum.index(max(alphabetNum)))])

# while (1):
#     x,y = map(int,input().split())
#     if x==0 and y==0:
#         break
#     if x<y and y%x==0:
#         print("factor")
#     elif x>y and x%y==0:
#         print("multiple")
#     else:
#         print("neither")

N,K = map(int, input().split())
NumList = []
for i in range(1,N+1):
    if N%i==0:
        NumList.append(i)
if len(NumList)<K:
    print(0)
else: print(NumList[K])
