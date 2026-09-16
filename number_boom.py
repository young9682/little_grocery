import random
print("💣炸弹游戏💣")
low=int(input("请输入最小值："))
high=int(input("请输入最大值："))
boom = random.randint(low,high)#randint是抽取范围内的一个随机整数
count = 0

print(f"范围在{low}~{high}之间")

while True:
    guess=int(input("请输入猜测数字："))
    count+=1
    if (guess == boom):
        print("猜对了喵！")
        if(count>10):
            print(f"怎么猜了{count}次才猜到^~^")
        if(1<count<=10):
            print(f"猜了{count}次就猜到了，还不错哦~")
        if(count == 1):
            print(f"蛤？开了吧，怎么可能猜一次就猜到了")
        break
    elif (guess < boom):
        print("太小了:(")
    else:
        print("太大了QAQ")




