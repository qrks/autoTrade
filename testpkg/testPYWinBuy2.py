#coding:utf-8
'''
pywin32测试
'''
import win32con,win32gui,win32api

def pressChar(char):
    win32api.keybd_event(char,0,0,0);
    win32api.keybd_event(char,0,win32con.KEYEVENTF_KEYUP,0);

wdname1=u'网上股票交易系统5.0'
print(wdname1)
w1hd=win32gui.FindWindow(0,wdname1)

#获取窗口焦点
win32gui.SetForegroundWindow(w1hd)

#快捷键F1 按下按键，再释放，这就是一次按键
win32api.keybd_event(112,0,0,0);
win32api.keybd_event(112,0,win32con.KEYEVENTF_KEYUP,0);

stock_code = '150200'
for i in range(len(stock_code)):
    pressChar(int(stock_code[i]) + 96)

#tab
pressChar(9)

price = '1.10'
for i in range(len(price)):
    if price[i] == '.':
        pressChar(110)
    else:
        pressChar(int(price[i]) + 96)

#tab
pressChar(9)

vol = '100000'
for i in range(len(vol)):
    pressChar(int(vol[i]) + 96)
    
#按键B，买入
win32api.keybd_event(66,0,0,0);
win32api.keybd_event(66,0,win32con.KEYEVENTF_KEYUP,0);

