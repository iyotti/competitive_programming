#https://yukicoder.me/problems/no/82

'''
幅Wと高さHと左上の色が指定されるので市松模様を描け。
市松模様は、黒と白が交互に現れる模様である。
模様は黒を'B'、白を'W'を使って描くものとする。
'''
W,H,C = list(map(str,input().split()))
for i in range(int(H)):
	color = C
	rt=""
	for j in range(int(W)):
		rt+=color
		color="W" if color=="B" else "B"
	C="W" if C=="B" else "B"
	print(rt)