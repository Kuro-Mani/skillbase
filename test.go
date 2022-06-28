package main

import ("fmt"
		)

func main(){
	//fmt.Print("go ","west")文字出力
	//fmt.Print("\n")改行
	//fmt.Println("excuse",1+2,"e")文字と値の混合
	//var a,b,c int =1,10,111
	//fmt.Println(b,c)数字出力
	//fmt.Println(a+b)和
	//const d =100
	//const e =d/b
	//fmt.Println(e)除
	//i :=1繰り返し
	//for i <= 10{
	//	fmt.Println(i)
	//	i=i+1
	//}
	//for j:= 1 ;j<=10;j++{繰り返し別パターン
	//if j%2 == 0 {条件式
	//	fmt.Println(j)
	//	}
	//continue再開
	//}
	for a:=1 ;a<=11;a++{
		if 7%a == 0 {
			fmt.Println("even")
		}else{
			fmt.Println("odd")
		}
		if 8%a == 0{
			fmt.Println("is evens")
		}
		if a==10{
			fmt.Println("at",a)
		}else if a<10{
			fmt.Println("under",a)
		}else{
			fmt.Println("no mark")
		}
	}
}
