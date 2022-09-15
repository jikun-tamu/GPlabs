part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

product = 1
for el in part1:
    product = product * el
print('product:',product)
# output: product: 302231454903657293676544

sum = 0
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
for el in part2:
    sum = sum + el
print('sum:',sum)
# output: sum: 719788176

part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21]
sum2 = 0
for el in part3:
    if el % 2 == 0:
        sum2 = sum2 + el
print('sum2:',sum2)
# output: sum2: 458
