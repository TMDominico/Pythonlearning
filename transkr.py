"""
인풋 숫자를 -> 아웃풋 한글로
필요한거
단위 별로 끊어내기
십백천만 구분 0이 연속 몇개오나인가????????
"""
numdic = {0: "", 1: "일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}
unit = {1: "십", 2: "백", 3: "천"}
unit2 = {0:"", 1: "만", 2: "억", 3: "조"}

#str_num = input("금액을 숫자로")

def TransKr(str_num):
    sprit_num = []
    result = []
    final_result = []
    inp_num = int(str_num)

    if inp_num == 0:
        return "영"

    for i in range(0, len(str_num)):
        sprit_num.append((inp_num // 10 ** i) % 10)

    for i in range(0, len(str_num)):
        num_result = str()

        if sprit_num[i] != 0:
            num_result += numdic.get(sprit_num[i])
            if i % 4 != 0 :
                num_result += unit.get(i % 4)
        result.append(num_result)
    print(result)

    for i in range(0, len(result), 4):
        if i >= 4 and result[i+1:i+4] != ["", "", ""]:
            final_result.extend(list(unit2.get(i // 4)) + result[i:i+4])
        else:
            final_result.extend(result[i:i + 4])
        print(final_result)

    reversed_result = "".join(reversed(final_result))
    print(reversed_result)
    return reversed_result


print(TransKr("0") == "영")
print(TransKr("1") == "일")
print(TransKr("10") == "일십")
print(TransKr("100") == "일백")
print(TransKr("1000") == "일천")
print(TransKr("10000") == "일만")
print(TransKr("100000") == "일십만")
print(TransKr("1000000") == "일백만")
print(TransKr("10000000") == "일천만")
print(TransKr("100000000") == "일억")
print(TransKr("1000000000") == "일십억")
print(TransKr("10000000000") == "일백억")
print(TransKr("100000000000") == "일천억")
print(TransKr("1000000000000") == "일조")
print(TransKr("1234567890") == "일십이억삼천사백오십육만칠천팔백구십")
print(TransKr("10000100000") == "일백억일십만")

