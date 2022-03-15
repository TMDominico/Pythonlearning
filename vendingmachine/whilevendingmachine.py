"""
자판기 만들기
돈을 넣으면 상품을 줍니다

1.동전 투입
2.상품 선택
3. 상품 투하
4. 잔돈 반환

다음 과제 명시적으로 종료하기전까지 계속 사용되는 자판기
동전이 없으면 동전을 입력하라고 지랄
동전이 있으면 상품을 고르거나 동전 추가하거나 동전 반환 하라고 지랄
"""

products = {10: ["커피", 300], 22: ["콜라", 500], 34: ["물", 100]}
process = {1: "동전투입", 2: "상품선택", 3: "재고관리", 4: "전원끄기"}
selled = {"커피": 0, "콜라": 0, "물": 0, "번 돈": 0}

int_num = 0
coin = 0


def intinp(text):
    inp = input(text)
    try:
        return int(inp)

    except:
        return 0


def menu1():
    global coin
    coin += intinp("넣을 동전을 입력해주세요\n")


def menu2():
    global coin
    print("상품목록\n")
        for key in products.keys():
            print(f"{key}번 {products.get(key)[0]}:{products.get(key)[1]}원\n")
            cxinput = intinp("상품을 선택해 주세요\n")
            product = products.get(cxinput)
            if product is None:
                print("Fuck you!!!!!!!!!!!!!\n")
            else:
                if coin >= products.get(cxinput)[1]:
                    selled[products.get(cxinput)[0]] += 1
                    selled["번 돈"] += products.get(cxinput)[1]
                    coin -= products.get(cxinput)[1]
                    print(f"{products.get(cxinput)[0]}를 받아주세요\n")
                else:
                    print("동전이 모자랍니다. 거지새끼야\n")
            return coin


def menu3():
    print(f'현재 총 매상은 {selled["번 돈"]} 입니다.')
    for key in selled.keys():
        print(f'현재 팔린 {key}는 {selled.get(key)}개 입니다.')


def menu4():
    print(f"잔돈{coin}원 받고 꺼저라, 장사 접는다\n")


def main():
    global int_num, coin
    print("개구린 자판기 마크3를 이용해 주셔서 감사합니다\n")

    while int_num != 4:
        print(f"현재 잔액은{coin}원 입니다.\n")
        print("동작선택\n")
        for key in process.keys():
            print(f"{key}번 {process.get(key)}")

        int_num = intinp("\n동작을 선택해주세요\n")

        if int_num == 1:
            menu1()
        elif int_num == 2:
            menu2()

        elif int_num == 3:
            menu3()

        elif int_num == 4:
            menu4()

        else:
            print("선택하신 번호는 없는 동작입니다\n")


main()
