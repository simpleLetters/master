from django.db import models

class Menu(models.Model):
    """
    菜单表
    """
    title = models.CharField(verbose_name='标题',max_length=32)
    icon = models.CharField(verbose_name='图标',max_length=32)
    def __str__(self):
        return  self.title

class Permission(models.Model):
    """
    权限表
    """
    url = models.CharField(verbose_name='URL(含正则)', max_length=128)
    title = models.CharField(verbose_name='名称',max_length=32)
    name = models.CharField(verbose_name='别名',max_length=32,unique=True)

    menu = models.ForeignKey(verbose_name='管理菜单',to='Menu',to_field='id',null=True,blank=True)
    parent = models.ForeignKey(verbose_name='父菜单',to='Permission',null=True,blank=True)
    def __str__(self):
        return  self.title
    
    
class Role(models.Model):
    """
    角色表
    """
    title = models.CharField(verbose_name='名称', max_length=32)
    permissions = models.ManyToManyField(verbose_name='关联权限',to='Permission')
    def __str__(self):
        return  self.title
    
class UserInfo(models.Model):
    """
    用户表
    """
    username = models.CharField(verbose_name='用户名',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=64)
    roles = models.ManyToManyField(verbose_name='关联角色',to='Role')
    def __str__(self):
        return self.username