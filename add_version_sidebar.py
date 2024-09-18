import os
from bs4 import BeautifulSoup


folder_path = '.'  # html folder
template_file_path = './version_template.html' 
# read template
with open(template_file_path, 'r', encoding='utf-8') as template_file:
    template_content = template_file.read()

# check all html files in this folder.
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith('.html'):
            file_path = os.path.join(root, filename)

            # read html content.
            with open(file_path, 'r', encoding='utf-8') as html_file:
                soup = BeautifulSoup(html_file, 'html.parser')

            # find target div
            target_div = soup.find('div', class_='wy-grid-for-nav')

            # insert template
            if target_div:
                print(file_path)
                template_soup = BeautifulSoup(template_content, 'html.parser')
                target_div.insert_after(template_soup)

                with open(file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(str(soup))



