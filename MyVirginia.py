#!usr/bin/python
#coding:utf-8

'''
    维吉利亚密码加密解密

'''

class MyVirginia():
    def __init__(self):
        self.text = ''
        self.key = ''
        self.ciper = ''
        self.tmpstr = ''
        self.uppermap = []
        self.lowermap = []

    def init_virginia(self):
        for i in range(26):
            self.tmpstr += chr(i+97)
        self.lowermap = list(self.tmpstr)
        self.uppermap = list(self.tmpstr.upper())

    def encode(self,text,key):
        self.text = text
        self.key = key
        klen = len(key)
        tlen = len(text)
        i = 0
        while(i<tlen):
            j = i%klen
            if key[j].isupper() and text[i].isupper():
                kindex = self.uppermap.index(key[j])
                tindex = self.uppermap.index(text[i])
                self.ciper += self.uppermap[(kindex+tindex)%26]

            elif key[j].islower() and text[i].islower():
                kindex = self.lowermap.index(key[j])
                tindex = self.lowermap.index(text[i])
                self.ciper += self.lowermap[(kindex+tindex)%26]
            i+=1
        print '维吉尼亚密码：'+self.ciper


api = MyVirginia()
api.init_virginia()
text = input('Input the text that will be encrypt:')
key = input('Input the key to encrypt:')
api.encode(text,key)

#解密程序到时补充