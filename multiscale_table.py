#!/usr/bin/python
#-*-coding:utf-8-*-
from htmltab import HtmlTable

DATA_FILE=r'data.txt'
OUT_FILE=r'tables.html'
COLOR_TABLE=('white','cyan','blue','lightblue','purple','yellow','magenta','lime','olive','green','orange')


def isDigitLine(line):
    items=line.split(' ')
    for i in items:
        if not i.isdigit():
            return False
    return True
    
def readFile(file_name):
    with open(file_name) as f:
        return [line.strip() for line in f.readlines() if not line.isspace()]
        
def getBlocks(lines):
    blocks=[]
    l=len(lines)
    i=0
    while i<l:
        if not isDigitLine(lines[i]):
            label=lines[i]
            data=[]
            i+=1
            while (i<l and isDigitLine(lines[i])):
                data.append(lines[i].split(' '))
                i+=1
            blocks.append((label,data))
            i-=1
        i+=1
    return blocks

def test():
    lines=readFile(DATA_FILE)
    blocks=getBlocks(lines)
    seed1_row=13
    seed1_col=2
    seed2_row=2
    seed2_col=13
    with open(OUT_FILE,'w') as f:
        for i,blk in enumerate(blocks):
            table=HtmlTable(title=blk[0],data=blk[1])
            table.setStyleByRule(lambda i: True,lambda i:'width:20px;height:20px')
            if i in (0,2,8,14):
                table.setStyleByRule(lambda i:i['data']=='1',lambda i: 'background-color:{}'.format(COLOR_TABLE[1]))
                table.setStyleByPos(seed1_row,seed1_col,'background-color:red')
                table.setStyleByPos(seed2_row,seed2_col,'background-color:green')
                seed1_col/=2
                seed1_row/=2
                seed2_col/=2
                seed2_row/=2
            else:
                table.setStyleByRule(lambda i: i['data'].isdigit(),lambda i:'background-color:{}'.format(COLOR_TABLE[min(int(i['data']),10)]))
            f.write(table.getHtml())    
            
if __name__=='__main__':
    test()
           
