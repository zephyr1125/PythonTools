import openpyxl, requests, bs4, threading
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def ExcelToWeb():
    websites = []
    titles = []
    # 1. fetch websites from excel
    wb = openpyxl.load_workbook(dirPath.get())
    sheet = wb.get_sheet_by_name('Sheet1')

    for row in range(2, sheet.max_row + 1):
        websites = websites + [sheet['A' + str(row)].value]

    # 2. visit all the websites

    for site in websites:
        try:
            progress.set(site)
            r = requests.get(site)
            soup = BeautifulSoup(r.text.encode(r.encoding), "html.parser")
            titles = titles + [soup.title.string]
        except:
            titles = titles + ['error']

    # 3. write back to excel

    for i, title in enumerate(titles):
        sheet['C'+str(i+2)].value = title
    wb.save(dirPath.get())
    progress.set('完成')

def ChooseFile():
    dirPath.set(filedialog.askopenfilename())

def ThreadWork():
    t = threading.Thread(target=ExcelToWeb)
    t.setDaemon(True)
    t.start()

root  = Tk()
root.title("Excel工具")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

dirPath = StringVar()
progress = StringVar()
ttk.Button(mainframe, text="选择文件", command=ChooseFile).grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, textvariable=dirPath).grid(column=2, row=1, sticky=E)
ttk.Label(mainframe, text="注意：必须为.xlsx文件").grid(column=1, row=2, sticky=W)
ttk.Button(mainframe, text="开始", command=ThreadWork).grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, textvariable=progress).grid(column=1, row=4, sticky=W, columnspan=3)

root.mainloop()
