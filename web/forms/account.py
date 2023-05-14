from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from web import models


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
