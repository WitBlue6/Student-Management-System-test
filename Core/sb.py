import tkinter as tk
from tkinter import messagebox


class LoginPage:
    """
    登录页面
    主页面
    """
    def __init__(self, master:tk.Tk):
        self.root = master
        self.root.geometry('300x150')
        self.root.title('欢迎登陆')

        self.page = tk.Frame(self.root)

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.create_menu()
        self.show_login()

    def show_login(self):
        """
        展示登录页面信息
        :return:
        """
        self.about_frame.pack_forget()
        tk.Label(self.page).grid(row=0, column=0)

        tk.Label(self.page, text='账户').grid(row=1, column=1)
        tk.Entry(self.page, textvariable=self.username).grid(row=1, column=2)
        tk.Label(self.page, text='密码').grid(row=2, column=1, pady=5)
        tk.Entry(self.page, textvariable=self.password).grid(row=2, column=2)
        tk.Label(self.page).grid(row=3, column=0)
        tk.Button(self.page, text='登录', command=self.login).grid(row=4, column=1, pady=5)
        tk.Button(self.page, text='退出', command=self.page.quit).grid(row=4, column=3)

        self.page.pack()

    def create_menu(self):
        """
        创建菜单栏
        :return:
        """
        menubar = tk.Menu()

        self.about_frame = tk.Frame()
        tk.Label(self.about_frame, text='本作品为半成品').pack()
        tk.Label(self.about_frame, text='暂未实现注册功能').pack()
        tk.Label(self.about_frame, text='登录账号:lzh').pack()
        tk.Label(self.about_frame, text='登陆密码:123').pack()

        menubar.add_command(label='登录', command=self.show_login)
        menubar.add_command(label='关于', command=self.show_about)

        self.root['menu'] = menubar

    def login(self):
        """
        登录功能实现
        :return:
        """
        usn = self.username.get()
        psw = self.password.get()
        if usn == 'lzh' and psw == '123':
            messagebox.showwarning(title='', message='登陆成功')
            self.page.destroy()
            MainPage(master=self.root)
        else:
            messagebox.showwarning(title='警告', message='账号或密码错误')

    def show_about(self):
        self.page.pack_forget()
        self.about_frame.pack()

