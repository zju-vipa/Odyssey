from pathlib import Path
import numpy as np
import re
import pandas as pd 
def merge_results(results_dir: Path, task: str, output_dir: Path):
    output_dir.mkdir(exist_ok=False, parents=True)
    for _dir in results_dir.iterdir():
        if _dir.is_dir():
            task_results_dir = _dir / 'results' / task
            if task_results_dir.exists():
                for _file in task_results_dir.iterdir():
                    if _file.is_file():
                        new_file = output_dir / _file.name
                        # breakpoint()
                        with open(_file, 'r') as f:
                            data = f.read()
                        with open(new_file, 'a') as f:
                            f.write(data)

def extract_infos_and_errors(result_file: Path, task: str = 'combat')->tuple[list[dict], list[dict]]:
    with open(result_file, 'r') as f:
        data = f.read()
    lines = data.split('\n')
    infos = []
    errors = []
    # 正则表达式，提取关键信息
    if task == 'combat':
        pattern1 = r'Route (\d+); Plan list: \[(.*?)\]; Equipments obtained: \[(.*?)\]; Ticks on each step: \[(.*?)\]; LLM iters: (\d+); Health: (\d+\.\d+).*'
        pattern2 = r'Route (\d+): Plan list: \[(.*?)\], Equipments obtained: \[(.*?)\], Ticks on each step: \[(.*?)\], LLM iters: (\d+), Health: (\d+\.\d+).*'
        error_pattern = r'.*caused by (.*)'
    else:
        raise NotImplementedError(f"Task {task} pattern not implemented.")

    for line in lines:
        # 使用正则表达式提取信息
        
        error_info = re.search(error_pattern, line)
        if error_info:
            # print('error:', error_info.group(1))
            error = error_info.group(1)
            if error not in errors:
                errors.append(error)
        else:
            extracted_info = re.search(pattern1, line)
            if not extracted_info:
                extracted_info = re.search(pattern2, line)
            if extracted_info:
                route = int(extracted_info.group(1))
                plan_list = [plan.strip() for plan in extracted_info.group(2).split(', ')]
                equipments_obtained = [equip.strip() for equip in extracted_info.group(3).split(', ')]
                ticks_on_each_step = [int(tick) for tick in extracted_info.group(4).split(',')]
                last_ticks = ticks_on_each_step[-1]
                minutes = last_ticks / 1200
                llm_iters = int(extracted_info.group(5))
                health = float(extracted_info.group(6))
                infos.append({'route': route, 'plan_list': plan_list, 'equipments_obtained': equipments_obtained, 'ticks_on_each_step': ticks_on_each_step, 'last_ticks': last_ticks, 'minutes': minutes , 'llm_iters': llm_iters, 'health': health})
                # print(f"Route: {route}, Last Ticks: {last_ticks}, LLM iters: {llm_iters}, Health: {health}")
            else:
                if line not in ['', '\n', '\t']:
                    print(line)
    errors = [{'error': error} for error in errors]
    return infos, errors

def merge_csvfiles(csv_file1: Path, csv_file2: Path, output_file: Path, *additional_csv_files: Path):
    df1 = pd.read_csv(csv_file1)
    df2 = pd.read_csv(csv_file2)
    dfs = [df1, df2]
    for _file in additional_csv_files:
        dfs.append(pd.read_csv(_file))
    concats = pd.concat(dfs, axis=0)
    # inplace = True, 会直接修改concats 数据帧，而不创建返回新数据帧
    concats.drop_duplicates(inplace=True)
    concats.to_csv(output_file, index=False)

def cal_avg_and_std(csv_file: Path, output_dir:Path):
    df = pd.read_csv(csv_file)
    sucess_rate = []
    indexs = []
    nums = []
    for col in df.columns:
        if col.endswith('health'):
            failed = df[col].eq(0).sum()
            total = df[col].notna().sum()
            nums.append(total)
            if total == 0:
                sucess_rate.append(0)
            else:
                sucess_rate.append((total - failed) / total*100)
            indexs.append(col.replace('health', 'success_rate'))
            df[col] = df[col].replace(0, np.nan)
    
    success_rate_df = pd.DataFrame({'success_rate': sucess_rate, 'nums': nums}, index=indexs)
    avg = df.mean()
    std = df.std()
    avg_std_df = pd.DataFrame({'avg': avg, 'std': std})
    pd.concat([success_rate_df, avg_std_df], axis=1).to_csv(output_dir / 'avg_std_success_rate.csv')

def main():
    # ------need to modify-----
    all_results_dir = Path(__file__).parent.parent.parent / f'results/combat_results_66_2'
    suffix = '66_2'
    # ------need to modify-----
    # merge_output_dir = all_results_dir.parent / f'merged_results_{suffix}'

    # merge_results(all_results_dir, 'combat', output_dir=merge_output_dir)

    # all_errors = []
    # all_infos_df = []
    # for _file in merge_output_dir.iterdir():
    #     if _file.is_file() and _file.suffix == '.txt':
    #         infos, errors = extract_infos_and_errors(_file, 'combat')
    #         all_errors += errors
    #         all_infos_df.append(pd.DataFrame(infos).add_prefix(f'{_file.stem}_')) 
    #         # pd.DataFrame(errors).to_csv(_file.parent / f'{_file.stem}_errors.csv', index=False)
    #         # break
    # pd.DataFrame(all_errors).to_csv(all_results_dir.parent / f'all_errors_{suffix}.csv', index=False)
    # pd.concat(all_infos_df, axis=1).to_csv(all_results_dir.parent / f'all_infos_{suffix}.csv', index=False)

    csv_file1 = all_results_dir.parent / 'all_infos_66.csv'
    csv_file2 = all_results_dir.parent / 'all_infos_64.csv'
    output_file = all_results_dir.parent / 'all_infos.csv'
    merge_csvfiles(csv_file1, csv_file2, output_file, all_results_dir.parent / 'all_infos_66_2.csv')
    
    # csv_file = all_results_dir.parent / 'all_infos.csv'
    # cal_avg_and_std(csv_file, output_dir=all_results_dir.parent)

def test():
    line = '''Route 0; Plan list: ['craft wooden sword', 'craft iron helmet', 'craft iron leggings', 'craft iron boots']; Equipments obtained: [None, None, None, None, 'crafting_table', None]; Ticks on each step: [322, 609, 898, 1098, 1329, 12723, 13172, 13489, 13813, 15231, 15549, 15867, 16179, 16489, 16803, 17120]; LLM iters: 16; Health: 0.0; Combat result: failed'''
    pattern1 = r'Route (\d+);.*Ticks on each step: \[(.*?)\]; LLM iters: (\d+); Health: (\d+\.\d+).*'
    pattern2 = r'Route (\d+):.*Ticks on each step: \[(.*?)\], LLM iters: (\d+), Health: (\d+\.\d+).*'
    error_pattern = r'.*caused by (.*)'
    error_info = re.search(error_pattern, line)
    extracted_info = re.search(pattern1, line)
    if not extracted_info:
        extracted_info = re.search(pattern2, line)
    if extracted_info:
        route = int(extracted_info.group(1))
        last_ticks = int(extracted_info.group(2).split(',')[-1])
        minutes = last_ticks / 1200
        llm_iters = int(extracted_info.group(3))
        health = float(extracted_info.group(4))
        print(f"Route: {route}, Last Ticks: {last_ticks}, LLM iters: {llm_iters}, Health: {health}")

if __name__ == '__main__':
    main()


