# *****************学生视角********************
import json 
import os
from datetime import datetime

class JsonData:
    @staticmethod
    def read(file:str) ->list[dict[str,any]]:
        #退格查找文件
        file_path = os.path.join("..","data",file)
        #查找文件是否为空
        if not os.path.exists(file_path):
            return []
        #找到文件后读取返回成字典
        with open(file_path,"r",encoding="utf=8") as f:
            return json.load(f)
    @staticmethod
    def write(file:str,data:list[dict[str,any]]) ->None:
        file_path = os.path.join("..","data",file)
        with open(file_path,"w",encoding="utf=8") as f:
            json.dump(data,f,ensure_ascii=False,indent=4)

# ==============学生查阅============
class Students:
    def __init__(self) ->None:
        self.books_file = "books.json" 
        self.student_file = "students.json"
        self.stu = None
    
    def login_stu(self,login_id:str) ->bool:
        """登入系统"""
        if not login_id.strip():
            print("不允许空输入")
            return False
        stu_id = JsonData.read(self.student_file)
        stu = next((s for s in stu_id if s["student_id"] == login_id),None)
        if stu:
            self.stu = stu
            return True
        return False

    def show_




            
        