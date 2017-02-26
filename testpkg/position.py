#coding:utf-8

import time
import win32ui,win32con,pythoncom,win32gui,win32api
import ref1 as ref
import win32clipboard as CP
import pandas as pd

def get_clipboard():
    win32api.keybd_event(17, 0, 0, 0)
    win32api.keybd_event(67, 0, 0, 0)
    win32api.keybd_event(67, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    CP.OpenClipboard()
    raw_text = CP.GetClipboardData(win32con.CF_TEXT)
    CP.CloseClipboard()
    decode = raw_text.decode('gb2312').split()
    decode.pop()
    return decode

wdname1=u'网上股票交易系统5.0'
Main=win32gui.FindWindow(0,wdname1)
while Main == 0:
    print('to get Main!')
    Main=win32gui.FindWindow(0,wdname1)

#获取窗口焦点
win32gui.SetForegroundWindow(Main)

#快捷键F1 按下按键，再释放，这就是一次按键
win32api.keybd_event(112,0,0,0)
win32api.keybd_event(112,0,win32con.KEYEVENTF_KEYUP,0)

time.sleep(0.5)

Afxwnd = win32gui.GetDlgItem(Main,59648)

#买入的frame
FrameBuy = win32gui.GetDlgItem(Afxwnd,59649)

win32gui.SetForegroundWindow(FrameBuy)

B_refresh = win32gui.GetDlgItem(FrameBuy, 32790)  # 刷新持仓按钮

F_Bhexin = win32gui.GetDlgItem(FrameBuy, 1047)  # 持仓显示框架
F_Bhexinsub = win32gui.GetDlgItem(F_Bhexin, 200)  # 持仓显示框架

G_position = win32gui.GetDlgItem(F_Bhexinsub, 1047)  # 持仓列表

#按键W，显示持仓
win32api.keybd_event(87,0,0,0)
win32api.keybd_event(87,0,win32con.KEYEVENTF_KEYUP,0)

win32gui.SendMessage(B_refresh, win32con.BM_CLICK, None, None)  # 刷新持仓

time.sleep(0.2)
win32gui.SetForegroundWindow(G_position)
time.sleep(0.1)
position = []
data = get_clipboard()
for i in range(1, int((len(data)-14)/14)+1):
    item = data[14*i:14*(i+1)]
    position.append(item)
df = pd.DataFrame(position, columns=data[:14])

print df

#TODO  
pass



'''
数据样式：
               证券代码    证券名称  股票余额   可用余额 参考盈亏    参考成本价 参考盈亏比例(%)      市价      市值  资讯
0       600148  长春一东    500  500  525.260    26.359   3.987  27.410   
1    0  600561  江西长运    100  100   75.940    14.280   5.322  15.040   
2    0  000785  武汉中商    900  900  210.060    14.697   1.585  14.930   
3    0  150176   H股B  18700    0  -15.500     0.799  -0.125   0.798   
4    0  300125   易世达    200  200  128.920    32.255   2.000  32.900   
5    0  300214  日科化学    200  200   67.730     8.501   3.988   8.840   


c.2使用numpy.where

df=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8],"C":[1,1,1,1]})
df["then"]=np.where(df.A<3,1,0)
print df

.根据条件选择取DataFrame
df=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8],"C":[1,1,1,1]})
df=df[df.A>=2]
print df
'''

