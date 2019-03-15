#coding:utf-8
 
from wxpy import *
import requests
import json
 
'''
作者：pk哥
公众号：Python知识圈
日期：2018/07/28
代码解析详见公众号。
如疑问或需转载，请联系微信号：dyw520520，备注来意，谢谢。
'''
 
 
robot = Bot()
 
def talk_robot(info='你好啊'):   #定义一个默认参数
    api_url = 'http://www.tuling123.com/openapi/api'  # 图灵接口url
    apikey = 'xxxxxxxx'       # 注册图灵生成key
    data = {'key': apikey, 'info': info}
    r = requests.post(api_url, data=data).text
    response = json.loads(r)['text']
    return response
 
# 定义一个话痨微信机器人
# @robot.register()
# def reply_my_friend(msg):
#     message = '{}'.format(msg.text)
#     response = talk_robot(info=message)
#     return response
 
# 定义一个当被@才回复的微信机器人
@robot.register()
def print_group_msg(msg):
    if msg.is_at:
        message = '{}'.format(msg.text)
        response = talk_robot(info=message)
        return response
 
embed()