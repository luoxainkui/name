from core.logs import Logs
from core.Library_books import LibrarySystem
from core.students import Students

# 全局实例（只初始化一次）
log = Logs()
book = LibrarySystem()
stu = Students()

# 管理员默认密码（可修改）
ADMIN_PASSWORD = "admin123"


class LibraryManager:
    """图书馆管理系统主类（封装所有功能）"""
    def __init__(self):
        self.log = log
        self.book = book
        self.stu = stu

    # ====================== 管理员菜单 ======================
    def _admin_menu(self) -> None:
        """管理员子菜单（私有方法）"""
        while True:
            print("\n===== 管理员菜单 =====")
            print("1. 图书管理")
            print("2. 学生管理")
            print("3. 查看所有借阅日志")
            print("0. 返回主菜单")
            choice = input("请选择：").strip()

            if choice == "1":
                self._book_manage_menu()
            elif choice == "2":
                self._student_manage_menu()
            elif choice == "3":
                self.log.show_all_logs()
            elif choice == "0":
                print("👋 退出管理员菜单")
                break
            else:
                print("❌ 输入错误，请重新选择！")

    def _book_manage_menu(self) -> None:
        """图书管理子菜单（私有方法）"""
        while True:
            print("\n===== 图书管理 =====")
            print("1. 添加图书")
            print("2. 删除图书")
            print("3. 修改图书")
            print("4. 查询图书")
            print("5. 展示所有图书")
            print("0. 返回上一级")
            choice = input("请选择：").strip()

            if choice == "1":
                self.book.add_book()
            elif choice == "2":
                self.book.delete_book()
            elif choice == "3":
                self.book.update_book()
            elif choice == "4":
                self.book.query_book()
            elif choice == "5":
                self.book.show_all_books()
            elif choice == "0":
                break
            else:
                print("❌ 输入错误，请重新选择！")

    def _student_manage_menu(self) -> None:
        """学生管理子菜单（私有方法）"""
        while True:
            print("\n===== 学生管理 =====")
            print("1. 添加学生")
            print("2. 删除学生")
            print("3. 修改学生")
            print("4. 查询学生")
            print("5. 展示所有学生")
            print("0. 返回上一级")
            choice = input("请选择：").strip()

            if choice == "1":
                self.stu.add_student()
            elif choice == "2":
                self.stu.delete_student()
            elif choice == "3":
                self.stu.update_student()
            elif choice == "4":
                self.stu.query_student()
            elif choice == "5":
                self.stu.show_all_students()
            elif choice == "0":
                break
            else:
                print("❌ 输入错误，请重新选择！")

    # ====================== 学生菜单 ======================
    def _student_menu(self) -> None:
        """学生子菜单（私有方法）"""
        # 1. 学生登录校验
        stu_id = input("请输入学号登录：").strip()
        if not self.stu.check_student(stu_id):
            print("❌ 学号不存在，登录失败！")
            return

        stu_name = self.stu.get_student_name(stu_id)
        print(f"✅ 欢迎，{stu_name}同学！")

        while True:
            print("\n===== 学生菜单 =====")
            print("1. 查看所有图书")
            print("2. 借阅图书")
            print("3. 归还图书")
            print("4. 查看我的借阅记录")
            print("0. 退出登录")
            choice = input("请选择：").strip()

            if choice == "1":
                self.book.show_all_books()

            elif choice == "2":
                book_id = input("请输入要借阅的图书编号：").strip()
                # 校验图书是否存在
                book_name = self.book.get_book_name(book_id)
                if book_name == "未知图书":
                    print("❌ 图书不存在！")
                    continue
                # 校验图书是否可借
                if not self.book.is_available(book_id):
                    print("❌ 该图书已被借出，无法借阅！")
                    continue
                # 执行借书 + 写日志
                self.book.borrow_book(book_id)
                self.log.add_borrow_log(stu_id, book_id, book_name)
                print(f"✅ 成功借阅《{book_name}》！")

            elif choice == "3":
                book_id = input("请输入要归还的图书编号：").strip()
                book_name = self.book.get_book_name(book_id)
                if book_name == "未知图书":
                    print("❌ 图书不存在！")
                    continue
                # 执行还书 + 写日志
                if self.book.return_book(book_id):
                    self.log.add_return_log(stu_id, book_id, book_name)
                    print(f"✅ 成功归还《{book_name}》！")
                else:
                    print("❌ 还书失败！")

            elif choice == "4":
                self.log.query_student_logs(stu_id)

            elif choice == "0":
                print(f"👋 再见，{stu_name}同学！")
                break
            else:
                print("❌ 输入错误，请重新选择！")

    # ====================== 主菜单（入口） ======================
    def run(self) -> None:
        """启动系统主入口"""
        print("=" * 50)
        print("📚 欢迎使用图书馆管理系统 📚")
        print("=" * 50)

        while True:
            print("\n===== 主菜单 =====")
            print("1. 管理员登录")
            print("2. 学生登录")
            print("0. 退出系统")
            choice = input("请选择：").strip()

            if choice == "1":
                # 管理员密码校验
                pwd = input("请输入管理员密码：").strip()
                if pwd == ADMIN_PASSWORD:
                    print("✅ 管理员登录成功！")
                    self._admin_menu()
                else:
                    print("❌ 密码错误，登录失败！")

            elif choice == "2":
                self._student_menu()

            elif choice == "0":
                print("👋 感谢使用，再见！")
                break
            else:
                print("❌ 输入错误，请重新选择！")


if __name__ == "__main__":
    # 启动系统
    app = LibraryManager()
    app.run()
