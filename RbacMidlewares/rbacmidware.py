#！/bin/python3
# -*- coding: utf-8 -*-
import re
from  django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

class RbacMidleware(MiddlewareMixin):
    def process_request(self,request):
        """
        当前请求的URL
        :param request:
        :return:
        """

        current_url=request.path_info
        # 1. 白名单处理
        for valid in settings.WITH_LIST:
            if re.match(valid,current_url):
                return  None
        # 2. 获取权限信息
        """
          permission_dict = {
              'user_list': {'url': '/app01/user/', 'menu_id': 1, 'parent_name': None},
              'user_add': {'url': '/app01/user/add/', 'menu_id': None, 'parent_name': 'user_list'},
              'user_edit': {'url': '/app01/user/edit/(\\d+)', 'menu_id': None, 'parent_name': 'user_list'},
              'order': {'url': '/app01/order/', 'menu_id': 2, 'parent_name': None}
          }
          """
        permissions_dict=request.session.get(settings.PERSSION_SESSION_KEY)
        match=False
        if not permissions_dict:
            #用户没登录
            return  HttpResponse("当前用户无权限信息，请重新登录")
        # 3. 权限匹配
        for k,v in permissions_dict.items():
            reg="^%s$" % v["url"]
            if re.match(reg,current_url):
                if v["menu_id"]:
                    request.default_select_menu_name=k
                else:
                    request.default_select_menu_name=v['parent_name']
                match=True
                break
        if not match:
            return  HttpResponse("无权访问")

