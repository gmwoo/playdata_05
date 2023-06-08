nums = [1, 2, 3, 33, 4, 6, 23, 26, 17, 19, 21, 8, 19, 27]
# 짝수만 필터링

evenList = []  # 리스트 타입 객체를 만듦
for n in nums:
    if n%2==0:
        evenList.append(n)
print(evenList)

############################# 위의 코드를 함수로 만듦
## 조건식만 바꾸면 됨
# 함수를 함수의 매개변수로 전달 (compare)
# 함수도 주소 -> 변수에 함수를 저장할 수 있음
# 함수에 매개변수로 전달되는 함수는 콜백함수라고 부름
 ### 호출자가 직접하는게 아니고 다른 함수
 ### 함수의 매개변수나 반환값의 결정자는 본인이 아니며 약속된 형태만 보내야 함
def myfilter(compare, nums):
    evenList = []
    for n in nums:
        if compare(n):
            evenList.append(n)
    return evenList

def myCompare(x):
    return x%2==0  # 짝수인가?
    
print(myfilter(myCompare, nums))

# def add(x, y):
#     return x+y
# calc = add  # 함수의 주소를 변수에 저장 가능
# print(calc(4, 5))

############################# 위의 함수를 filter, lambda로 변환
# 프로그램 중에 일부만 살짝 고칠 수 있다면 함수를 미리 만들고 나머지는 사용자가 완성하도록
print(list(filter(myCompare, nums)))

# myCompare 함수를 lambda로 변환하기
## lambda x : x%2==0     => return 사용 X, 한 줄
print(list(filter(lambda x: x%2==0, nums)))


wordList = ["school", "book", "bookstore", "desk", "hospital", "survey",
            "assembly", "president", "python", "flower", "sky", "cloud",
            "language", "phone", "house"]

# 단어 길이가 5개 이상인 단어 추출
print(len("school")>=5)
## lambda와 filter 사용
for item in filter(lambda x: len(x)>=5, wordList):
    print(item)
    
# 단어가 b로 시작하는 것만 추출
print(list(filter(lambda u: u[0]=="b", wordList)))

# b를 포함하고 있는
print(list(filter(lambda w: "b" in w, wordList)))