import sys
import os
import django

# 1、将项目的根目录填入环境变量
BASE_DIR = os.path.dirname('D:/PycharmProjects/web/Django/djangoDaily')
sys.path.append(BASE_DIR)

# 2、引入项目的配置环境，然后无需启动django项目就可以使用其配置环境了
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoDaily.settings')
django.setup()

# 可以将上述代码粘贴进交互式环境，直接在交互式环境测试

if __name__ == "__main__":
    # 编写测试代码，直接运行本文件即可
    from app01.models import Employee

    obj = Employee(name="Egon", gender=0, birth='1997-01-27', department="财务部", salary=100.1)
    obj.save()

    obj = Employee.objects.filter(name="Egon").first()  # 查询所有名字为Egon的记录并取第一条
    print(obj.id, obj.name, obj.birth)  # 输出1 Egon 1997-01-27

    Employee.objects.filter(name="Egon").update(name="EGON")  # 过滤出所有名字为Egon的记录并将name字段改成大写EGON

    Employee.objects.filter(name="EGON").delete()  # 过滤出所有名字为EGON的记录并删除

    all = Employee.objects.all().values()
    print(all)

