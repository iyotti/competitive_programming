'''
https://beta.atcoder.jp/contests/abs/tasks/abc081_b
'''
n = int(input())
ary = list(map(int, input().split()))
count=0
flag = True

while flag:
	for i in range(n):
		if ary[i]%2 != 0 or ary[i] == 0:
			flag = False
			break
		ary[i] = ary[i]//2
	if flag:
		count+=1

print(count)