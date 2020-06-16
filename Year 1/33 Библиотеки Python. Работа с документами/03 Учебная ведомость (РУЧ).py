from docxtpl import DocxTemplate


def create_training_sheet(class_name, subject_name, tpl_name, *tups):
    doc = DocxTemplate(tpl_name)
    marks = []
    tups = sorted(tups, key=lambda x: x[0])
    for i in range(len(tups)):
        marks.append({"num": i + 1, "fio": tups[i][0], "mark": tups[i][1]})
    context = {
        'class_name': class_name,
        'subject_name': subject_name,
        'marks': marks
    }
    doc.render(context)
    doc.save("res.docx")
