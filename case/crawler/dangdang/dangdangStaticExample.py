from bs4 import BeautifulSoup

bookMsg = '''
   <!-- 图书展示区 begin -->
   <div class="product_main clearfix" dd_name="单品区域">
    <div class="pic_info">
     <!-- 大图区开始 -->
     <div class="pic" id="largePicDiv">

      <div class="big_pic" id="detailPicDiv" style="display: none;">
       <img alt="东野圭吾：解忧杂货店（胡歌、王俊凯、刘昊然倾情推荐，东野圭吾长篇小说代表作，这家店帮你找回内心流失的东西）
易中天、王安忆盛赞。畅销天王东野圭吾长篇小说代表作，登顶北大图书馆预约榜，5年销量超900万册，豆瓣40万人点评8.5高分，创造出版奇迹！" height="800" id="detailPic" src="//img3m8.ddimg.cn/92/3/23464478-1_u_10.jpg" width="800"/>
      </div>
<div class="messbox_info">
        <span class="t1" dd_name="作者" ddt-area="002" id="author">
         作者:(日)
         <a dd_name="作者" href="http://search.dangdang.com/?key2=%B6%AB%D2%B0%B9%E7%CE%E1&amp;medium=01&amp;category_path=01.00.00.00.00.00" target="_blank">
          东野圭吾
         </a>
         著，
         <a dd_name="作者" href="http://search.dangdang.com/?key2=%D0%C2%BE%AD%B5%E4&amp;medium=01&amp;category_path=01.00.00.00.00.00" target="_blank">
          新经典
         </a>
         出品
        </span>
        <span class="t1" dd_name="出版社" ddt-area="003">
         出版社:
         <a dd_name="出版社" href="http://search.dangdang.com/?key3=%C4%CF%BA%A3%B3%F6%B0%E6%B9%AB%CB%BE&amp;medium=01&amp;category_path=01.00.00.00.00.00" target="_blank">
          南海出版公司
         </a>
        </span>
        <span class="t1">
         出版时间:2014年05月
        </span>
        <!-- 评论数 -->
        <div class="pinglun clearfix">
         <!-- 排名 -->
         <span class="t1" dd_name="图书排行榜排名" id="pubbang" style="display:none">
         </span>
         <!-- 星级 -->
         <span class="t1" id="messbox_info_comm_num" style="display:none">
          <span class="star_box">
           <span class="star" style="width:97%">
           </span>
          </span>
          <a dd_name="评论数" href="javascript:void(0)" id="comm_num_down">
           2306257
          </a>
          条评论
         </span>
         <!--        <a href="javascript:;" class="score write_comment" id="w-comment">我要写评论</a>-->
        </div>
</div>
<div class="price_pc" id="pc-price">
     <div style="width:206px;height: 64px;">
      <div class="price_d">
       <p class="t">
        <span id="dd-price-text">
         当当价
        </span>
        <a class="price_down_remind score write_comment" href="javascript:void(0);" id="price_down">
         降价通知
        </a>
       </p>
       <p id="dd-price">
        <span class="yen">
         ¥
        </span>
        29.60
       </p>
      </div>
      <div class="price_zhe" id="dd-zhe">
      </div>
     </div>
     <div style="width:206px;height: 35px">
      <div class="price_m price_m_t" id="original-price-text">
       定价
      </div>
      <div class="price_m" id="original-price">
       <span class="yen">
        ¥
       </span>
       39.50
      </div>
      <div class="price_vip" id="dd-vip" style="display:none">
       <span>
       </span>
      </div>
     </div>
</div>
<div class="t_box_left" dd_name="商品详情" id="detail_all" name="Detail_pub">
       <div class="pro_content" ddt-area="010" id="detail_describe">
        <ul class="key clearfix">
         <li>
          开 本：32开
         </li>
         <li>
          纸 张：胶版纸
         </li>
         <li>
          包 装：精装
         </li>
         <li>
          是否套装：否
         </li>
         <li>
          国际标准书号ISBN：9787544270878
         </li>
         <li class="clearfix fenlei" dd_name="详情所属分类" id="detail-category-path">
          <label>
           所属分类：
          </label>
          <span class="lie">
           <a class="green" data-category-id="1805" href="http://category.dangdang.com/cp01.00.00.00.00.00.html" target="_bland">
            图书
           </a>
           &gt;
           <a class="green" data-category-id="11656" href="http://category.dangdang.com/cp01.03.00.00.00.00.html" target="_bland">
            小说
           </a>
           &gt;
           <a class="green" data-category-id="16846" href="http://category.dangdang.com/cp01.03.45.00.00.00.html" target="_bland">
            社会小说
           </a>
          </span>
         </li>
        </ul>
'''

soup2 = BeautifulSoup(bookMsg, 'lxml')
# 打印出整齐有排面的样式
print(soup2.prettify())
unit = soup2.find(name='div', class_='product_main clearfix')

# 作者
print('作者：', unit.find(id='author').find(name='a').string.strip())
print('作者：', unit.find_all(class_='t1')[0].find_all(name='a')[0].string.strip())
# 图片
print('图片：', unit.find(class_='big_pic').find(name='img').attrs['src'])
# 出版社
print('出版社：', unit.find_all(class_='t1')[1].find(name='a').string.strip())
# 出版时间
print('出版时间：', unit.find_all(class_='t1')[2].string.strip())
# 价格
'''

      <div class="price_m" id="original-price">
       <span class="yen">
        ¥
       </span>
       39.50
      </div>

'''
print('价格', unit.find(id='original-price').get_text(strip=True))
print('价格', unit.find(id='original-price').get_text(strip=True)[1:])
print('价格', unit.find(id='original-price').contents[2].strip())
print('价格', unit.find(id='original-price').string)
print('价格', unit.find(id='original-price').text.strip())

book_detail = soup2.find(name='ul', class_='key clearfix')

print(book_detail.find_all(name='li')[0].string.strip())
print(book_detail.find_all(name='li')[1].string.strip())
print(book_detail.find_all(name='li')[2].string.strip())
print(book_detail.find_all(name='li')[3].string.strip())
print(book_detail.find_all(name='li')[4].string.strip())