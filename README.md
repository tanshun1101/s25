4.redis基本操作
4.1 安装redis
   修改redis配置，ip地址和密码（requiementpass）
4.2 python操作redis的模块
   redis 直接连接

作业
   1.ModelForm页面
   2.register页面写ajax, 手机号和模版字符串tpl
   3.校验
   4.sms+redis
   5.进阶
      倒计时效果
      注册按钮：字段校验 + 手机验证码校验
      py操作redis改成django-redis
      pythonav.com/wiki/detail/10/82/
 
day03 用户认证
内容回顾&补充
1.虚拟环境 virtualenv (每个项目创建独立虚拟环境)
2. requirements.txt(pip freeze > requirements.txt) 将项目中需要用到的模块都放到该文件下
3. local_settings.py 做本地配置，开发/测试/生产三套环境隔离开
4. gitignore git上传时，忽略到一些文件(不上传)
5. 腾讯云短信/阿里云短信 (阅读文档，文档不清晰：谷歌、bing、搜狗、百度)
   Api 提供url,你去访问这些URL并根据提示传递参数
   requests.get("http://www.xxxxx.com//adsf/ab",json = {....})
   SDK 模块：下载安装模块，基于模块完成功能
   sms.py
       def func():
           return requests.get("http://www.xxxxx.com//adsf/ab",json = {....}")
   如何使用：
   pip install sms
   sms.func()
   两者的区别：api是提供接口，sdk是提供软件包，需要安装软件包才可以使用
6. redis
   帮助我们在内存可以存储数据的软件（基于内存的数据库）
   redis会定期将数据写到硬盘上，所以如果真的宕机了，redis数据也可以不丢失
   1.在A主机安装redis并进行配置和启动
   2.连接redis
        方式1：利用redis提供的客户端（redis-cli）,直接在终端输入：redis-cli
        方式2：利用相关模块
             1.安装模块
                 pip install redis
             2.使用模块，参考代码【不推荐】
             # 操作redis
                import redis
                
                # 直接连接redis
                conn = redis.Redis(host="10.211.55.28", port=6379, password="maxwell", encoding="utf-8")
                
                # 设置键值：1512121212="9999" 且超时时间为10秒（值写入到redis时会自动转字符串）
                conn.set('1512121212', 9999, ex=10)
                
                # 根据键获取值，如果存在获取值（获取到的是字节类型）; 不存在则返回None
                value = conn.get('1512121212')
                print(value)
             3.使用模块【推荐连接池】
                import redis
                
                # 创建redis连接池（默认连接池最大连接数2**31-2147483648）
                pool = redis.ConnectionPool(host="10.211.55.28", port=6379, password="maxwell", encoding="utf-8", max_connections=1000)
                
                #去连接池中获取一个连接
                conn = redis.Redis(connection_pool=pool)
                
                # 设置键值：1512121212="9999" 且超时时间为10秒（值写入到redis时会自动转字符串）
                conn.set('name', "张三", ex=10)
                
                # 根据键获取值，如果存在获取值（获取到的是字节类型）; 不存在则返回None
                value = conn.get('name')
                print(value)
   
   3 django-redis, 在django中方便的使用redis
     不方便： redis模块   + 连接池
     方便： Django-redis
     3.1 安装django-redis
         pip install django-redis
     3.2 使用，修改django项目settings（建议local_settings）
         CACHES = {
            "default": {
                "BACKEND": "django_redis.cache.RedisCache",
                "LOCATION": "redis://10.211.55.28:6379",  # 安装redis的主机的IP和端口号
                "OPTIONS": {
                    "CLIENT_CLASS": "django_redis.client.DefaultClient",
                    "CONNECTION_POOL_KWARGS": {
                        "max_connections": 1000,
                        "encoding": "utf-8"
                    },
                    "PASSWORD": "maxwell"  # redis密码
                    
                   
                }
        
            }
        
        }
   4 在Django的视图函数中写下面的代码：
   from django.shortcuts import HttpResponse
   from django_redis import get_redis_connection
   
   def index(request):
       # 去连接池中获取一个连接,默认去连接default
       conn = get_redis_connection("default")
       conn.set('nickname', '武沛齐'，ex=10)
       value = conn.get('nickname')
       print(value)
       return HttpResponse("ok")
       
               
今日概要
1.注册
2.短信验证码登陆
3.用户名密码登陆

今日详细
1.实现注册
1.1 展示注册页面
1.1.1 创建web的应用 & 注册 ：python manage.py startapp web
      并注册APP:
      INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'app_01.apps.App01Config',
        'web.apps.WebConfig'
        ]

