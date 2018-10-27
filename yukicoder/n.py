#https://yukicoder.me/problems/no/46

'''
1歩でぴったりaセンチメートル歩ける。
bセンチメートルの区間を歩くのに最小で何歩歩く？
なお、区間はオーバーしても良い。
'''
import math
a,b = list(map(int,input().split()))
print(math.ceil(b/a))

