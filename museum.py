import sys
import csv
import time
import numpy as np
from itertools import product
import cv2

start_time = time.time() # 開始時間

img = cv2.imread('mario.jpg',cv2.IMREAD_GRAYSCALE) #グレースケールで画像読み込み
dst = cv2.resize(img,(100, 100))
edges = cv2.Canny(dst,50,200) #エッジ抽出
rows,cols = dst.shape

data = [['' for j in range(cols)] for i in range(rows)] #照明配置用の配列を作成
x = [['' for j in range(cols)] for i in range(rows)] #照明を配置可能か判別用の配列を作成(制約：照明を配置できないマスには1を代入する)

for i in range(rows):
    for j in range(cols):
        if edges[i][j] == 255: #エッジ部分の値は255なので、その時黒マスを配置
            data[i][j] = 'x'
            x[i][j] = 'x'
        else:
            pass

for i in range(rows):
    for j in range(cols):
        if not x[i][j]: #白マスを探す
            data[i][j] = '◯' #data[i][j]は白マスなので照明を配置
            x[i][j] = 1 #data[i][j]に照明を配置したのでx[i][j]に1を配置する(制約：照明を配置できないマスにはx[i][j]に1を代入する)
            #十字方向全てを探索する際のカウント用変数を宣言
            x_right_count = 0
            x_left_count = 0
            y_up_count = 0
            y_down_count = 0
            #美術館パズルのルールとして、照明配置後十字方向全ての白マスには照明を配置できないため、十字方向の全ての白マスを探索しxに1を代入する
            while j + x_right_count + 1 < cols and not data[i][j + x_right_count + 1]: #右方向の白マス全てを探索するため、右隣のマスが枠内かつ白マスの時ループ実行
                x_right_count += 1
                x[i][j + x_right_count] = 1 #右隣のマスに1を代入
            while j - x_left_count - 1 >= 0 and not data[i][j - x_left_count - 1]:
                x_left_count += 1      
                x[i][j - x_left_count] = 1
            while i + y_down_count + 1 < rows and not data[i + y_down_count + 1][j]:
                y_down_count += 1  
                x[i + y_down_count][j] = 1    
            while i - y_up_count - 1 >= 0 and not data[i - y_up_count - 1][j]:
                y_up_count += 1
                x[i - y_up_count][j] = 1

for i, j in product(range(rows),range(cols)):
    suji = 0
    if data[i][j] == 'x': #美術館パズルでは数字マスの数字だけ隣接するマスに照明を配置しなければいけないので、黒マスに隣接する照明の数だけその数字マスにする
        suji = sum(x[i + dy][j + dx] for dy, dx in [(0, -1), (1, 0), (0, 1), (-1, 0)]if 0 <= i + dy < rows and 0 <= j + dx < cols and data[i + dy][j + dx] == '◯') #黒マスに隣接する照明の数を数える
        if suji > 0:
            data[i][j] = int(suji) #黒マスを数字マスに変換
        if suji == 0:
            if np.random.randint(1,9) == 1: #美術館パズルには0の数字マスが存在するので、ランダムで0の数字マスを生成
                data[i][j] = 'none'

sizes = ['' for i in range(cols)]
sizes[0] = rows
sizes[1] = cols
data.insert(0, sizes)

with open('problem'+'_sol.csv', 'w') as out_f:
  writer = csv.writer(out_f)
  writer.writerows(data)

elapsed_time = time.time() - start_time

print("Running time: {0}".format(elapsed_time)+" [sec]")