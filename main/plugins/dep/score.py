# -*- coding: utf-8 -*-

import time, random, string
import urllib.request
from urllib.request import ProxyHandler
from urllib.request import build_opener
import pyamf
from pyamf import remoting
from pyamf.flex import messaging
from ...import app

url = app.config['JW_WAN_HOST']


# 发送请求
def invoke(data):
    proxie = None
    # 调试模式代理
    if app.config['DEBUG'] and app.config['debug_proxie']:
        proxie = app.config['debug_proxie']
    # 构造请求
    req = urllib.request.Request(
        url, data, headers={"Content-Type": "application/x-amf"})
    # 设置代理
    httpproxy_handler = ProxyHandler(proxie)
    # 设置启动器
    opener = build_opener(httpproxy_handler)
    # 请求，解码AMF协议返回的数据
    resp = remoting.decode(opener.open(req).read())
    return resp


# 组装请求内容
def getAllStudentMultiExam(student_id):
    msg = messaging.RemotingMessage(
        operation="getAllStudentMultiExam",
        source=None,
        timeTolive=0,
        clientId=None,
        destination="multiExamServiceNew",
        messageId="C",
        timestamp=0,
    )
    msg.body = [0, student_id, None]
    msg.headers["DSRequestTimeout"] = 600
    msg.headers["DSId"] = "C"
    msg.headers["DSEndpoint"] = None
    # 按AMF协议编码
    req = remoting.Request("null", body=(msg, ))
    env = remoting.Envelope(amfVersion=pyamf.AMF3)
    env.bodies = [("/2", req)]
    data = bytes(remoting.encode(env).read())
    return invoke(data)


def get_meStudentScore(student_id):
    # 返回数据
    res = {
        # 学生姓名
        'student_name': '',
        # 是否查到数据
        'success': False,
        # 所有考试 直接用subjects字典替代
        'all_MultiExam': {
            # 所有考试 list
            #'MultiExam_name':{   # 这里的seid指每个科目试卷的id
            #'seid1': {
            #    "seCourseName": None,  # 科目名称
            #    "seScore": 'seStudentScore["essScore"]',
            #    "essGradeOrder": 'seStudentScore["essGradeOrder"]',
            #    "essClassOrder": 'seStudentScore["essClassOrder"]',
            #}
            #},
        }
    }

    raw_amf = getAllStudentMultiExam(student_id)
    # 有用的数据在这里
    respons_data = raw_amf.bodies[0][1].body.body

    # 查到数据
    if respons_data:
        res['success'] = True
        # 学生姓名位置
        studentName = respons_data[0]["meStudentScore"]["studentName"]
        # 向返回数据中添加学生姓名
        res['student_name'] = studentName

        # 循环遍历每次考试
        for multiExam in respons_data:
            seIds = []  # 试卷id
            # 初始化考试名称
            MultiExam_name = multiExam["multiExam"]["meName"]
            res['all_MultiExam'][MultiExam_name] = {}
            # 从 v0.2抄过来的
            # 总分
            messScore = multiExam["meStudentScore"]["messScore"]
            res['all_MultiExam'][MultiExam_name]['total'] = {
                'seCourseName': '总分',
                'seScore': messScore,
                'class_order': multiExam['meStudentScore']['messClassOrder'],
                'grade_order': multiExam['meStudentScore']['messGradeOrder'],
            }

            for seStudentScore in multiExam["seStudentScoreList"]:
                # 试卷id
                seId = str(seStudentScore["seId"])
                seIds.append(seId)
                seScore = seStudentScore["essScore"]
                essGradeOrder = seStudentScore["essGradeOrder"]
                essClassOrder = seStudentScore["essClassOrder"]

                res['all_MultiExam'][MultiExam_name][seId] = {
                    "seCourseName": None,
                    "seScore": seScore,
                    "essGradeOrder": essGradeOrder,
                    "essClassOrder": essClassOrder,
                }

            for singleExam in multiExam["singleExams"]:
                seId = str(singleExam["seId"])
                if seId in seIds:
                    seCourseName = singleExam["seCourseName"]
                    res['all_MultiExam'][MultiExam_name][seId][
                        "seCourseName"] = seCourseName

    return res


if __name__ == "__main__":
    print(get_meStudentScore('00000000'))