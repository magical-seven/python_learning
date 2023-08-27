# -*- encoding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : stusystem.py
# @Time : 2023/8/25 16:55
# @Tool : PyCharm
import os.path

filename = 'student.txt'

def main():
    while True:
        menm()    # 菜单
        choice = int(input('please choose:'))
        if choice in [0,1,2,3,4,5,6,7]:  # 选择菜单功能
            if choice == 0:
                answer = input('y/n:')
                if answer == 'y' or answer == 'Y':
                    print('over!')
                    break     # 退出系统
                else:
                    continue
            elif choice == 1:
                insert()  # 录入学生信息
            elif choice == 2:
                search()  # 查找学生
            elif choice == 3:
                delete()   # 删除学生信息
            elif choice == 4:
                modify()   # 修改学生信息
            elif choice == 5:
                sort()    # 学生排序
            elif choice == 6:
                total()  # 统计学生信息
            elif choice == 7:
                show()   # 显示学生所有信息

def menm():   # 菜单函数
    print('-------------------------------------------------')
    print('\t\t\t\t\t  学生信息管理系统\t\t\t\t\t')
    print('\t\t\t\t\t\t 功能菜单\t\t\t\t\t')
    print('\t\t\t\t\t1、录入学生信息')
    print('\t\t\t\t\t2、查找学生信息')
    print('\t\t\t\t\t3、删除学生信息')
    print('\t\t\t\t\t4、修改学生信息')
    print('\t\t\t\t\t5、排序')
    print('\t\t\t\t\t6、统计学生总人数')
    print('\t\t\t\t\t7、显示所有学生信息')
    print('\t\t\t\t\t0、退出')
    print('-------------------------------------------------')

