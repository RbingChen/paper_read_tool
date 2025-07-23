#coding:utf-8

import json
import re

def extract_json_simple(input_str):
    """
    通过定位第一个 { 和最后一个 } 提取 JSON 字符串

    参数:
    input_str: 包含 JSON 的原始字符串

    返回:
    提取的 JSON 字符串
    """
    # 找到第一个 { 的位置
    start_index = input_str.find('{')
    if start_index == -1:
        return None

    # 找到最后一个 } 的位置
    end_index = input_str.rfind('}')
    if end_index == -1 or end_index < start_index:
        return None
    json_str = input_str[start_index:end_index+1]
    try:
        import json
        json_obj = json.loads(json_str)
        print("\n解析后的 JSON 对象:")
        print(json.dumps(json_obj, indent=2, ensure_ascii=False))
        return json_obj
    except:
        print("\n注意：提取的字符串不是有效的 JSON，可能需要手动处理")
    # 提取 JSON 部分（包含大括号）
    return None


def extract_json_from_string(input_str):
    """
    从包含 JSON 的字符串中提取 JSON 对象

    参数:
    input_str: 包含 JSON 的原始字符串

    返回:
    提取的 JSON 对象（字典形式）
    """
    # 方法1：使用正则表达式匹配完整的 JSON 对象
    json_match = re.search(r'\{[\s\S]*\}', input_str)
    if json_match:
        json_str = json_match.group(0)
        try:
            # 尝试解析为 JSON
            return json.loads(json_str)
        except json.JSONDecodeError:
            # 如果解析失败，尝试修复常见的格式问题
            pass

    # 方法2：直接搜索特定键（更健壮的方法）
    if '"output":' in input_str:
        # 找到 JSON 对象的起始位置
        start_index = input_str.find('{')
        if start_index == -1:
            return None

        # 手动解析 JSON
        brace_count = 0
        in_string = False
        escape = False
        json_chars = []

        for char in input_str[start_index:]:
            json_chars.append(char)

            # 处理转义字符
            if char == '\\' and in_string:
                escape = not escape
                continue
            else:
                escape = False

            # 处理字符串边界
            if char == '"' and not escape:
                in_string = not in_string

            # 处理大括号计数
            if not in_string:
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        # 找到完整的 JSON 对象
                        json_str = ''.join(json_chars)
                        try:
                            return json.loads(json_str)
                        except json.JSONDecodeError:
                            # 如果仍然失败，返回原始字符串
                            return json_str

    return None


def string_find_json(text):
    try:

        json_string = re.search(r'\{.*?\}', text, re.DOTALL).group(0)
        print(json_string)
        json_data = json.loads(json_string)
        #print(json_data)
        return json_data

    except Exception as e:
        return None

    return None


def extract_and_repair_html(raw_text):
    """
    从原始字符串中提取完整的 HTML 内容，并补全缺失的闭合标签

    参数:
        raw_text (str): 包含 HTML 的原始字符串（可能包含冗余字符）

    返回:
        str|None: 修复后的完整 HTML 内容，若未找到有效 HTML 则返回 None
    """
    # 正则表达式匹配 HTML 内容
    pattern = r'<!DOCTYPE html>(?:(?!<!DOCTYPE html>).|[\r\n])*?(?:<\/html>|$)'
    match = re.search(pattern, raw_text, re.DOTALL)

    if not match:
        return None  # 未找到有效 HTML

    html_content = match.group(0)

    # # 补全缺失的 </body> 和 </html> 标签
    # repaired = False
    # if '</body>' not in html_content and '</html>' in html_content:
    #     html_content = html_content.replace('</html>', '</body></html>')
    #     repaired = True
    # if '</html>' not in html_content:
    #     html_content += '</html>'
    #     repaired = True
    #
    # # 补全缺失的 <html> 标签
    # if '<html' in html_content and not re.search(r'<\/html>', html_content, re.I):
    #     html_content += '</html>'
    #     repaired = True
    #
    # # 输出修复信息（可选）
    # if repaired:
    #     print("已修复 HTML 结构")

    return html_content.strip()