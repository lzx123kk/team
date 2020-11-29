import re
import  requests
import xlsxwriter
import  time

def GetxxintoExcel(html):
    global count
    a = re.findall(r'"raw_title":"(.*?)"', html)      #名称
    b = re.findall(r'"view_price":"(.*?)"', html)   #价格~
    c = re.findall(r'"item_loc":"(.*?)"', html)   #地区
    d = re.findall(r'"view_sales":"(.*?)"', html)   #销量

    x = []    #excel表
    for i in range(len(a)):
        try:
            x.append((a[i],b[i],c[i],d[i]))
        except IndexError:
            break
    i = 0
    for i in range(len(x)):
        worksheet.write(count + i + 1, 0, x[i][0])
        worksheet.write(count + i + 1, 1, x[i][1])
        worksheet.write(count + i + 1, 2, x[i][2])
        worksheet.write(count + i + 1, 3, x[i][3])
    count = count +len(x)     #爬取总量
    return print("已完成")


def Geturls(q, x):   #q要查询的商品名称，x是要爬取的页数
    url = "https://s.taobao.com/search?q=" + q + "&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm" \
                                                 "=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306 "
    urls = []
    urls.append(url)
    if x == 1:
        return urls
    for i in range(1, x ):
        url = "https://s.taobao.com/search?q="+ q + "&commend=all&ssid=s5-e&search_type=item" \
              "&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306" \
              "&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=" + str(
            i * 44)
        urls.append(url)
    return urls


def GetHtml(url):
    r = requests.get(url,headers =headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r

if __name__ == "__main__":
    count=0
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        ,"cookie":"！ax__wpkreporterwid_=3d55eeb9-19b5-4af9-a8d7-61f5051fb364; miid=205897625319241678; ctoken=MdKHx8qOPlkoT48ccwxriNn8; lego2_cna=MD2RCC4CMCECH4R85HRTU5RK; _m_h5_tk=f50f8205a47060af1b455b19e5a9f0ce_1606058232706; _m_h5_tk_enc=45d24cb9622f4ee4800aedb5e8a68a24; cna=jb4yGMg1SEECAbfuTw/vYkEC; xlly_s=1; _samesite_flag_=true; cookie2=1ac584087c6cd41e59258742d5a19b49; t=675f1b70ff33d6742109a4c79687fdf1; _tb_token_=3eeebb77579a; sgcookie=E100GIZVJAT8unnkCWMl85GzAdh1W2owqbXMKwhEwSdnyj9Jq2gddw1i0i0%2FkTVQDTjUd3vmRFwB79Vn%2BUxHTUKK4Q%3D%3D; unb=3983794605; uc3=nk2=F5RGMcgWh11p8V0%3D&vt3=F8dCufwph9bbxge%2FQGE%3D&id2=UNk%2FSy7i%2FRxwaA%3D%3D&lg2=W5iHLLyFOGW7aA%3D%3D; csg=c83cc6ba; lgc=tb375503612; cookie17=UNk%2FSy7i%2FRxwaA%3D%3D; dnk=tb375503612; skt=eff8a07d506970c1; existShop=MTYwNjA0ODg5Mg%3D%3D; uc4=nk4=0%40FY4NBLDe1XeCXkXfA%2FKggN0MkWOWBw%3D%3D&id4=0%40Ug41Su%2BHJAMvuU%2BxKmWXnw98ymum; tracknick=tb375503612; _cc_=VFC%2FuZ9ajQ%3D%3D; _l_g_=Ug%3D%3D; sg=25b; _nk_=tb375503612; cookie1=BvbS1kiLjLo5Hib06l%2Bg%2BBI%2BRLIBHMVLQGqlC5MJS2M%3D; mt=ci=25_1; uc1=cookie15=WqG3DMC9VAQiUQ%3D%3D&cookie14=Uoe0azas1AgKoA%3D%3D&cookie21=UtASsssme%2BBq&existShop=false&pas=0&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D; thw=cn; enc=8aQIW%2BTlIfCd05S8N6Vla%2FZYio4L%2F3xQom9HUQpaJLZ1yum90HAhwwl20w1ahbRB%2F%2BsSRmxgQrtbOBLgvv6B8Q%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; v=0; tfstk=c9MOBQcsaeYgeHZK4fdhhRwDnrGOafsToGaAH3tLfCPW6FBAhsjKEYIF2CZVWJKd.; l=eBT66gV7OlGHaw4sBO5Zlurza77OFIObzsPzaNbMiInca1PG6UAALNQV73nJJdtjgtCA7F-r09hQ7RhD8MUdgmyD-JluBKWt3xvO.; isg=BDIybAz9uffGnoXLcByucnTcg3gUwzZdN3nA2PwKcOXyj9CJ41J6bXKtfysz_671"

                }       #把cookie前面的！ax去掉才可用cookie，不过使用频率不可太高
    q = input("输入货物")
    x = int(input("你想爬取几页"))
    urls = Geturls(q,x)
    workbook = xlsxwriter.Workbook(q+".xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.set_column('A:A', 70)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 20)
    worksheet.write('A1', '名称')
    worksheet.write('B1', '价格')
    worksheet.write('C1', '地区')
    worksheet.write('D1', '付款人数')
    #xx = []
    for url in urls:
        html = GetHtml(url)
        s = GetxxintoExcel(html.text)
        time.sleep(5)
    workbook.close()

