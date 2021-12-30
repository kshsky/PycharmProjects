import os
import os.path

html_path = r'F:\PDF\python_html_to_pdf\html'
pdf_path = r'F:\PDF\python_html_to_pdf'

html_set = set()
for root,dirs,file in os.walk(pdf_path):
    print(root)
    print(dirs)
    print(file)

    print('---------------------------------')
    # for i in directory:
    #     print(i)
    # print('---------------------------------')
    # for i in file[:7]:
    #     # print(os.path.abspath(i))
    #     print(os.path.dirname(i))
    #     # html_set.add(i)
print('---------------------------------')
# for i in html_set:
#     print(i)