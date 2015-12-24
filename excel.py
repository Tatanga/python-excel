#!/usr/bin/env python
# encoding: utf-8

fix_encoding = lambda s: s.decode('utf8')

import xlwt
import   MySQLdb
wbk=xlwt.Workbook()

sheet=wbk.add_sheet('sheet 1')

sheet.write(0,0,'galore_name')
sheet.write(0,1,'username')
sheet.write(0,2,'tel')
sheet.write(0,3,'addr')
sheet.write(0,4,'create_at')

conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='mydb1', charset='utf8')

cursor=conn.cursor()
cursor.execute('select galore_name,name,mobile,addr,create_at from cash_event')

row=1
#for galore_name,username,tel,addr,create_at in cursor.fetchall():
for galore_name,username,tel,addr,create_at in cursor.fetchall():
    sheet.write(row, 0, fix_encoding(galore_name))
    sheet.write(row, 1, fix_encoding(username))
    sheet.write(row, 2, fix_encoding(tel))
    sheet.write(row, 3, fix_encoding(addr))
    sheet.write(row, 4, create_at)
    print row
    row+=1

wbk.save(u'cash.xls')
cursor.close()
conn.commit()
conn.close()