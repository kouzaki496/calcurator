#ライブラリのインポート
import tkinter as tk
from tkinter import Frame, Label, ttk

LAYOUT = [
    ['', 'C', 'AC', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '00', '.', '=']
]

calc_SYMBOL = ['+', '-', '*', '/']  #数字以外の記号をまとめて定義しておく
numbers = ['1','2','3','4','5','6','7','8','9','0'] #いらない?

class calculator(ttk.Frame):
    def __init__(self, master=None):
        self.calc_str = '' # 計算用の文字列
    #     self.createStyle()

    # def createStyle(self):
    #   style = ttk.Style()
    #   style.configure('TLabel', font=('Helvetica', 20), background='black', foreground='white')

        # MainWindowを作成
        master.title('けーさんき')
        master.geometry('300x470') # MainWindow のサイズを設定する（geometry）
        # app.configure(bg='black')


        # Frameを作成
        main_frame = ttk.Frame(master, width=300, height=50) # ディスプレイのFrame
        main_frame.propagate(False) #レスポンシブなし
        button_frame = ttk.Frame(master, width=300, height=400) # 計算ボタン用のFrame
        button_frame.propagate(False) #レスポンシブなし

        #作成したFrameを配置（pack）
        main_frame.pack(side=tk.TOP, padx=10, pady=20) #padxはWidget外側の横余白　padyはWidget外側の縦余白
        button_frame.pack(side=tk.BOTTOM)



        #Buttonを配置 LAYOUTからforループで取り出して配置していく
        for y, row in enumerate(LAYOUT, 1): 
            for x, num in enumerate(row):
                button = tk.Button(button_frame, text=num, font=('', 15), width=6, height=3)
                button['bg'] = '#161666'
                button['fg'] = '#ffffff'
                button.grid(row=y, column=x)
                button.bind('<1>', self.press_button) 

        button['bg'] = '#86b8eb' #要修正
        button['fg'] = 'black'

        # 計算式と計算結果の表示用Labelを作成、配置
        self.calc_var = tk.StringVar() # 計算式を格納する変数
        self.answer_var = tk.StringVar() # 結果を格納する変数
        self.answer_var.set('0') #計算結果の初期値を設定する
        calc_label = tk.Label(main_frame, textvariable=self.calc_var, font=("",15)) # 計算式のLabel
        result_label = tk.Label(main_frame, textvariable=self.answer_var, font=("",22)) # 計算結果のLabel
        calc_label.pack(anchor="e") #eはeast　つまり右寄せ
        result_label.pack(anchor="e")


    #Buttonが押下された時の処理を定義する
    def press_button(self, event):
        check = event.widget['text'] # 押したボタンのCheck

        if check == '=':
            if self.calc_str[-1:] in calc_SYMBOL:
                self.calc_str = self.calc_str[:-1]

            res = '= ' + str(eval(self.calc_str)) #計算処理
            self.answer_var.set(res)
        elif check == 'C': # backspace
            self.calc_str = self.calc_str[:-1]
        elif check == 'AC': # clear
            self.calc_str = ''
            self.answer_var.set('')
            self.answer_var.set('0')

        elif check in calc_SYMBOL: # 記号の場合
            if self.calc_str[-1:] not in calc_SYMBOL and self.calc_str[-1:] != '':
                self.calc_str += check
            elif self.calc_str[-1:] in calc_SYMBOL:
                self.calc_str = self.calc_str[:-1] + check
        else:
            self.calc_str += check

        self.calc_var.set(self.calc_str)
    


def main():
    app = tk.Tk()
    app.resizable(width=False, height=False) #Windowを固定サイズにする
    calculator(app)
    app.mainloop()

if __name__ == '__main__':
    main()