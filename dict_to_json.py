from datetime import datetime
import json
import os

example_dict = {
    "123": "tttt",
    "1123": ["123", "fffff"],
    "fffff": "d12c%%^^",
    "c": "你好啊！！"
}

def main(save_json_path, save_json_name, data_dict):
    """
    :param save_json_path: 你要儲存 JSON 的位置
    :param save_json_name: 你要將字典存入到 JSON 的檔案名稱叫做什麼
    :param data_dict: 字典資料
    """
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(save_json_path + save_json_name + ".json", 'w') as json_file:
        json.dump(data_dict, json_file)
    print("[%s] JSON 檔案儲存至: %s" % (now_time, save_json_path + save_json_name + ".json"))

# 使用示例字典進行函數調用
main(save_json_path=os.getcwd() + '/', save_json_name='test', data_dict=example_dict)
