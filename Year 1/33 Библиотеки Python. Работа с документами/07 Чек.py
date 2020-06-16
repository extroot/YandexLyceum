import xlsxwriter


def export_check(text):
    workbook = xlsxwriter.Workbook('res.xlsx')
    worksheet = workbook.add_worksheet()
    text = text.split('\n')
    for i in range(len(text)):
        item, price, count = text[i].split('\t')
        worksheet.write(i, 0, item)
        worksheet.write(i, 1, int(price))
        worksheet.write(i, 2, int(count))
        worksheet.write(i, 3, int(count) * int(price))
        worksheet.write(i, 3, f'=B{i + 1}*C{i + 1}')
    worksheet.write(len(text), 0, 'Итого')
    worksheet.write(len(text), 3, f'=SUM(D1:D{len(text)})')
    workbook.close()
