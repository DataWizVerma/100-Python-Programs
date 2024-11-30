# # count = 1
# # while count <= 100:
# #     print(count)
# #     count+=1
# # print(count)

# # count = 100
# # while count >= 1:
# #     print(count)
# #     count-=1
# #     print(count)

# n=int(input("Enter Your Number: "))
# i = 1
# while i <= 10:
#     print(n*i)
#     i+=1

# # count = 5
# # while count >= 1:
# #     print(count)
# #     count -=1
# # print('ended')


# num=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx < len(num):
#     print(num[idx])
#     idx +=1

# num = (1,4,9,16,25,36,49,64,81,100)
# x= 36
# i=0
# while i<len(num):
#     if (num[i]==x):
#         print("Found at idx",i)
#     else:
#         print("Finding...")
#     i+= 1


list=[1,4,9,16,25,36,49,64,81,100]
x=49
idx=0
for el in list:
    if (el==x):
        print("Number found at idx",idx)
    idx+=1

print(range(5))