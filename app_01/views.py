from django.shortcuts import render, HttpResponse
from utils.tencent.sms import send_sms_single
from django.conf import settings
from django import forms
import random


# Create your views here.
def send_sms(request):
    """发送短信
       ?tpl=login   -> 548762
       ?tpl=register  -> 548760
    """

    tpl = request.GET.get('tpl')
    template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
    if not template_id:
        return HttpResponse('模版不存在')

    code = random.randrange(1000, 9999)
    res = send_sms_single('12131313213', template_id, [code, ])
    if res["result"] == 0:
        return HttpResponse("成功")
    else:
        return HttpResponse(res["errmsg"])


from django import forms
from app_01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class RegisterModelForm(forms.ModelForm):
    # 重写手机号验证字段
    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])
    # 修改密码属性
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    # 增加重复密码字段
    confirm_password = forms.CharField(label="重复密码", widget=forms.PasswordInput())
    # 增加验证码字段
    code = forms.CharField(label="验证码", widget=forms.TextInput())

    class Meta:
        model = models.UserInfo
        # 修改页面字段展示顺序
        fields = ["username", "email", "password", "confirm_password", "mobile_phone", "code"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control'
            filed.widget.attrs['placeholder'] = '请输入%s' % (filed.label,)


def register(request):
    form = RegisterModelForm()
    return render(request, 'app_01/register.html', {'form': form})


# 操作redis
import redis

# 直接连接redis
conn = redis.Redis(host="10.211.55.28", port=6379, password="maxwell", encoding="utf-8")

# 设置键值：1512121212="9999" 且超时时间为10秒（值写入到redis时会自动转字符串）
conn.set('1512121212', 9999, ex=10)

# 根据键获取值，如果存在获取值（获取到的是字节类型）; 不存在则返回None
value = conn.get('1512121212')
print(value)