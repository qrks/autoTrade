#coding:utf-8
'''
pywin32测试
'''
import time
import win32ui,win32con,pythoncom,win32gui,win32api
import ref1 as ref

def pressChar(char):
    win32api.keybd_event(char,0,0,0);
    win32api.keybd_event(char,0,win32con.KEYEVENTF_KEYUP,0);

wdname1=u'网上股票交易系统5.0'
print(wdname1)
w1hd=win32gui.FindWindow(0,wdname1)


# w2 = win32gui.FindWindowEx(w1hd,0,'AfxMDIFrame42s',None)
# show_window_attr(w2)

# w3 = win32gui.FindWindowEx(w2,0,u'#32770 (对话框)',None)
# print(w3)
# show_window_attr(w3)

#获取窗口焦点
win32gui.SetForegroundWindow(w1hd)


#快捷键F2 按下按键，再释放，这就是一次按键
win32api.keybd_event(113,0,0,0);
win32api.keybd_event(113,0,win32con.KEYEVENTF_KEYUP,0);

stock_code = '150023'
for i in range(len(stock_code)):
    pressChar(int(stock_code[i]) + 96)

#tab
pressChar(9)

price = '0.600'
for i in range(len(price)):
    if price[i] == '.':
        pressChar(110)
    else:
        pressChar(int(price[i]) + 96)

#tab
pressChar(9)

vol = '1000'
for i in range(len(vol)):
    pressChar(int(vol[i]) + 96)
    
#按键B，卖出
win32api.keybd_event(83,0,0,0);
win32api.keybd_event(83,0,win32con.KEYEVENTF_KEYUP,0);

