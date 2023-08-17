import tkinter as tk
root= tk.Tk()


# copy right PythonKing, can use only in your products not allowed developer or own for selling another version of this library without permession

#important to pass the async arugment (event_target_prop) within the drawing loop, that used latter in the callback any time in app lifetime
from functools import partial
# called the ez grid tkinter py
index = 0
btns = {}
dic = {}
# this dynamic function can draw any number of grid, in html grid is max 12 but here grid max unlimted contrled with width, height you as native match use the valid height, w=width/2, width=50, this how size handled can accept all sizes fit with cells, and cols, and add dynamic custom callback using partials you control, it and get the event listener target class in your cb !!before simplest way to draw grid unlimited rows, col3 , cols can automated to
def dynamicGridDraw(total_rows=3, total_col=3, width=75, h=0, height=50, clickCB=lambda: None):
    global index
    global btns
    # me and html grid reached same consipet must be max size for rows in the grid, currently is 3 max you can have from unlimit rows, and until 3 max cells , can be 1,2,3,0, in future will increased to 12 but unlike grid 12 and unlimited rows
    # next level control the canvas height and width to fit dynamic shape, sure for tkinter must be limit, or make size very small but require math to know the valid arugment 25, 50 for height
    canvas1 = tk.Canvas(root, width = width*3, height = (h*total_rows)+h, scrollregion=(0,0,0,int((h*total_rows)+h)))

    table_frame = tk.Frame(canvas1, pady=10, padx=5, background="yellow")
    vsb = tk.Scrollbar(root, orient="vertical", command=canvas1.yview, )
    canvas1.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas1.pack(side="top", fill="both", expand=True)
    canvas1.create_window((4,4), window=table_frame, anchor="nw")
    
    #canvas1.pack()
    for r in range(total_rows):        
        for i in range(total_col):
            if i == 0:
                rc_string = 'row{}-{}'.format(r, i)
                button1 = tk.Button(text='', command=partial(clickCB,rc_string), bg='brown',fg='white', font=('helvetica', 15, 'bold'))                
                btns[rc_string] = {'target': button1, 'row': r, 'col': i, 'w': width/2, 'h': h, 'width': width, 'height': height}
                canvas1.create_window(int(width/2), h, window=button1, width=width, height=height)
                # w
            if i == 1:
                rc_string = 'row{}-{}'.format(r, i)
                button1 = tk.Button(text='', command=partial(clickCB,rc_string), bg='brown',fg='white', font=('helvetica', 15, 'bold'))
                btns[rc_string] = {'target': button1, 'row': r, 'col': i, 'w': width/2, 'h': h, 'width': width, 'height': height}
                canvas1.create_window(int(width/2)*3, h, window=button1, width=width, height=height)
                # w * 3
            if i == 2:
                rc_string = 'row{}-{}'.format(r, i)
                #must int as python deep match so will return bigger numb /2 and in multiple 2 int good, also tkinter need simple 1 , 1,22
                button1 = tk.Button(text='', command=partial(clickCB,rc_string), bg='brown',fg='white', font=('helvetica', 15, 'bold'))                
                btns[rc_string] = {'target': button1, 'row': r, 'col': i, 'w': width/2, 'h': h, 'width': width, 'height': height}
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


dynamicGridDraw(total_rows=20, total_col=3, width=75, h=50, height=50, clickCB=clickEventListener)
root.mainloop()
