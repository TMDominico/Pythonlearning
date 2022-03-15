"""
자판기 만들기
돈을 넣으면 상품을 줍니다

1.동전 투입
2.상품 선택
3. 상품 투하
4. 잔돈 반환
"""
print("""개구린 자판기를 이용해 주셔서 감사합니다
상품목록
커피:300원 콜라:500원 물:100원
""")
coin = int(input("동전을 넣어주세요"))
product = input("상품을 선택해 주세요")

if product == "커피":
    if coin >= 300:
        changes = coin - 300
        print(f"커피와 잔돈 {changes}를 받아주세요.")
    else:
        print("동전이 모자랍니다. 거지새끼야")
elif product == "콜라":
    if coin >= 500:
        changes = coin - 500
        print(f"콜라와 잔돈 {changes}를 받아주세요.")
    else:
        print("동전이 모자랍니다. 거지새끼야")
elif product >= "물":
    if coin >= 100:
        changes = coin - 100
        print(f"물과 잔돈 {changes}를 받아주세요.")
    else:
        print("동전이 모자랍니다. 거지새끼야")
else:
    print("그런거 없으니 딴대가쇼")
