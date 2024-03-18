import requests
import pandas as pd
from bs4 import BeautifulSoup

req = requests.get('https://coinmarketcap.com/')
# print(req)
link = BeautifulSoup(req.text, 'html.parser')
# print(link)

main = link.find_all('div', attrs={'class': 'sc-14cb040a-2 hptPYH'})
# print(main)

header_list = []
data_set = []
for obj in main:
    for table_id in obj.find_all('table'):
        for table_trs in table_id.find_all('tr'):
            if table_trs.find_all('th'):
                for header_data in table_trs.find_all('th'):
                        header_list.append(header_data.get_text())
            else:
                list_with_td = []
                for body_data in table_trs.find_all('td'):
                    if body_data.get_text().strip() != '':
                        # list_with_td.append(float(body_data.get_text())) sau
                        list_with_td.append(body_data.get_text().replace(',', '.'))

                print(list_with_td)
                data_set.append(list_with_td)


# ceva nu-i bine in output


# main = link.find_all('div', attrs={'id': 'contentDiv'})
# print(main)

# header_list = []
# data_set = []
# for obj in main:
#     for table_id in obj.find_all('table'):
#         for table_trs in table_id.find_all('tr'):
#             if table_trs.find_all('th'):
#                 for header_data in table_trs.find_all('th'):
#                     if header_data.get_text() != 'HRK':
#                         header_list.append(header_data.get_text())
#             else:
#                 list_with_td = []
#                 for body_data in table_trs.find_all('td'):
#                     if body_data.get_text().strip() != '':
#                         # list_with_td.append(float(body_data.get_text())) sau
#                         list_with_td.append(body_data.get_text().replace(',', '.'))
#
#                 print(list_with_td)
#                 data_set.append(list_with_td)

# print(header_list)
# print(data_set)

# [header] [body [] [] [] []]

# df = pd.DataFrame(data_set, columns=header_list)
# df.to_excel('Curs_BNR_data.xlsx', index=False)
# print(df)

# pip install openpyxl pentru fisiere .xlsx
