import json
import os
from datetime import datetime

# ==============================
# 工具类：统一读写 JSON（绝对不丢数据）
# ==============================
class JsonHandler:
    @staticmethod
    def read(filename):
        if not os.path.exists(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def write(filename, data):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

# ==============================
# 学生核心业务类（全部封装）
# ==============================
class StudentSystem:
    def __init__(self):
        self.book_file = "books.json"
        self.stu_file  = "students.json"
        self.current_student = None

    # 登录
    def login(self, student_id):
        students = JsonHandler.read(self.stu_file)
        for stu in students:
            if stu["student_id"] == student_id:
                self.current_student = stu
                return True
        return False

    # 显示所有图书
    def show_all_books(self):
        books = JsonHandler.read(self.book_file)
        print("\n===== 图书列表 =====")
        for b in books:
            print(f"ID:{b['book_id']} | 《{b['title']}》 | 库存:{b['stock']}")

    # 借阅图书（核心）
    def borrow_book(self, book_id):
        students = JsonHandler.read(self.stu_file)
        books    = JsonHandler.read(self.book_file)

        # 找图书
        book = next((b for b in books if b["book_id"] == book_id), None)
        if not book:
            print("❌ 图书不存在")
            return
        if book["stock"] <= 0:
            print("❌ 库存不足")
            return

        # 检查是否已借
        for borrowed in self.current_student["borrowed_books"]:
            if borrowed["book_id"] == book_id:
                print("❌ 已借阅过此书")
                return

        # 更新学生借阅记录
        for stu in students:
            if stu["student_id"] == self.current_student["student_id"]:
                stu["borrowed_books"].append({
                    "book_id": book_id,
                    "title": book["title"],
                    "date": datetime.now().strftime("%Y-%m-%d")
                })
                break

        # 更新库存
        for b in books:
            if b["book_id"] == book_id:
                b["stock"] -= 1
                break

        JsonHandler.write(self.stu_file, students)
        JsonHandler.write(self.book_file, books)
        print(f"✅ 借阅成功：《{book['title']}》")

    # 归还图书（核心）
    def return_book(self, book_id):
        students = JsonHandler.read(self.stu_file)
        books    = JsonHandler.read(self.book_file)

        # 检查是否真的借过
        has_book = any(b["book_id"] == book_id for b in self.current_student["borrowed_books"])
        if not has_book:
            print("❌ 未借阅此书，无法归还")
            return

        # 移除借阅记录
        for stu in students:
            if stu["student_id"] == self.current_student["student_id"]:
                stu["borrowed_books"] = [
                    b for b in stu["borrowed_books"] if b["book_id"] != book_id
                ]
                break

        # 库存+1
        for b in books:
            if b["book_id"] == book_id:
                b["stock"] += 1
                break

        JsonHandler.write(self.stu_file, students)
        JsonHandler.write(self.book_file, books)
        print("✅ 归还成功")

    # 查看我的借阅
    def show_my_borrowed(self):
        print("\n===== 我的借阅 =====")
        records = self.current_student["borrowed_books"]
        if not records:
            print("暂无借阅")
            return
        for r in records:
            print(f"《{r['title']}》 ID:{r['book_id']} | {r['date']}")

# ==============================
# 学生菜单入口
# ==============================
def student_main():
    system = StudentSystem()
    sid = input("请输入学号：")

    if not system.login(sid):
        print("❌ 学号不存在")
        return

    print(f"欢迎，{system.current_student['name']}！")

    while True:
        print("\n===== 学生借阅系统 =====")
        print("1. 查看所有图书")
        print("2. 借阅图书")
        print("3. 归还图书")
        print("4. 查看我的借阅")
        print("0. 退出")
        c = input("请选择：")

        if c == "1":
            system.show_all_books()
        elif c == "2":
            book_id = input("输入图书ID：")
            system.borrow_book(book_id)
        elif c == "3":
            book_id = input("输入图书ID：")
            system.return_book(book_id)
        elif c == "4":
            system.show_my_borrowed()
        elif c == "0":
            print("退出成功")
            break
        else:
            print("输入无效")

if __name__ == "__main__":
    student_main()