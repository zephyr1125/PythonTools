import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

#需求
#检查指定文件夹下(包括子文件夹)所有文件的GUID
#统计在目标文件夹内的引用次数，从少到多排序
#结束显示里要包括受检查的文件名、引用次数、引用了的文件名

#UI


def ChooseFolder():
    dirPath.set(filedialog.askdirectory())

#选择来源文件夹与目标文件夹
root  = Tk()
root.title("检查GUID")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

dirPath = StringVar()
ttk.Button(mainframe, text="选择源文件夹", command=ChooseFolder).grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, textvariable=dirPath).grid(column=2, row=1, sticky=E)

root.mainloop()
