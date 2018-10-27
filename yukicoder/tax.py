#https://yukicoder.me/problems/no/56

'''
ある国の通貨単位は「ユキコダ」である。
いまからDユキコダの品物を買おうとしている？
しかし、品物の金額に対して消費税率P%の消費税が加算される。
実際に支払う金額はいくらか？
ただし、小数点以下は切り捨てします。'''
import math
D, P = list(map(int,input().split()))

print(int(D+(D*(P/100))))
