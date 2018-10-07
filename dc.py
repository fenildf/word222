#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author zhibin time:2018/10/4
import xlrd
import tkinter

# 预先准备工作

L1 = []  # L1列表负责存储 英文单词
L2 = []  # L2列表负责存储 中文意思
L3 = []  # 存储词性
k = 0  # 复习模式下使用的计数器


# 功能1：载入3000单词组
def loadwordlist(j):
    wb = xlrd.open_workbook("3000coreword.xls")  # 打开文件
    sheet = wb.sheet_by_index(0)  # 指定读取第一个表格的信息
    t = (j - 1) * 15 + 1

    for i in range(15):
        r = i + t  # r为取数列
        WordE = sheet.cell(r, 2).value  # 获取第r行，第3列的英文单词
        WordC = sheet.cell(r, 3).value  # 获取第r行，第4列的中文意思
        L1.append(WordE)
        L2.append(WordC)


# 功能2：载入50+考研真题的文章单词组
def loadwordlist2(j):
    wb2 = xlrd.open_workbook("text50.xlsx")  # 打开文件
    sheet2 = wb2.sheet_by_index(0)  # 指定读取第一个表格的信息
    r = 1  # 从第二行开始读取
    while sheet2.cell(r, 0).value != j:  # 循环到(r,2)数值 与 设定数相等为止
        r += 1
    while sheet2.cell(r, 0).value == j:  # 循环到(r,2)数值 与 设定数值不等为止
        WordE = sheet2.cell(r, 1).value  # 获取第r行，第3列的英文单词
        WordC = sheet2.cell(r, 3).value  # 获取第r行，第4列的中文意思
        WordS = sheet2.cell(r, 2).value  # 读取第r行，第2列的单词词性
        L1.append(WordE)
        L2.append(WordC)
        L3.append(WordS)
        r += 1


# 功能2：单词螺旋滚动
def Wordshark(i):
    # 单词出现的顺序数列 N1
    N1 = [1, 1, 2, 2, 1, 2, 1, 2, 3, 3, 1, 2, 3, 1, 2, 3, 2, 3, 4, 4, 2, 3, 4, 1, 2, 3, 4, 2, 3, 4, 5, 5, 1, 3, 4, 5, 2,
          3, 4, 5, 1, 3, 4, 5, 6, 6, 2, 4, 6, 1, 3, 5, 6, 2, 4, 6, 7, 7, 3, 5, 7, 2, 4, 6, 7, 3, 5, 7, 1, 2, 3, 8, 8, 4,
          6, 8, 3, 5, 7, 8, 4, 6, 8, 9, 9, 5, 7, 9, 4, 6, 8, 9, 3, 5, 7, 9, 10, 10, 6, 8, 10, 5, 7, 9, 10, 4, 6, 8, 10,
          11, 11, 5, 7, 9, 11, 6, 8, 10, 11, 7, 9, 11, 12, 12, 6, 8, 10, 12, 7, 9, 11, 12, 6, 8, 10, 12, 13, 13, 9, 11,
          13, 1, 2, 3, 8, 10, 12, 13, 9, 11, 13, 14, 14, 8, 10, 12, 14, 4, 5, 6, 9, 11, 13, 14, 12, 8, 10, 12, 15, 15,
          11, 13, 15, 4, 10, 12, 14, 15, 11, 13, 15, 1, 3, 5, 7, 9, 14, 11, 13, 15, 2, 4, 14, 6, 8, 15, 10, 12, 14, 1,
          3, 5, 7, 2, 4, 6, 8, 9, 11, 13, 15, 10, 12, 14, 1, 1]
    word = L1[N1[i] - 1]  # 读取第i个单词
    chinese = L2[N1[i] - 1]  # 读取第i个单词的中文意思
    try:
        if N1[i] == N1[i + 1]:
            var.set(word)
            var2.set(chinese)  # 如果该单词第一次出现，在lb2上显示中文单词意思
            BDC.after(4000, Wordshark, i + 1)  # 第一次出现的单词停留4s
        else:
            var.set(word)
            var2.set(" ")
            BDC.after(2000, Wordshark, i + 1)  # 再一次出现的单词停留2.0S
    # 当程序执行完成的时候，会进入益处异常，跳到该程序段
    except IndexError:
        var.set(" ")
        var2.set(" ")
        ks1 = '{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}\n{10}\n{11}\n{12}\n{13}\n{14}'.format(L1[0], L1[1],
                                                                                                      L1[2], L1[3],
                                                                                                      L1[4], L1[5],
                                                                                                      L1[6], L1[7],
                                                                                                      L1[8], L1[9],
                                                                                                      L1[10], L1[11],
                                                                                                      L1[12], L1[13],
                                                                                                      L1[14], )
        ks2 = '{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}\n{10}\n{11}\n{12}\n{13}\n{14}'.format(L2[0], L2[1],
                                                                                                      L2[2], L2[3],
                                                                                                      L2[4], L2[5],
                                                                                                      L2[6], L2[7],
                                                                                                      L2[8], L2[9],
                                                                                                      L2[10], L2[11],
                                                                                                      L2[12], L2[13],
                                                                                                      L2[14], )
        var3.set(ks1)
        var4.set(ks2)
        BDC.after(40000, Qinkong)


