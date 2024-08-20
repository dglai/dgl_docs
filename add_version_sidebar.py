import os
from bs4 import BeautifulSoup

# 设定文件夹路径和模板文件路径
folder_path = '.'  # 替换为你 HTML 文件夹的路径
template_file_path = './version_template.html'  # 替换为 template.html 的路径

# 读取模板文件内容
with open(template_file_path, 'r', encoding='utf-8') as template_file:
    template_content = template_file.read()

# 递归遍历文件夹中的所有 HTML 文件
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith('.html'):
            file_path = os.path.join(root, filename)

            # 读取 HTML 文件内容
            with open(file_path, 'r', encoding='utf-8') as html_file:
                soup = BeautifulSoup(html_file, 'html.parser')

            # 找到目标 div 标签
            target_div = soup.find('div', class_='wy-grid-for-nav')

            # 插入模板内容
            if target_div:
                print(file_path)
                template_soup = BeautifulSoup(template_content, 'html.parser')
                target_div.insert_after(template_soup)

                # 将修改后的 HTML 写回文件
                with open(file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(str(soup))


