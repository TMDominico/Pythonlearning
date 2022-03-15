"""
자판기 만들기
돈을 넣으면 상품을 줍니다

1. 동전 투입
2. 상품 선택
3. 상품 투하
4. 잔돈 반환

동전 관리기
money 10 50 100 500 1000
머신 잔고

"""

class CoinBox: # {10: 11, 50: 2, 100: 1, 500: 21, 1000: 23}
    def __init__(self, defaultcoins):
        self.defaultcoins = defaultcoins
        self.machinecoins = 0
        self.cxowncoins = 0
        for key in self.defaultcoins.keys():
            self.machinecoins += key*self.defaultcoins.get(key)

    def coinscalc(self):



class VendingMachine:
    def __init__(self, products):
        self.products = products
        self.sold = {}
        for value in self.products.values():
            self.sold[value[0]] = 0

    process = {1: "동전투입", 2: "상품선택", 3: "재고관리", 4: "전원끄기"}
    int_num = 0


    def intinp(self):
        inp = input(self)

        try:
            return int(inp)

        except:
            return 0

    def menu1(self):
        print("동전을 넣어주세요")
        self.cxowncoins += self.intinp()

    def menu2(self):
        print("상품목록\n")
        for key in self.products.keys():
            print(f"{key}번 {self.products.get(key)[0]}:{self.products.get(key)[1]}원\n")
        print("상품을 선택 해 주세요")
        cxinput = self.intinp()
        product = self.products.get(cxinput)
        if product is None:
            print("Fuck you!!!!!!!!!!!!!\n")
        else:
            if self.cxowncoins >= self.products.get(cxinput)[1]:
                self.sold[self.products.get(cxinput)[0]] += 1
                self.cxowncoins -= self.products.get(cxinput)[1]
                print(f"{self.products.get(cxinput)[0]}를 받아주세요\n")
            else:
                print("동전이 모자랍니다. 거지새끼야\n")
        return self.cxowncoins

    def menu3(self):
        earnedmoney = 0
        for value in self.products.values():
            earnedmoney += value[1]*self.sold.get(value[0])

        print(f'현재 총 매상은 {earnedmoney} 입니다.')
        for key in self.sold.keys():
            print(f'현재 팔린 {key}는 {self.sold.get(key)}개 입니다.')

    def menu4(self):
        print(f"잔돈{self.cxowncoins}원 받고 꺼저라, 장사 접는다\n")


    def main(self):
        print("개구린 자판기 마크3를 이용해 주셔서 감사합니다\n")

        while self.int_num != 4:
            print(f"현재 잔액은{self.cxowncoins}원 입니다.\n")
            print("동작선택\n")
            for key in self.process.keys():
                print(f"{key}번 {self.process.get(key)}")
            print("동작을 선택해주세요")
            self.int_num = self.intinp()

            if self.int_num == 1:
                self.menu1()

            elif self.int_num == 2:
                self.menu2()

            elif self.int_num == 3:
                self.menu3()

            elif self.int_num == 4:
                self.menu4()

            else:
                print("선택하신 번호는 없는 동작입니다\n")


vendingmachine1 = VendingMachine({10: ["커피", 300], 22: ["콜라", 500], 34: ["물", 100]})
vendingmachine1.main()
