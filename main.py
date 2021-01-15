#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 下午3:15
# @Author  : Jay.Chen
# @File    : Pygame_fonts.py
# @Software: PyCharm

import pygame
import os
import cv2
import numpy as np
import time
import random
from tqdm import tqdm

NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

# 生成图像
# image = Image.new('RGB', (1024, 224), (255, 255, 255))  # w,h
# 将图像保存下来
# image.save(open(str(1) + '.png', 'wb'), 'png')
# 初始化
pygame.init()
# 读取图像
# img = pygame.image.load('template/template_1.png')
# 导入字体
fontType = os.path.join("fonts/fangsong_GB2312.ttf")
# 设置一个字体对象
fontObject = pygame.font.Font(fontType, 32)
# 得到预计输入字体的所需大小
# print(fontObject.size('xs'))
# 设置加粗
# fontObject.set_bold(True)
# 设置斜体
# fontObject.set_italic(True)
# 设置下划线
# fontObject.set_underline(True)

label_txt = open("rec_gt.txt", "w")

saved_path = "crop_img"
if os.path.exists(saved_path):
    import shutil

    shutil.rmtree(saved_path)
    os.makedirs(saved_path)
else:
    os.makedirs(saved_path)


def gd_txt():
    txt = ""
    # a = np.random.choice(LETTERS, 1)
    txt += random.choice(LETTERS) + " "
    for _ in range(2): txt += random.choice(LETTERS)
    for _ in range(4): txt += str(random.choice(NUMBERS))
    txt += random.choice(LETTERS)
    for _ in range(2):
        txt += " " + random.choice(LETTERS)
        for _ in range(8): txt += str(random.choice(NUMBERS))
    txt += " (" + random.choice(LETTERS) + ") " + random.choice(LETTERS) + " " + str(random.choice(NUMBERS))

    return txt


def gd_txt_file():
    # B LD0329G P20201217 E20221217 (L) A 3
    num = 0
    txt = ""
    for i_1 in LETTERS:
        # txt = ""
        txt += i_1 + " "
        for i_2 in LETTERS:
            txt += i_2
            for i_3 in LETTERS:
                txt += i_3
                for i_4 in NUMBERS:
                    txt += str(i_4)
                    for i_5 in NUMBERS:
                        txt += str(i_5)
                        for i_6 in NUMBERS:
                            txt += str(i_6)
                            num += 1
                            txt = txt[:-1]
                        txt = txt[:-1]
                    txt = txt[:-1]
                txt = txt[:-1]
            txt = txt[:-1]
        txt = ""
    print(num)


def runner():
    for _ in tqdm(range(5)):
        file_name = str(np.random.uniform(0.1, 0.9) * time.time()).replace(".", "_")
        # 创建文本surface
        txt = "B LD0329G P20201217 E20221217 (L) A 3"
        # txt = gd_txt()

        # print(fontObject.size(txt))

        cv_img = cv2.imread("template/template_1.png")
        t_w, t_h = fontObject.size(txt)[:]
        img_h, img_w = cv_img.shape[:2]

        assert img_h > t_h and img_w > t_w

        offset = 10
        s_w, s_h = np.random.randint(0, int(img_w - t_w) - offset), np.random.randint(0, int(img_h - t_h) - offset)

        cv_img = cv_img[s_h:s_h + t_h + offset, s_w:s_w + t_w + offset]
        cv2.imwrite("1.png", cv_img)
        img = pygame.image.load('1.png')

        create_text = fontObject.render(txt, True, (0, 0, 0))  # 文本、抗锯齿、字体颜色、背景颜色

        # surface的复制
        img.blit(create_text, (int(offset / 2), int(offset / 2)))  # 文本surface、复制到目标surface的起始坐标
        # 保存
        saved_name = file_name + '.png'
        pygame.image.save(img, os.path.join("output", saved_name))
        label_txt.write("crop_img/" + saved_name + "\t" + str(txt).replace(" ", "") + "\n")


if __name__ == '__main__':
    runner()
    # gd_txt_file()
