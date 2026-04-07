from core.logs import Logs
from core.Library_books import LibrarySystem 
from core.students import Students 

log = Logs()# 日志
book = LibrarySystem() #图书类型
stu = Students() #学生类型
ADMIN_PASSWORD = "13456"
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
            elif program == '3':
                self.log.show_logs()
            elif program == '0':
                print("已退出，回到主菜单")
                break 
            else:
                print("请勿点其他键")         
    def book_manage_menu(self):
        self.book.run()
    def student_manage_menu(self):
        self.stu.student_interface()

# ================学生菜单==============
    def students_name(self):
        stu_id = input("请输入你的学号:").strip()
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
                book_name = self.book.get_books_name(book_id)
                if book_name == "未知图书":
                    print("图书不存在")
                    continue
                if not self.book.is_borrow_books(book_id):
                    print("该图书已被借出！")
                    continue
                self.book.borrow_book(book_id)
                self.log.add_logs(stu_id,book_id,is_book_name)

                is_book_name = self.book.get_books_name(book_id)
                is_suc = True
                if is_suc:
                    print(f"已经成功借阅《{is_book_name}》~")
            elif stu == '2':
                book_id = input("请输入需要归还的图书:").strip()
                book_name = self.book.status_books(book_id)
                if book_name == "未知图书":
                    print("图书不存在")
                    continue
                is_book_name = self.book.get_books_name(book_id)
                if self.book.return_books(book_id):
                    self.log.return_logs(stu_id,book_id,is_book_name)
                    print(f"成功归还《{is_book_name}》")
                else:
                    print("归还失败！")
            elif stu == '3':
                self.log.query_logs(stu_id)
            elif stu == '4':
                print("已退出本页面")
                break
            else:
                print("请勿点其他键")


# ================主菜单==============
    def run(self) ->None:
        """分流"""           
        print("#"*50)
        print("=======欢迎来到图书管理系统========")
        print("@"*50)
        while True:
            print("\n+++++++++主菜单++++++++")
            print("………………1.管理员模式…………………")
            print("******2.学生模式********")
            print("******3.退出主程序******")
            run = input("请输入需要进入的程序:")
            if run == '1':
                ru = input("请输入密码:")
                if ru == ADMIN_PASSWORD:
                    self.administrator_menu()
                else:
                    print("验证失败!")
                    continue
            elif run == '2':
                self.students_name()
            elif run == '3':
                print("已经退出主程序了")
                break
            else:
                print("错误请重新输入")

if __name__ == "__main__":
    LM = LibraryManager()
    LM.run()




