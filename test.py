import xlsxwriter
work = xlsxwriter.Workbook('new.xlsx')
worksheet = work.add_worksheet()

work.close()