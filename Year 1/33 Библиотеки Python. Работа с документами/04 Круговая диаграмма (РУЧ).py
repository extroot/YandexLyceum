import sys
import xlsxwriter

data = [(x[0], int(x[1])) for x in list(map(str.split, sys.stdin))]

workbook = xlsxwriter.Workbook('res.xlsx')
worksheet = workbook.add_worksheet()

for row, (item, price) in enumerate(data):
    worksheet.write(row, 0, item)
    worksheet.write(row, 1, price)


chart = workbook.add_chart({'type': 'pie'})
chart.add_series({
    'categories': f'=Sheet1!A1:A{len(data)}',
    'values': f'=Sheet1!B1:B{len(data)}',
})
worksheet.insert_chart('C3', chart)
workbook.close()
