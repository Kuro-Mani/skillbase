print("hello")
#message="next stage"                       # messageの入れ子に文字列を入れる
#print(message)                             # messasgeを出力する
#group=['red','blue','yellow','green']      # groupの入れ子にリストを作る
#print(group)                               # groupを出力
                                            # インデックスは0から
#group.append('white')                      # リストへ追加
#group.sort()                               # 文字コード順に並び替え
#print(group)
#group.sort(reverse=True)                   # 物字コード順に逆順
#print(group)
#size=len(group)                            # リストの要素数を数える
#print(size)
#for magician in group:print(magician)      # groupリストから１つずつ呼び出して出力するループ処理
#for valueint in range(5):print(valueint)   # 0~4までのレンジで1つずつ呼び出して出力するループ処理
#numbers = list(range(1,11))                # numbers入れ子にlist関数で1~10までのリストを作る
#print(numbers)
#numbers = list(range(1,11,2))              # list関数で1~10までのなかで2ずつ加算するリストを作る
#print(numbers)
#square = []                                # squareをリスト化
#for values in range(1,101):                # 1~100までのレンジで1つずつ要素を呼び出す
#    sqx = values ** 2                      # [*] ＝乗算、[**]　＝べき乗 要素を2乗する
#    square.append(sqx)                     # squareリストに追加する。
#print(square)
                                            # ３の段バージョン
#square2 = []
#for value in range(1,10):
#    square2.append(value*3)
#print(square2)
#digits =[1,2,3,4,5,6,7,8,9,0]              # digits関数　最大値、最小値、合計などできる
#print(min(digits))                         # 最小値
#print(max(digits))                         # 最大値
#print(sum(digits))                         # 合計値
#sumple1 = []                               # sumple1をリスト化
#for value in range(1,21):                  #１から２０まで出力
#    sumple1.append(value)
#print(sumple1)
#sumple2 = []                               # 1から1000000までの数値リスト
#for value in range(1,1000001):
#    sumple2.append(value)
#print(sumple2)
#sumple3 = []                               # 1000000sum
#for value in range(1,1000001):
#    sumple3.append(value)
#print(sum(sumple3))
#sumple4 = []                               # 1~20までの奇数を出力
#for value in range(1,21,2):
#    sumple4.append(value)
#print(sumple4)
#sumple5=[]                                 # 3~30までの3の倍数
#for value in range(3,31,3):
#    sumple5.append(value)
#print(sumple5)
#sumple6=[]                                 # 立方数
#for value in range(1,11):
#    sumple6.append(value **3)
#print(sumple6)
#player = ['alice','bob','charry','deen','eli','fred']
#print(player)                              # リストの中身をすべて出力
#print(player[2:5])                         # リストの3番目から5番目までを出力
#print(player[:2])                          # リストの2番目まで出力
#print(player[4:])                          # リストの5番目から出力
#print(player[-3:])                         # リストの最後から３つ出力
#print(player[:-2])                         # リストの最後から2つを除いて出力
#for players in player[:3]:                 # リストスライスのループ
#    print(players.title())
#food = ['あめ','チョコ','ガム','グミ','アイス']
#friend_food = food[:]                      #　リストコピー
#food.append('ラムネ')
#print("私が好きなもの上から３つ")
#print(food[:3])
#friend_food.append('せんべい')
#print("\nあなたが好きなもの３つ")
#print(friend_food[1:4])
#for foods in food[:] + friend_food[:]:     # foodリストとfriend_foodリストを併せて要素を1つずつ出力するループ処理
#    print(foods.title())
#dimension = (200,100,50,25,12,6,3,1)       # タプル →　タプルは（）、リストは[]
                                            # 不変なリストをタプルという。書き換えはtypeerrorで返される。
#print(dimension[0])                        # タプルの1番目を出力 
#print(dimension[3+4])                      # タプルの7番目を出力（値の演算は成立する）
#for dimensions in dimension:               # タプルの上書き
#   print(dimensions)
#print("変更後")
#dimension = (400,200,100,50,25,10,5)
#for dimensions in dimension:
#    print(dimensions)
                                            # タプルでメニュー
#menurist = ('ショートケーキ','モンブラン','シフォンケーキ','ドーナッツ','パフェ')
#for granmenu in menurist:
#    print(granmenu)
#menurist[0]='チョコケーキ'
#print(menurist[0])
#menurist = ('チョコレートケーキ','モンブラン','シフォンケーキ','ベイクドチーズ','パフェ')
#for ranchmenu in menurist:
#    print(ranchmenu)
car = 'subaru'                             # if文
#print("car = 'subaru'の結果をTRUE")
#print(car == 'subaru')                    # carの要素が'subaru'か比較
#print(car == 'daihatsu')
#print(car == 'suzuki')
#print(car == 'honda')
#print(car == 'mitsubishi')
#print(car != 'toyota')                    # 否定バージョン
#print(car.lower() =='subaru')             # carの要素を小文字化
#print(car.upper() =='subaru')             # carの要素を大文字化
#if car == 'subaru':                       # ifelse文
#   print("合致しました")
#else:
#   print("合致していません")
#if car == 'suzuki':                       # ifelifelse文
#   print("合致しました")
#elif car == 'subaru':
#   print("スバルです")
#else:
#   print("合致してません")
#age = 18                                  # 年齢認証
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
#alian_color = 'blue'                      # 複数条件
#if alian_color == 'green':
#    print("5点")
#elif alian_color == 'yellow':
#    print("10点")
#elif alian_color == 'red':
#    print("15点")
#else:
#    print("0点")
#favorite_fruits = ('リンゴ','オレンジ','ぶどう','なし','メロン')
#for fruitslist in favorite_fruits:         # for-if文連結
#    if fruitslist == 'なし':               # なし条件
#       print(f"{fruitslist}大好き")
#   else:                                   # それ以外の処理
#       print(f"{fruitslist}はそれなりに")
                                            # 連結応用
