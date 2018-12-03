#!/usr/bin/python
from tkinter import *
import time
#函式:ConsoleScreen()-控制畫面
def ConsoleScreen():
    #函式:PrintLine()-輸出文字
    def PrintLine():
       #設定字型大小(螢幕寬度/句子長度)
       #用判斷式決定字型大小(如果句子長度為0,預設為1):可擴充
        if len(Input.get())>0:
            font_size=2000 // len(Input.get()) // 2
        else:
            font_size=1
        #變更Output的內容
        Output.config(text= Input.get(),font=("Noto Sans Mono CJK TC Bold", font_size))
        #每200毫秒重新呼叫自己一次來更新
        Output.after(200,PrintLine)
    #函式:ccleaner()-清除畫面
    def ccleaner():
        #刪除輸出的訊息
        Output.config(text= "")
        #刪除輸入方塊的字串(0到END)
        Input.delete(0,END)
    #函式: SaySomething()-預設字詞
    def SaySomething(yee):
        #先清空內容
        ccleaner()
        #仿Switch用法
            #擴充方式 i:lambda:Input.insert(0,""),
        {
            0:lambda: Input.insert(0,"時間快到了"),
            1:lambda: Input.insert(0,"快!收尾!!"),
            2:lambda: Input.insert(0,"抽獎時間"),
            3:lambda: Input.insert(0,"公佈投票結果"),
            4:lambda: Input.insert(0,"我的王之力啊啊"),
            5:lambda: Input.insert(0,"你渴望力量嗎?"),
            6:lambda: Input.insert(0,"やらないか"),
            7:lambda: Input.insert(0,"すっごーい！"),
            8:lambda: Input.insert(0,".........."),
            9:lambda: Input.insert(0,"The!World!!"),
            10:lambda: Input.insert(0,"たーのしー！"),
            11:lambda: Input.insert(0,"夏亞，你算計我！"),
            
            }.get(yee,lambda: Input.insert(0,"default"))()
        #輸出文字
        PrintLine()
    #函式:Adios()-關閉程式
    def Adios():
        exit(0)
    #建立控制畫面(SLG)物件    
    SLG=Tk()
    #視窗標題
    SLG.title("主控台")
    #視窗大小
    SLG.geometry('550x135')
    #提示文字:請輸入要顯示的文字
    Label(SLG,text="請輸入要顯示的文字:",font=48,width="20", height="3", fg="blue").grid(row=0)
    #生成輸入方塊
    Input = Entry(SLG)
    #輸入方塊顯示位置
    Input.grid(row=0, column=1,padx=10,sticky=W)
    #顯示畫面的訊息:font(字體,字型大小)
    
    Output = Label(SIK,text="預設顯示",font=("Noto Sans Mono CJK TC Bold",150),fg="white",bg="black")
    #顯示畫面的訊息位置
    Output.grid(row=1,sticky=N,padx=20)
    #輸入方塊與<ENTER>鍵和函式:<PrintLine()>連結
    Input.bind('<Return>', (lambda event: PrintLine()))
    #預設關鍵詞:擴充式
    Show=Label(SLG,text="F1:時間快到了，F2:快!收尾!!，F3:抽獎時間，F4:公佈投票結果，F5:"+'\n'+"F6:，F7:，F8:，F9:，F10:，F11:，F12:",fg="blue").grid(row=1,columnspan=3,sticky=N,padx=20)
    SLG.bind('<F1>',(lambda event: SaySomething(0)))
    SLG.bind('<F2>',(lambda event: SaySomething(1)))
    SLG.bind('<F3>',(lambda event: SaySomething(2)))
    SLG.bind('<F4>',(lambda event: SaySomething(3)))
    SLG.bind('<F5>',(lambda event: SaySomething(4)))
    SLG.bind('<F6>',(lambda event: SaySomething(5)))
    SLG.bind('<F7>',(lambda event: SaySomething(6)))
    SLG.bind('<F8>',(lambda event: SaySomething(7)))
    SLG.bind('<F9>',(lambda event: SaySomething(8)))
    SLG.bind('<F10>',(lambda event: SaySomething(9)))
    SLG.bind('<F11>',(lambda event: SaySomething(10)))
    SLG.bind('<F12>',(lambda event: SaySomething(11)))
    #一鍵清除按鈕
    Clear=Button(SLG, text="一鍵清除",command=ccleaner).grid(row=2,column=1,padx=20,pady=0,sticky=W+E+N+S)
    #逃生出口按鈕
    #Button(SLG,text="EXIT",command=函式)
    Exit=Label(SLG, text="按ESC退出",fg="blue").grid(row=2,column=0,padx=20,sticky=W)
    SLG.bind('<Escape>',(lambda event: Adios()))
    #必要
    SLG.mainloop()
#函式:tick()-顯示時間
def tick():
    #從PC上取得正確時間
    time2 = time.strftime('%H : %M : %S')
    # 如果時間變動就更新
    clock.config(text=time2)
    #每200毫秒重新呼叫自己一次
    #來更新顯示時間
    #可以依需要調整大於200,但不建議
    clock.after(200, tick)
#建立顯示畫面
SIK=Tk()
#視窗大小:全螢幕
SIK.attributes('-fullscreen', True)
#視窗大小:全螢幕(備用)
#SIK.state('zoomed')
#設定背景顏色:黑色
SIK.configure(background="black")
#設一變數為螢幕寬度
screen_width = int(SIK.winfo_screenwidth())
#顯示時間
clock = Label(SIK, font=("Segoe UI Bold", 100), fg="yellow",bg="black")
#時間顯示位置
clock.grid(row=0)
#呼叫顯示時間函式
tick()
#呼叫控制畫面函式
ConsoleScreen()
#必要
SIK.mainloop()