def insert():
    student_lst = []
    while True:
        id = input('输入id（如1001）:')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break

        try:  # 录入学生信息
            english = int(input('请输入英语成绩：'))
            python = int(input('python成绩：'))
            java = int(input('请输入Java成绩：'))
        except:
            print('输入无效，非整数类型，重新输入')
            continue
        # 将录入信息保存到字典之中
        student = {'id':id,'name':name,'english':english,'python':python,'java':java}
        student_lst.append(student)
        answer = input('是否继续添加？y/n\n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    save(student_lst)  # 保存录入的信息
    print('学生信息录入完毕')

def save(lst):  # 保存函数
    try:   # 如果出现打开失败，则更换打开方式
        stu_txt = open(filename,'a',encoding='utf-8')
    except:
        stu_txt = open(filename,'w',encoding='utf-8')

    for item in lst:   # 按列表将文件信息写入文件
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按id查找请输入1，按姓名查找请输入2：')
            if mode == '1':
                id = input("请输入学生的id：")
            elif mode == '2':
                name = input('请输入学生姓名：')
            else:
                print("您的输入有错，请重新输入")
                continue
            with open(filename,'r',encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id!='':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name!='':
                        if d['name'] == name:
                            student_query.append(d)
            # 显示查询结果
            show_student(student_query)
            # 清空列表
            student_query.clear()
            answer = input("是否要继续查询：y/n\n")
            if answer == 'y':
                continue
            else:
                break
        else:
            print("还未保存学生信息")
            return

def show_student(lst):   # 显示学生信息
    if len(lst) == 0:   # 如果列表为空则未查到信息
        print('没有查到学生信息，无数据显示。')
        return
    # 定义标题的显示格式
    fomat_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'   # 字符串格式化，^表示居中，显示标题
    print(fomat_title.format('ID','姓名','英语成绩','python成绩','Java成绩','总成绩'))

    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'   # 字符串格式化，显示数据
    for item in lst:
        print(format_data.format(item['id'],
                                 item['name'],
                                 item['english'],
                                 item['python'],
                                 item['java'],
                                 int(item['english'])+int(item['python'])+int(item['java'])))

def delete():
    while True:
        student_id = input('请输入要删除的学生id：')
        if student_id !='':   # 输入不为空时
            if os.path.exists(filename):    # 如果学生信息文件存在并录入过
                with open(filename,'r',encoding='utf-8') as file:
                    student_old = file.readlines()
            else:    # 如果学生信息文件还不存在
                student_old = []
            flag = False    # 标记是否删除
            if student_old:   # 学生文件中有学生信息
                with open(filename,'w',encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))   # eval()将字符串转变为字典，在用dict()方法创建字典。
                        if d['id'] != student_id:    # 如果输入的id和文件的id不相同，那么将信息写入文件里面
                            wfile.write(str(d)+'\n')
                        else:               # 否则删除
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已经删除')
                    else:
                        print(f'没有找到id为{student_id}的学生')
            else:  # 学生信息还不存在
                print('还未录入学生信息')
                break
        show()
        answer = input('是否继续删除？y/n:\n')
        if answer == 'y':
            continue
        else:
            break

def modify():
    show()
    if os.path.exists(filename):   # 判断是否存在学生信息文件
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old = rfile.readlines()            # 学生信息放入变量中
    else:
        return
    studen_id = input('请输入要修改的学员id：\n')            # 输入要修改的学生id
    with open(filename,'w',encoding='utf-8') as wfile:    # 打开文件进行修改
        for item in student_old:      # 对于原文件的信息中学生id进行比对
            d = dict(eval(item))
            if d['id'] == studen_id:     # 若id与输入id相同
                print("找到学生信息，可以修改相关信息：")
                while True:   # 开始修改
                    try:
                        d['name'] = input('请输入姓名：')
                        d['english'] = input('请输入英语成绩：')
                        d['python'] = input('请输入python成绩：')
                        d['java'] = input('请输入Java成绩：')
                    except:
                        print('您的输入有错，请重新输入：')   # 若有错，则继续重新输入
                    else:
                        break   # 退出循环
                wfile.write(str(d)+'\n')        # 将修改信息覆盖原有的学生信息文件
                print('修改成功')
            else:
                wfile.write(str(d)+'\n')       # 如果id与输入id不同则正常录入当前信息
        answer = input('是否继续修改其他学生信息：y/n\n')
        if answer == 'y':
            modify()

def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_lst = rfile.readlines()
        student_new = []
        for item in student_lst:
            student_new.append(eval(item))   # 以字典形式存储至列表中
    else:
        return
    while True:
        asc_or_desc = input('请选择（0：升序；1：降序）\n')
        if asc_or_desc == '0':
            asc_or_desc_bool = False
            # break
        elif asc_or_desc == '1':
            asc_or_desc_bool = True
            # break
        else:
            print('输入有误，重新输入!')
            continue
        mode = input("请选择排序方式：（1、按英语成绩排序；2、按python成绩排序；3、按照Java成绩排序；0、按照总成绩排序）\n")
        if mode == '1':
            student_new.sort(key=lambda student_new:int(student_new['english']),reverse=asc_or_desc_bool)
            # 匿名函数lambda，这里student_new作为参数传入，表示列表中的每一项
        elif mode == '2':
            student_new.sort(key=lambda student_new:int(student_new['python']),reverse=asc_or_desc_bool)
        elif mode == '3':
            student_new.sort(key=lambda student_new:int(student_new['java']),reverse=asc_or_desc_bool)
        elif mode == '0':
            student_new.sort(key=lambda student_new:int(student_new['english'])+int(student_new['python'])+int(student_new['java']),
                             reverse=asc_or_desc_bool)
        else:
            print("输入有误，重新输入！")
            continue
        show_student(student_new)
        return

def total():
    if os.path.exists(filename):   # 检查学生信息文件是否存在
        with open(filename,'r',encoding='utf-8') as rfile:
            student = rfile.readlines()    # 获取文件的内容，并以列表的信息存储
            if student:               # 如果列表不空，则输出列表的长度，即学生信息条目
                print('一共有{0}学生'.format(len(student)))
            else:
                print('还没有录入学生信息')
    else:
        print('学生信息暂未保存')

def show():   # 显示所有学生信息
    student_lst = []    # 定义一个列表，用以保存学生的基本信息
    if os.path.exists(filename):  # 检查学生文件是否存在
        with open(filename,'r',encoding='utf-8') as rfile:   #
            students = rfile.readlines()
            for item in students:
                student_lst.append(eval(item))  # 将信息输入至列表中
            if student_lst:    # 如果列表不空，则调用show_student()函数输出列表的内容
                show_student(student_lst)
    else:
        print('暂未保存数据')

if __name__ == '__main__':
    main()