1.1.2 模版文件路径处理
     由于app_01是学习的项目，因此在app_01下面的templates下创建app_01的包，并把html放到包目录下
     母版准备
     路由处理
     1.1.5 注册页面展示
     <1>. 母版中导航
     <2>. 注册页面样式
     <3>. ModelForm放到指定目录forms
     Git地址：在GitHub
     commit: 注册页面展示

1.2 点击获取验证码
    参考注册页面
    1.2.1 按钮绑定点击事件
    1.2.2 获取手机号
    1.2.3 发送ajax
    1.2.4 手机号格式校验
      <1>. 不能为空
      <2>. 格式正确
      <3>. 没有注册过
    1.2.5 验证通过
       <1> 发送短信
       <2> 将短信保存到redis中 （60s
    1.2.6 成功与失败
        <1>.失败，错误消息
        <2>.成功，倒计时 
            disable属性
             $("#btnSms").prop("disabled",true); 添加disabled属性，不可操作
             $("#btnSms").prop("disabled",false); 移除disabled属性，可操作
            定时器
            var obj = setInterval(function()){
                console.log(123);
            },1000)
            clearInterval(obj);
            
            var time = 60;
            var obj = setInterval(function()){
                time = time -1;
                if(time <1){
                    #清除定时器
                    clearInterval(obj);
                }
            },1000)  
