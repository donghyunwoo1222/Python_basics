cart = ["우유", "빵"]
cart2 = ["커피","치즈"]

cart.append("계란")
cart.insert(1,"사과")
cart.extend(cart2)
cart.remove("빵")
removed = cart.pop(0)
print(removed)
del cart[3]

print(cart)