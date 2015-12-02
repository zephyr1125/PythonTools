import openpyxl, requests, bs4
from bs4 import BeautifulSoup

# 1. fetch websites from excel

path = 'ExcelToWebsite\\example.xlsx'
websites = []
titles = []

wb = openpyxl.load_workbook(path)
sheet = wb.get_sheet_by_name('Sheet1')

for row in range(2, sheet.max_row + 1):
    websites = websites + [sheet['A' + str(row)].value]

# 2. visit all the websites

for site in websites:
    try:
        print(site)
        r = requests.get(site)
        print(r.encoding)
        soup = BeautifulSoup(r.text.encode(r.encoding), "html.parser")
        titles = titles + [soup.title.string]
    except:
        titles = titles + ['error']


# 3. write back to excel

for i, title in enumerate(titles):
    sheet['C'+str(i+2)].value = title
wb.save(path)