#user_list =['Admin','Becky','Charry','Deen','Emiry','Frank']
#current_list =['Becky','Charry','Dave','Emiry','Fillip']
#if user_list:                              # リストチェック::ifにリスト変数が指定されるとpythonはリストに１つ以上値があるか判定する
#    for users in user_list:                # リストチェックがtrueの場合にfor文が実行される。
#       if users =='Admin':                 
#           print(f"{users}です")
#       elif users =='Frank':
#           print(f"{users}はロックされています")
#       else:
#           print("ようこそ")
#else:                                       # userlistが空の場合に実行
#   print("ユーザがいません")
#for currentuser in current_list:            # current_listから1つずつ要素を取り出し、currentuserに入れる
#    if currentuser in user_list:            # currentuserの値がuser_listにあるか比較
#        print(f"{currentuser}は登録済みです")
#    else:                                   # ない場合
#        print(f"{currentuser}はいません。")
#num_list = [0,1,2,3,4,5,6,7,8,9]            # 序数
#for numbers in num_list:
#    if numbers == 1:
#        print(f"{numbers}st")
#    elif numbers == 2:
#        print(f"{numbers}nd")
#    elif numbers == 3:
#        print(f"{numbers}rd")
#    else:
#        print(f"{numbers}th")
#alian_0 ={'color':'green','point':'5'}      # 辞書（キー:値）
#print(alian_0['color'])                     # 辞書からcolorに関連付けされた値を返す
#print(alian_0['point'])                     # 辞書からpointに関連付けされた値を返す
#alian_0['x-pos'] = 0                        # 辞書に新しいキーと値を追加
#alian_0['y-pos'] = 25
#print(alian_0)
#alian_1 ={}                                 # 新しい辞書を作る
#alian_1['color'] ='yellow'
#alian_1['point'] =10
#alian_1['x-pos'] = 5
#alian_1['y-pos'] = 10
#print(alian_1)
#del alian_1['point']                        # 辞書のキーを消す。
#print(alian_1)
                                             # 複数格納
#favorite_langages={                        
#    'jen': 'python',
#    'sarah':'c',
#    'edward':'ruby',
#    'phil':'python',
#    }                                       # キー:値の後に","で区切ると連続でキーを作れる
#langage = favorite_langages['phil'].title()
#print(f"{langage}")                         # sortedで辞書の並びを文字列順に変更
#for name,language in sorted(favorite_langages.items()):
#    print(f"{name.title()}の好きな言語は{language.title()}")
#    friends=['jen','sarah']                 # jenとsarahの別リストfriendsを作成
#    if name in friends:                     # favalite_langagesループ処理中で nameの値がjenとsarahの時に限定している
#        languages = favorite_langages[name].title()
#        print(f"{name.title()}は{languages}がすきだもんね")
#alians =[]                                  # 入れ子
#for alian_member in range(30):              # 0~29まで合計30個、ループ処理でaliansのリストに辞書追加
#    new_alian = {'color':'green','points':5,'speed':'slow'}
#    alians.append(new_alian)
#for alian in alians[:5]:
#    print(alian)
#print(f"総数：{len(alians)}")               # 30個作れたか数える
#for alian in alians[:3]:                    # 先頭から3番目までキーの値を変更するループ処理
#    if alian['color']== 'green':
#        alian['color'] ='yellow'
#        alian['points'] = 10
#        alian['speed'] = 'medium'
#for alian in alians[11:15]:                 # 12番目から15番目までのキーの値を変更するループ処理
#    if alian['color']== 'green':
#        alian['color'] ='red'
#        alian['points'] = 15
#        alian['speed'] = 'high'
#for alian in alians:                        # リスト入れられた辞書を1つずつ出力
#    print(alian)
                                             # 辞書イン辞書
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
#for username,user_info in users.items():    # username変数をusersのキーに割り当て、user_infoにその値を割り当てペアずつ引き出す 
#    fullname = f"{user_info['last']}{user_info['first']}"
#    location = user_info['location']
#    print(f"{username}")
#    print(f"{fullname}")
#    print(f"{location}")
#message = input("please:")                  # インプット
#print(message)                              # messsageに格納されたinput変数が出力される
#height =input("your height?:")              # input変数に入力された値をheightに入れる
#height = int(height)                        # heightの値をintにする
#if height <= 180:
#    print("OK")
#else:
#    print("your over")
#number = input("yournumber?:")              # 奇数か偶数か
#number = int(number)
#if number %2==0:                            # ２で割れるか       
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
#unc_users=['ai','ben','dai','jo']
#c_users =[]
#while unc_users:
#    current_users = unc_users.pop()
#    print(f"確認中:{current_users.title()}")
#    c_users.append(current_users)
#print("以下確認済み")
#for c_user in c_users:
#    print(c_user.title())
#　ユーザー入力から辞書
#responses = {}
#polling_active = True
#while polling_active:
#    name = input("your name?:")
#    respons = input("your hobby?:")
#    responses[name]=respons
#    repeat = input("more(Y/N)")
#    if repeat == 'N':
#        polling_active = False
#print("/n 結果")
#for name,response in responses.items():
#    print(f"{name} is hobby {respons}")
class Dog:
    def __init__(self,name,age):
        self.name= name
        self.age = age
    def sit(self):
        print(f"{self.name}")
    def roll_over(self):
        print(f"{self.name}は{self.age}歳")

my_dog = Dog('ジリ','6')
my_dog.sit()
my_dog.roll_over()