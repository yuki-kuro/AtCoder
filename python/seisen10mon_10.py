# ABC 086 C - Traveling

import sys

def solve():
    # 入力：地点の数 N
    n = int(sys.stdin.readline())
    
    # 現在の時刻と座標（初期位置は (0, 0, 0)）
    current_t, current_x, current_y = 0, 0, 0
    
    for _ in range(n):
        # 次の目的地の情報
        next_t, next_x, next_y = map(int, sys.stdin.readline().split())
        
        # 1. 前の地点からの経過時間と移動距離を計算
        dt = next_t - current_t
        dist = abs(next_x - current_x) + abs(next_y - current_y)
        
        # 2. 条件チェック
        # ・最短距離 dist が残り時間 dt より大きいと到達不可能
        # ・余った時間 (dt - dist) が偶数でないと、ちょうどその場に止まれない
        if dt < dist or (dt - dist) % 2 != 0:
            print("No")
            return
        
        # 現在の情報を更新して次のループへ
        current_t, current_x, current_y = next_t, next_x, next_y
        
    # すべての地点をクリアできれば Yes
    print("Yes")

if __name__ == '__main__':
    solve()






