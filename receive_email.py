# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 23:06:25 2018

@author: Administrator
"""



          
import poplib,email
from email.header import decode_header
def check_email():
    try:
        p = poplib.POP3('pop.126.com')  
        p.user('u******@126.com')  
        p.pass_('*******')
        ret = p.stat()
    except:
        print('Login failed!')
    st = p.top(ret[0], 0)
    strlist = []
    for x in st[1]:
            try:
                strlist.append(x.decode())
            except:
                try:
                    strlist.append(x.decode('gbk'))
                except:
                    strlist.append((x.decode('big5')))
    mm = email.message_from_string('\n'.join(strlist))
    sub = decode_header(mm['subject'])
    if sub[0][1]:
        submsg = sub[0][0].decode(sub[0][1])
    else:
        submsg = sub[0][0]
    print(submsg.strip())
    su = decode_header(mm['Date'])
    if su[0][1]:
        sumsg = su[0][0].decode(su[0][1])
    else:
        sumsg = su[0][0]
    print(sumsg.strip().split(' ')[4][:-3])
    p.quit()
check_email()
