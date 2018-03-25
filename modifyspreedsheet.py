import xlsx

def addDate(date):

    workbook = xlsx.Workbook('plan.xlsx')

    for worksheet in workbook:

        print(worksheet.name)
        worksheet['A1']=100

    workbook.close()



