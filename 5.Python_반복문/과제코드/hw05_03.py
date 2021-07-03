
student = {} #학생정보 dictionary
while True:
    opr=int(input("동작 번호를 입력하시오:")) #숫자 입력
    if opr==1:#학생 조회
        stuNum=int(input("학생 번호를 입력하시오:")) #숫자 입력
        if stuNum in student:
            info =student[stuNum]
            print("이름 : {}, 성별 : {}, 나이 {}".format(info[0],info[1],info[2]))
        else:
            print("학번없어요~~~~~~\n")

    elif opr==2: #학생 정보 입력
        stuInfo =[]
        stuNum=int(input("입력할 학생 번호를 입력하시오:"))
        stuName = input("입력할 학생 이름을 입력하세요:")
        stuSex = input("입력할 학생 성별을 입력하세요:")
        stuAge = int(input("입력할 학생 나이를 입력하세요:"))
        
        stuInfo.append(stuName)
        stuInfo.append(stuSex)
        stuInfo.append(stuAge)
        student[stuNum] = stuInfo

    elif opr==3: #학생 정보 변경
        stuInfo =[]
        stuNum=int(input("변경할 학생 번호를 입력하시오:"))
        if stuNum in student:
            stuName = input("변경할 이름을 입력하세요:")
            stuSex = input("변경할 성별을 입력하세요:")
            stuAge = int(input("변경할 나이를 입력하세요:"))

            stuInfo.append(stuName)
            stuInfo.append(stuSex)
            stuInfo.append(stuAge)
            student[stuNum] = stuInfo
        else:
            print("학번없어요~~~~~~\n")
        

    elif opr == 4: #학생 삭제
        stuNum=int(input("삭제할 학생 번호를 입력하시오:"))
        if stuNum in student:
            del student[stuNum]
        else:
            print("학번없어요~~~~~~\n")
    elif opr == 5: #프로그램 종료
        print("프로그램을 종료합니다.\n")
        break
