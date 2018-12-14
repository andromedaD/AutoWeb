#_*_coding:utf-8_*_

import xlrd
def open_xls(file='file.xls'):#解析excel文件
    try:
        data=xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))
def xls_by_index(file='file.xls',colnameindex=0,by_index=0):
    data=open_xls(file)
    table=data.sheets()[by_index]
    nrows=table.nrows
    ncols=table.ncols
    colnametable=table.row_values(colnameindex)
    list = []
    for rownum in range(1,nrows):
        row=table.row_values(rownum)

        if row:
            app={}
            for i in range(len(colnametable)):

                app[colnametable[i]]=row[i]
            list.append(app)
    return list

def main():
    lists=xls_by_index()
    for list in lists:
        print(list)


lists=xls_by_index()
# print(lists)
print(int(lists[0]['password']))


# if __name__ == '__main__':
#     main()