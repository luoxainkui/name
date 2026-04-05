# &&&&&&&&&&&&&&日志&&&&&&&&&&&&&&
import json
import os 
from datetime import datetime as dt
BASE_DTR = os.path.dirname(os.path.abspath(__file__))
LOG_DTR = os.path.join(BASE_DTR,"..","data")
os.makedirs(LOG_DTR,exist_ok=True)
# ==========日志路径===========
LOG_PATH = os.path.normcase(os.path.join(LOG_DTR,"books_log.json"))

class Logs:
    def __init__(self) ->None:
        # 日志类
        self.log = []
        self.logs_books()
    
# ===========日志查阅============
    def logs_books(self) ->None:
        if not os.path.exists(LOG_PATH):
            self.log = []
            self.save_logs()
            return
        try:
            with open(LOG_PATH,"r",encoding="utf-8" ) as f:
                self.log = json.load(f)
        except json.JSONDecodeError:
            print("books_log.json格式出现错误,已重置为空列表！")
            self.log = []
            self.save_logs()
    def save_logs(self) ->None:
        with open(LOG_PATH,"w",encoding="utf-8") as f:
            json.dump(self.log,f,ensure_ascii=False,indent=4)

#============添加借书日志==========
    def add_logs(self,student_id:any,books_id:any,books_name:any) ->None:
        now =  dt.now().strftime("%Y-%m-%d %H:%M:%S")
        sog = {
            "student_id": student_id,
            "books_id": books_id,
            "books_name": books_name,
            "status": "已借出",
            "books_time": now,
            "return_time": "" 
        }
        self.log.append(sog)
        self.save_logs()

#============还书时间==============
    def return_logs(self,student_id:any,books_id:any,books_name:any) ->None:
        now_id = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        for n in self.log:
            if n["student_id"] == student_id and n["books_id"] == books_id and n["books_name"] == books_name and n["status"] == "已借出":
                n["status"] = "已归还"
                n["return_time"] = now_id
                break
        self.save_logs()
#===========返回日志==============
    def show_logs(self) ->None:
        if not self.log:
            print("暂无日志记录")
            return
        for index,log in enumerate(self.log,1):
            print(f"序号:{index}")
            print(f"学生序号:{log['student_id']}")
            print(f"图书序号:{log['books_id']}|书名:{log['books_name']}")
            print(f"状态:{log['status']}")
            print(f"借书时间:{log['books_time']}")
            print(f"归还时间:{log['return_time']}")
            print("#"*50)
# ============按学号查日志===========
    def query_logs(self,student_id):
        query = [q for q in self.log if q['student_id'] == student_id]
        if not query:
            print(f"没有找到学生{student_id}借阅记录")
            return
        print(f"学生{student_id}的借阅记录")
        for r in query:
            print(f"图书:{r['books_id']}|书名:{r['books_name']}")
            print(f"借书时间:{r['books_time']}")
            print(f"归还时间:{r['return_time']}")
            print("*"*50)