#https://yukicoder.me/problems/no/264

'''
自分と相手がじゃんけんをする。
じゃんけんの結果を標準出力に出力してください。
結果は、自分が勝ったら「Won」、自分が負けたら「Lost」、引き分けなら「Drew」を出力してください。
入力
N K
ぐー, ちょき, ぱーをそれぞれ 0, 1, 2とし、１つ目に自分のが２つ目に相手のが与えられます。
'''
import time
start = time.time()


N, K = list(map(int,input().split()))

if N == K:
	print("Drew")
elif N-K == -1 or N-K == 2:
	print("Won")
elif N-K == -2 or N-K == 1:
	print("Lost")

print(time.time()-start)
	
#0 1, 1 2, 2 0 勝ち
#0 0, 1 1, 2 2 引き分け
#0 2, 1 0, 2 1 負け
