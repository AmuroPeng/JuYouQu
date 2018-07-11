from pos_generation import get_loc
from module import add_shop


def add_shops():
    # 添加商铺:
    result = get_loc('北京市朝阳区劲松北路2号楼')
    add_shop('北京麦当劳潘家园餐厅', '北京市朝阳区劲松北路2号楼', result['lng'], result['lat'], 5.0,
             '营业时间： 00:00-04:45 / 05:15-10:15 / 10:30-23:55', '美食', '/picture/0.jpg')

    result1 = get_loc('北京市朝阳区东四环南路9号')
    add_shop('和合谷(朝阳区燕莎奥特莱斯店)', '北京市朝阳区东四环南路9号新燕莎奥特莱斯MALLC座三层3021', result1['lng'], result1['lat'], 5.0,
             '营业时间： 10:00-20:00', '美食', '/picture/1.jpg')

    result2 = get_loc('海淀区中关村海淀大街34号海置创投大厦')
    add_shop('东来顺饭庄（中关村海淀大街店）', '海淀区中关村海淀大街34号海置创投大厦', result2['lng'], result2['lat'], 4.2, '周一至周日 10:00-21:30', '美食',
             '/picture/2.jpg')

    result3 = get_loc('海淀区复兴路甲36号百朗园')
    add_shop('好伦哥（永定路店）', '海淀区复兴路甲36号百朗园东北角', result3['lng'], result3['lat'], 3.4, '营业时间： 10:30-21:30', '美食',
             '/picture/3.jpg')

    result4 = get_loc('朝阳区朝阳北路107号院')
    add_shop('火宴山（大悦城店）', '朝阳区朝阳北路107号院58号楼二层', result4['lng'], result4['lat'], 3.5, '营业时间：周一至周日 11:00-22:30', '美食',
             '/picture/4.jpg')

    result5 = get_loc('通州区新华西街')
    add_shop('京八珍（新华店）', '通州区新华西街西门物美生活超市隔壁', result5['lng'], result5['lat'], 3.9, '营业时间：周一至周日 07:00-21:30', '美食',
             '/picture/5.jpg')

    result6 = get_loc('海淀区成府路28号')
    add_shop('水木锦堂·自助铁板烧（五道口店）', '海淀区成府路28号5道口购物中心3F', result6['lng'], result6['lat'], 3.2,
             '营业时间： 周一至周日 11:30-14:00 17:30-21:00', '美食', '/picture/6.jpg')

    result7 = get_loc('朝阳区百环家园甲19号')
    add_shop('汉丽轩自助涮烤超市（双井店）', '朝阳区百环家园甲19号恺兴文化二楼', result7['lng'], result7['lat'], 3.0, '营业时间： 周一至周日 11:00-22:00',
             '美食',
             '/picture/7.jpg')

    result8 = get_loc('海淀区西直门北大街32号枫蓝国际购物中心')
    add_shop('韩时烤肉（枫蓝国际购物中心店）', '海淀区西直门北大街32号枫蓝国际购物中心2层', result8['lng'], result8['lat'], 4.7,
             '营业时间： 周一至周日 10:30-21:30',
             '美食', '/picture/8.jpg')

    result9 = get_loc('丰台区大成路23号天泰大厦')
    add_shop('金滏山自助烤肉（大成路店）', '丰台区大成路23号天泰大厦3楼', result9['lng'], result9['lat'], 3.0, '营业时间： 11:00-14:00 17:00-21:00 ',
             '美食', '/picture/9.jpg')

    result10 = get_loc('海淀区万泉河路')
    add_shop('天使食府（人大店）', '海淀区万泉河路人大西门南侧20米（万泉庄桥东侧）', result10['lng'], result10['lat'], 4.1,
             '营业时间： 周一至周日 11:00-14:00 17:00-21:30', '美食', '/picture/10.jpg')

    result11 = get_loc('海淀区远大路1号金源时代购物中心')
    add_shop('金源福城肥牛火锅（远大路金源店）', '海淀区远大路1号金源时代购物中心五层5-17号', result11['lng'], result11['lat'], 4.2,
             '营业时间：周一至周日 10:00-23:00',
             '美食', '/picture/11.jpg')

    result12 = get_loc('大兴区兴华大街百联清城购物中心')
    add_shop('伊尔克啤酒烤肉自助（大兴店）', '大兴区兴华大街百联清城购物中心三层', result12['lng'], result12['lat'], 3.0,
             '营业时间：周一至周日 11:00-14:00 17:00-21:30', '美食', '/picture/12.jpg')

    result13 = get_loc('通州区通州北苑')
    add_shop('三清洞摩西年糕火锅（万达店）', '通州区通州北苑万达广场西门金街b区二层264号', result13['lng'], result13['lat'], 4.2,
             '营业时间： 周一至周日 09:30-21:30 ',
             '美食', '/picture/13.jpg')

    result14 = get_loc('海淀区复兴路69号蓝色港湾购物中心')
    add_shop('耀莱成龙国际影城(五棵松店)', '海淀区复兴路69号蓝色港湾购物中心北区5层', result14['lng'], result14['lat'], 4.8,
             '营业时间： 周一至周日 09:30-23:30',
             '电影演出', '/picture/14.jpg')

    result15 = get_loc('朝阳区西大望南路与弘燕南一路交叉口铭泽生活广场')
    add_shop('大地影院(十里河铭泽影院 )', '朝阳区西大望南路与弘燕南一路交叉口铭泽生活广场5层', result15['lng'], result15['lat'], 3.8,
             '营业时间：周一至周日 09:30-23:30',
             '电影演出', '/picture/15.jpg')

    result16 = get_loc('海淀区西三环北路87号国际财经中心')
    add_shop('温莎KTV（花园桥店）', '海淀区西三环北路87号国际财经中心B1层', result16['lng'], result16['lat'], 4.0, '营业时间：周一至周日 全天', '休闲娱乐',
             '/picture/16.jpg')

    result17 = get_loc('朝阳区雅成一里19号')
    add_shop('唱吧麦颂KTV（朝阳大悦城店）', ' 朝阳区雅成一里19号（宝岛眼镜店旁） ', result17['lng'], result17['lat'], 4.2, '营业时间：周一至周日 13:00-06:00',
             '休闲娱乐', '/picture/17.jpg')

    result18 = get_loc(' 朝阳区南磨房乡大柳树路南楼梓庄')
    add_shop('唱吧麦颂ktv（北工大店）', ' 朝阳区南磨房乡大柳树路南楼梓庄一幢一层106室（工大桥东南角如家酒店旁）', result18['lng'], result18['lat'], 4.2,
             '营业时间：  周一至周日 13:00-06:00', '休闲娱乐', '/picture/18.jpg')

    result19 = get_loc(' 朝阳区青年路华纺新天地')
    add_shop('BOXING熔石训练馆', ' 朝阳区青年路华纺新天地3号楼302', result19['lng'], result19['lat'], 3.5, '营业时间：周一至周日 10:00-23:00',
             '运动健身',
             '/picture/19.jpg')

    result20 = get_loc(' 朝阳区天辰东路11号国家游泳中心 ')
    add_shop('水立方游泳俱乐部', ' 朝阳区天辰东路11号国家游泳中心 ', result20['lng'], result20['lat'], 4.2, '营业时间：周一至周日 09:00-18:00', '运动健身',
             '/picture/20.jpg')


if __name__ == '__main__':
    add_shop();
