import configparser
import threading


class FluentInit(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        conf = configparser.ConfigParser()
        conf.read("aop/fluent_config.ini")
        self.aop_status = conf.get("fluent.aop", "fluent.aopStatus")
        self.project_name = conf.get("fluent.aop", "project.name")
        self.fluent_url = conf.get("fluent.aop", "fluent.url")
        self.fluent_port = conf.get("fluent.aop", "fluent.port")

    def __new__(cls, *args, **kwargs):
        if not hasattr(FluentInit, "_instance"):
            with FluentInit._instance_lock:
                if not hasattr(FluentInit, "_instance"):
                    FluentInit._instance = object.__new__(cls)
        return FluentInit._instance
    # conf = configparser.ConfigParser()
    # conf.read("aop/fluent_config.ini")
    # aop_status = conf.get("fluent.aop", "fluent.aopStatus")
    # project_name = conf.get("fluent.aop", "project.name")
    # fluent_url = conf.get("fluent.aop", "fluent.url")
    # fluent_port = conf.get("fluent.aop", "fluent.port")
# obj1 = FluentInit()
# obj2 = FluentInit()
# print(obj1,obj2)
# def task(arg):
#     obj = FluentInit()
#     print(obj)
#
# for i in range(10):
#     t = threading.Thread(target=task,args=[i,])
#     t.start()