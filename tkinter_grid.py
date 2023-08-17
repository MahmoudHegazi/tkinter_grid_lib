import tkinter as tk
root= tk.Tk()
# me and html grid reached same consipet must be max size for rows in the grid, currently is 3 max you can have from unlimit rows, and until 3 max cells , can be 1,2,3,0, in future will increased to 12 but unlike grid 12 and unlimited rows
# next level control the canvas height and width to fit dynamic shape, sure for tkinter must be limit, or make size very small but require math to know the valid arugment 25, 50 for height
canvas1 = tk.Canvas(root, width = 75*3, height = 900)
canvas1.pack()

# copy right PythonKing, can use only in your products not allowed developer or own for selling another version of this library without permession

#important to pass the async arugment (event_target_prop) within the drawing loop, that used latter in the callback any time in app lifetime
from functools import partial
# called the ez grid tkinter py
index = 0
btns = {}
dic = {}
# this dynamic function can draw any number of grid, in html grid is max 12 but here grid max unlimted contrled with width, height you as native match use the valid height, w=width/2, width=50, this how size handled can accept all sizes fit with cells, and cols, and add dynamic custom callback using partials you control, it and get the event listener target class in your cb
def dynamicGridDraw(total_rows=3, total_col=3, w=25, width=75, h=0, height=50, clickCB=lambda: None):
    global index
    global btns    
    for r in range(total_rows):        
        for i in range(total_col):      
            if i == 0:
                rc_string = 'row{}-{}'.format(r, i)
                button1 = tk.Button(text='X', command=partial(clickCB,rc_string), bg='brown',fg='white', font=('helvetica', 15, 'bold'))                
                btns[rc_string] = {'target': button1, 'r': r, 'i': i, 'w': width/2, 'h': h, 'width': width, 'height': height}
                canvas1.create_window(int(width/2), h, window=button1, width=width, height=height)
                # w
            if i == 1:
                rc_string = 'row{}-{}'.format(r, i)
                button1 = tk.Button(text='O', command=partial(clickCB,rc_string), bg='brown',fg='white', font=('helvetica', 15, 'bold'))
                btns[rc_string] = {'target': button1, 'r': r, 'i': i, 'w': width/2, 'h': h, 'width': width, 'height': height}
                canvas1.create_window(int(width/2)*3, h, window=button1, width=width, height=height)
                # w * 3
            if i == 2:
                rc_string = 'row{}-{}'.format(r, i)
                #must int as python deep match so will return bigger numb /2 and in multiple 2 int good, also tkinter need simple 1 , 1,22
                button1 = tk.Button(text='X', command=partial(clickCB,rc_string), bg='brown',fg='white', font=('helvetica', 15, 'bold'))                
                btns[rc_string] = {'target': button1, 'r': r, 'i': i, 'w': width/2, 'h': h, 'width': width, 'height': height}
                canvas1.create_window(int(width/2)*5, h, window=button1, width=width, height=height)
                # w * 5
            index += 1
        h += 50
    print('hello')
    print(dic)


def clickEventListener(rc_string):
    # the asynco part
    btns[rc_string]['target'].config(text='hi')
    print(btns[rc_string])


dynamicGridDraw(total_rows=23, total_col=3, w=3, width=75, h=50, height=50, clickCB=clickEventListener)
root.mainloop()
