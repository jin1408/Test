import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        self.sandwidth = StringVar()
        self.cake = StringVar()
        window.title("고객: " + self.name)
        window.geometry('350x200')
        Label(window, text="샌드위치 (5000원)").grid(column=0, row=0)
        Label(window, text="케이크 (20000원)").grid(column=0, row=1)
        Entry(window, textvariable=self.sandwidth).grid(row=0, column=1, padx=10, pady=10)
        Entry(window, textvariable=self.cake).grid(row=1, column=1, padx=10, pady=10)
        Button(window, text="주문하기", command=self.send_order).grid(row=2, column=0, padx=10, pady=10)

    def send_order(self):
        a = self.sandwidth.get()
        b = self.cake.get()

        if (int(a) ==0 or int(a) < 0 or a == " " or  a.isalpha()) and (int(b) ==0 or int(b) < 0 or b == " " or  b.isalpha()):
            order_text = " "
            print("1")
        elif int(a) ==0 or int(a) < 0 or a == " " or  a.isalpha():
            order_text = self.name + ": 케이크(20000원) " + b + "개"
            print("@")
        elif int(b) ==0 or int(b) < 0 or b == " " or  b.isalpha():
            order_text = self.name + ": 샌드위치(5000원) " + a + "개"
        else:
            order_text = self.name + ": 샌드위치(5000원) " + a + "개, 케이크(20000원) " + b + "개"


        self.bakeryView.add_order(order_text)


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
