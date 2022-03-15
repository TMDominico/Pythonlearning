"""
자판기 만들기
돈을 넣으면 상품을 줍니다

1.동전 투입
2.상품 선택
3. 상품 투하
4. 잔돈 반환
"""

products = {10: ["커피", 300], 22: ["콜라", 500], 34: ["물", 100]}

print(f"개구린 자판기를 이용해 주셔서 감사합니다\n"
      f"상품목록\n")
for key in products.keys():
    print(f"{key}번 {products.get(key)[0]}:{products.get(key)[1]}원")

#print(f"개구린 자판기를 이용해 주셔서 감사합니다\n"
#      f"상품목록\n"
#      f"10번 {products.get(10)[0]}:{products.get(10)[1]}원 \n"
#      f"22번 {products.get(22)[0]}:{products.get(22)[1]}원 \n"
#      f"34번 {products.get(34)[0]}:{products.get(34)[1]}원 \n")

coin = int(input("\n동전을 넣어주세요"))
cxinput = int(input("상품을 선택해 주세요"))
product = products.get(cxinput)

if product is None:
    print("Fuck you!!!!!!!!!!!!!")
else:
    if coin >= products.get(cxinput)[1]:
        changes = coin - products.get(cxinput)[1]
        print(f"{products.get(cxinput)[0]}와 잔돈 {changes}를 받아주세요.")
    else:
        print("동전이 모자랍니다. 거지새끼야")
