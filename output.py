import sys
import csv
import time
from PIL import Image
import math
from itertools import product
from reportlab.pdfgen import canvas
from reportlab.lib.colors import *

basename = sys.argv[1]
with open(basename+'.csv') as inp_f:
  reader = csv.reader(inp_f)
  data = [row for row in reader]

start_time = time.time() # 開始時間

img = Image.open('mario.jpg')
img_resize = img.resize((100, 100))
rgb_im = img_resize.convert('RGB')
size = rgb_im.size

#reportlabで指定できる138色を基本色11個のグループに分ける
snows = {
    'aliceblue':[240, 248, 255],
    'azure':[240, 255, 255], 
    'cornsilk':[255, 248, 220],
    'floralwhite':[255, 250, 240], 
    'ghostwhite':[248, 248, 255], 
    'honeydew':[240, 255, 240], 
    'lavender':[230, 230, 250],
    'lavenderblush':[255, 240, 245],
    'lemonchiffon':[255, 250, 205],
    'lightcyan':[224, 255, 255], 
    'lightgoldenrodyellow':[250, 250, 210], 
    'lightyellow':[255, 255, 224], 
    'linen':[250, 240, 230], 
    'mintcream':[245, 255, 250],
    'mistyrose':[255, 228, 225], 
    'oldlace':[253, 245, 230], 
    'seashell':[255, 245, 238],
    'snow':[255, 255, 255], 
    'whitesmoke':[245, 245, 245]
}

grays = {
    'cadetblue':[95, 158, 160],
    'cyan':[0, 156, 209], 
    'darkcyan':[0, 139, 139], 
    'darkkhaki':[189, 183, 107], 
    'darkolivegreen':[85, 107, 47], 
    'darkseagreen':[143, 188, 143], 
    'darkturquoise':[0, 206, 209], 
    'dimgray':[105, 105, 105], 
    'gray':[128, 128, 128], 
    'lightseagreen':[32, 178, 170], 
    'lightslategray':[119, 136, 153], 
    'mediumaquamarine':[102, 205, 170], 
    'mediumpurple': [147, 112, 219], 
    'mediumseagreen': [60, 179, 113], 
    'mediumslateblue':[123, 104, 238], 
    'mediumspringgreen':[0, 250, 154], 
    'olivedrab':[107, 142, 35], 
    'palevioletred':[219, 112, 147], 
    'rosybrown':[188, 143, 143], 
    'royalblue':[65, 105, 225], 
    'seagreen':[46, 139, 87],
    'slateblue':[106, 90, 205], 
    'slategray':[112, 128, 144], 
    'steelblue':[70, 130, 180], 
    'teal':[0, 128, 128], 
    'yellowgreen':[154, 205, 50]
 }

reds = {
    'orangered':[255, 69, 0],
    'red':[255, 0, 0]
}

blues ={
    'blue':[0, 0, 255], 
    'darkblue':[0, 0, 139], 
    'deepskyblue':[0, 191, 255], 
    'dodgerblue':[30, 144, 255], 
    'mediumblue':[0, 0, 205], 
    'navy':[0, 0, 128]
}

greens = {
    'darkgreen':[0, 100, 0], 
    'darkslategray':[47, 79, 79], 
    'forestgreen':[34, 139, 34], 
    'green':[0, 128, 0], 
    'lime':[0, 255, 0], 
    'limegreen':[50, 205, 50], 
    'springgreen':[0, 255, 127]
}

yellows = {
    'chartreuse':[127, 255, 0], 
    'greenyellow':[173, 255, 47], 
    'lawngreen':[124, 252, 0], 
    'yellow':[255, 255, 0]
}

oranges = {
    'coral':[255, 127, 80], 
    'darkgoldenrod':[184, 134, 11], 
    'darkorange':[255, 140, 0], 
    'goldenrod':[218, 165, 32], 
    'orange':[255, 165, 0], 
    'peru':[205, 133, 63], 
    'sandybrown':[244, 164, 96], 
    'tomato':[255, 99, 71]
}

pinks = {
    'antiquewhite':[250, 235, 215], 
    'beige':[231, 208, 169],
    'bisque':[255, 228, 196], 
    'blanchedalmond':[255, 235, 205], 
    'gainsboro':[220, 220, 220], 
    'hotpink':[255, 105, 180], 
    'khaki':[240, 230, 140], 
    'lightcoral':[240, 128, 128], 
    'lightpink':[255, 182, 193], 
    'lightsalmon':[255, 160, 122], 
    'moccasin':[255, 228, 181], 
    'navajowhite':[255, 222, 173], 
    'palegoldenrod':[238, 232, 170], 
    'papayawhip':[255, 39, 213], 
    'peachpuff':[255, 218, 185], 
    'pink':[255, 192, 203], 
    'plum':[221, 160, 221], 
    'salmon':[250, 128, 114], 
    'violet':[238, 130, 238], 
    'wheat':[245, 222, 179]
}

purples = {
    'blueviolet':[138, 43, 226], 
    'darkmagenta':[139, 0, 139], 
    'darkorchid':[153, 50, 204], 
    'darkslateblue':[72, 61, 139], 
    'darkviolet':[148, 0, 211], 
    'deeppink':[255, 20, 147], 
    'fuchsia':[255, 0, 255], 
    'indigo':[75, 0, 130], 
    'magenta':[255, 0, 255], 
    'mediumvioletred':[199, 21, 133], 
    'midnightblue':[25, 25, 112], 
    'purple':[128, 0, 128]
}

