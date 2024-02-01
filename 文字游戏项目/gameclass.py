from  playclass import *
import datetime
import time
import sys

# 日常玩法
class Dailygame:
    def __init__(self) -> None:
        # 连续签到最大时间戳
        self.sign_in_time_max=172800
         

    # 签到
    def sign_in(self,player:Playerdata)->bool:
        time_=int(time.time())
        datatime=str(datetime.date.today())
        # 判断当日签到没签到
        if player.systemdata['sign_datatime']==datatime:
            print('签到过了')
        else:
            print('签到成功')
            if time_ - int(player.systemdata['sign_time'])<self.sign_in_time_max:
                print('连续签到')
            else:
                print('连续签到中断')

# 多人玩法
class Onlinegame:
    def __init__(self) -> None:
        pass


# 总系统
class Server:
    def __init__(self) -> None:
        # 玩家列表
        self.player_dict={
        }

        # 系统参数加载
        # self.system_dict=self.load_system()

    # 加载系统
    def load_system(self)->dict:
        config_dict=self.open_system_config()
        for _ in config_dict:
            pass
    
    # 加载系统配置
    def open_system_config(self)->dict:
        pass

    # 加载玩家到缓存区
    def player_load(self,uid):
        self.player_dict[uid]=Playerdata(uid)


# p1='0000'

# sys=Server()
# sys.player_load(p1)
# Dailygame().sign_in(sys.player_dict[p1])
# print(sys.player_dict)

module_obj = sys.modules['playclass']

# 获取 my_module 中的所有名称
module_contents = module_obj.__dict__
class_list=module_contents.get('__all__')

for _ in class_list:
    print(eval(_).__dict__)