class MainPage:
    """
    登陆后的主面板
    目前包含:
        self.name 姓名
        self.age 年龄
        self.university 大学
        self.wechat 微信
        self.QQ QQ号码
        self.phone 电话号码
    """
    def __init__(self, master: tk.Tk):
        self.root = master
        self.root.title('人员管理系统v0.1')
        self.root.geometry('600x400')

        self.name = tk.StringVar()
        self.age = tk.StringVar()
        self.university = tk.StringVar()
        self.wechat = tk.StringVar()
        self.QQ = tk.StringVar()
        self.phone = tk.StringVar()

        self.s_name = ''
        self.s_age = ''
        self.s_uni = ''
        self.s_wechat = ''
        self.s_QQ = ''
        self.s_phone = ''

        self.create_page()
        self.show_about()

    def create_page(self):
        """
        创建主页面以及菜单栏
        :return:
        """
        self.about_frame = tk.Frame(self.root)
        tk.Label(self.about_frame, text='作者:lzh').pack()
        tk.Label(self.about_frame, text='关于作者: 宇宙第一帅').pack()
        tk.Label(self.about_frame, text='本作品是半成品, 且数据只储存在本地').pack()
        tk.Label(self.about_frame, text='这个程序其实没有任何实际使用价值，做这个程序是为了练习tkinter').pack()
        tk.Label(self.about_frame).pack()
        tk.Label(self.about_frame, text='欢迎使用人员管理系统！', height=4, font=30, foreground='red').pack()

        self.admit_frame = tk.Frame(self.root)
        tk.Label(self.admit_frame, text='查询').grid(row=2,column=2)
        tk.Label(self.admit_frame).grid(row=3)
        tk.Label(self.admit_frame, text='请输入你要查找的姓名').grid(row=4, column=1)
        tk.Entry(self.admit_frame, textvariable=self.name).grid(row=4,column=3)
        tk.Label(self.admit_frame).grid(row=5)
        tk.Button(self.admit_frame, text='查询', command=self.search).grid(row=6, column=2)


        self.write_frame = tk.Frame(self.root)
        tk.Label(self.write_frame, text='请输入').grid(row=0, column=2)
        tk.Label(self.write_frame).grid(row=1)
        tk.Label(self.write_frame, text='姓名').grid(row=2, column=1)
        tk.Entry(self.write_frame, textvariable=self.name).grid(row=2, column=2)
        tk.Label(self.write_frame).grid(row=3)
        tk.Label(self.write_frame, text='年龄').grid(row=4, column=1)
        tk.Entry(self.write_frame, textvariable=self.age).grid(row=4, column=2)
        tk.Label(self.write_frame).grid(row=5)
        tk.Label(self.write_frame, text='大学').grid(row=6, column=1)
        tk.Entry(self.write_frame, textvariable=self.university).grid(row=6, column=2)
        tk.Label(self.write_frame).grid(row=7)
        tk.Label(self.write_frame, text='微信').grid(row=8, column=1)
        tk.Entry(self.write_frame, textvariable=self.wechat).grid(row=8, column=2)
        tk.Label(self.write_frame).grid(row=9)
        tk.Label(self.write_frame, text='QQ').grid(row=10, column=1)
        tk.Entry(self.write_frame, textvariable=self.QQ).grid(row=10, column=2)
        tk.Label(self.write_frame).grid(row=11)
        tk.Label(self.write_frame, text='电话').grid(row=12, column=1)
        tk.Entry(self.write_frame, textvariable=self.phone).grid(row=12, column=2)
        tk.Button(self.write_frame, text='录入', command=self.write_in).grid(row=13)

        self.all_frame = tk.Frame()
        self.pagenum = 0  # 查看栏的当前浏览页
        self.recent_pagenum = 0  # 上一次浏览的页面
        tk.Label(self.all_frame, text='所有录入人员如下').grid(row=0)

        self.change_frame = tk.Frame()
        tk.Label(self.change_frame, text='修改已录入的信息').grid(row=0, column=0, padx=(120,0))
        tk.Label(self.change_frame).grid(row=1)
        tk.Label(self.change_frame, text='输入你要修改的人的姓名').grid(row=2, column=0)
        tk.Entry(self.change_frame, textvariable=self.name).grid(row=2, column=1)
        tk.Label(self.change_frame).grid(row=3)
        tk.Button(self.change_frame, text='确定', command=self.change_info).grid(row=4, column=0, padx=(120,0))

        self.delete_frame = tk.Frame()
        tk.Label(self.delete_frame, text='删除一个联系人').grid(row=0, column=0, padx=(120,0))
        tk.Label(self.delete_frame).grid(row=1)
        tk.Label(self.delete_frame, text='输入要删除的人的姓名').grid(row=2, column=0)
        tk.Entry(self.delete_frame, textvariable=self.name).grid(row=2, column=1)
        tk.Label(self.delete_frame).grid(row=3)
        tk.Button(self.delete_frame, text='确定', command=self.delete_info).grid(row=4, column=0, padx=(120, 0))

        # 菜单栏
        menubar = tk.Menu(self.root)
        menubar.add_command(label='查看', command=self.show_all)
        menubar.add_command(label='查询', command=self.show_admit)
        menubar.add_command(label='录入', command=self.show_write)
        menubar.add_command(label='修改', command=self.show_change)
        menubar.add_command(label='删除', command=self.show_delete)
        menubar.add_command(label='关于', command=self.show_about)


        self.root['menu'] = menubar

    def search(self):
        """
        通过姓名搜索录入的信息
        并将搜索结果展示
        :return:
        """
        name = self.name.get()
        try:
            with open('Person.txt', 'r') as f:
                flag = False
                for data in f.readlines():
                    if name == data.split(',')[0]:
                        self.s_name = data.split(',')[0]
                        self.s_age = data.split(',')[1]
                        self.s_uni = data.split(',')[2]
                        self.s_wechat = data.split(',')[3]
                        self.s_QQ = data.split(',')[4]
                        self.s_phone = data.split(',')[5]

                        flag = True
                        break
        except:
            print("未发现人员录入")
            # 找到
        if flag:
            messagebox.showinfo(title='提示', message='查询成功')
            self.show_search(False)
        else:
            messagebox.showinfo(title='提示', message='未查询到该对象')

    def write_in(self):
        """
        录入信息
        至少录入姓名，否则录入失败
        录入模式：
            姓名可以改变，录入新信息
        修改模式：
            姓名不能改变，信息进行重写，不自动补充。
        :return:
        """
        name = self.name.get()
        age = self.age.get()
        uni = self.university.get()
        wec = self.wechat.get()
        qq = self.QQ.get()
        phone = self.phone.get()
        if self.writing_mode:
            # 录入模式
            with open('Person.txt', 'a') as f:
                if name:
                    f.writelines([name,',', age, ',', uni, ',', wec, ',', qq, ',', phone, '\n'])
                    messagebox.showinfo(title='提示', message='录入成功')
                else:
                    messagebox.showinfo(title='提示', message='录入失败！至少输入一个姓名!')
        else:
            # 修改模式
            with open('Person.txt', 'r') as f:
                data = f.readlines()
                flag = False
                no = -1
                for person in data:
                    no += 1
                    if name == person.split(',')[0]:
                        flag = True
                        break
                if not flag:
                    messagebox.showinfo(title='提示', message='请输入正确的姓名!')
                    return
                data[no] = name +','+ age +','+ uni +','+ wec +','+ qq +','+ phone +'\n'
            with open('Person.txt', 'w') as f:
                f.writelines(data)
            messagebox.showinfo(title='提示', message='修改成功!')

        self.write_frame.pack_forget()

    def change_info(self):
        """
        修改或补充已录入人员的信息
        :return:
        """
        try:
            with open('Person.txt', 'r') as f:
                find = False
                for person in f.readlines():
                    if person.split(',')[0] == self.name.get():
                        # 查找到相关人员
                        find = True
                        break
        except:
            print('未发现人员录入')
        if find:
            messagebox.showinfo(title='提示', message='查找成功，请修改!')
            self.show_write(False)
        else:
            messagebox.showinfo(title='提示', message='未查找到该人员！')

    def delete_info(self):
        """
        删除存在的联系人
        :return:
        """
        name = self.name.get()
        try:
            with open('Person.txt', 'r+') as f:
                data = f.readlines()
                no = -1
                for person in data:
                    no += 1
                    if name == person.split(',')[0]:
                        data[no] = ''
                        f.seek(0)
                        f.truncate()
                        f.writelines(data)
                        messagebox.showinfo(title='提示', message='删除成功!')
                        self.pagenum = 0
                        return
        except:
            print('未发现人员录入')
        messagebox.showinfo(title='提示', message='查找失败！请检查输入姓名!')


    def show_about(self):
        """
        展示关于栏
        一些关于该程序的基本信息
        :return:
        """
        self.about_frame.pack()
        self.admit_frame.pack_forget()
        self.write_frame.pack_forget()
        self.change_frame.pack_forget()
        self.delete_frame.pack_forget()
        try:
            self.search_frame.destroy()
        except:
            pass

    def show_admit(self):
        """
        展示查询栏
        查询录入的信息
        :return:
        """
        self.admit_frame.pack()
        self.about_frame.pack_forget()
        self.write_frame.pack_forget()
        self.delete_frame.pack_forget()
        try:
            self.search_frame.destroy()
        except:
            pass

    def show_write(self, writing=True):
        """
        展示录入栏
        录入新的人员信息
        :return:
        """
        if writing:
            self.writing_mode = True
        else:
            self.writing_mode = False
        self.write_frame.pack()
        self.admit_frame.pack_forget()
        self.about_frame.pack_forget()
        self.change_frame.pack_forget()
        self.delete_frame.pack_forget()
        try:
            self.search_frame.destroy()
        except:
            pass
    def show_change(self):
        """
        展示修改页面
        :return:
        """
        self.change_frame.pack()
        self.admit_frame.pack_forget()
        self.about_frame.pack_forget()
        self.write_frame.pack_forget()
        self.delete_frame.pack_forget()
        try:
            self.search_frame.destroy()
        except:
            pass
    def show_delete(self):
        """
        展示删除页面
        :return:
        """
        self.delete_frame.pack()
        self.change_frame.pack_forget()
        self.admit_frame.pack_forget()
        self.write_frame.pack_forget()
        self.about_frame.pack_forget()
        try:
            self.search_frame.destroy()
        except:
            pass

    def show_all(self):
        """
        展示当前已录入的所有人员信息名单
        通过换页按钮进行换页
        :return:
        """
        try:
            self.search_frame.destroy()
        except:
            pass
        try:
            with open('Person.txt', 'r') as f:
                self.All_People = []
                each = dict()
                for Person in f.readlines():
                    if Person.split(',')[0] != '\n':
                        print(Person)
                        each = each.copy()
                        each["name"] = Person.split(',')[0]
                        each["age"] = Person.split(',')[1]
                        each["uni"] = Person.split(',')[2]
                        each["wechat"] = Person.split(',')[3]
                        each["QQ"] = Person.split(',')[4]
                        each["phone"] = Person.split(',')[5]

                        self.All_People.append(each)
        except:
            print('未发现人员录入')
        try:
            self.s_name = self.All_People[self.pagenum]["name"]
            self.s_uni = self.All_People[self.pagenum]["uni"]
            self.s_age = self.All_People[self.pagenum]["age"]
            self.s_wechat = self.All_People[self.pagenum]["wechat"]
            self.s_QQ = self.All_People[self.pagenum]["QQ"]
            self.s_phone = self.All_People[self.pagenum]["phone"]
        except:
            print('未建立人员薄')

        self.show_search(True)


    def lastpage(self):
        """
        查看栏回到上一页
        :return:
        """
        self.recent_pagenum = self.pagenum
        if self.pagenum > 0:
            self.pagenum -= 1
            self.show_all()

    def nextpage(self):
        """
        查看栏进入下一页
        :return:
        """
        self.recent_pagenum = self.pagenum
        if self.pagenum < len(self.All_People)-1:
            self.pagenum += 1
            self.show_all()
    def show_search(self, Button: bool):
        """
        展示搜索的结果
        若缺失信息，缺失的那一栏为空
        :param Button:
        :return:
        """
        self.search_frame = tk.Frame()

        tk.Label(self.search_frame).grid(row=0)
        tk.Label(self.search_frame, text='姓名:').grid(row=1, column=1)
        tk.Label(self.search_frame, text=self.s_name).grid(row=1, column=2)
        tk.Label(self.search_frame).grid(row=2)
        tk.Label(self.search_frame, text='年龄:').grid(row=3, column=1)
        tk.Label(self.search_frame, text=self.s_age).grid(row=3, column=2)
        tk.Label(self.search_frame).grid(row=4)
        tk.Label(self.search_frame, text='大学:').grid(row=5, column=1)
        tk.Label(self.search_frame, text=self.s_uni).grid(row=5, column=2)
        tk.Label(self.search_frame).grid(row=6)
        tk.Label(self.search_frame, text='微信:').grid(row=7, column=1)
        tk.Label(self.search_frame, text=self.s_wechat).grid(row=7, column=2)
        tk.Label(self.search_frame).grid(row=8)
        tk.Label(self.search_frame, text='QQ:').grid(row=9, column=1)
        tk.Label(self.search_frame, text=self.s_QQ).grid(row=9, column=2)
        tk.Label(self.search_frame).grid(row=10)
        tk.Label(self.search_frame, text='手机:').grid(row=11, column=1)
        tk.Label(self.search_frame, text=self.s_phone).grid(row=11, column=2)
        if Button:
            tk.Button(self.search_frame, text='上一页',
                      command=self.lastpage, height=2).grid(row=12, column=1, padx=(0,30))
            tk.Button(self.search_frame, text='下一页',
                      command=self.nextpage, height=2).grid(row=12, column=2, padx=(30,0))
            tk.Label(self.search_frame, text="第{}页".format(self.pagenum+1), height=2).grid(row=13, column=2, padx=(0, 90))

        self.search_frame.pack()
        self.admit_frame.pack_forget()
        self.about_frame.pack_forget()
        self.write_frame.pack_forget()
        self.change_frame.pack_forget()
        self.delete_frame.pack_forget()

root = tk.Tk()
LoginPage(root)

root.mainloop()