browns = {
    'brown':[165, 42, 42], 
    'chocolate':[80, 56, 48], 
    'crimson':[220, 20, 60], 
    'darkred':[139, 0, 0], 
    'firebrick':[178, 34, 34], 
    'indianred':[205, 92, 92], 
    'maroon':[128, 0, 0], 
    'olive':[92, 84, 36], 
    'saddlebrown':[139, 69, 19], 
    'sienna':[136, 45, 23]
}

silvers = {
    'aqua':[0, 255, 255], 
    'aquamarine':[127, 255, 212], 
    'burlywood':[222, 184, 135], 
    'cornflowerblue':[100, 149, 237], 
    'darkgray':[169, 169, 169], 
    'darksalmon':[233, 150, 122], 
    'ivory':[222, 210, 191], 
    'lightblue':[173, 216, 230], 
    'lightgreen':[144, 238, 144], 
    'lightgrey':[211, 211, 211], 
    'lightskyblue':[135, 206, 250], 
    'lightsteelblue':[176, 196, 222], 
    'mediumorchid':[186, 85, 211], 
    'mediumturquoise':[72, 209, 204], 
    'orchid':[218, 112, 214], 
    'palegreen':[152, 251, 152], 
    'paleturquoise':[175, 238, 238], 
    'powderblue':[176, 224, 230], 
    'silver':[192, 192, 192], 
    'skyblue':[137, 189, 222], 
    'tan':[210, 180, 140], 
    'thistle':[216, 191, 216], 
    'turquoise':[64, 224, 208]
}

kijun = {
    'snow': [255,255,255],
    'black': [0,0,0],
    'gray':[128,128,128],
    'red': [255,0,0],
    'blue': [0,0,255],
    'green':[0,128,0],
    'yellow': [255,255,0],
    'orange':[255,165,0],
    'pink':[255,192,203],
    'purple':[128,0,128],
    'brown':[165,42,42],
    'gold':[255,215,0],
    'silver':[192,192,192]
}

sizes = data.pop(0)
rows = int(sizes[0])
cols = int(sizes[1])

color_data= [['' for j in range(cols)] for i in range(rows)] #画像の各ピクセルに対応した色を格納するための配列を作成

def color_serch(mr,mg,mb,color_name): #画像の各ピクセルの色をreportlabで指定できる色に近似する関数
    for key in color_name:
      r,g,b = color_name[key]
      #RGB値を3次元空間として考え、２点間の距離を求める
      distance = math.sqrt((mr-r)*(mr-r)+(mg-g)*(mg-g)+(mb-b)*(mb-b))
      distant_dict[key] = distance
    #最も距離が近い（値が小さい）順に並べる
    srt_distance_dict = sorted(distant_dict.items(), key=lambda x:x[1])
    color,value = srt_distance_dict[0]
    return color

for i in range(rows):
    for j in range(cols):
      mr,mg,mb = rgb_im.getpixel((j,i))
      distant_dict = {}
      color = color_serch(mr,mg,mb,kijun) #画像のピクセルの色がどの基本色に最も近いか調べる
      if color == 'snow': 
        color_serch(mr,mg,mb,snows) #基本色のグループの中から最も近い色を探す
      elif color == 'black': 
        color_data[i][j] = 'black'
      elif color == 'gray': 
        color_serch(mr,mg,mb,grays)
      elif color == 'red': 
        color_serch(mr,mg,mb,reds)
      elif color == 'blue': 
        color_serch(mr,mg,mb,blues)
      elif color == 'green': 
        color_serch(mr,mg,mb,greens)
      elif color == 'yellow': 
        color_serch(mr,mg,mb,yellows)
      elif color == 'orange': 
        color_serch(mr,mg,mb,oranges)
      elif color == 'pink': 
        color_serch(mr,mg,mb,pinks)
      elif color == 'purple': 
        color_serch(mr,mg,mb,purples)
      elif color == 'brown': 
        color_serch(mr,mg,mb,browns)
      elif color == 'gold': 
        color_data[i][j] = 'gold'
      elif color == 'silver': 
        color_serch(mr,mg,mb,silvers)
      color_data[i][j] = color

ylist = list(range(50, 50*(rows+2), 50))
xlist = list(range(50, 50*(cols+2), 50))
c = canvas.Canvas(basename+'.pdf',bottomup=False)
c.setPageSize((xlist[-1]+50, ylist[-1]+50))
c.grid(xlist, ylist)
c.setStrokeColor(snow)

for y, x in product(range(rows), range(cols)):
  if data[y][x]:
    if 'x' in data[y][x]: #黒マスの時、画像の各ピクセルの色に対応した色マスにする
      c.setFillColor(color_data[y][x])
      c.rect(xlist[x], ylist[y], 50, 50, fill=True)
    elif '◯' in data[y][x]: #照明マス
      c.setFontSize(40)
      c.setFillColor(black)
      c.drawCentredString(xlist[x]+25, ylist[y]+40, 'O')      
    elif 'none' in data[y][x]: #0の数字マス
      c.setFillColor(color_data[y][x])
      c.rect(xlist[x], ylist[y], 50, 50, fill=True)
      c.setFillColor(snow)
      c.drawCentredString(xlist[x]+25, ylist[y]+40, '0')  
    else: #数字マス
      c.setFillColor(color_data[y][x])
      c.rect(xlist[x], ylist[y], 50, 50, fill=True)
      c.setFillColor(snow)
      c.drawCentredString(xlist[x]+25, ylist[y]+40, data[y][x])  
      
elapsed_time = time.time() - start_time
print("Running time: {0}".format(elapsed_time)+" [sec]")

c.showPage()
c.save()

