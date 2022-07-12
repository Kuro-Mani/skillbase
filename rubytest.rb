puts "hello"#呼び出し
#print("hero")#出力
#print(3**2)#累乗
#print(Math.sqrt(9))#平方根
#3.times do
# print("go")
#end# do ～ end　間を*.time分実行
#print("go"*3)#指定文字列を3回
#puts "jimmy".reverse#文字の逆転並び替え
#puts "arigatou".length#文字数
#puts 1123.to_s.reverse#数字の逆転並び替え
#puts [1,10,1-9]#入れ子、1-9は数式認識
#print([1,2,3,4,5].max)#グループ内の最大値
list = [1,11,111,111,1.1]
#print(list)#listを表示
#print(list.min)#listの最小値
#print(list.sort)#listを順列で並び替え
#print(list.sort!)#listを順列で並び替えてその配列で保存
#！つけたら変数の並び替えを保存する。つけない場合は表示だけ並び替えて保存はされない
#puts list[1]#listの要素１に入ってるものを出力
string ="Hello\r\n"
string +="What would you like to have?\r\n"
string +="One Hamburger and a Coffee please.\r\n"
string +="We have 3 sizes for coffee, Small, Medium and Large.\r\nWhich size would you like?\r\n"
string +="Small one, please.\r\n"
string +="For here, or to go?\r\n"
string +="To go please.\r\n"
string +="$3.45"
#puts string.reverse #文字の逆転並び替え
#puts string.gsub(/Coffee/i,"Coke")#文字の置換、/～/iは大小文字区別なし
#puts string.lines.reverse #文字列を逆転並び替え
book ={} # 配列ボックス作成
book["ame"] =:sad # 配列に追加とシンボル追加
book["kumori"] =:soso
book["hare"] =:fine
book["kaisei"] =:fine
#print(book.keys)# 配列項目を引き出す
#puts book["ame"]　
#puts book.length# 配列項目数
# ratingsという配列を値で作成、eachメソッドでbook配列にある項目分rate検索して各項目ごとカウントする
#ratings = Hash.new {0}

#book.values.each { |rate|
#  ratings[rate] += 1
#}
#puts ratings# 項目ごとのカウント結果がratingsの配列に格納されたのでそれを出力
#5.times { |time|
#  puts time
#}
#　メソッド定義
#def check(num)
#	num.times {
#		puts "test"
#	}
#	return num
#end
#puts check (2)
#a=0
#if a>=0
# puts "ok"
#else
# puts "err"
#end
# 自作メソッドと条件分岐処理
def hungry(hour)
	if hour > 12
		puts "be hungry"
		true
	else
		puts "I'm full"
	end
end
def eat(what)
	puts "eat the #{what}\n"
end
eat 'bicmac' if hungry(10)
eat 'bicmac' if hungry(13)
class commander
	attr_accessor :content, :time, :mood
	def initialize(mood,content="")
		@time	=time.now
		@content=content[0..39]
		@mood	=mood
	end
end
commander.new.time
=begin
Kuro-mani
=end
