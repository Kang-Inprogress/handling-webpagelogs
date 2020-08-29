# access_log의 문법: 180.76.15.5 - - [15/Nov/2015:03:45:45 +0000] "GET / HTTP/1.1" 200 6812

# 사용자 수 체크
def getUserCount():
    USER = []
    with open("access_log", 'r') as file:
        logs = file.readlines()
        for log in logs:
            ip = log.split()[0]
            if ip not in USER:
                USER.append(ip)
    return len(USER)

# 총 페이지 뷰 수
def getTotalPageviews():
    views = 0
    with open("access_log", 'r') as file:
        logs = file.readlines()
        for log in logs:
            status = log.split()[8]
            if status == '200':
                views += 1
    return views

# 사용자 별 서비스 용량 계산하기
def getServiceByte():
    service_byte = {}
    with open("access_log", 'r') as file:
        logs = file.readlines()
        for log in logs:
            ip = log.split()[0]
            bytes = log.split()[9]
            if not bytes.isdigit():
                bytes = 0

            if ip not in service_byte:
                service_byte[ip] = int(bytes)
            else:
                service_byte[ip] += int(bytes)

    service_byte = sorted(service_byte.items(), key=lambda x:x[1], reverse=True)

    for ip, bytes in service_byte:
        print("%s의 사용량: %d Bytes" %(ip, bytes))

print("""1 : 고유 사용자 수 확인
2 : 총 페이지 뷰 수 확인
3 : 사용자 별 서비스 용량 확인
exit : 나가기""")

while True:
    answer = input("서비스 선택: ")
    if answer == '1':
        users = getUserCount()
        print("유저 수: %d" % users)
    elif answer == '2':
        views = getTotalPageviews()
        print("총 페이지 뷰: %d views" %views)
    elif answer == '3':
        getServiceByte()
    elif answer == 'exit':
        break