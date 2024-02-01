import json
import logging
import os


logging.basicConfig(format='[%(asctime)s] [line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO,
                    filename='log.log',
                    filemode='a',
                    encoding="utf-8")
# 玩家数据库类


class Sqlserver:
    def __init__(self) -> None:
        self.palydir = 'sql/playersql/'
        self.systemdir = 'sql/systemsql/'

    def write_playerdata_log(self, uid, type_name, value):
        pass

    def write_playerdata(self, uid, type_name, value):
        pass

    # 获取玩家所有数据
    def get_playerdata(self, user_id) -> dict:
        alldata = {
            "bag": None,
            "email": None,
            "player_attribute_data": None,
            'system': None,
            "weapon": None
        }
        print(os.getcwd())
        for _ in alldata:
            with open(self.palydir+str(user_id)+'/'+_+'.json', encoding='utf-8') as f:
                alldata[_] = json.load(f)

        return alldata

    def write_shop(self, shopname, value):
        pass

    def get_shopdata(self, shopname) -> dict:
        if shopname == '1':
            return {"药瓶": 1}
        else:
            return {}

    def write_bag(self, type_name, value):
        pass

    def write_weapon(self, type_name, value):
        pass

    def get_article_data(self):
        dirname = 'sql/systemsql/articlesql/'
        load_file_dir = dirname+'load_config.json'
        new_dict = {}
        config_dict = {}
        try:
            with open(load_file_dir) as f:
                config_dict = json.load(f)
        except Exception as e:
            logging.error(str(e))
            return new_dict

        try:
            for _ in config_dict.get('name_list', []):
                with open(dirname+_+config_dict.get("type", ".json"), encoding='utf-8') as f:
                    new_dict[_] = json.load(f)

        except Exception as e:
            logging.error(str(e))
            return new_dict
        return new_dict

# a=Sqlserver()

# print(a.get_article_data())