1.3 点击注册
    内容总结
    视图 view.py --> views目录
    模版，根目录templates-->根据app注册顺序去每个app的templates中
    静态文件，同上 static
    项目中多个app且想要各自模版，静态文件隔离，建议通过app名称再进行嵌套即可。
    路由分发
        include 
        namespace 多个app中进行区分
    母版
     title
     css
     content
     js
    bootstrap 导航条、去除圆角、container
    ModelForm 生产HTML标签时，自动生成ID id_字段名
    发送ajax请求
    $.ajax({
      url:'/index',
      type:'GET',
      data: {},
      dataType: "JSON",
      success:function(res){
         console.log(res)
      }
    })
    Form & ModelForm可以进行表单验证
      form = SendSmsForm(data=request.POST) #QueryDict
      form = SendSmsForm(data=request.GET)  #QueryDict
    Form & ModelForm中如果想要用视图中的值（request）
    
    class SendSmsForm(forms.Form):
    mobile_phone = forms.CharField(label="手机号", validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$','手机号格式错误'),])

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
    短信
    redis(django-redis)
    倒计时
    今日作业
    点击注册按钮【必须做】
    短信登陆 【可选】
    可选的：django 实现图片验证码
    day04
    内容回顾
    项目规则
       创建项目：静态、视图、路由
    $.ajax({
      url:'/index',
      type:'GET',
      data: {},
      dataType: "JSON",
      success:function(res){
     
      }
    })
    ModelForm/Form中想要使用视图中的数据， 例如：request
       重写ModelForm/Form中的__init__方法，把想要的数据传递
    django-redis
     
    今日概要
    点击注册
    用户登录
       短信验证码登陆
       手机or邮箱/密码登录
    项目管理（创建&星标）
    
    今日详细
    1、点击注册
    1.1 点击收集数据&ajax
     $.ajax({
            url:"{% url 'register' %}",
            type:"POST",
            data:$('#regForm').serialize(), //所有字段数据 + csrf token
            dataType: "JSON",
            success:function (res) {
                console.log(res);
            }
        })
    1.2 数据校验（ 每个字段）
    1.3 写入数据库
    1.4 项目bug
    2. 短信登录
    2.1 展示页面
    2.2 点击发送短信
    2.3 点击登陆
    任务：3小时（下午4点开讲）
    3.用户名/密码登陆
    3.1 Python生产图片+写文字 参考武沛齐博客 ： 
        https://www.cnblogs.com/wupeiqi/articles/5812291.html
        pip3 install pillow
    3.2 session & cookie
        
    
    
    3.3 页面显示
    3.4 登陆
    
    总结&任务（一期项目结束）
    项目代码
    思维导图（知识点）
    今日概要
    1. Django中如何编写离线脚本
    2. 探讨业务
    3. 设计表结构
    4. 我的表结构
    5. 功能实现
        查看项目列表
        创建项目
        星标项目
    
    今日详细
    1. Django离线脚本
     django, 框架
     离线， 非web运行时
     脚本， 一个或几个py文件
     在某个py文件中对django项目做一些处理
     示例1：使用离线脚本在用户表插入数据
     import django
     import os
     import sys
     base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
     sys.path.append(base_dir)
    
     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "s25.settings")
     django.setup()
     from web import models
     # 往数据库中添加数据：链接数据库、操作、关闭链接
     models.UserInfo.objects.create(username='陈硕', email='chengshuo@163.com',
      mobile_phone='13183838381', password='123123')
     示例2：数据库中存储全国的省市县（基础数据）
     示例3：朋友圈项目敏感字、词语
     示例4：saas免费版：1G  5项目  10人
     
     2.探讨业务
     2.1 价格策略
      分类         标题               价格/年      创建项目个数     每个项目成员    每个项目空间    单文件  创建时间
      免费版       个人免费版             0            5            5              20M          5M
      收费版       vip                 199          20           100            50G           500M
      收费版       Svip                299          50           200            100G           1G
      其他         其他
      注意：新用户注册拥有免费版的额度
     2.2 用户
     用户名     手机号         密码
     alex     13818657387    1234555
     2.3 交易
       ID    状态     用户    价格     实际支付     开始        结束       数量    订单
       1     已支付   1       1        0        2020-3-18   null       0     ada11
       2     已支付   2       1        0        2020-3-18   null       0     ada12
       3     已支付   3       1        0        2020-3-18   null       0     ada13
       4     已支付   2       2        199      2020-4-18   2021-4-18  1     ada14
       5  未支付/已支付   3       3       299*2     2020-5-18   2021-5-18  2     ada15
       request.tracer = 交易对象
       2.4 创建存储
       基于腾讯对象存储COS存储数据。
       2.5 项目
       ID      项目名称   描述   颜色       星标     参与人数   创建者    已使用空间
       1       CRM             #dddd      true     5        3          5M
       2       路飞学城         #dddd      false    10       3          1G
       3       SAAS            #dddd      false    20       3          2G
       2.6 项目参与者
       ID     项目     用户     星标         
       1       1       1       true       
       2       1       2       False
       
       3.任务
       3.1 创建相应表结构
       3.2 离线脚本创建价格策略【免费版】
       分类         标题      价格/年   创建项目个数    每个项目成员   每个项目空间    单文件   创建时间
       1.免费版   个人免费版     0          3            2             20M         5M
       
       3.3 用户注册 【改】
       之前  注册成功只是新建用户
       现在：
           新建用户
           新建交易记录【免费版】
       3.4 添加项目
       3.5 展示项目
           星标
           我创建的
           我参与的
       3.6 星标项目
     day06  今日概要
     表结构
     离线脚本
     用户注册
     添加项目
     展示项目
     星标项目
     
     今日详细
     1.表结构
     
              

