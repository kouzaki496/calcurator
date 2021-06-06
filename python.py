import tkinter as tk
from tkinter import ttk

buttonList = [
    ['', 'B', 'C', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['00', '0', '.', '=']
]

operators = ['+', '-', '*', '/']
numbers = ['1','2','3','4','5','6','7','8','9','0']

class calculator(object):
    def __init__(self, app=None):
        # Define
        self.calcStr = '' # 計算用の文字列

        # MainWindowを作成
        app.title('でんたく') # Window のタイトル
        app.geometry('300x470') # Window のサイズ
        # app.configure(bg='#ffffff')


        # 電卓のFrameを作成
        mainFrame = ttk.Frame(app, width=300, height=50) # 計算式と結果用のFrame
        mainFrame.propagate(False) # サイズが固定される
        mainFrame.pack(side=tk.TOP, padx=10, pady=20) # 余白の設定
        #計算ボタンのFrameを作成
        buttonFrame = ttk.Frame(app, width=300, height=400) # 計算ボタン用のFrame
        buttonFrame.propagate(False) # サイズが固定される
        buttonFrame.pack(side=tk.BOTTOM) # 余白の設定

        # Labelを配置
        self.calcVar = tk.StringVar() # 計算式用の動的変数
        self.answerVar = tk.StringVar() # 結果用の動的変数
        calcLabel = tk.Label(mainFrame, textvariable=self.calcVar, font=("",15)) # 計算式のLabel
        resultLabel = tk.Label(mainFrame, textvariable=self.answerVar, font=("",20)) # 計算結果のLabel
        calcLabel.pack(anchor=tk.E) # 右揃えで配置
        resultLabel.pack(anchor=tk.E) # 右揃えで配置

        #Buttonを配置
        for y, row in enumerate(buttonList, 1): 
            for x, num in enumerate(row):
                button = tk.Button(buttonFrame, text=num, font=('', 15), width=6, height=3)
                button.grid(row=y, column=x) # 列や行を指定して配置
                button.bind('<Button-1>', self.clickButton) # Buttonが押された場合

        button['fg'] = '#FF4500'


    #Buttonが押下された時の処理を定義する
    def clickButton(self, event):
        check = event.widget['text'] # 押したボタンのCheck

        if check == '=':
            if self.calcStr[-1:] in operators: # SYMBOLが押下された場合、SYMBOLの手前を計算
                self.calcStr = self.calcStr[:-1]

            res = '= ' + str(eval(self.calcStr)) #計算処理
            self.answerVar.set(res)
        elif check == 'B': # 一個もどす
            self.calcStr = self.calcStr[:-1]
        elif check == 'C': # 全部消去
            self.calcStr = ''
            self.answerVar.set('')
        elif check in operators: # 記号の場合
            if self.calcStr[-1:] not in operators and self.calcStr[-1:] != '':
                self.calcStr += check
            elif self.calcStr[-1:] in operators: # 記号の場合、入れ替える
                self.calcStr = self.calcStr[:-1] + check
        else: # 数字などの場合
            self.calcStr += check

        self.calcVar.set(self.calcStr)
    


def main():
    # Window Setting
    app = tk.Tk()
    # Window size non resizable
    app.resizable(width=False, height=False)
    calculator(app)
    # Display
    app.mainloop() # Window をループで回すことで Widgit に対応できるようになる

if __name__ == '__main__':
    main()