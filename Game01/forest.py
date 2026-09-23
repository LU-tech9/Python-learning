import random

print("=======================")
print("      《迷雾森林》")
print("=======================")

name = input("请输入你的名字:")
max_hp = 100
player_hp = max_hp
monster_hp = 50
coins = 0
exp = 0
level = 1
bag = []
bag.append("药水")

def show_status():
    print()
    print("========玩家状态========")
    print("生命值:", player_hp, "/", max_hp)
    print("等级:", level)
    print("经验:", exp)
    print("金币", bag)
    print("背包:", bag)
    print("=======================")

def drink_potion():
    global player_hp

    if "药水" in bag:
        player_hp = player_hp + 30

        if player_hp > max_hp:
           player_hp = max_hp
           bag.remove("药水")

           print("你喝下了药水！")
           print("你的生命值恢复了30点！")
           print("当前生命值:", player_hp)
           print("当前背包:", bag)
    else:
         print("你的背包里没有药水！")

def attack():
    global monster_hp
    global exp
    global level
    global coins
    global player_hp
    global max_hp
    monster_hp = monster_hp - 10

    print("你攻击了怪物！")
    print("怪物剩余生命值：", monster_hp)

    if monster_hp <= 0:
        print("你击败了怪物！")

        coins = coins + 10
        exp = exp + 50

        print("你获得了10枚金币！")
        print("当前金币：", coins)
        print("你获得了50点经验！")
        print("当前经验：", exp)

        if exp >= 100:
            level = level + 1
            exp = 0
            max_hp = max_hp + 20
            player_hp = max_hp

            print("恭喜你升级了！")
            print("当前等级：", level)
            print("最大生命值增加了20！")
            if player_hp <= 0:
                print("你的生命值归零了！")
                print("游戏结束！")
                return False

        return True

    monster_damage = random.randint(5, 15)
    player_hp = player_hp - monster_damage

    print("怪物反击了！")
    print("你受到了", monster_damage, "点伤害！")
    print("你的剩余生命值：", player_hp)

print()
print("欢迎你，" + name + "！")
print("你来到了神秘的迷雾森林。")
print()
print("你发现面前有两条路")
print("1.进入森林")
print("2.离开森林")

choice = input("请选择:")
if choice == "1":
    print("你勇敢地走进了森林。")
    event = random.randint(1, 3)
    if event == 1:
        print("你发现了一个宝箱！")

        reward = random.randint(5, 30)
        coins = coins + reward

        bag.append("金币")
        bag.append("药水")

        if "药水" in bag:
            print("你发现背包里有一瓶药水！")

        print("你打开了宝箱！")
        print("你获得了:", reward, "枚金币！")
        print("当前金币:", coins)
        print("你的背包:", bag)
    elif event == 2:
        print("不好！你遇到了一只怪物！")
        print("你的生命值:", player_hp)
        print("怪物的生命值:", monster_hp)
        while player_hp > 0 and monster_hp > 0:
            print()
            print("1.逃跑")
            print("2.攻击")
            print("3.喝药水")
            print("4.查看状态")

            action = input("请选择：")
            if action == "2":
               attack()
            elif action == "1":
                print("你逃跑了！")
                break
            elif action == "3":
                drink_potion()
            elif action=="4":
                show_status()
            else:
                print("请输入1,2,3或4!！")
    else:
        print("你在森林里走了很久，什么也没有发生")
elif choice == "2":
    print("你选择离开了森林。")
else:
    print("请输入1或2！")
