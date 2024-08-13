import json

# 文件路径
pre_item_path = 'MCskill/json/pre_item.json'
pre_tool_path = 'MCskill/json/pre_tool.json'
pre_smelt_path = 'MCskill/json/pre_smelt.json'
func_path = 'MCskill/json/func.json'

# 读取JSON文件
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# 写入JSON文件
def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# 排序函数
def sort_func_json_data(data):
    # 将字典按值排序，值相同的按键排序
    sorted_data = dict(sorted(data.items(), key=lambda item: (item[1], item[0])))
    return sorted_data

# 更新func.json并记录冲突
def update_func_json():
    # 读取所有JSON文件
    pre_item_data = read_json(pre_item_path)
    pre_tool_data = read_json(pre_tool_path)
    pre_smelt_data = read_json(pre_smelt_path)
    func_data = read_json(func_path)

    # 记录更新过程中的所有键及其出现次数
    key_counts = {}

    # 更新函数，记录键出现次数
    def update_keys(data, value):
        for key in data.keys():
            if key not in key_counts:
                key_counts[key] = 0
            key_counts[key] += 1
            if key_counts[key] == 1:
                func_data[key] = value

    # 更新func.json
    update_keys(pre_item_data, 'craft')
    update_keys(pre_tool_data, 'mine')
    update_keys(pre_smelt_data, 'smelt')

    # 记录冲突的键
    conflicts = [key for key, count in key_counts.items() if count > 1]

    # 排序func.json
    sorted_func_data = sort_func_json_data(func_data)

    # 写回func.json
    write_json(sorted_func_data, func_path)

    # 输出冲突的键
    if conflicts:
        print("Conflicts detected for the following keys:")
        for conflict in conflicts:
            print(conflict)

# 排序函数
def sort_func_json(file_path):
    data = read_json(file_path)
    # 将字典按值排序，值相同的按键排序
    sorted_data = dict(sorted(data.items(), key=lambda item: (item[1], item[0])))
    write_json(sorted_data, file_path)

# 运行排序函数
sort_func_json(func_path)

