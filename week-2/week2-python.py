#第一題
def calculate(min, max):
# 請用你的程式補完這個函式的區塊
    sum=0
    for x in range(min,max+1):
        sum+=x
    print(sum)    
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

#第二題
def avg(data):
# 請用你的程式補完這個函式的區塊
    result=0
    sum=0
    if data["count"]!=0:
        for x in data["employees"]:
            sum+=x["salary"]
            result=sum/data["count"]
    print(result)

avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式

#第三題
def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
    biggest=float("-inf")
    for x in nums:
        for i in nums:
            if x==i:
                continue
            else:
                product=x*i
                if product>biggest:
                    biggest=product
    print(biggest)                


maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) #得到 2

#第四題
def twoSum(nums, target):
# your code here
    for x in range(len(nums)):
        for i in range(len(nums)):
            if(nums[x]+nums[i]==target):
                if(x!=i):
                    return [x,i]
                else:
                    continue

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9