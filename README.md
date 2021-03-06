# 目标
聚会是人们日常生活中重要的休闲活动之一，但是高效地确定合适的聚会地点却不容易。通过对本校师生的调查，本研究组发现很多人都遇到过组织聚会时聚会地点难以确定的问题。组织者在确定聚会地点时需要考虑能否让大多数甚至所有聚会人员在相对短的时间到达聚会地点，需要考虑聚会地点对处于不同初始位置、使用不同出行方式的聚会人员是否相对公平，需要考虑聚会地点的活动是否符合聚会人员的喜好等诸多复杂的因素。在达成一致前，聚会人员可能需要在即时通讯类、地图类、点评类、社交类应用之间不停转换以做出选择。这一过程比较浪费时间也消耗精力。   
针对这个问题，本项目旨在开发出相关的系统为遇到这方面问题的人们提供最优方案。在现有的地图、点评类应用的基础上，通过系统对**人们的喜好**、**所处地点**、**出行方式**、**出行时间**、**聚会地点特征**等因素的分析与计算，从而为聚会人员提**供聚会地点的最优推荐**，并为聚会人员提供优质的导航服务。提高人们的出行与聚会体验。
# 功能
用户注册与登录   
聚会地点的分析与建议  
聚会地点路线查询  
商家信息查看与评价  
个人中心展示
# 环境
## 运行环境
Win10 64位 教育版 & Ubuntu 16.04  
Mysql 5.5.60  
Python 3.7 3.6 3.5  
chrome 67.0.3396.99
## 测试工具
Postman  
LoadRunner  
Xshell6  
WinSCP
# 安装说明
## 第三方模块
> Flask==1.0.2  
Flask-Login==0.4.1  
Flask-SQLAlchemy==2.3.2  
Flask-WTF==0.14.2  
Jinja2==2.10  
mysql-connector==2.1.6  
PyMySQL==0.9.2  
SQLAlchemy==1.2.8  
WTForms==2.2.1

## 数据库名称替换
在根目录下的**module.py**中，将第82/84行里的**用户名**、**密码**和**数据库名称**替换为自己使用的数据库信息

或直接执行
> pip install -r requirements.txt
# 运行
执行：
> python3 main.py

为了简化商铺数据库的添加，可在使用前执行：
> python3 insert_module.py

如果在服务器上运行，需要先停止Nginx等反向代理进程
# 参考
Graham 扫描法  
SpatialRelationUtil 引射线法  
百度地图定位api  
百度地图线路规划api  

![suanfa](https://github.com/AmuroPeng/JuYouQu/blob/master/image/suanfa.png)
# 预览图
![my_wife](https://github.com/AmuroPeng/JuYouQu/blob/master/image/my_wife.jpg)  
咳咳咳不对，不是这张  

![index](https://github.com/AmuroPeng/JuYouQu/blob/master/image/index.png)  

![shop](https://github.com/AmuroPeng/JuYouQu/blob/master/image/shop.png)
# 后记
>if branch[Amuro] == branch[dev] == branch[master]:
>>print ( ´•̥̥̥ω•̥̥̥` )  

C:\Users\Amuro\Desktop> ( ´•̥̥̥ω•̥̥̥` )  

稳中带皮 _(°:з」∠)_
