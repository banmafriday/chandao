import qrcode

img = qrcode.make("HCC202109240017")
img.save('hello.png')
img.show()

# YJC202109160029
# YJC202109160036
# 求平均值
# result = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# code = 0
# for i in result:
#     code = code + i
#     print(code / len(result))

# # 计算最大值
# result = (1, 2, 3, 4, 5, 6, 7, 8, 9,943545354354,3534543543,54,3,5,43,54,35,34,5)
# co = 0
# for i in result:
#     if i < co:
#         co = i
# print(co)

