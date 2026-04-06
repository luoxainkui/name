# =============图书管理系统============
# --------------管理员模式-------------
import json
import os
# 获取当点脚本目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 退一步查找data文件
ROOT_DTR = os.path.join(BASE_DIR,"..","data")
# 检验是不是空文件
os.makedirs(ROOT_DTR,exist_ok = True)
# ===========路径========= 
BOOK_PATH = os.path.normpath(os.path.join(ROOT_DTR,"books.json"))


class LibrarySystem:
    def __init__(self) ->None:
        self.books = []
        self.obtain_books() 
# ===========图书信息储存=========    
    def obtain_books(self) ->None:
        if not os.path.exists(BOOK_PATH):
            print("书籍文件不存在，已经创建为空文件!")
            self.books = []
            self.save_books()
            return
        try:
            with open(BOOK_PATH,"r",encoding="utf-8") as i:
                self.books = json.load(i)
        except json.JSONDecodeError:
            print("books.json格式出现错误,已经重置为空列表！")
            self.books = []
            self.save_books()
    def save_books(self) ->None:
        with open(BOOK_PATH,"w",encoding="utf-8") as i:
            json.dump(self.books,i,ensure_ascii=False,indent=4)

# ===========图书馆系统========== 
    def system_books(self) ->None:
        print("\n###############图书管理系统##############")
        print("=================a添加图书=================")
        print("=================b删除图书=================")
        print("=================c修改图书=================")
        print("=================d查询图书=================")
        print("=================e展示图书=================")
        print("=========================================")
        print("=================0退出页面=================")

    def add_books(self) ->None:
        """添加图书不重复"""
        book_id = input("请输入添加图书的编号:").strip()
        if not book_id:
            print("图书编号不能为空")
            return
        exists = any(book['book_id'] == book_id for book in self.books)
        if exists:
            print("图书编号已经存在")
            return
        book = input("请输入添加的图书：")
        author = input("请输入图书的作者：")
        publish_date = input("请输入添加图书的日期：")
        borrow_time =input("请输入添加图书的时间：")

        nooks_books = {
            "book_id" : book_id,
            "book_name" : book,
            "author" : author,
            "publish_date" :publish_date,
            "borrow_time" :borrow_time,
            "status" : "可借"
        }
        self.books.append(nooks_books)
        self.save_books()
        print(f"添加成功～{self.books}")
    
    def delete_books(self) ->None:
        """删除图书"""
        book_id = input("请输入删除的图书id:").strip()
        if not book_id:
            print("图书id不能为空!")
            return 
        nwo_list = [b for b in self.books if b['book_id'] != book_id]
        if len(nwo_list) == len(self.books):
            print("找不到该图书id")
        self.books = nwo_list
        self.save_books()
        print("删除成功～")

    def update_books(self) ->None:
        """修改图书"""
        student = input("请输入修改图书id:").strip()
        if not student:
            print("未找到图书id!")
            return
        stu = None
        for stu in self.books:
            if stu["book_id"] == student:
                book_n = input(f"请输入新的图书名字{stu['book_name']}:").strip()
                author_n = input(f"请输入新作者名字{stu['author']}:").strip()
                publish_d = input(f"请输入新图书日期{stu['publish_date']}:").strip()
                time_t = input(f"请输入新图书借阅时间{stu['borrow_time']}:").strip()
                if book_n:
                    stu['book_name'] = book_n
                if author_n :
                    stu['author'] = author_n
                if publish_d:
                    stu['publish_date'] = publish_d
                if time_t:
                    stu['borrow_time'] = time_t
                print(f"修改成功{stu}")
                return None
        self.save_books()
        print("找不到该图书id")
    
    def query_books(self) ->None:
        """查询打印"""
        query = input("请输入要查询图书的id:").strip()
        for book in self.books:
            if book['book_id'] == query:
                print(f"图书编号id:{book['book_id']}|图书:{book['book_name']}|作者：{book['author']}|日期：{book['publish_date']}|时间：{book['borrow_time']}") 
                return 
        print("没有id名字")

    def show_books(self) ->None:
        """展示"""
        if not self.books:
            print("没有图书！")
            return None
        for index,show in enumerate(self.books,1):
            print(f"序号:{index:2d}|id:{show['book_id']:<6s}|图书:{show['book_name']:<8s}|作者：{show['author']:<8s}|日期：{show['publish_date']:<6s}|时间：{show['borrow_time']}")
        print("="*70 + "\n")
    def status_books(self,books_id) ->str:
        """借阅图书"""
        for b in self.books:
            if b['book_id'] == books_id:
                return b['status']
        return "未知图书"
    def is_borrow_books(self,books_id:any) ->bool:
        """判断是否可借"""
        for b in self.books:
            if b['book_id'] == books_id:
                return b['status'] == "可借"
        return False
    def borrow_book(self,books_id) ->bool:
        for b in self.books:
            if b['book_id'] == books_id:
                if b['status'] == "可借":
                    b['status'] == "已借出"
                    self.save_books()
                    return True
                else:
                    return False
        return False
    def return_books(self,books_id:any) ->bool:
        """还书"""
        for b in self.books:
            if b['book_id'] == books_id:
                b['status'] = "可借"
                self.save_books()
                return True
        return False
        
    def run(self) ->None:
        """接口"""
        while True:
            self.system_books()
            Interface = input("请输入：").strip()
            if Interface == 'a':
                self.add_books()
            elif Interface == 'b':
                self.delete_books()
            elif Interface == 'c':
                self.update_books()
            elif Interface == 'd':
                self.query_books()
            elif Interface == 'e':
                self.show_books()
            elif Interface == '0':
                print("拜拜～")
                break
            else:
                print("请重新输入")

