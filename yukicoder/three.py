#https://yukicoder.me/problems/no/264

'''
A以上B以下の整数のうち、3の倍数および3の付く数を、小さい順に出力してください。

なお、「3の付く数」とは、10進数表記にした時、少なくとも1つの桁が3であるような数のことです。

入力
A B
入力はすべて整数で与えられる。
1≤A≤2000000000
1≤B≤2000000000
0≤B−A<100
'''
import time
start = time.time()

A, B = list(map(int,input().split()))

while A <= B:
	if A%3==0 or str(A).count("3"):
		print(A)
	A+=1


#print(time.time()-start)
