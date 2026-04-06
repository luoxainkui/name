from core.logs import Logs
from core.Library_books import LibrarySystem 
from core.students import Students 

log = Logs()# 日志
book = LibrarySystem() #图书类型
stu = Students() #学生类型
class LibraryManager:
    """图书管理系统主程序"""
    def __init__(self):
        self.log = log
        self.book = book
        self.stu = stu
# ================管理员菜单===========
    def administrator_menu(self) ->None:
        """管理员主菜单"""
        while True:
            print("1$$$$$$图书管理$$$$$$$$")
            print("2$$$$$$学生管理$$$$$$$$")
            print("3$$$$$$$查看日志$$$$$$$")
            print("0&&&&&&&&关闭程序&&&&&&&&&")
            program = input("请输入指令:").strip()
            if program == '1':
                self.book_manage_menu()
            elif program == '2':
                self.student_manage_menu()
            elif program == '0':
                print("已退出，回到主菜单")
                break          
    def book_manage_menu(self):
        self.book.run()
    def student_manage_menu(self):
        self.stu.student_interface()

# ================学生菜单==============
    def students_name(self):
        stu_id = input("请输入:").strip()
        if not self.stu.check_student(stu_id):
            print("学生校验失败无法登陆")
            return
        stu_name = self.stu.student_name(stu_id)
        while True:
            print(f"欢迎{stu_name}同学～")
            print("\n@@@@@@请输入如下操作@@@@@@")
            print("########0.查看所有图书#######")
            print("********1.借阅借书********")
            print("########2.归还图书########")
            print("########3.查看日志########")
            print("&&&&&&&&4.退出程序$$$$$$$$")
            stu = input("请输入:").strip()
            if stu == '0':
                self.book.show_books()
            elif stu == '1':
                book_id = input("请输入需要借的图书编号:").strip()
                """获取"""
                book_name = self.book.status_books(book_id)
                if book_name == "未知图书":
                    print("图书不存在")
                    continue
                if not self.book.is_borrow_books(book_id):
                    print("该图书已被借出！")
                    continue
                self.book.borrow_book(book_id)
                self.log.add_logs(stu_id,book_id,book_name)
                print(f"已经成功借阅{book.name}~")
            elif stu == '2':
                book_id = input("请输入需要归还的图书:").strip()
                

