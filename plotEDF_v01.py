# coding=utf-8

##############################################################
#  Author: Guangming Wang  2022/3/20
#  Use: Plot earthquake distribution figure control module
#  Version：1.0
# ------------------------------------------------------------
#  Modify history
#
#
##############################################################

from flask import Flask, request, Response
import requests
from plot_module import *
import json

app = Flask(__name__)

@app.route('/IntelligentConsultation', methods=['GET', 'POST'])
def earthquake_distribution_figure():
    para = []  # 返回值
    # *** Read plot parameters ***
    # --- Read figure name ---
    figName = request.args.get('figName', '')  # 图件名称
    # --- Read figure range ---
    """
    There are 6 figure ranges in this program
    figRange = 0 ： Custom（自定义）;
    figRange = 1 ： Globe（全球）;
    figRange = 2 ： China（全国）；
    figRange = 3 : Sichuan-Yunnan(川滇)；
    figRange = 4 : Yunnan(云南地区：21-29°N，97-106°E)；
    figRange = 5 : Tibet(藏南部分地区：26.5-32°N，82-94.5°E)；
    """
    figRange = int(request.args.get('figRange', ''))  # 图件范围
    # print('figRange:'+figRange)
    # --- Read figure type ---
    """
    Threre are 2 figure types in this program
    figType = 1 ： 单时间范围;
    figType = 2 ： 双时间范围；
    """
    figType = int(request.args.get('figType', ''))  # 图件类型
    # print('figType:'+figType)
    print(type(figType))
    # --- Read magnitude range ---
    maxMag = request.args.get('maxMag', '')  # 震级上限
    minMag = request.args.get('minMag', '')  # 震级下限
    # --- Read space range ---
    maxLat = request.args.get('maxLat', '')  # 纬度上限
    minLat = request.args.get('minLat', '')  # 纬度下限
    maxLon = request.args.get('maxLon', '')  # 经度上限
    minLon = request.args.get('minLon', '')  # 经度下限
    print('icon1')
    # --- Read time range ---
    if figType == 1:
        print('icon2')
        startDate = request.args.get('startDate', '')  # 目录起始时间
        endDate = request.args.get('endDate', '')  # 目录结束时间
        if figRange == 0:
            plotEDF_custom_single(startDate, endDate, maxLon, minLon, maxLat, minLat,
                                  maxMag, minMag, figName, para)
        elif figRange == 1:
            plotEDF_globe_single(startDate, endDate, maxLon, minLon, maxLat, minLat,
                                 maxMag, minMag, figName, para)
        elif figRange == 2:
            plotEDF_CN_single(startDate, endDate, maxLon, minLon, maxLat, minLat, maxMag,
                              minMag, figName, para)
        elif figRange == 3:
            plotEDF_chuandian_single(startDate, endDate, maxLon, minLon, maxLat, minLat,
                                     maxMag, minMag, figName, para)
        elif figRange == 4:
            plotEDF_YN_single(startDate, endDate, maxLon, minLon, maxLat, minLat, maxMag,
                              minMag, figName, para)
        elif figRange == 5:
        # else:
            plotEDF_Tibet_single(startDate, endDate, maxLon, minLon, maxLat, minLat, maxMag,
                                 minMag, figName, para)
    # elif figType == 2:
    # if figType == 2:
    else:
        startDate1 = request.args.get('startDate1', '')  # 目录起始时间1
        endDate1 = request.args.get('endDate1', '')  # 目录结束时间1
        startDate2 = request.args.get('startDate2', '')  # 目录起始时间2
        endDate2 = request.args.get('endDate2', '')  # 目录结束时间2
        if figRange == 0:
            plotEDF_custom_double(startDate1, endDate1, maxLon, minLon, maxLat, minLat, maxMag,
                                  minMag, startDate2, endDate2, figName, para)
        elif figRange == 1:
            plotEDF_globe_double(startDate1, endDate1, maxLon, minLon, maxLat, minLat, maxMag,
                                 minMag, startDate2, endDate2, figName, para)
        elif figRange == 2:
            plotEDF_CN_double(startDate1, endDate1, maxLon, minLon, maxLat, minLat, maxMag,
                              minMag, startDate2, endDate2, figName, para)
        elif figRange == 3:
            plotEDF_chuandian_double(startDate1, endDate1, maxLon, minLon, maxLat, minLat, maxMag,
                                     minMag, startDate2, endDate2, figName, para)
        elif figRange == 4:
            plotEDF_YN_double(startDate1, endDate1, maxLon, minLon, maxLat, minLat, maxMag,
                              minMag, startDate2, endDate2, figName, para)
        elif figRange == 5:
        # else:
            plotEDF_Tibet_double(startDate1, endDate1, maxLon, minLon, maxLat, minLat, maxMag,
                                 minMag, startDate2, endDate2, figName, para)


    return Response(json.dumps(para, ensure_ascii=False, indent=4), mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8003)