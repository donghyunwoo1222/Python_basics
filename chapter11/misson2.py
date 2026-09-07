
cart = []

cart.append("우유")
cart.append("계란")
cart.append("빵")

print("계란" in cart)
cart.remove("계란")

print(f"최종 리스트는 {cart}이고, 개수는 {len(cart)}개 입니다. ")