import requests  #请求
import pprint  #打印
import os  #导入操作系统接口模块（内置）
import re  #正则表达式

url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'  #需要获取图片信息的地址

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'  #加入伪装
}

def change_title(title):  #修改爬取的内容中出现的不能保存的符号
    mode = re.compile(r'[\\\/\:\*\?\"\<\>\|]')
    new_title = re.sub(mode, '_', title)  #把上面出现的符号转换为“_”
    return new_title

def save(title,name,img_url):  #图片保存函数
    filename = f'{title}\\'  #保存到独立的英雄文件夹
    if not os.path.exists(filename):  #if判断是否存在文件夹
        os.mkdir(filename)  #创建文件夹
    img_content = requests.get(url=img_url, headers=headers).content  #获取图片内容，即二进制数据
    with open(filename + name + '.jpg', mode='wb') as f:
        f.write(img_content)  #写入图片数据
        print(name)


response = requests.get(url=url, headers=headers)  #解析数据，获取英雄数据信息
# pprint.pprint(response.json())

hero_list = response.json()['hero']  #返回解析数据中hero的信息
for index in hero_list:  #使用for循环，遍历出所有的英雄名称（heroId）
    # pprint.pprint(index)
    hero_id = index['heroId']
    hero_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'.format(hero_id)  #format格式化函数，把hero_id传入
    response_1 = requests.get(url=hero_url, headers=headers)  #获取英雄图片信息
    pprint.pprint(response_1.json())
    skins = response_1.json()['skins']  #返回解析数据中的skins信息（皮肤信息）
    for lol in skins:
        img_url = lol['mainImg']  #皮肤图片地址
        title = lol['heroTitle']  #英雄名字
        name = lol['name']        #皮肤名字

        new_name = change_title(name)
        new_title = change_title(title)

        if img_url:
            save(new_title, new_name, img_url)
        else:
            chroma_img = lol['chromaImg']  #获取炫彩的皮肤
            save(new_title, new_name, chroma_img)
