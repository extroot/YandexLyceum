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


export_check("""товар 1\t100\t5
товар 2\t200\t6
товар 3\t7\t500""")

def export_check(text):
    workbook = xlsxwriter.Workbook('res.xlsx')
    text = text.split("---")
    for check in text:
        res = {}
        worksheet = workbook.add_worksheet()
        for data_row in check.split("\n"):
            if not data_row.strip():
                continue
            item, price, count = data_row.strip().split("\t")
            price = float(price)
            count = int(count)
            res[(item, price)] = res.get((item, price), 0) + count
        for i, data_row in enumerate(sorted(res.keys(), key=lambda x: x[0])):
            worksheet.write(i, 0, data_row[0])
            worksheet.write(i, 1, int(data_row[1]))
            worksheet.write(i, 2, int(res[data_row]))
            worksheet.write(i, 3, f'=B{i + 1}*C{i + 1}')
        worksheet.write(i + 1, 0, "Итого")
        worksheet.write(i + 1, 3, f'=SUM(D1:D{len(res)})')
    workbook.close()