# 功能3：复习模式下单词显示
def Fuxi(i):
    word = L1[i]  # 读取第i个单词ff  # 读取第i个单词
    var.set(word)  # 显示第i个单词
    var2.set("")  # 清空中文意思


# 功能4：复习模式下显示中文
def Toukan(i):
    Chinese = L2[i]  # 读取第i个单词的中文意思
    cixing = L3[i]
    kkk = cixing + " " + Chinese
    var2.set(kkk)
    BDC.after(1000, Fuxi, k - 1)


# 功能5：数据清空
def Qinkong():
    global L1, L2, k
    L1 = []  # 清空所有单词
    L2 = []  # 清空所有单词
    var.set(" ")
    var2.set(" ")
    var3.set(" ")
    var4.set(" ")
    k = 0


# 3个调用的中转程序
def run1():  # 调用单词组1
    a = int(inp1.get())
    loadwordlist(a)


def run2():  # 调用单词滚动
    Wordshark(0)


def run3():  # 调用复习
    global k
    Fuxi(k)
    k += 1


def run4():  # 调用偷看功能
    global k
    Toukan(k - 1)


def run5():  # 调用50text的单词组2
    a = int(inp1.get())
    loadwordlist2(a)


# 构建窗口用的按钮、显示器
BDC = tkinter.Tk()
BDC.title("极速闪回法背单词")
BDC.geometry("2400x1200+100+100")
frame = tkinter.Frame(height=1200, width=2400, bg="Wheat")  # 界面背景色：麦黄色
frame.pack(expand="YES", )

# 输出变量，用于将输出的数据传给输出框
var = tkinter.StringVar()
var2 = tkinter.StringVar()
var3 = tkinter.StringVar()
var4 = tkinter.StringVar()

# 输入框，输入要学习的单元
inp1 = tkinter.Entry(BDC)
inp1.place(relx=0.79, y=1050, height=50, width=100)  # 指定输入框的位置

# 按键，负责调用功能。
b1 = tkinter.Button(BDC, text="载入数据\n共1-219组", command=run1, width=15, height=2, bd=4)
b1.place(relx=0.85, y=1050, relheight=0.05)  # 指定按钮框的位置
b6 = tkinter.Button(BDC, text="载入数据\n共1-50篇文章", command=run5, width=15, height=2, bd=4)
b6.place(relx=0.85, y=1110, relheight=0.05)  # 指定按钮框的位置
b2 = tkinter.Button(BDC, text="滚动模式", command=run2, width=20, height=2, bd=4, )
b2.place(relx=0.92, y=1050, relheight=0.1)  # 指定按钮框的位置
b3 = tkinter.Button(BDC, text="复习模式\n下一个", command=run3, width=20, height=2, bd=4, )
b3.place(relx=0.02, y=1050, relheight=0.1)  # 指定按钮框的位置
b4 = tkinter.Button(BDC, text="清空单词列表", command=Qinkong, width=15, height=2, bd=4, )
b4.place(relx=0.79, y=1110, relheight=0.05)
b5 = tkinter.Button(BDC, text="偷看一下\n(仅复习模式下使用)", command=run4, width=15, height=2, bd=4)
b5.place(relx=0.02, y=950, relheight=0.05)

# 输出框，分别负责输出 1英文 2中文 3全英文列表 4全中文列表
lb1 = tkinter.Label(BDC, textvariable=var, fg="black", font=("Calibri", 200), bg="Wheat")
lb1.place(x=300, y=200)  # 该位置负责输出英文
lb2 = tkinter.Label(BDC, textvariable=var2, fg="black", font=("黑体", 50), bg="Wheat")
lb2.place(x=600, y=600)  # 该位置负责输出中文
lb3 = tkinter.Label(BDC, textvariable=var3, fg="black", font=("Calibri", 45), bg="Wheat")
lb3.place(x=300, y=0)  # 该位置负责结束的时候输出英文列表
lb4 = tkinter.Label(BDC, textvariable=var4, fg="black", font=("Calibri", 45), bg="Wheat")
lb4.place(x=700, y=0)  # 该位置负责结束的时候输出英文列表

BDC.mainloop()
