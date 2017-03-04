#!/usr/bin/python
#-*-coding:utf-8-*-

class HtmlTable(object):
    
    def __init__(self,title='',data=None):
        self.title=title
        self.table=[]
        if data:
            self.setData(data)
        
    def setData(self,data):
        self.table=[]
        for row_i,row in enumerate(data):
            r=[]
            for col_i,item in enumerate(row):
                r.append({'data':item,'style':'','pos':(row_i,col_i)})
            self.table.append(r)
        
    def setTitle(self,title):
        self.title=title
        
    def getHtml(self):
        rv=r'<h1>{}</h1>'.format(self.title)
        rv+=r'''<table border="1" cellspacing="0" cellpadding="0" 
            style="border-collapse: collapse;border-width:0px;text-align: center;">'''
        for row in self.table:
            rv+=r'<tr>'
            for item in row:
                rv+=r'<td'
                if item['style']:
                    rv+=r''' style="{}"'''.format(item['style'])
                rv+=r'>'    
                rv+=str(item['data'])
                rv+=r'</td>'
            rv+=r'</tr>'
        return rv+r'</table>'
            
    def setStyleByRule(self,fn1,fn2):
        for row in self.table:
            for item in row:
                if fn1(item):
                    item['style']+=fn2(item)+';'
    def setStyleByPos(self,row,col,style):
        self.table[row][col]['style']+=style+';'

