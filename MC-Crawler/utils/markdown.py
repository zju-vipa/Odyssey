from pathlib import Path
class LIST_TYPE:
    OL = 'ol'
    UL = 'ul'
def to_md_table(table_content: list[list[str]])->str:
    if not table_content:
        return ""

    # Determine maximum width of each column
    column_widths = [max(len(str(item)) for item in column) for column in zip(*table_content)]

    # Create the Markdown table string
    markdown_table = ""

    # Add header row
    header_row = [item.replace('\n', ' ') for item in table_content[0]]

    markdown_table += "| " + " | ".join(f"{item:{column_widths[i]}}" for i, item in enumerate(header_row)) + " |\n"

    # Add separator row
    markdown_table += "|-" + "-|-".join("-" * width for width in column_widths) + "-|\n"

    # Add data rows
    for row in table_content[1:]:
        row = [item.replace('\n', ' ') for item in row]
        try:
            markdown_table += "| " + " | ".join(f"{item:{column_widths[i]}}" for i, item in enumerate(row)) + " |\n"
        except Exception as e:
            breakpoint()

    return markdown_table+'\n'

def to_header(title: str, level: int)->str:
    return f"{'#' * level} {title}\n"

def to_list(items: list[dict], list_type: LIST_TYPE, depth: int=0)->str:
    list_str = ''
    if list_type == LIST_TYPE.OL:
        list_str += to_o_list(items, depth=depth)
    elif list_type == LIST_TYPE.UL:
        list_str += to_u_list(items, depth=depth)
    return list_str
def to_u_list(items: list[dict], depth: int=0)->str:
    list_str = ''
    for item in items:
        list_str += '\t'*depth
        list_str += '- '
        list_str += item['title']
        list_str += '\n'

        if item.get('sub_sections'):
            list_str += to_list(item['sub_sections'], list_type=item['sub_sections_list_type'],depth=depth+1)
    return list_str

def to_o_list(items: list[dict], depth: int=0)->str:
    list_str = ''
    for i, item in enumerate(items):
        list_str += '\t'*depth
        list_str += f'{i+1}. '
        list_str += item['title']
        list_str += '\n'
        if item.get('sub_sections'):
            list_str += to_list(item['sub_sections'], list_type=item['sub_sections_list_type'],depth=depth+1)
    return list_str

def split_file(file_path: Path, word_count_limit: int = 1000, word_count_thres:int = 40):
    # word_count_threshold: if the word count of a split file is less than this value, delete it
    # because crawler still crawl some unimportant content, like "See also"...s
    print(f'Splitting {file_path}...')
    # read content of origin files
    with open(file_path, 'r') as f:
        filename = file_path.stem
        content = f.read()
    lines = content.split('\n')
    total_line_count = len(lines)
    total_word_count = len(content.split())
    # check if the file has been split
    split_file_dir = file_path.parent.parent / f'{file_path.parent.name}_split'
    split_file_dir.mkdir(exist_ok=True, parents=True)
    if (split_file_dir / f'{filename}.md').exists() or (split_file_dir / f'{filename}_0.md').exists():
        print(f'{filename} has been split. Skip.')
        return
    # no need to split
    # if total_word_count <= word_count_limit:
    #     with open(split_file_dir / f'{filename}.md', 'w') as split_f:
    #         split_f.write(content)
    #     return
    
    # determine the minimum number of split files
    split_file_num = 1
    while total_word_count / split_file_num > word_count_limit:
        split_file_num += 1
    # I want all split files to have similar word count
    word_count_limit = total_word_count // split_file_num
    start_line = 0
    for i in range(split_file_num):
        # maybe some chapters are very long
        # maybe chapters number is less than split_file_num
        if start_line == total_line_count:
            print('there is no more content to split')
            break
        word_count = 0
        split_content = []
        with open(split_file_dir / f'{filename}_{i}.md', 'w') as split_f:
            for line_i in range(start_line, total_line_count):
                line = lines[line_i]
                split_line = line.split()
                if len(split_line)>0 and split_line[0] in ['#', '##', '###', '####', '#####', '######']:
                    if word_count > word_count_limit and i != split_file_num-1:
                        start_line = line_i
                        for split_content_line in split_content:
                            split_f.write(split_content_line+'\n')
                        break
                word_count += len(line.split())
                split_content.append(line)
                if line_i == total_line_count-1:
                    start_line = line_i+1
                    for split_content_line in split_content:
                        split_f.write(split_content_line+'\n')
                    break
            print(f'generate {split_file_dir / f"{filename}_{i}.md"}: {word_count} words')
        if word_count < word_count_thres:
            (split_file_dir / f'{filename}_{i}.md').unlink()
            print(f'delete {split_file_dir / f"{filename}_{i}.md"}: {word_count} words less than {word_count_thres}')
    print()
                



if __name__ == '__main__':
    # items = [{'title': '1 Obtaining', 'sub_sections': [{'title': '1.1 Mining'}, {'title': '1.2 Chest loot'}, {'title': '1.3 Suspicious sand loot'}, {'title': '1.4 Crafting'}, {'title': '1.5 Smelting'}]}, {'title': '2 Usage', 'sub_sections': [{'title': '2.1 Crafting ingredient'}, {'title': '2.2 Trading'}, {'title': '2.3 Repairing'}, {'title': '2.4 Beacons'}, {'title': '2.5 Smithing ingredient'}]}, {'title': '3 Data values', 'sub_sections': [{'title': '3.1 ID'}]}, {'title': '4 Achievements'}, {'title': '5 Advancements'}, {'title': '6 History'}, {'title': '7 Issues'}, {'title': '8 Trivia'}, {'title': '9 Gallery', 'sub_sections': [{'title': '9.1 Screenshots'}, {'title': '9.2 In other media'}]}, {'title': '10 External links'}]
    # with open('list.md', 'w') as f:
    #     f.write(to_list(items))
    split_file(Path('/Users/akai/Documents/mc/汇报/4.10/mc_crawler/crawler_data/Item_urls/Acacia_Boat.md'))
