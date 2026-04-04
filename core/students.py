# ==================管理员视角添加注册学生=====================
import json
import os
BASE_DTR = os.path.dirname(os.path.abspath(__file__))
STU_DTR = os.path.join(BASE_DTR,"..","data")
os.makedirs(STU_DTR,exist_ok = True)
STU_PATH = os.path.join(STU_DTR,"students.json")
STU_PATH = os.path.normpath(STU_PATH)
class Students:
    def __init__(self) ->None:
        self.students = []
        self.obtain_students()
    # ===========学生信息储存=========  
    def obtain_students(self) ->None:   
        if not os.path.exists(STU_PATH):
            self.students = []
            return
        try:
            with open(STU_PATH,"r",encoding="utf-8") as f:
                self.students = json.load(f)
        except json.JSONDecodeError:
            print("students.json")
            self.students = []
            self.save_students()
    def save_students(self) ->None:
        with open(STU_PATH,"w",encoding="utf-8") as i:
            json.dump(self.students,i,ensure_ascii=False,indent=4)

    def int_students(self,it) ->int|None:
        try:
            return int(it)
        except:
            return None
    
    def system_students(self) ->None:
        print("============图书管理学生系统============")
        print("============1添加学生=============")
        print("============2删除学生=============")
        print("============3修改学生=============")
        print("============4查询学生=============")
        print("============5展示学生名单=============")
        print("============6退出页面=============")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

    def add_students(self) ->None:
        """添加学生"""
        stu_id = input("请输入添加学生编号id:")
        if not stu_id:
            print("学生编号不能为空！")
            return  
        if any(s ['id'] == stu_id for s in self.students):
            print("学生编号已经存在！")
            return
        name = input("请输入需要添加学生的姓名：")
        cls = input("请输入学生班级：")
        age_i = input("请输入学生年龄：")
        age = self.int_students(age_i)
        if  not age or age<=0:
            print("年龄不能小于零必须是整数！")
            return  None
        gender = input("请输入学生性别：")
        obtain={
            "id" : stu_id,
            "name" : name,
            "cls" : cls,
            "age" : age,
            "gender" :gender
        }
        self.students.append(obtain)
        self.save_students()
        print(f"学生添加成功～{self.students}")
    
    def delete_students(self) ->None:
        """删除学生"""
        delete = input("请输入需要删除的学生id:")
        if not delete: 
            print("为找到该学生id!")
            return 
        nwo_list = [s for s in self.students if s['id'] != delete]
        if len(nwo_list) == len(self.students):
            print("找不到该学生的id!")
        self.students = nwo_list
        self.save_students()
        print("已删除该学生的所有信息")      
    def get_students(self)->None:
        """修改学生"""
        stu_id = input("请输入修改的学生编号id:").strip()
        get = [g for g in self.students if g['id'] == stu_id]
        if not get:
            print("未找到该学生id")
            return 
        stu = get [0]
        name_i = input(f"请输入需要修改的学生名字{stu['name']}:")
        cls_i = input(f"请输入需要修改的学生班级{stu['cls']}:")
        age_i = input(f"请输入需要修改学生的年龄{stu['age']}:")
        gender_i = input(f"请输入需要修改的学生性别{stu['gender']}:")
        fields = {
            "id" : stu_id,
            "name" : name_i,
            "cls" : cls_i,
            "age" : age_i,
            "gender" : gender_i
        }
        for key,value in fields.items():
            if value:
                stu[key] = value
        self.save_students()
        print("修改成功～")
    def query_students(self)->None:
        """查询学生"""
        query = input("请输入需要在查询的学生编号id:").strip()
        query_list = [q for q in self.students if q['id'] == query]
        if query_list:
            stu = query_list[0]
            print(f"学生编号id:{stu['id']}|姓名:{stu['name']}|班级:{stu['cls']}|年龄:{stu['age']}|性别:{stu['gender']}")
            return
        print("没有找到学生id")
    def show_students(self) ->None:
        """展示学生"""
        if not self.students:
            print("没有找到该学生id!")
            return
        for show in self.students:
            print(f"学生编号id:{show['id']}|姓名:{show['name']}|班级:{show['cls']}|年龄:{show['age']}|性别:{show['gender']}")
    def student_interface(self):
        while True:
            self.system_students()
            Interface = input("请输入：")
            if Interface == '1':
                self.add_students()
            elif Interface == '2':
                self.delete_students()
            elif Interface == '3':
                self.get_students()
            elif Interface == '4':
                self.query_students()
            elif Interface == '5':
                self.show_students()
            elif Interface == '6':
                print("已退出学生系统～")
                break
            else:
                print("错误无效字符！！！")



if __name__== "__main__":
    run = Students()
    run.student_interface()

