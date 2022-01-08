def maxZeros(nums):
# 請用你的程式補完這個函式的區塊
    resultmax=0
    compare=0
    for x in nums:
        if x==0:
            compare+=1
        else:
            if compare>resultmax:
                resultmax=compare
                compare=0
    if compare>resultmax:
        resultmax=compare
    print(resultmax)                       

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3