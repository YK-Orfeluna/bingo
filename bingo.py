# -*- coding: utf-8 -*
"""
=========================================================
                    BINGO MACHINE                        
=========================================================
This system is developed by Python 2.7.12 & Numpy1.1.0 & Opencv 2.4.13.
(c) 2016 Yuki Kitagishi
"""

import sys
import cv2
import numpy as np

bingos = np.arange(1, 100, dtype=np.int8)	# ビンゴの配列を作成
np.random.shuffle(bingos)					# 配列の中身を乱数で回転させる

length = 500

length_c = length / 20						# 数字を表示する円の半径&1行目の円の中心座標初期位置
circle_x = length_c							# 1列目の円の中心x座標
circle_y = length_c							# 1行目の円の中心y座標

windowName = "BINGO"
cv2.namedWindow(windowName)					# 描画ウィンドウの用意

x = 5										# テキスト描画のx座標初期位置
y = length_c + 10							# テキスト描画のy座標初期位置
size = int(round(length * 0.004))			#　テキストのフォントサイズ
color = 255									# テキストのカラー
bold = 2									# テキストの太さ

esc = 27
anykey = -1
enter = 13

start = np.zeros((length, length, 1))	# スタート画面を作成
cv2.putText(start, "BINGO GAME", (150, 200), cv2.FONT_HERSHEY_PLAIN, size, color, bold, cv2.CV_AA)
cv2.putText(start, "START: ENTER", (140, 300), cv2.FONT_HERSHEY_PLAIN, size, color, bold, cv2.CV_AA)
cv2.putText(start, "EXIT: ESC", (170, 350), cv2.FONT_HERSHEY_PLAIN, size, color, bold, cv2.CV_AA)
cv2.putText(start, "NEXT NUMBER: ANYKEY", (70, 450), cv2.FONT_HERSHEY_PLAIN, size, color, bold, cv2.CV_AA)

img = np.zeros((length, length, 1))			# 表示画面を作成（正方形の幅はlength）
for i in xrange(10) :						# 表示画面上に10*10の列で円を描画
	if i == 9 :								# 表示画面上方から描画，最下行の円は9個
		limit = 9
	else :									# それ以外の行は10個
		limit = 10
	for j in xrange(limit) :				# 1行ずつ円を描画していく
		cv2.circle(img, (circle_x, circle_y), length_c, color, bold)
		circle_x += length_c * 2			# 円1つごとに円の直径（半径*2）だけx座標を進める
	circle_x = length_c						# 1行の円を描画し終えたら，円のx座標を初期化
	circle_y += length_c * 2				# 円のy座標を1行下へ

while True :
	cv2.imshow(windowName, start)

	key = cv2.waitKey(0)
	if key == enter :
		break
	elif key == esc :
		exit()
	else :
		continue

cv2.imshow(windowName, img)
key = cv2.waitKey(0)

if key == esc :
	exit()
elif key != anykey :						# Push anykey(without "esc")
	for i in bingos :
		if i < 10 :							# 数字が9以下の場合，数字を2桁にするために"0"を追加
			text = str(0) + str(i)
		else :
			text = str(i)

		cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, size, color, bold, cv2.CV_AA)

		x += length_c * 2					# テキスト描画のx座標を円の直径だけ進める
		if x >= length :					# テキスト描画のx座標がlengthを超えたら，テキスト描画のx座標は初期化，y座標は1行下へ
			x = 5
			y += length_c * 2

		cv2.imshow(windowName, img)			# 表示画面を更新

		key = cv2.waitKey(0)
		if key == esc :						# Push "esc"
			break
		else :								# Push anykey(without "esc")
			continue

	key = cv2.waitKey(0)
	if key == esc :
		exit()