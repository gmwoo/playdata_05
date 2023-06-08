############ map
wordList = ["school", "book", "bookstore", "desk", "hospital", "survey",
            "assembly", "president", "python", "flower", "sky", "cloud",
            "language", "phone", "house"]
nums = [1,2,33,4,6,23,26,17,19,8,19,27]


# nums에 값을 10씩 더하기
print(list(map(lambda x: x+10, nums)))

# wordList 의 문자들을 대문자로 변환
print(list(map(lambda x: x.upper(), wordList)))


############ zip
nameList = ["홍길동", "임꺽정", "장길산"]
phoneList = ["010-0000-0001", "010-0000-0002", "010-0000-0003"]
emailList = ["1", "2", "3"]

for data in zip(nameList, phoneList, emailList):
    print(data, type(data))
    

# 정렬
# list 타입에 존재하는 함수가 sort - 자기 자신의 순서 바꿈
# default: 오름차순 정렬
# 내림차순: reverse() 

# nums.sort()
# print(nums)

# nums.reverse()
# print(nums)

sortedList = sorted(nums)
print("정렬된: ", sortedList)
print("원본: ", nums)

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

# dataList -> 각 요소가 dict type
dataList.sort(key=lambda x: x["name"])
print(dataList)

# 역순 정렬
sortedDataList = sorted(dataList, key=lambda x: x["name"], reverse=True)
print(sortedDataList)
print()

# 나이순으로 정렬
print(sorted(dataList, key=lambda x: x["age"]))

# 나이순으로 역정렬
print(sorted(dataList, key=lambda x: x["age"], reverse = True))

