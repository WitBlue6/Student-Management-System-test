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
    """
    def __init__(self, master: tk.Tk):
        self.root = master
        self.root.title('垃圾系统v0.1')
        self.root.geometry('600x400')

        self.name = tk.StringVar()
        self.age = tk.StringVar()
        self.university = tk.StringVar()

        self.s_name = ''
        self.s_age = ''
        self.s_uni = ''

        self.create_page()

    def create_page(self):
        """
        页面
        :return:
        """
        self.about_frame = tk.Frame(self.root)
        tk.Label(self.about_frame, text='作者:lzh').pack()
        tk.Label(self.about_frame, text='关于作者: 宇宙第一帅').pack()
        tk.Label(self.about_frame, text='本作品是半成品, 且数据只储存在本地').pack()

        self.admit_frame = tk.Frame(self.root)
        tk.Label(self.admit_frame, text='查询').grid(row=2,column=2)
        tk.Label(self.admit_frame).grid(row=3)
        tk.Label(self.admit_frame, text='请输入你要查找的姓名').grid(row=4, column=1)
        tk.Entry(self.admit_frame, textvariable=self.name).grid(row=4,column=3)
        tk.Label(self.admit_frame).grid(row=5)
        tk.Button(self.admit_frame, text='查询', command=self.search).grid(row=6, column=2)
        tk.Label(self.admit_frame).grid(row=7,column=2)
        tk.Label(self.admit_frame, text='剩下懒得做了，仅支持姓名查找').grid(row=8, column=1)

        self.write_frame = tk.Frame(self.root)
        tk.Label(self.write_frame, text='录入').pack()
        tk.Label(self.write_frame).pack()
        tk.Label(self.write_frame, text='对象的姓名').pack()
        tk.Entry(self.write_frame, textvariable=self.name).pack()
        tk.Label(self.write_frame).pack()
        tk.Label(self.write_frame, text='对象的年龄').pack()
        tk.Entry(self.write_frame, textvariable=self.age).pack()
        tk.Label(self.write_frame).pack()
        tk.Label(self.write_frame, text='对象的大学').pack()
        tk.Entry(self.write_frame, textvariable=self.university).pack()
        tk.Button(self.write_frame, text='录入', command=self.write_in).pack()

        self.search_frame = tk.Frame()

        # 菜单栏
        menubar = tk.Menu(self.root)
        menubar.add_command(label='查询', command=self.show_admit)
        menubar.add_command(label='录入', command=self.show_write)
        menubar.add_command(label='关于', command=self.show_about)
        self.root['menu'] = menubar

    def search(self):
        name = self.name.get()
        with open('Person.txt', 'r') as f:
            flag = False
            for data in f.readlines():
                if name == data.split(' ')[0]:
                    age = data.split(' ')[1]
                    uni = data.split(' ')[2]
                    flag = True
                    break
            # 找到
            if flag:
                self.s_name = name
                self.s_age = age
                self.s_uni = uni
                messagebox.showinfo(title='提示', message='查询成功')
                self.show_search()
            else:
                messagebox.showinfo(title='提示', message='未查询到该对象')

    def write_in(self):
        name = self.name.get()
        age = self.age.get()
        uni = self.university.get()
        with open('Person.txt', 'a') as f:
            f.writelines([name,' ', age, ' ', uni, '\n'])
        messagebox.showinfo(title='提示', message='录入成功')
        self.write_frame.pack_forget()

    def show_about(self):
        """
        展示关于栏
        :return:
        """
        self.about_frame.pack()
        self.admit_frame.pack_forget()
        self.write_frame.pack_forget()
        self.search_frame.pack_forget()

    def show_admit(self):
        """
        展示查询栏
        :return:
        """
        self.admit_frame.pack()
        self.about_frame.pack_forget()
        self.write_frame.pack_forget()
        self.search_frame.pack_forget()

    def show_write(self):
        self.write_frame.pack()
        self.admit_frame.pack_forget()
        self.about_frame.pack_forget()
        self.search_frame.pack_forget()

    def show_search(self):
        tk.Label(self.search_frame).grid(row=0)
        tk.Label(self.search_frame, text='姓名').grid(row=1, column=1)
        tk.Label(self.search_frame, text=self.s_name).grid(row=2, column=1)
        tk.Label(self.search_frame).grid(row=3)
        tk.Label(self.search_frame, text='年龄').grid(row=4, column=1)
        tk.Label(self.search_frame, text=self.s_age).grid(row=5, column=1)
        tk.Label(self.search_frame).grid(row=6)
        tk.Label(self.search_frame, text='大学').grid(row=7, column=1)
        tk.Label(self.search_frame, text=self.s_uni).grid(row=8, column=1)
        tk.Label(self.search_frame).grid(row=9)
        self.search_frame.pack()
        self.admit_frame.pack_forget()

root = tk.Tk()
LoginPage(root)

root.mainloop()

