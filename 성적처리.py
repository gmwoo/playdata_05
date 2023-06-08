scoreList = [
    {"name":"홍길동", "kor":90, "eng":80, "mat":90},
    {"name":"둘리", "kor":100, "eng":40, "mat":90},
    {"name":"임꺽정", "kor":100, "eng":100, "mat":100},
    {"name":"장길산", "kor":70, "eng":60, "mat":70},
    {"name":"도우너", "kor":90, "eng":80, "mat":90},
]

# 총점, 평균, 학점

def process(score):
    score["total"] = score["kor"] + score["eng"] + score["mat"]
    score["avg"] = round(score["total"] / 3, 2)
    score["grade"] = ""
    if score["avg"] >= 90:
        score["grade"] = '수'
    elif score["avg"] >=80:
        score["grade"] = '우'
    elif score["avg"] >=70:
        score["grade"] = '미'
    elif score["avg"] >=60:
        score["grade"] = '양'
    else:
        score["grade"] = '가'

def outp(s):
    print(f"{s['name']} {s['kor']}", end=' ')
    print(f"{s['eng']} {s['mat']}", end=' ')
    print(f"{s['total']} {s['avg']} {s['grade']}")

def processAll():
    for score in scoreList:
        process(score)
        
def outpAll():
    for score in scoreList:
        outp(score)

processAll()
outpAll()

# 검색 함수
def search():
    name = input("찾을 이름: ")
    # result = list(filter(lambda x: x['name']==name, scoreList))   # lambda, filter 사용
    result = [i for i in scoreList if i["name"]==name]   # comprehension 사용
    if len(result) == 0:
        print(f"{name}을 찾을 수 없음")
        return
    
    for item in result:
        outp(item)
    
# 수정 함수
def modify():
    name = input("수정할 이름: ")
    # result = list(filter(lambda x: x['name']==name, scoreList))   # lambda, filter 사용
    result = [i for i in scoreList if i["name"]==name]   # comprehension 사용
    if len(result) == 0:
        print(f"{name}을 찾을 수 없음")
        return
    
    result[0]['name'] = input("바꿀 이름은: ")
    result[0]['kor'] = int(input("국어 점수: "))
    result[0]['eng'] = int(input("영어 점수: "))
    result[0]['mat'] = int(input("수학 점수: "))
    process(result[0])   # 다시 계산
    outpAll()
    
# 삭제 함수
def delete():
    name = input("삭제할 이름: ")
    # result = list(filter(lambda x: x['name']==name, scoreList))   # lambda, filter 사용
    result = [i for i in scoreList if i["name"]==name]   # comprehension 사용
    if len(result) == 0:
        print(f"{name}을 찾을 수 없음")
        return
    
    scoreList.remove(result[0])
    outpAll()
    
# 정렬 함수
#  이름으로. 총점으로. 국어 성적으로 정렬 
            
def sorting():
    sel = int(input("이름 순: 1, 총점 순: 2, 국어 성적 순: 3 고르시오 -> "))
    if sel == 1:
        key = "name"
        
    elif sel == 2:
        key = "total"
        
    elif sel == 3:
        key = "kor"
    
    sortedList = sorted(scoreList, key=lambda score: score[key])
    for s in sortedList:
        outp(s)   
        
def appending():
    score = dict()
    score["name"]=input('이름: ')
    score["kor"]=int(input('국어: '))
    score["eng"]=int(input('영어: '))
    score["mat"]=int(input('수학: '))
    process(score)
    scoreList.append(score)

def close():
    return

def menu():  # 고르시오
    menus = ['1.추가', "2.출력", "3.검색", "4.수정", "5.삭제", "6.정렬", "0.종료"]
    # process()
    
    for menu in menus:
        print(menu)
        
def start():
    functionList = [None, appending, outpAll, search, modify, 
                    delete, sorting]
    processAll()
    while True:
        menu()
        sel = int(input("선택: "))
        
        if sel<1 or sel>len(functionList):
            print('종료')
            return
        
        functionList[sel]()   #### 함수 호출
        
start()