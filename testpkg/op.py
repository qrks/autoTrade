#coding:utf-8

import win32con,win32gui,win32api
import ref1 as ref
import time

bigtitle = u'网上股票交易系统5.0'

def pressChar(char):
    win32api.keybd_event(char,0,0,0);
    win32api.keybd_event(char,0,win32con.KEYEVENTF_KEYUP,0);

#按键方式买入
def buy_stock_key(stock_code,buy_price,buy_vol):
    
    w1hd=win32gui.FindWindow(0,bigtitle)
    
    #获取窗口焦点
    win32gui.SetForegroundWindow(w1hd)
    
    #快捷键F1 按下按键，再释放，这就是一次按键
    win32api.keybd_event(112,0,0,0)
    win32api.keybd_event(112,0,win32con.KEYEVENTF_KEYUP,0)
    
    for i in range(len(stock_code)):
        pressChar(int(stock_code[i]) + 96)
    
    #tab
    pressChar(9)
    
    for i in range(len(buy_price)):
        if buy_price[i] == '.':
            pressChar(110)
        else:
            pressChar(int(buy_price[i]) + 96)
    
    #tab
    pressChar(9)
    
    for i in range(len(buy_vol)):
        pressChar(int(buy_vol[i]) + 96)
        
    #按键B，买入
    win32api.keybd_event(66,0,0,0);
    win32api.keybd_event(66,0,win32con.KEYEVENTF_KEYUP,0);
    
#按键方式卖出
def sell_stock_key(stock_code,buy_price,buy_vol):
    
    w1hd=win32gui.FindWindow(0,bigtitle)
    
    #获取窗口焦点
    win32gui.SetForegroundWindow(w1hd)
    
    #快捷键F2 按下按键，再释放，这就是一次按键
    win32api.keybd_event(113,0,0,0)
    win32api.keybd_event(113,0,win32con.KEYEVENTF_KEYUP,0)
    
    for i in range(len(stock_code)):
        pressChar(int(stock_code[i]) + 96)
    
    #tab
    pressChar(9)
    
    for i in range(len(buy_price)):
        if buy_price[i] == '.':
            pressChar(110)
        else:
            pressChar(int(buy_price[i]) + 96)
    
    #tab
    pressChar(9)
    
    for i in range(len(buy_vol)):
        pressChar(int(buy_vol[i]) + 96)
        
    #按键B，卖出
    win32api.keybd_event(83,0,0,0);
    win32api.keybd_event(83,0,win32con.KEYEVENTF_KEYUP,0);
    
#获取句柄方式买入
def buy_stock(stock_code,buy_price,buy_vol):
    
    #先按下回车，防止有弹出窗口存在
    win32api.keybd_event(13,0,0,0)
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
    
    Main=win32gui.FindWindow(0,bigtitle)
    
    while Main == 0:
        print('to get Main!')
        Main=win32gui.FindWindow(0,bigtitle)
    
    #获取窗口焦点
    win32gui.SetForegroundWindow(Main)
    
    #快捷键F1 按下按键，再释放，这就是一次按键
    win32api.keybd_event(112,0,0,0)
    win32api.keybd_event(112,0,win32con.KEYEVENTF_KEYUP,0)
    
    time.sleep(0.3)
    
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
    
    price = float(buy_price) * 1.01
    price = str("%.2f"%price)
    
#     stock_code = '150100'
#     price = '1.00'
#     price = float(price) * 1.01
#     price = str("%.2f"%price)
#     buy_vol = '100'

    ref.setEditText(buyEdit,stock_code)
    ref.setEditText(buyPriceEdit,price)
    ref.setEditText(buyVolEdit,buy_vol)
    
#     B_refresh = win32gui.GetDlgItem(FrameBuy, 32790)  # 刷新持仓按钮
# 
#     win32gui.SendMessage(B_refresh, win32con.BM_CLICK, None, None)  # 刷新持仓
    
    time.sleep(0.3)
    
    ref.clickButton(buyButton)
    
    
    #获取上证还是深圳的下拉框  59392
#     toolbar = win32gui.GetDlgItem(Main,59392)
#     toolbardlg = win32gui.GetDlgItem(toolbar,0)
#     combo = win32gui.GetDlgItem(toolbardlg,1003)
#      
#     if stock_code.startswith('60'):
#         print('shanghai')
#         ref.selectComboboxItem(combo,0);
#     else:
#         print('shenzheng')
#         ref.selectComboboxItem(combo,1);
    
    #####################
    
    
   
#获取句柄方式卖出 
def sell_stock(stock_code,sell_price,sell_vol):
    
    #先按下回车，防止有弹出窗口存在
    win32api.keybd_event(13,0,0,0)
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
    
    Main=win32gui.FindWindow(0,bigtitle)
    while Main == 0:
        print('to get Main!')
        Main=win32gui.FindWindow(0,bigtitle)
    
    #获取窗口焦点
    win32gui.SetForegroundWindow(Main)
    
    #快捷键F2 按下按键，再释放，这就是一次按键
    win32api.keybd_event(113,0,0,0)
    win32api.keybd_event(113,0,win32con.KEYEVENTF_KEYUP,0)
    
    time.sleep(0.3)
    
    Afxwnd = win32gui.GetDlgItem(Main,59648)
    
    #买入的frame
    FrameSell = win32gui.GetDlgItem(Afxwnd,59649)
    
    win32gui.SetForegroundWindow(FrameSell)
    
    #卖出的股票代码框
    sellEdit = win32gui.GetDlgItem(FrameSell,1032)
    
    #卖出价格框
    sellPriceEdit = win32gui.GetDlgItem(FrameSell,1033)
    
    #卖出数量框
    sellVolEdit = win32gui.GetDlgItem(FrameSell,1034)
    
    #卖出按钮 1006
    sellButton = win32gui.GetDlgItem(FrameSell,1006)
    
    price = float(sell_price) * 0.99
    price = str("%.2f"%price)
    
    ref.setEditText(sellEdit,stock_code)
    ref.setEditText(sellPriceEdit,price)
    #默认卖出全部
#     ref.setEditText(sellVolEdit,sell_vol)
    
    time.sleep(0.3)
    ref.clickButton(sellButton)




    