def calc_order_cost(*args, coupon=0, score=0, express=0):
    total_price = [good[1] * good[2] for good in args]
    total_cost = sum(total_price)

    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon

    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100

    total_cost += express
    return total_cost


total = calc_order_cost(("鼠标", 188, 2), ("手机", 3999, 1), coupon=10, score=4000, express=9.9)
print(f"订单实付: {total} 元")
