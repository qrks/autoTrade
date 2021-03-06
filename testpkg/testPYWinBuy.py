#coding:utf-8
'''
pywin32测试
'''
import time
import win32ui,win32con,pythoncom,win32gui,win32api
import ref1 as ref

def show_windows(hWndList):  
    for h in hWndList:  
        show_window_attr(h)  
        
def gbk2utf8(s):  
    return s.decode('gbk').encode('utf-8')  

def show_window_attr(hWnd):  
    ''''' 
    显示窗口的属性 
    :return: 
    '''  
    if not hWnd:  
        return  
  
    #中文系统默认title是gb2312的编码  
    title = win32gui.GetWindowText(hWnd)  
    title = gbk2utf8(title)  
    clsname = win32gui.GetClassName(hWnd)  
  
    print '窗口句柄:%s ' % (hWnd)  
    print '窗口标题:%s' % (title)  
    print '窗口类名:%s' % (clsname)  
    print '' 



wdname1=u'网上股票交易系统5.0'
print(wdname1)
Main=win32gui.FindWindow(0,wdname1)

#print(Main)

# w2 = win32gui.FindWindowEx(w1hd,0,'AfxMDIFrame42s',None)
# show_window_attr(w2)

# w3 = win32gui.FindWindowEx(w2,0,u'#32770 (对话框)',None)
# print(w3)
# show_window_attr(w3)

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

#买入的股票代码框
buyEdit = win32gui.GetDlgItem(FrameBuy,1032)

#买入价格框
buyPriceEdit = win32gui.GetDlgItem(FrameBuy,1033)

#买入数量框
buyVolEdit = win32gui.GetDlgItem(FrameBuy,1034)

#买入按钮 1006
buyButton = win32gui.GetDlgItem(FrameBuy,1006)

stock_code = '150100'
price = '1.00'
price = float(price) * 1.01
price = str("%.2f"%price)
vol = '100'

ref.setEditText(buyEdit,stock_code)
ref.setEditText(buyPriceEdit,price)
ref.setEditText(buyVolEdit,vol)
ref.clickButton(buyButton)


