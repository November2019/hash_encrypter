#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
#
# Written By:
#       S.S.B
#       surajsinghbisht054@gmail.com
#       bitforestinfo.blogspot.com
#   
#

__author__='''
S.s.b
surajsinghbisht054@gmail.com
'''

try:
    from Tkinter import *
except:
    from tkinter import *
import hashlib
import base64

def mainframe():
    def out():
        mn.quit()
    def cut():
        mn.withdraw()
    def clr():
        var1.set("")
        var2.set("")
    def h_md5():
        mystring = var1.get()
        hash_object = hashlib.md5(mystring.encode())
        var2.set(hash_object.hexdigest())
        return
    def h_sha1():
        mystring = var1.get()
        hash_object = hashlib.sha1(mystring.encode())
        var2.set(hash_object.hexdigest())
        return
    def h_sha224():
        mystring = var1.get()
        hash_object = hashlib.sha224(mystring.encode())
        var2.set(hash_object.hexdigest())
        return
    def base_16():
        mystring = var1.get()
        ency= base64.b16encode(mystring)
        var2.set(ency)

        return

    def base_32():
        mystring = var1.get()
        ency= base64.b32encode(mystring)
        var2.set(ency)
        return
    def base_64():
        mystring = var1.get()
        ency= base64.b64encode(mystring)
        var2.set(ency)
        return
    def h_sha256():
        mystring = var1.get()
        hash_object = hashlib.sha256(mystring.encode())
        var2.set(hash_object.hexdigest())
        return
    def h_sha384():
        mystring = var1.get()
        hash_object = hashlib.sha384(mystring.encode())
        var2.set(hash_object.hexdigest())
        return
    def h_sha512():
        mystring = var1.get()
        hash_object = hashlib.sha512(mystring.encode())
        var2.set(hash_object.hexdigest())
        return

    
    mn=Tk()
    mn.title("Hash_Encryter_Program by S.s.b")
    f1=Frame(mn, bg="GREY", bd=4)
    f1.pack(side=TOP)
    f2=Frame(f1, bg="GREY", bd=4)
    f2.pack(side=BOTTOM)
    f3=Frame(f1, bg="GREY", bd=4)
    f3.pack(side=BOTTOM)
    f4=Frame(mn, bg="GREY", bd=4)
    f4.pack(side=BOTTOM)
    f5=Frame(mn, bg="GREY", bd=4)
    f5.pack(side=BOTTOM)
    ll=Label(f1, bg="Yellow", text="[+] Hash Encrypter Created By surajsinghbisht054@gmail.com [+]", fg="Blue", font=('arial 15 bold'))
    ll.pack(side=TOP)
    var1=StringVar()
    var2=StringVar()
    var1.set("Please Enter Here Your Text For Encryption [press clear]")
    
    var2.set("Your Encrypted Cipher")
    b1=Button(f1, width=29, borderwidth=8, anchor=CENTER, fg="Black",bg="Powder blue", text="Clear", cursor="dot", command=clr, relief=RAISED, height=3, activebackground="RED", activeforeground="Green", font=('arial 10 bold'))
    b2=Button(f1, width=29, borderwidth=8, anchor=CENTER, fg="Black",bg="Powder blue", text="Quit", cursor="dot", command=out, relief=RAISED, height=3, activebackground="RED", activeforeground="Green", font=('arial 10 bold'))
    b10=Button(f1, width=29, borderwidth=8, anchor=CENTER, fg="Black",bg="Powder blue", text="Exit", cursor="dot", command=cut, relief=RAISED, height=3, activebackground="RED", activeforeground="Green", font=('arial 10 bold'))
    b3=Button(f3, width=29, borderwidth=8, anchor=CENTER, fg="Black",bg="Powder blue", text="MD5", cursor="dot", command=h_md5, relief=RAISED, height=2, activebackground="RED", activeforeground="Green", font=('arial 10 bold'))
    b4=Button(f3, width=29, borderwidth=8, anchor=CENTER, fg="Black",bg="Powder blue", text="SHA1", cursor="dot", command=h_sha1, relief=RAISED, height=2, activebackground="RED", activeforeground="Green", font=('arial 10 bold'))
    b5=Button(f3, width=29, borderwidth=8, anchor=CENTER, fg="Black",bg="Powder blue", text="SHA224", cursor="dot", command=h_sha224, relief=RAISED, height=2, activebackground="RED", activeforeground="Green", font=('arial 10 bold'))
    b6=Button(f2, width=29, borderwidth=8, anchor=CENTER, fg="Black",bg="Powder blue", text="SHA256", cursor="dot", command=h_sha256, relief=RAISED, height=2, activebackground="RED", activeforeground="Green", font=('arial 10 bold'))
    b7=Button(f2, width=29, borderwidth=8, anchor=CENTER, fg="Black",bg="Powder blue", text="SHA384", cursor="dot", command=h_sha384, relief=RAISED, height=2, activebackground="RED", activeforeground="Green", font=('arial 10 bold'))
    b8=Button(f2, width=29, borderwidth=8, anchor=CENTER, fg="Black",bg="Powder blue", text="SHA512", cursor="dot", command=h_sha512, relief=RAISED, height=2, activebackground="RED", activeforeground="Green", font=('arial 10 bold'))
    b9=Button(f5, width=29, borderwidth=8, anchor=CENTER, fg="Black",bg="Powder blue", text="Base_16", cursor="dot", command=base_16, relief=RAISED, height=2, activebackground="RED", activeforeground="Green", font=('arial 10 bold'))
    b12=Button(f5, width=29, borderwidth=8, anchor=CENTER, fg="Black",bg="Powder blue", text="Base_32", cursor="dot", command=base_32, relief=RAISED, height=2, activebackground="RED", activeforeground="Green", font=('arial 10 bold'))
    b11=Button(f5, width=29, borderwidth=8, anchor=CENTER, fg="Black",bg="Powder blue", text="Base_64", cursor="dot", command=base_64, relief=RAISED, height=2, activebackground="RED", activeforeground="Green", font=('arial 10 bold'))
    
    
    e1=Entry(f1, selectbackground="White", selectborderwidth=25, selectforeground="RED", bd=15, fg="Green", bg="BLACK", relief=GROOVE, width=50, font=('arial 20'), textvariable=var2)
    e2=Entry(f1, selectbackground="Grey", selectborderwidth=25, selectforeground="RED", bd=15, fg="Black", bg="powder blue", relief=GROOVE, width=50, font=('arial 20'), textvariable=var1)
    e1.pack(side=TOP, padx=3)
    e2.pack(side=TOP, padx=3)
    b1.pack(side=LEFT, padx=3)
    b2.pack(side=LEFT, padx=3)
    b10.pack(side=LEFT, padx=3)
    b3.pack(side=LEFT, padx=3)
    b4.pack(side=LEFT, padx=3)
    b5.pack(side=LEFT, padx=3)
    b6.pack(side=LEFT, padx=3)
    b7.pack(side=LEFT, padx=3)
    b8.pack(side=LEFT, padx=3)
    b9.pack(side=LEFT, padx=3)
    b12.pack(side=LEFT, padx=3)
    b11.pack(side=LEFT, padx=3)
    mn.mainloop()



if __name__=="__main__":
    mainframe()