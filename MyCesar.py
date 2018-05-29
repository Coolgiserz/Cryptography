#!/usr/bin/python
#coding:utf-8
lalphalist = []
halphalist = []
string=''
for i in range(26):
    string += chr(i+97)
lalphalist = list(string)
halphalist = list(string.upper())
# print lalphalist
# print string
# print halphalist
def cesarencode(text,offset):
    '''
        凯撒密码：
            参数：
            text：明文
            offset：偏移量
    '''
    result = ""
    for ch in text:
        if ch.isupper():
            result = result+ halphalist[((halphalist.index(ch)+offset)%26)]
        elif ch.islower():
            result = result+ lalphalist[((lalphalist.index(ch)+offset)%26)]
        elif ch.isdigit():
            result+ch
        else:
            result=result+ch
    
    return result

def cesardecode(ciper,offset):
    '''
        凯撒密码：
            参数：
            ciper：密文
            offset：偏移量
    '''
    result = ""
    for ch in ciper:
        if ch.isupper():
            result = result+halphalist[((halphalist.index(ch)-offset)%26)]
        elif ch.islower():
            result = result+lalphalist[((lalphalist.index(ch)-offset)%26)]
        elif ch.isdigit():
            result+ch
        else:
            result=result+ch
    
    return result
def bfprintallresult1(text):
    '''
        打印25种可能结果
    '''
    for i in range(len(lalphalist)):
        order = 'ROT'+str(i)+': '
        print order,cesarencode(text,i)

def bfprintallresult2(ciper):
    '''
        打印25种可能结果
    '''
    for i in range(len(lalphalist)):
        order = 'ROT'+str(i)+': '
        print order,cesardecode(ciper,i)

def main():
    choice = input('Wanna encode? choose1.Wanna decode? choose2:')
    if int(choice)==1:
        text = input('Input Cesar Text:')
        bfprintallresult1(text)
    else:
        ciper = input('Input Cesar Ciper:')
        bfprintallresult2(ciper)

main()
