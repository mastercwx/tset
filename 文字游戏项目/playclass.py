from sqlclass import *

SQL=Sqlserver()

# 玩家数据类系统
class Playerdata:
    __sql=SQL
    def __init__(self,uid) -> None:
        # 玩家qq
        self.uid=uid
        # 消息容器
        self.msg=None
        self.alldata=self.__sql.get_playerdata(uid)

        self.bag=self.alldata["bag"]
        self.weapon=self.alldata["weapon"]
        self.systemdata=self.alldata["system"]
        self.emailbox=self.alldata["email"]
        self.player_attribute_data=self.alldata["player_attribute_data"]
        
        
    # 背包变动
    def chmod_bag(self,name,value)->bool:
        # tabel_name='背包表名'
        if value>0:
            return True
        else:
            return True
    
    # 属性变动
    def chmod_attribute(self,name,value)->bool:
        # tabel_name='属性表名'
        if value>0:
            return True
        else:
            return True
        
    # 装备穿戴
    def chmod_weapon(self,name,valse)->bool:
        # tabel_name='装备表名'
        if valse>0:
            return True
        else:
            return True
        
    # 查看玩家基础属性
    def show_attribute(self):
        pass

    # 查看玩家详细属性
    def show_attribute_all(self):
        pass

    # 获得货币
    def add_gold(self,value,come_from=None)->bool:
        pass
    
    # 使用货币
    def sub_gold(self,value,come_from=None)->bool:
        pass

    # 保存数据

    def save(self):
        pass
    
    # 获取玩家总属性
    @property
    def player_attribute(self)->dict:
        pass
        

# 银行系统
class Bank:
    def __init__(self) -> None:
        pass
        

#商店系统
class Shop:
    __sql=SQL
    def __init__(self) -> None:
        self.all_shop=self.load_shopdata()
        self.a=123

    # 显示商店
    def show_shop(self):
        print('查看商店')
        print(self.all_shop)

    # 加载商店数据
    def load_shopdata(self)->dict:
        new_dict={}
        # 商店名
        shop_names=self.get_shop_names()
        for _ in shop_names:
            new_dict[_]=self.__sql.get_shopdata(_)

        return new_dict

    # 加载商店名
    def get_shop_names(self)->list:

        return [
            "1"
        ]



# 邮件系统
class Emailbox:
    __sql=SQL
    def __init__(self) -> None:
        pass

    # 查看邮件
    def show_email(self,player:Playerdata):
        pass

    # 领取邮件
    def get_email(self,player:Playerdata):
        pass

    # 发送邮件
    def send_email(self,player:Playerdata,email_data):
        pass


# 战斗系统
class Fight:
    def __init__(self) -> None:
        self.fight_lists[str,int]={}
    
    # 加载玩家数据
    def create_playter_data(self,player_1:Playerdata,player_2:Playerdata)->dict:
        pass

    # 开始战斗
    def start_fighting(self,fight_id):
        pass
    
# 物品系统
class Article:
    __sql=SQL
    def __init__(self) -> None:
        self.article_all_data=self.__sql.get_article_data()

    # 生成绝对id
    def generate_abs_id(self,article_id):
        pass


__all__=["Playerdata","Bank","Shop","Emailbox","Fight","Article"]