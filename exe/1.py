import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from functools import partial
global web_name,web_express,entry_web,entry_web_express,but_web
global cmb_name,entry_cmb,but_cmb
global web_list
global txt_name,cmb
root=tk.Tk()
root.attributes("-topmost", True)
root.resizable(False,False)
root.geometry("800x600+350+120")
def get_content(path):#获取.txt中的内容放到list中
    f=open(path,'r',encoding='utf-8')
    list=f.readlines()
    f.close()
    return list
def create_new_txt(path):#创建新的.txt
    f=open(path,'w',encoding='utf-8')
    f.close()
def add_line_txt(path,content):#在.txt文件中加入一行
    f=open(path,'a',encoding='utf-8')
    f.write(content)
    f.close()

def set_cmb():#将combobox中的内容设为"allcmb.txt"
    cmb['value']=get_content("allcmb.txt")
def set_web():#将listbox中的内容设为对应文件的内容
    txt_exp_path=txt_name.get().rstrip('\n')+"_exp.txt"
    web_list.delete(0,"end")
    all_web_exp=get_content(txt_exp_path)
    for item in all_web_exp:
        web_list.insert("end",item)
    
def add_cmb():#添加选项
    new_cmb=cmb_name.get()
    if new_cmb=='':
        return
    #写入"allcmb.txt"
    add_line_txt("allcmb.txt",new_cmb.rstrip('\n')+'\n')
    #更新combobox
    set_cmb()
    #创建新文件 .txt和_exp.txt
    create_new_txt(new_cmb+".txt")
    create_new_txt(new_cmb+"_exp.txt")
    #输入的entry清空
    cmb_name.set('')

def add_web():#在该选项添加网址
    txt_path=txt_name.get().rstrip('\n')+".txt"
    txt_exp_path=txt_name.get().rstrip('\n')+"_exp.txt"
    new_web=web_name.get().rstrip('\n')+'\n'
    new_web_exp=web_express.get().rstrip('\n')+'\n'
    if new_web=='':
        return
    if new_web_exp=='':
        return
    #.txt存入网站,_exp.txt 存入网站说明
    add_line_txt(txt_path,new_web)
    add_line_txt(txt_exp_path,new_web_exp)
    #更新list
    set_web()

def change(event):
    set_web()
def open_url(event):
    if not web_list.curselection():#如果没有网站，则获取不了选择的index
        return
    selected_index=web_list.curselection()[0]
    txt_path=txt_name.get().rstrip('\n')+".txt"
    all_web=get_content(txt_path)
    str=all_web[selected_index]
    import webbrowser
    webbrowser.open(str,new=0)
#选择框
txt_name=tkinter.StringVar()
cmb=ttk.Combobox(root,textvariable=txt_name)
set_cmb()
cmb.place(x=600,y=50,width=90,height=50)
cmb.bind("<<ComboboxSelected>>",change)
#list框,显示选项的网站内容
web_list=tk.Listbox(root)
web_list.place(x=0,y=0,width=500,height=800)
web_list.bind("<<ListboxSelect>> ",open_url)
#加入新选项
cmb_name=tkinter.StringVar()
entry_cmb=tk.Entry(root,textvariable=cmb_name)

but_cmb=tk.Button(root,text="添加新收藏夹",command=add_cmb)

entry_cmb.place(x=510,y=150,width=280,height=50)
but_cmb.place(x=610,y=210,width=90,height=50)
#加入新网站
web_name=tkinter.StringVar()
web_express=tkinter.StringVar()

entry_web=tk.Entry(root,text="网站地址",textvariable=web_name)
entry_web_express=tk.Entry(root,text="网站说明",textvariable=web_express)

but_web=tk.Button(root,text="添加新网站",command=add_web)

entry_web.place(x=510,y=350,width=280,height=50)
entry_web_express.place(x=510,y=420,width=280,height=50)
but_web.place(x=610,y=500,width=90,height=50)
tk.mainloop()