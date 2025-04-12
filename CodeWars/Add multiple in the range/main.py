def solution(number):
    if number < 0:
        return 0
    else:
        total = 0
        for num in range(0, number):
            if num%3 != 0 and num%5 != 0:
                continue
            else:
                total += num
        return total
print(solution(20))