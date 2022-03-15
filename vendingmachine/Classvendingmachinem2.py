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


class CoinBox:  # {10: 11, 50: 2, 100: 1, 500: 21, 1000: 23}
    def __init__(self, defaultcoins):
        self.defaultcoins = defaultcoins
        self.machinecoins = 0
        self.cxowncoins = 0
        for key in self.defaultcoins.keys():
            self.machinecoins += key * self.defaultcoins.get(key)

    def intinp(self):
        inp = input(self)

        try:
            return int(inp)
        except:
            return 0

    def coininsert(self):
        print("동전을 넣어주세요")

        """
            leftcoins =
            if
                print("동전이 부족하여", end=", ")
                for key in self.defaultcoins.keys():
                    print("{}원", end=", ")
                print("짜리는 사용 하실 수 없습니다.")
        """
        insert = self.intinp()
        if insert in self.defaultcoins.keys():
            self.cxowncoins += insert
        else:
            print("쓰레기 넣지마")

    def coinscalc(self):
        allcoins: int = self.machinecoins + self.cxowncoins
        smallestprice = sorted(VendingMachine.products.values())[0]

        if allcoins < :


#{"커피": 300, "콜라":500 , "물": 100}
#{10: ["커피", 300], 22: ["콜라", 500], 34: ["물", 100]}
class VendingMachine:
    def __init__(self, products, defaultcoins):
        self.products = products
        self.productsdic = {}
        for value in self.products.values():
            i = 1
            self.productsdic[value] = self.productsdic.values()
            i += 1
        self.cbox = CoinBox(defaultcoins)
        self.sold = {}
        for value in self.productsdic.values():
            self.sold[value[0]] = 0

    process = {1: "동전투입", 2: "상품선택", 3: "재고관리", 4: "전원끄기"}
    int_num = 0

    def menu1(self):
        self.cbox.coininsert()

    def menu2(self):
        print("상품목록\n")
        for key in self.productsdic.keys():
            print(f"{key}번 {self.productsdic.get(key)[0]}:{self.productsdic.get(key)[1]}원\n")
        print("상품을 선택 해 주세요")
        cxinput = self.cbox.intinp()
        product = self.productsdic.get(cxinput)
        if product is None:
            print("Fuck you!!!!!!!!!!!!!\n")
        else:
            if self.cbox.cxowncoins >= self.productsdic.get(cxinput)[1]:
                self.sold[self.productsdic.get(cxinput)[0]] += 1
                self.cbox.cxowncoins -= self.productsdic.get(cxinput)[1]
                print(f"{self.productsdic.get(cxinput)[0]}를 받아주세요\n")
            else:
                print("동전이 모자랍니다. 거지새끼야\n")
        return self.cbox.cxowncoins

    def menu3(self):
        earnedmoney = 0
        for value in self.productsdic.values():
            earnedmoney += value[1] * self.sold.get(value[0])

        print(f'현재 총 매상은 {earnedmoney} 입니다.')
        for key in self.sold.keys():
            print(f'현재 팔린 {key}는 {self.sold.get(key)}개 입니다.')

    def menu4(self):
        print(f"잔돈{self.cbox.cxowncoins}원 받고 꺼저라, 장사 접는다\n")

    def main(self):
        print("개구린 자판기 마크3를 이용해 주셔서 감사합니다\n")

        while self.int_num != 4:
            print(f"현재 잔액은{self.cbox.cxowncoins}원 입니다.\n")
            print("동작선택\n")
            for key in self.process.keys():
                print(f"{key}번 {self.process.get(key)}")
            print("동작을 선택해주세요")
            self.int_num = self.cbox.intinp()

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


vendingmachine1 = VendingMachine({10: ["커피", 300], 22: ["콜라", 500], 34: ["물", 100]},
                                 {10: 11, 50: 2, 100: 1, 500: 21, 1000: 23})
vendingmachine1.main()
