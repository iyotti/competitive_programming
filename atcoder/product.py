'''
https://beta.atcoder.jp/contests/abs/tasks/abc086_a
シカのAtCoDeerくんは二つの正整数 
a,b
 を見つけました。 
a と b
 の積が偶数か奇数か判定してください。整数 a+b+c と、文字列 s を並べて表示しなさい。
'''

a, b = list(map(int, input().split()))
if (a*b)%2 == 0:
	print("Even")
else:
	print("Odd")
