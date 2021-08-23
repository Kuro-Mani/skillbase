print("hello")
#message="next stage"
#print(message)
#group=['red','blue','yellow','green']
#print(group)
#  インデックスは０から
#group.append('white')
#group.sort()
#print(group)
#group.sort(reverse=True)
#print(group)
#size=len(group)
#print(size)
#for magician in group:print(magician)
#for valueint in range(5):print(valueint)
#numbers = list(range(1,11))
#print(numbers)
#numbers = list(range(1,11,2))
#print(numbers)
#square = []
#for values in range(1,100):
#    sqx = values ** 2
#    square.append(sqx)
# [*] ＝乗算、[**]　＝べき乗、
#print(square)
# 3nodan
#square2 = []
#for value in range(1,10):
#    square2.append(value*3)
#print(square2)
# digits関数　最大値、最小値、合計などできる
#digits =[1,2,3,4,5,6,7,8,9,0]
#print(min(digits))
#print(max(digits))
#print(sum(digits))
#　１から２０まで出力
#sumple1 = []
#for value in range(1,21):
#    sumple1.append(value)
#print(sumple1)
#　1から1000000までの数値リスト
#sumple2 = []
#for value in range(1,1000001):
#    sumple2.append(value)
#print(sumple2)
# 1000000sum
#sumple3 = []
#for value in range(1,1000001):
#    sumple3.append(value)
#print(sum(sumple3))
# kisuu
#sumple4 = []
#for value in range(1,21,2):
#    sumple4.append(value)
#print(sumple4)
# 3bai
#sumple5=[]
#for value in range(3,31,3):
#    sumple5.append(value)
#print(sumple5)
# 立方数
#sumple6=[]
#for value in range(1,11):
#    sumple6.append(value **3)
#print(sumple6)
# リストスライス
#player = ['alice','bob','charry','deen','eli','fred']
#print(player)
#print(player[2:5])
#print(player[:2])
#print(player[4:])
#print(player[-3:])
#print(player[:-2])
# リストスライスのループ
#for players in player[:3]:
#    print(players.title())
#　リストコピー
#food = ['あめ','チョコ','ガム','グミ','アイス']
#friend_food = food[:]
#food.append('ラムネ')
#print("私が好きなもの上から３つ")
#print(food[:3])
#friend_food.append('せんべい')
#print("\nあなたが好きなもの３つ")
#print(friend_food[1:4])
#for foods in food[:] + friend_food[:]:
#    print(foods.title())
# タプル →　タプルは（）、リストは[]
dimension = (200,100,50,25)
# 書き換えはtypeerrorで返される
#print(dimension[0])
#print(dimension[3])
# タプルの上書き
#for dimensions in dimension:
#   print(dimensions)
#print("変更後")
#dimension = (400,200,100,50,25)
#for dimensions in dimension:
#    print(dimensions)
#　タプルでメニュー
#menurist = ('ショートケーキ','モンブラン','シフォンケーキ','ドーナッツ','パフェ')
#for granmenu in menurist:
#    print(granmenu)
#menurist[0]='チョコケーキ'
#print(menurist[0])
#menurist = ('チョコレートケーキ','モンブラン','シフォンケーキ','ベイクドチーズ','パフェ')
#for ranchmenu in menurist:
#    print(ranchmenu)
# if文
#car = 'subaru'
#print("car = 'subaru'の結果をTRUE")
#print(car == 'subaru')
#print(car == 'daihatsu')
#print(car == 'suzuki')
#print(car == 'honda')
#print(car == 'mitsubishi')
#print(car == 'toyota')
#print(car.lower() =='subaru')
#print(car.upper() =='subaru')
#if car == 'subaru':
#    print("合致しました")
#else:
#    print("合致していません")
#if car == 'suzuki':
#    print("合致しました")
#elif car == 'subaru':
#   print("スバルです")
#else:
#    print("合致してません")
# 年齢認証
age = 18
#print (f"{age}です")
#if age > 18:
#        print ("選挙権があります")
#elif age> 16:
#    print(f"{age}は高校生")
#elif age> 13:
#   print(f"{age}は中学生です")
#elif age> 7:
#    print(f"{age}は小学生です")
#else:
#    print(f"{age}は幼児です")
#複数条件
alian_color = 'blue'
#if alian_color == 'green':
#    print("5点")
#elif alian_color == 'yellow':
#    print("10点")
#elif alian_color == 'red':
#    print("15点")
#else:
#    print("0点")
#for-if文連結
#favorite_fruits = ('リンゴ','オレンジ','ぶどう','なし','メロン')
#for fruitslist in favorite_fruits:
#    if fruitslist == 'なし':
#       print(f"{fruitslist}大好き")
#   else:
#       print(f"{fruitslist}はそれなりに")
#5-8,5-9連結応用
#user_list =['Admin','Becky','Charry','Deen','Emiry','Frank']
#current_list =['Becky','Charry','Dave','Emiry','Fillip']
#if user_list:#リストチェックのためのif
#    for users in user_list:
#        if users =='Admin':
#            print(f"{users}です")
#        elif users =='Frank':
#            print(f"{users}はロックされています")
#        else:
#            print("ようこそ")
#else:
#    print("ユーザがいません")
#for currentuser in current_list:
#    if currentuser in user_list:
#        print(f"{currentuser}は登録済みです")
#    else:
#        print(f"{currentuser}はいません。")
#序数
#num_list = [0,1,2,3,4,5,6,7,8,9]
#for numbers in num_list:
#    if numbers == 1:
#        print(f"{numbers}st")
#    elif numbers == 2:
#        print(f"{numbers}nd")
#    elif numbers == 3:
#        print(f"{numbers}rd")
#    else:
#        print(f"{numbers}th")
#　辞書
alian_0 ={'color':'green','point':'5'}
#print(alian_0['color'])
#print(alian_0['point'])
#alian_0['x-pos'] = 0
#alian_0['y-pos'] = 25
#print(alian_0)
#alian_1 ={}
#alian_1['color'] ='yellow'
#alian_1['point'] =10
#alian_1['x-pos'] = 5
#alian_1['y-pos'] = 10
#print(alian_1)
#del alian_1['point']
#print(alian_1)
#　複数格納
#favorite_langages={
#    'jen': 'python',
#    'sarah':'c',
#    'edward':'ruby',
#    'phil':'python',
#    }
#langage = favorite_langages['phil'].title()
#print(f"{langage}")
#for name,language in sorted(favorite_langages.items()):
#    print(f"{name.title()}の好きな言語は{language.title()}")
#    friends=['jen','sarah']
#    if name in friends:
#        languages = favorite_langages[name].title()
#        print(f"{name.title()},は{languages}がすきだもんね")
# 入れ子
#alians =[]
#for alian_member in range(30):
#    new_alian = {'color':'green','points':5,'speed':'slow'}
#    alians.append(new_alian)
#for alian in alians[:5]:
#    print(alian)
#print(f"総数：{len(alians)}")
#for alian in alians[:3]:
#    if alian['color']== 'green':
#        alian['color'] ='yellow'
#        alian['points'] = 10
#        alian['speed'] = 'medium'
#for alian in alians[11:15]:
#    if alian['color']== 'green':
#        alian['color'] ='red'
#        alian['points'] = 15
#        alian['speed'] = 'high'
#for alian in alians:
#    print(alian)
#辞書イン辞書
#users={
#    'kine':{
#        'first':'robart',
#        'last':'kine',
#        'location':'ciba',
#        },
#    'terry':{
#        'first':'bogard',
#        'last':'terry',
#        'location':'tokyo',
#        },
#    'jone':{
#        'first':'mear',
#        'last':'jone',
#        'location':'osaka',
#        },
#}
#for username,user_info in users.items():
#    fullname = f"{user_info['last']}{user_info['first']}"
#    location = user_info['location']
#    print(f"{username}")
#    print(f"{fullname}")
#    print(f"{location}")
#インプット
#message = input("please:")
#print(message)
#height =input("your height?:")
#height = int(height)
#if height <= 180:
#    print("OK")
#else:
#    print("your over")
# 奇数か偶数か
#number = input("yesorno:")
#number = int(number)
#if number %2==0:
#    print("yes")
#else:
#    print("no")
# while
#current_number = 1
#while current_number <=100:
#    print(current_number)
#    current_number +=10
#prompt = "なにか書いてください"
#prompt += "\n止めるには「終了」と入れてください"
#prompt += "\n==>"
#active = True
#while active:
#    message = input(prompt)
#    if message =='終了':
#        active = False
#    else:
#        print(message)
# break　ループの強制離脱
# continue　条件に基づいて戻る
#current_number = 0
#while current_number <10:
#    current_number +=1
#    if current_number % 2 ==0:
#        continue
#    print(current_number)
# whileで辞書
unc_users=['ai','ben','dai','jo']
c_users =[]
while unc_users:
    current_users = unc_users.pop()
    print(f"確認中:{current_users.title()}")
    c_users.append(current_users)
print("以下確認済み")
for c_user in c_users:
    print(c_user.title())
#　ユーザー入力から辞書
responses = {}
polling_active = True
while polling_active:
    name = input("your name?:")
    respons = input("your hobby?:")
    responses[name]=respons
    repeat = input("more(Y/N)")
    if repeat == 'N':
        polling_active = False
print("/n 結果")
for name,response in responses.items():
    print(f"{name} is hobby {respons}")