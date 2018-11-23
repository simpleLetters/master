# ！/bin/python3
# -*- coding: utf-8 -*-

from django.conf import settings

def init_permission(user, request):
    """
    初始化权限信息和菜单信息，权限信息和菜单信息放入session中
    :param user: 当前登录用户对象
    :param request:请求先关的所有数据
    :return:
    """
    permission_list = user.roles.filter(permissions__isnull=False).distinct().values(
        "permissions__title",
        "permissions__url",
        "permissions__name",
        "permissions__menu_id",
        "permissions__menu__title",
        "permissions__menu__icon",
        "permissions__parent_id",
        "permissions__parent__name"
    )
    # 当前用户所有角色所有权限信息
    permission_dic = {}
    menu_dic = {}
    for item in permission_list:
        name = item["permissions__name"]

        url = item["permissions__url"]
        menu_id = item["permissions__menu_id"]
        parent_name = item["permissions__parent__name"]
        permission_dic[name] = {"url": url, "menu_id": menu_id, "parent_name": parent_name}
        if menu_id:
            menu_id = item["permissions__menu_id"]
            if menu_id in menu_dic:
                menu_dic[menu_id]["children"].append(
                    {"title": item["permissions__title"], "url": item["permissions__url"],'name': item['permissions__name']})
            else:
                menu_dic[menu_id] = {
                    "title": item["permissions__title"],
                    "icon": item["permissions__menu__icon"],
                    'class': 'hide',
                    "children": [
                        {"title": item["permissions__title"], "url": item["permissions__url"],  'name': item['permissions__name']}
                    ]
                }

    request.session[settings.PERSSION_SESSION_KEY] = permission_dic
    request.session[settings.MENU_SESSION_KEY] = menu_dic
