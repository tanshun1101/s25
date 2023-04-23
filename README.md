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

1.1.2 模版文件路径处理
     由于app_01是学习的项目，因此在app_01下面的templates下创建app_01的包，并把html放到包目录下

1.2 点击获取验证码
1.3 点击注册



         


