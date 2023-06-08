wordList = ["school", "book", "bookstore", "desk", "hospital", "survey",
            "assembly", "president", "python", "flower", "sky", "cloud",
            "language", "phone", "house"]
nums = [1,2,33,4,6,23,26,17,19,8,19,27]

##### soft copy
# nums2 = nums  # 이 때 두 변수는 같은 데이터 공간을 소유
# nums2[0] = 100
# print(nums2)
# print(nums)

##### hard copy
nums2 = [x for x in nums] 
nums[0] = 100

print(nums)
print(nums2)

evenList = [n for n in nums if n%2==0]
print(evenList)

# 3의 배수만 추출
multiple_3 = [i for i in nums if i%3==0]  # 컴프리헨션
print("comprehension", multiple_3)
print("lambda,filter", list(filter(lambda i: i%3==0, nums)))

# wordList에서 문자열 크기가 5글자 넘어가는 것만 추출
wordListOut = [x for x in wordList if len(x)>5]
print(wordListOut)

# wordList에서 문자열 크기가 5글자 넘어가면서 대문자로 추출
wordListOut_upper = [x.upper() for x in wordList if len(x)>5]
print(wordListOut_upper)


# 나이가 30세 넘어가는 사람 추출
dataList = [
    {"name": "강감찬", "age": 23},
    {"name": "감강찬", "age": 20},
    {"name": "김연경", "age": 33},
    {"name": "조승연", "age": 28},
    {"name": "김연아", "age": 30},
    {"name": "이순신", "age": 43},
    {"name": "서희", "age": 35},
    {"name": "윤관", "age": 27},
    {"name": "박세리", "age": 43},
]
age30 = [i for i in dataList if i["age"]>=30]
print(age30)


import numpy as np

x = [1,2,3,4,5]  # list 타입
print(x)
x = np.array(x)  # ndarray 타입으로 전환
print(x)
y = 2*x + 1   # 벡터 연산
print(y, type(y))