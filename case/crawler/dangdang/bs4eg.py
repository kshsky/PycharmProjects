from bs4 import BeautifulSoup
textStr='''
<！-- example -->
<div>
<div _expose="new_vs3_banner1" _wind="columnname=精选_剧场入口广告&amp;controlname=new_vs3_banner1" class="mod_row_box mod_row_box_special" data-context="6" id="new_vs3_banner1">
</div>
<div _expose="new_vs_hot_movie1" _wind="columnname=精选_电影预告&amp;controlname=new_vs_hot_movie1" class="mod_row_box" cur-page-num="0" data-context="6" data-istyle="4" has-next-page="false" id="new_vs_hot_movie1">
</div>

<div _expose="new_vs3_games" _wind="columnname=精选_精品游戏&amp;controlname=new_vs3_games" class="mod_row_box" cur-page-num="0" data-context="6" data-istyle="4" has-next-page="false" id="new_vs3_games">
</div>

<div _expose="new_vs3_banner2" _wind="columnname=精选_v首品牌专区&amp;controlname=new_vs3_banner2" class="mod_row_box mod_row_box_special" data-context="5" data-istyle="100">
</div>
</div>
'''
soup=BeautifulSoup(textStr,'lxml')
#打印出整齐有排面的样式
print(soup.prettify())
print('========================================')
##########################################################################
#找到包含整个元素的最小单元unit
unit = soup.find_all(name='div', class_='mod_row_box')
c=0

for i in unit:
    c+=1
    print('--- {} ---'.format(c))
    print(i.attrs['_wind'])

print('=================================================')
# --- 1 ---
# columnname=精选_剧场入口广告&controlname=new_vs3_banner1
# --- 2 ---
# columnname=精选_电影预告&controlname=new_vs_hot_movie1
# --- 3 ---
# columnname=精选_精品游戏&controlname=new_vs3_games
# --- 4 ---
# columnname=精选_v首品牌专区&controlname=new_vs3_banner2