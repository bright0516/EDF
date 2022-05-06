"""
  This script contains different figure range modules
"""

import pygmt
import os
import numpy as np
import pandas as pd
import time
from earthquakeDataRequest import *
from magCounts import *

def catalog_statistic(data, para, magThreshold):
    """
    This module is used to events information statistic
    :param data: catalog
    :param para: parameter for return to program
    :param magThreshold: minimum earthquake magnitude for information collection
    :return: para(statistical results)
    """
    result = {}
    events = []
    eventMag = [i['zhenJiZhi'] for i in data]  # 地震震级
    eventTime = [i['riQi'] for i in data]
    eventLocation = [i['diMing'] for i in data]
    # --- 下限震级以上地震信息统计 ---
    for i in range(0, len(eventMag)):
        if float(eventMag[i]) >= magThreshold:
            events.append(eventTime[i] + eventLocation[i] + eventMag[i])
    # --- 不同震级地震数量统计 ---
    eventMagCount = magCounts(eventMag)
    # --- 输出结果 ---
    result['events'] = events
    result['eventMagCount'] = eventMagCount
    para.append(result)
    return para

def plot_time_label_for_single_time_range(startDate, endDate, fig):
    """
    This module is for single time range label plot
    :param startDate: figure range
    :param endDate: figure range
    :param fig: figure
    :return: fig
    """
    # ---plot colorbar---
    fig.shift_origin(xshift="-1c", yshift="-1.5c")
    fig.basemap(
        region=[0, 15.5, 0, 1],
        projection="X16c/1c",
        frame='+t" "'
    )
    fig.text(
        text=startDate,
        x=1.5,
        y=0.2,
        font="12p,4,black",
        justify="CB"
    )
    fig.text(
        text=endDate,
        x=14.5,
        y=0.2,
        font="12p,4,black",
        justify="CB"
    )

def singleTimeRangePlot(startDate, endDate, fig, data):
    """
    This module is for single time range earthquake distribution figure.
    :param startDate: parameter for time cpt
    :param endDate: parameter for time cpt
    :param fig: figure
    :param data: catalog
    :return: fig
    """
    # ---get plot parameters from request---
    startTime = time.mktime(time.strptime(startDate, "%Y-%m-%d"))  # 目录起始时间
    endTime = time.mktime(time.strptime(endDate, "%Y-%m-%d"))  # 目录结束时间
    catalog = data  # 获取到的地震目录数据
    # ---get events parameters---
    eventLongitude = [i['lon'] for i in catalog]  # 地震经度
    eventLatitude = [i['lat'] for i in catalog]  # 地震纬度
    eventMagnitude = [i['zhenJiZhi'] for i in catalog]  # 地震震级
    # ---get events time---
    eventDate = [time.mktime(time.strptime(i['riQi'].split('.', 1)[0], "%Y-%m-%d %H:%M:%S")) for i in
                 catalog]  # 日期中的秒数据格式混乱的情况（既有整数秒，又有小数点格式的秒数据）
    eventTime = np.array(eventDate)

    # ---make cpt---
    pygmt.makecpt(cmap="seis", series=[startTime, endTime], reverse=True)
    # pygmt.makecpt(cmap="seis", series=[firstStartDate, firstEndDate], reverse=True)
    eventPlotMagnitude = [float(i) * 0.08 for i in eventMagnitude]
    fig.plot(
        x=eventLongitude,
        y=eventLatitude,
        size=eventPlotMagnitude,
        style="cc",
        color=eventTime,
        cmap=True,
        pen="black"
    )  # ,label=f"Last_month+S0.25c")
    # # #---plot mag symbol---
    # with fig.inset(position="jBL+w4c/1.4c+o0.2c/0.2c", box="+pblack+gwhite"):
    #     fig.basemap(
    #         region=[0, 5, 0, 2],
    #         projection="X4c/1.4c",
    #         frame='+t" "'
    #     )
    #     fig.plot(
    #         x=[1.5, 2.5, 3.5, 4.5],
    #         y=[1.4, 1.4, 1.4, 1.4],
    #         size=[0.24, 0.32, 0.4, 0.48],
    #         style="cc",
    #         color="white",
    #         pen="black"
    #     )
    #     fig.text(
    #         text=['M', '3.0', '4.0', '5.0', '6.0'],
    #         x=[0.5, 1.5, 2.5, 3.5, 4.5],
    #         y=[0.2, 0.2, 0.2, 0.2, 0.2],
    #         font="12p,4,black",
    #         justify="CB"
    #     )
    # # ---plot colorbar---
    # fig.colorbar(frame=["a1000000000", "x+lTime"])
    # fig.shift_origin(xshift="-1c", yshift="-1.5c")
    # fig.basemap(
    #     region=[0, 14, 0, 1],
    #     projection="X14c/1c",
    #     frame='+t" "'
    # )
    # fig.text(
    #     text=startDate,
    #     x=1.5,
    #     y=0.2,
    #     font="12p,4,black",
    #     justify="CB"
    # )
    # fig.text(
    #     text=endDate,
    #     x=13.5,
    #     y=0.2,
    #     font="12p,4,black",
    #     justify="CB"
    # )
    return fig

def doubleTimeRangePlot(startDate1, endDate1, startDate2, endDate2, fig, data1, data2):
    """
    This module is for single time range earthquake distribution figure.
    :param startDate1: parameter for legend
    :param endDate1: parameter for legend
    :param startDate2: parameter for legend
    :param endDate2: parameter for legend
    :param fig: figure
    :param data1: catalog
    :param data2: catalog
    :return: fig
    """
    # ---get plot parameters from request---
    # firstCatalog = data1  # 获取到的地震目录数据
    # secondCatalog = data2  # 获取到的地震目录数据
    # ---get events parameters---
    firstEeventLongitude = [i['lon'] for i in data1]  # 地震经度
    firstEventLatitude = [i['lat'] for i in data1]  # 地震纬度
    firstEventMagnitude = [i['zhenJiZhi'] for i in data1]  # 地震震级
    secondEeventLongitude = [i['lon'] for i in data2]  # 地震经度
    secondEventLatitude = [i['lat'] for i in data2]  # 地震纬度
    secondEventMagnitude = [i['zhenJiZhi'] for i in data2]  # 地震震级
    # ---plot earthquakes---
    mag_plot = [float(i) * 0.08 for i in firstEventMagnitude]
    # ---plot 2 time_range earthquakes---
    fig.plot(
        x=firstEeventLongitude,
        y=firstEventLatitude,
        size=mag_plot,
        style="cc",
        color="blue",
        pen="black",
        label=f"%s~%s+S0.25c" % (startDate1, endDate1)
    )
    mag_plot = [float(i) * 0.08 for i in secondEventMagnitude]
    fig.plot(
        x=secondEeventLongitude,
        y=secondEventLatitude,
        size=mag_plot,
        style="cc",
        color="red",
        pen="black",
        label=f"%s~%s+S0.25c" % (startDate2, endDate2)
    )
    fig.legend(position="JBR+jBR+o0.2c/-1.6c", box="+pblack+gwhite")
    # ---plot mag symbol---
    # with fig.inset(position="jBL+w4c/1.4c+o0.2c/0.2c", box="+pblack+gwhite"):
    #     fig.basemap(
    #         region=[0, 5, 0, 2],
    #         projection="X4c/1.4c",
    #         frame='+t" "'
    #     )
    #     fig.plot(
    #         x=[1.5, 2.5, 3.5, 4.5],
    #         y=[1.4, 1.4, 1.4, 1.4],
    #         size=[0.3, 0.4, 0.5, 0.6],
    #         style="cc",
    #         color="white",
    #         pen="black"
    #     )
    #     fig.text(
    #         text=['M', '3.0', '4.0', '5.0', '6.0'],
    #         x=[0.5, 1.5, 2.5, 3.5, 4.5],
    #         y=[0.2, 0.2, 0.2, 0.2, 0.2],
    #         font="12p,4,black",
    #         justify="CB"
    #     )
    return fig

def plotEDF_custom_single(startDate, endDate, maxLon, minLon, maxLat, minLat, maxMag,minMag, figName, para):
    # ----------------------------------------------------------------------------------------------------------
    # --- 读取作图指令 ---
    if maxLon == '':
        maxLon = '106'  # 经度上限
    if minLon == '':
        minLon = '97'  # 经度下限
    if maxLat == '':
        maxLat = '29'  # 纬度上限
    if minLat == '':
        minLat = '21'  # 纬度下限
    if maxMag == '':
        maxMag = '9.9'  # 震级上限
    if minMag == '':
        minMag = '1.0'  # 震级下限
    if endDate == '':
        endDate = pd.to_datetime('today').strftime('%Y-%m-%d')  # 结束时间
    if startDate == '':
        startDate = endDate[0:4] + "-01-01"
        # startDate = str(int(endDate.split('-', 2)[0]) - 1) + "-01-01"
    # region = [minLon, maxLon, minLat, maxLat]
    # ------------------------------------------------------------------------------------------------------------
    # --- 设置访问目录种类 ---
    tag = "9"  # 访问目录种类
    # --- 请求目录 ---
    data = earthquakeDataRequest(tag, startDate, endDate, maxMag, minMag, maxLat, minLat, maxLon, minLon).json()
    # ------------------------------------------------------------------------------------------------------------
    magThreshold = 3.0
    catalog_statistic(data, para, magThreshold)
    # --- 画图 ---
    # --- 画底图 ---
    # *** plot earthquakes with colors based on event time ***
    fig = pygmt.Figure()
    fig.basemap(
        region=[minLon, maxLon, minLat, maxLat],
        projection="M15c",
        frame='a',
    )
    # ---plot boundaries---
    fig.plot(data="data/prov.txt", pen="1.5p,black")  # ,label="Province boundary"
    # ---plot faults---
    fig.plot(data="data/ynfault.txt", pen="0.5p,gray")  # ,label="Faults")
    singleTimeRangePlot(startDate, endDate, fig, data)
    # #---plot mag symbol---
    with fig.inset(position="jBL+w4c/1.4c+o0.2c/0.2c", box="+pblack+gwhite"):
        fig.basemap(
            region=[0, 5, 0, 2],
            projection="X4c/1.4c",
            frame='+t" "'
        )
        fig.plot(
            x=[1.5, 2.5, 3.5, 4.5],
            y=[1.4, 1.4, 1.4, 1.4],
            size=[0.24, 0.32, 0.4, 0.48],
            style="cc",
            color="white",
            pen="black"
        )
        fig.text(
            text=['ML', '3.0', '4.0', '5.0', '6.0'],
            x=[0.5, 1.5, 2.5, 3.5, 4.5],
            y=[0.2, 0.2, 0.2, 0.2, 0.2],
            font="12p,4,black",
            justify="CB"
        )
    # ---plot colorbar---
    fig.colorbar(
        frame=["a1000000000"],
        position="w10.5c/0.5c+h",
    )
    plot_time_label_for_single_time_range(startDate, endDate, fig)
    # --- 保存图片 ---
    # fig.savefig(figName)
    # figPath = (os.getcwd() + "\\" +figName)
    # print("本次做图成功，图件位置：%s" % figPath)
    figPath = "static/Custom/" + figName
    fig.savefig(figPath)
    figLoc = {'figLoc': figPath}
    para.append(figLoc)
    return para

def plotEDF_custom_double(startDate1, endDate1, maxLon, minLon, maxLat, minLat, maxMag,minMag, startDate2, endDate2, figName, para):
    # ----------------------------------------------------------------------------------------------------------
    # --- 读取作图指令 ---
    if maxLon == '':
        maxLon = '106'  # 经度上限
    if minLon == '':
        minLon = '97'  # 经度下限
    if maxLat == '':
        maxLat = '29'  # 纬度上限
    if minLat == '':
        minLat = '21'  # 纬度下限
    if maxMag == '':
        maxMag = '9.9'  # 震级上限
    if minMag == '':
        minMag = '1.0'  # 震级下限
    # if endDate == '':
    #     endDate = pd.to_datetime('today').strftime('%Y-%m-%d')  # 结束时间
    # if startDate == '':
    #     startDate = endDate[0:4] + "-01-01"
    # startDate = str(int(endDate.split('-', 2)[0]) - 1) + "-01-01"
    # region = [minLon, maxLon, minLat, maxLat]
    # ------------------------------------------------------------------------------------------------------------
    # --- 设置访问目录种类 ---
    tag = "9"  # 访问目录种类
    # --- 请求目录 ---
    data1 = earthquakeDataRequest(tag, startDate1, endDate1, maxMag, minMag, maxLat, minLat, maxLon, minLon).json()
    data2 = earthquakeDataRequest(tag, startDate2, endDate2, maxMag, minMag, maxLat, minLat, maxLon, minLon).json()
    # ------------------------------------------------------------------------------------------------------------
    magThreshold = 3.0
    catalog_statistic(data2, para, magThreshold)
    # --- 画图 ---
    fig = pygmt.Figure()
    fig.basemap(
        region=[minLon, maxLon, minLat, maxLat],
        projection="M15c",
        frame=True,
    )
    # ---plot boundaries---
    fig.plot(data="data/prov.txt", pen="1.5p,black")  # ,label="Province boundary"
    # ---plot faults---
    fig.plot(data="data/ynfault.txt", pen="0.5p,gray")  # ,label="Faults")
    doubleTimeRangePlot(startDate1, endDate1, startDate2, endDate2, fig, data1, data2)
    # ---plot mag symbol---
    with fig.inset(position="jBL+w4c/1.4c+o0.2c/-1.6c", box="+pblack+gwhite"):
        fig.basemap(
            region=[0, 5, 0, 2],
            projection="X4c/1.4c",
            frame='+t" "'
        )
        fig.plot(
            x=[1.5, 2.5, 3.5, 4.5],
            y=[1.4, 1.4, 1.4, 1.4],
            size=[0.3, 0.4, 0.5, 0.6],
            style="cc",
            color="white",
            pen="black"
        )
        fig.text(
            text=['ML', '3.0', '4.0', '5.0', '6.0'],
            x=[0.5, 1.5, 2.5, 3.5, 4.5],
            y=[0.2, 0.2, 0.2, 0.2, 0.2],
            font="12p,4,black",
            justify="CB"
        )
    # --- 保存图片 ---
    # fig.savefig(figName)
    # figPath = (os.getcwd() + "\\" +figName)
    # print("本次做图成功，图件位置：%s" % figPath)
    figPath = "static/Custom/" + figName
    fig.savefig(figPath)
    figLoc = {'figLoc': figPath}
    para.append(figLoc)
    return para

def plotEDF_globe_single(startDate, endDate, maxLon, minLon, maxLat, minLat, maxMag,minMag, figName, para):
    # ----------------------------------------------------------------------------------------------------------
    # --- 读取作图指令 ---
    if maxLon == '':
        maxLon = '180'  # 经度上限
    if minLon == '':
        minLon = '-180'  # 经度下限
    if maxLat == '':
        maxLat = '89.9'  # 纬度上限
    if minLat == '':
        minLat = '-89.9'  # 纬度下限
    if maxMag == '':
        maxMag = '9.9'  # 震级上限
    if minMag == '':
        minMag = '7.0'  # 震级下限
    if endDate == '':
        endDate = pd.to_datetime('today').strftime('%Y-%m-%d')  # 结束时间
    if startDate == '':
        startDate = str(int(endDate[0:4]) - 1) + "-01-01"
        # startDate = str(int(endDate.split('-', 2)[0]) - 1) + "-01-01"
    print('plot')
    # region = [minLon, maxLon, minLat, maxLat]
    # ------------------------------------------------------------------------------------------------------------
    # --- 设置访问目录种类 ---
    tag = "2"  # 访问目录种类
    # --- 请求目录 ---
    data = earthquakeDataRequest(tag, startDate, endDate, maxMag, minMag, maxLat, minLat, maxLon, minLon).json()
    # --- 数据检测模块 ---
    # if len(data) == 0:
    #     errorinfo = {"errorinfo":"There is no earthquake for both time_ranges of the required catalog !"}
    #     para.append(errorinfo)
    #     return para
    # ------------------------------------------------------------------------------------------------------------
    magThreshold = 7.0
    catalog_statistic(data, para, magThreshold)
    # --- 画图 ---
    fig = pygmt.Figure()
    fig.coast(
        region="g",
        projection="Q15c",
        land="white",
        water="lightblue",
        borders="1/0.1p",
        shorelines="1/0.1p",
        frame="a",
    )
    singleTimeRangePlot(startDate, endDate, fig, data)
    # #---plot mag symbol---
    with fig.inset(position="jBL+w2.8c/1.4c+o0.2c/0.2c", box="+pblack+gwhite"):
        fig.basemap(
            region=[0, 3.2, 0, 2],
            projection="X4c/1.4c",
            frame='+t" "'
        )
        fig.plot(
            x=[1.5, 2.5],
            y=[1.4, 1.4],
            size=[0.56, 0.64],
            style="cc",
            color="white",
            pen="black"
        )
        fig.text(
            text=['M', '7.0', '8.0'],
            x=[0.5, 1.5, 2.5],
            y=[0.2, 0.2, 0.2],
            font="12p,4,black",
            justify="CB"
        )
    # ---plot colorbar---
    fig.colorbar(
        frame=["a1000000000"],
        position="g50/-122+w10.5c/0.5c+h",
    )
    plot_time_label_for_single_time_range(startDate, endDate, fig)
    # --- 保存图片 ---
    # fig.savefig(figName)
    # figPath = (os.getcwd() + "\\" +figName)
    # print("本次做图成功，图件位置：%s" % figPath)
    figPath = "static/World/" + figName
    fig.savefig(figPath)
    figLoc = {'figLoc': figPath}
    para.append(figLoc)
    return para

def plotEDF_globe_double(startDate1, endDate1, maxLon, minLon, maxLat, minLat, maxMag,minMag, startDate2, endDate2, figName, para):
    # ----------------------------------------------------------------------------------------------------------
    # --- 读取作图指令 ---
    if maxLon == '':
        maxLon = '180'  # 经度上限
    if minLon == '':
        minLon = '-180'  # 经度下限
    if maxLat == '':
        maxLat = '89.9'  # 纬度上限
    if minLat == '':
        minLat = '-89.9'  # 纬度下限
    if maxMag == '':
        maxMag = '9.9'  # 震级上限
    if minMag == '':
        minMag = '7.0'  # 震级下限
    # if endDate == '':
    #     endDate = pd.to_datetime('today').strftime('%Y-%m-%d')  # 结束时间
    # if startDate == '':
    #     startDate = str(int(endDate[0:4]) - 1) + "-01-01"
        # startDate = str(int(endDate.split('-', 2)[0]) - 1) + "-01-01"
    # region = [minLon, maxLon, minLat, maxLat]
    # ------------------------------------------------------------------------------------------------------------
    # --- 设置访问目录种类 ---
    tag = "2"  # 访问目录种类
    # --- 请求目录 ---
    data1 = earthquakeDataRequest(tag, startDate1, endDate1, maxMag, minMag, maxLat, minLat, maxLon, minLon).json()
    data2 = earthquakeDataRequest(tag, startDate2, endDate2, maxMag, minMag, maxLat, minLat, maxLon, minLon).json()
    # ------------------------------------------------------------------------------------------------------------
    magThreshold = 7.0
    catalog_statistic(data2, para, magThreshold)
    # --- 画图 ---
    # --- 画底图 ---
    fig = pygmt.Figure()
    fig.coast(
        region="g",
        projection="Q15c",
        land="white",
        water="lightblue",
        borders="1/0.1p",
        shorelines="1/0.1p",
        frame="a",
    )
    # --- 调用双时间范围画图模块 ---
    doubleTimeRangePlot(startDate1, endDate1, startDate2, endDate2, fig, data1, data2)
    # --- 画图例 ---
    with fig.inset(position="jBL+w3.5c/1.0c+o0c/-1.6c", box="+p0.5p,black+gwhite"):
        fig.basemap(
            region=[0, 3.5, 0, 1],
            projection="X2.5c/0.7c",
            frame='+t" "'
        )
        fig.plot(
            x=[0.5, 2.3],
            y=[0.5, 0.5],
            size=[0.56, 0.64],
            style="cc",
            color="white",
            pen="black"
        )
        fig.text(
            text=['7.0', '8.0'],
            x=[1.3, 3.0],
            y=[0.35, 0.35],
            font="12p,4,black",
            justify="CB"
        )
    # --- 保存图片 ---
    # fig.savefig(figName)
    # figPath = (os.getcwd() + "\\" +figName)
    # print("本次做图成功，图件位置：%s" % figPath)
    figPath = "static/World/" + figName
    fig.savefig(figPath)
    figLoc = {'figLoc': figPath}
    para.append(figLoc)
    return para

def plotEDF_CN_single(startDate, endDate, maxLon, minLon, maxLat, minLat, maxMag,minMag, figName, para):
    # ----------------------------------------------------------------------------------------------------------
    # --- 读取作图指令 ---
    if maxLon == '':
        maxLon = '140'  # 经度上限
    if minLon == '':
        minLon = '70'  # 经度下限
    if maxLat == '':
        maxLat = '60'  # 纬度上限
    if minLat == '':
        minLat = '10'  # 纬度下限
    if maxMag == '':
        maxMag = '9.9'  # 震级上限
    if minMag == '':
        minMag = '5.0'  # 震级下限
    if endDate == '':
        endDate = pd.to_datetime('today').strftime('%Y-%m-%d')  # 结束时间
    if startDate == '':
        startDate = endDate[0:4] + "-01-01"
        # startDate = str(int(endDate.split('-', 2)[0]) - 1) + "-01-01"
    # region = [minLon, maxLon, minLat, maxLat]
    # ------------------------------------------------------------------------------------------------------------
    # --- 设置访问目录种类 ---
    tag = "2"  # 访问目录种类
    # --- 请求目录 ---
    data = earthquakeDataRequest(tag, startDate, endDate, maxMag, minMag, maxLat, minLat, maxLon, minLon).json()
    # ------------------------------------------------------------------------------------------------------------
    magThreshold = 5.0
    catalog_statistic(data, para, magThreshold)
    # --- 画图 ---
    # --- 画底图 ---
    fig = pygmt.Figure()
    fig.coast(
        region="CN",
        projection="M15c",
        land="lightgray",
        water="lightblue",
        borders="1/0.5p",
        shorelines="1/0.5p",
        frame="ag",
        dcw="CN+gwhite",
    )
    fig.coast(
        dcw="TW+gwhite",
    )
    singleTimeRangePlot(startDate, endDate, fig, data)
    # #---plot mag symbol---
    with fig.inset(position="jBL+w2.5c/1.4c+o0.2c/0.2c", box="+pblack+gwhite"):
        fig.basemap(
            region=[0, 4.7, 0, 2],
            projection="X4c/1.4c",
            frame='+t" "'
        )
        fig.plot(
            x=[1.5, 2.5, 3.5],
            y=[1.4, 1.4, 1.4],
            size=[0.4, 0.48, 0.56],
            style="cc",
            color="white",
            pen="black"
        )
        fig.text(
            text=['M', '5.0', '6.0', '7.0'],
            x=[0.5, 1.5, 2.5, 3.5],
            y=[0.2, 0.2, 0.2, 0.2],
            font="12p,4,black",
            justify="CB"
        )
    # ---plot colorbar---
    fig.colorbar(
        frame=["a1000000000"],
        position="g82/10+w10.5c/0.5c+h",
    )
    plot_time_label_for_single_time_range(startDate, endDate, fig)
    # --- 保存图片 ---
    # fig.savefig(figName)
    # figPath = (os.getcwd() + "\\" +figName)
    # print("本次做图成功，图件位置：%s" % figPath)
    figPath = "static/China/" + figName
    fig.savefig(figPath)
    figLoc = {'figLoc': figPath}
    para.append(figLoc)
    return para

def plotEDF_CN_double(startDate1, endDate1, maxLon, minLon, maxLat, minLat, maxMag,minMag, startDate2, endDate2, figName, para):
    # ----------------------------------------------------------------------------------------------------------
    # --- 读取作图指令 ---
    if maxLon == '':
        maxLon = '140'  # 经度上限
    if minLon == '':
        minLon = '70'  # 经度下限
    if maxLat == '':
        maxLat = '60'  # 纬度上限
    if minLat == '':
        minLat = '10'  # 纬度下限
    if maxMag == '':
        maxMag = '9.9'  # 震级上限
    if minMag == '':
        minMag = '5.0'  # 震级下限
    # if endDate == '':
    #     endDate = pd.to_datetime('today').strftime('%Y-%m-%d')  # 结束时间
    # if startDate == '':
    #     startDate = str(int(endDate[0:4]) - 1) + "-01-01"
        # startDate = str(int(endDate.split('-', 2)[0]) - 1) + "-01-01"
    # region = [minLon, maxLon, minLat, maxLat]
    # ------------------------------------------------------------------------------------------------------------
    # --- 设置访问目录种类 ---
    tag = "2"  # 访问目录种类
    # --- 请求目录 ---
    data1 = earthquakeDataRequest(tag, startDate1, endDate1, maxMag, minMag, maxLat, minLat, maxLon, minLon).json()
    data2 = earthquakeDataRequest(tag, startDate2, endDate2, maxMag, minMag, maxLat, minLat, maxLon, minLon).json()
    # ------------------------------------------------------------------------------------------------------------
    magThreshold = 5.0
    catalog_statistic(data2, para, magThreshold)
    # --- 画图 ---
    fig = pygmt.Figure()
    fig.coast(
        region="CN",
        projection="M15c",
        land="lightgray",
        water="lightblue",
        borders="1/0.5p",
        shorelines="1/0.5p",
        frame="ag",
        dcw="CN+gwhite",
    )
    fig.coast(
        dcw="TW+gwhite",
    )
    doubleTimeRangePlot(startDate1, endDate1, startDate2, endDate2, fig, data1, data2)
    # --- 画图例 ---
    with fig.inset(position="jBL+w4.5c/1.0c+o0c/-1.6c", box="+p0.5p,black+gwhite"):
        fig.basemap(
            region=[0, 5, 0, 1],
            projection="X2.5c/0.7c",
            frame='+t" "'
        )
        fig.plot(
            x=[0.5, 2.1, 3.7],
            y=[0.5, 0.5, 0.5],
            size=[0.4, 0.48, 0.56],
            style="cc",
            color="white",
            pen="black"
        )
        fig.text(
            text=['5.0', '6.0', '7.0'],
            x=[1.2, 2.9, 4.5],
            y=[0.35, 0.35, 0.35],
            font="12p,4,black",
            justify="CB"
        )
    # --- 保存图片 ---
    # fig.savefig(figName)
    # figPath = (os.getcwd() + "\\" +figName)
    # print("本次做图成功，图件位置：%s" % figPath)
    figPath = "static/China/" + figName
    fig.savefig(figPath)
    figLoc = {'figLoc': figPath}
    para.append(figLoc)
    return para

def plotEDF_chuandian_single(startDate, endDate, maxLon, minLon, maxLat, minLat, maxMag,minMag, figName, para):
    # ----------------------------------------------------------------------------------------------------------
    # --- 读取作图指令 ---
    if maxLon == '':
        maxLon = '108'  # 经度上限
    if minLon == '':
        minLon = '95'  # 经度下限
    if maxLat == '':
        maxLat = '35'  # 纬度上限
    if minLat == '':
        minLat = '21'  # 纬度下限
    if maxMag == '':
        maxMag = '9.9'  # 震级上限
    if minMag == '':
        minMag = '3.0'  # 震级下限
    if endDate == '':
        endDate = pd.to_datetime('today').strftime('%Y-%m-%d')  # 结束时间
    if startDate == '':
        startDate = endDate[0:4] + "-01-01"
        # startDate = str(int(endDate.split('-', 2)[0]) - 1) + "-01-01"
    # region = [minLon, maxLon, minLat, maxLat]
    # ------------------------------------------------------------------------------------------------------------
    # --- 设置访问目录种类 ---
    tag = "2"  # 访问目录种类
    # --- 请求目录 ---
    data = earthquakeDataRequest(tag, startDate, endDate, maxMag, minMag, maxLat, minLat, maxLon, minLon).json()
    # ------------------------------------------------------------------------------------------------------------
    magThreshold = 3.0
    catalog_statistic(data, para, magThreshold)
    # --- 画图 ---
    # --- 画底图 ---
    fig = pygmt.Figure()
    fig.basemap(
        region=[minLon, maxLon, minLat, maxLat],
        projection="M15c",
        frame=True,
    )
    # ---plot boundaries---
    fig.plot(data="data/prov.txt", pen="1.5p,black")  # ,label="Province boundary"
    # ---plot faults---
    fig.plot(data="data/CN-faults.dat", pen="0.5p,gray")  # ,label="Faults")
    singleTimeRangePlot(startDate, endDate, fig, data)
    # #---plot mag symbol---
    with fig.inset(position="jBL+w4c/1.4c+o0.2c/0.2c", box="+pblack+gwhite"):
        fig.basemap(
            region=[0, 5, 0, 2],
            projection="X4c/1.4c",
            frame='+t" "'
        )
        fig.plot(
            x=[1.5, 2.5, 3.5, 4.5],
            y=[1.4, 1.4, 1.4, 1.4],
            size=[0.24, 0.32, 0.4, 0.48],
            style="cc",
            color="white",
            pen="black"
        )
        fig.text(
            text=['M', '3.0', '4.0', '5.0', '6.0'],
            x=[0.5, 1.5, 2.5, 3.5, 4.5],
            y=[0.2, 0.2, 0.2, 0.2, 0.2],
            font="12p,4,black",
            justify="CB"
        )
    # ---plot colorbar---
    fig.colorbar(
        frame=["a1000000000"],
        position="g96.8/19.9+w10.5c/0.5c+h",
    )
    plot_time_label_for_single_time_range(startDate, endDate, fig)
    # --- 保存图片 ---
    # fig.savefig(figName)
    # figPath = (os.getcwd() + "\\" +figName)
    # print("本次做图成功，图件位置：%s" % figPath)
    figPath = "static/Chuandian/" + figName
    fig.savefig(figPath)
    figLoc = {'figLoc': figPath}
    para.append(figLoc)
    return para

def plotEDF_chuandian_double(startDate1, endDate1, maxLon, minLon, maxLat, minLat, maxMag,minMag, startDate2, endDate2, figName, para):
    # ----------------------------------------------------------------------------------------------------------
    # --- 读取作图指令 ---
    if maxLon == '':
        maxLon = '108'  # 经度上限
    if minLon == '':
        minLon = '95'  # 经度下限
    if maxLat == '':
        maxLat = '35'  # 纬度上限
    if minLat == '':
        minLat = '21'  # 纬度下限
    if maxMag == '':
        maxMag = '9.9'  # 震级上限
    if minMag == '':
        minMag = '3.0'  # 震级下限
    # if endDate == '':
    #     endDate = pd.to_datetime('today').strftime('%Y-%m-%d')  # 结束时间
    # if startDate == '':
    #     startDate = endDate[0:4] + "-01-01"
        # startDate = str(int(endDate.split('-', 2)[0]) - 1) + "-01-01"
    # region = [minLon, maxLon, minLat, maxLat]
    # ------------------------------------------------------------------------------------------------------------
    # --- 设置访问目录种类 ---
    tag = "2"  # 访问目录种类
    # --- 请求目录 ---
    data1 = earthquakeDataRequest(tag, startDate1, endDate1, maxMag, minMag, maxLat, minLat, maxLon, minLon).json()
    data2 = earthquakeDataRequest(tag, startDate2, endDate2, maxMag, minMag, maxLat, minLat, maxLon, minLon).json()
    # ------------------------------------------------------------------------------------------------------------
    magThreshold = 3.0
    catalog_statistic(data2, para, magThreshold)
    # --- 画图 ---
    # --- 画底图 ---
    fig = pygmt.Figure()
    fig.basemap(
        region=[minLon, maxLon, minLat, maxLat],
        projection="M15c",
        frame=True,
    )
    # ---plot boundaries---
    fig.plot(data="data/prov.txt", pen="1.5p,black")  # ,label="Province boundary"
    # ---plot faults---
    fig.plot(data="data/CN-faults.dat", pen="0.5p,gray")  # ,label="Faults")
    doubleTimeRangePlot(startDate1, endDate1, startDate2, endDate2, fig, data1, data2)
    # ---plot mag symbol---
    with fig.inset(position="jBL+w4c/1.4c+o0.2c/-1.6c", box="+pblack+gwhite"):
        fig.basemap(
            region=[0, 5, 0, 2],
            projection="X4c/1.4c",
            frame='+t" "'
        )
        fig.plot(
            x=[1.5, 2.5, 3.5, 4.5],
            y=[1.4, 1.4, 1.4, 1.4],
            size=[0.3, 0.4, 0.5, 0.6],
            style="cc",
            color="white",
            pen="black"
        )
        fig.text(
            text=['M', '3.0', '4.0', '5.0', '6.0'],
            x=[0.5, 1.5, 2.5, 3.5, 4.5],
            y=[0.2, 0.2, 0.2, 0.2, 0.2],
            font="12p,4,black",
            justify="CB"
        )
    # --- 保存图片 ---
    # fig.savefig(figName)
    # figPath = (os.getcwd() + "\\" +figName)
    # print("本次做图成功，图件位置：%s" % figPath)
    figPath = "static/Chuandian/" + figName
    fig.savefig(figPath)
    figLoc = {'figLoc': figPath}
    para.append(figLoc)
    return para

def plotEDF_YN_single(startDate, endDate, maxLon, minLon, maxLat, minLat, maxMag,minMag, figName, para):
    # ----------------------------------------------------------------------------------------------------------
    # --- 读取作图指令 ---
    if maxLon == '':
        maxLon = '106'  # 经度上限
    if minLon == '':
        minLon = '97'  # 经度下限
    if maxLat == '':
        maxLat = '29'  # 纬度上限
    if minLat == '':
        minLat = '21'  # 纬度下限
    if maxMag == '':
        maxMag = '9.9'  # 震级上限
    if minMag == '':
        minMag = '1.0'  # 震级下限
    if endDate == '':
        endDate = pd.to_datetime('today').strftime('%Y-%m-%d')  # 结束时间
    if startDate == '':
        startDate = endDate[0:4] + "-01-01"
        # startDate = str(int(endDate.split('-', 2)[0]) - 1) + "-01-01"
    # region = [minLon, maxLon, minLat, maxLat]
    # ------------------------------------------------------------------------------------------------------------
    # --- 设置访问目录种类 ---
    tag = "3"  # 访问目录种类
    # --- 请求目录 ---
    data = earthquakeDataRequest(tag, startDate, endDate, maxMag, minMag, maxLat, minLat, maxLon, minLon).json()
    # ------------------------------------------------------------------------------------------------------------
    magThreshold = 3.0
    catalog_statistic(data, para, magThreshold)
    # --- 画图 ---
    # --- 画底图 ---
    # *** plot earthquakes with colors based on event time ***
    fig = pygmt.Figure()
    fig.basemap(
        region=[minLon, maxLon, minLat, maxLat],
        projection="M15c",
        frame=True,
    )
    # ---plot boundaries---
    fig.plot(data="data/prov.txt", pen="1.5p,black")  # ,label="Province boundary"
    # ---plot faults---
    fig.plot(data="data/ynfault.txt", pen="0.5p,gray")  # ,label="Faults")
    singleTimeRangePlot(startDate, endDate, fig, data)
    # #---plot mag symbol---
    with fig.inset(position="jBL+w4c/1.4c+o0.2c/0.2c", box="+pblack+gwhite"):
        fig.basemap(
            region=[0, 5, 0, 2],
            projection="X4c/1.4c",
            frame='+t" "'
        )
        fig.plot(
            x=[1.5, 2.5, 3.5, 4.5],
            y=[1.4, 1.4, 1.4, 1.4],
            size=[0.24, 0.32, 0.4, 0.48],
            style="cc",
            color="white",
            pen="black"
        )
        fig.text(
            text=['ML', '3.0', '4.0', '5.0', '6.0'],
            x=[0.5, 1.5, 2.5, 3.5, 4.5],
            y=[0.2, 0.2, 0.2, 0.2, 0.2],
            font="12p,4,black",
            justify="CB"
        )
    # ---plot colorbar---
    fig.colorbar(
        frame=["a1000000000"],
        position="g98.3/20.4+w10.5c/0.5c+h",
    )
    plot_time_label_for_single_time_range(startDate, endDate, fig)
    # --- 保存图片 ---
    # fig.savefig(figName)
    # figPath = (os.getcwd() + "\\" +figName)
    # print("本次做图成功，图件位置：%s" % figPath)
    figPath = "static/Yunnan/" + figName
    fig.savefig(figPath)
    figLoc = {'figLoc': figPath}
    para.append(figLoc)
    return para

def plotEDF_YN_double(startDate1, endDate1, maxLon, minLon, maxLat, minLat, maxMag,minMag, startDate2, endDate2, figName, para):
    # ----------------------------------------------------------------------------------------------------------
    # --- 读取作图指令 ---
    if maxLon == '':
        maxLon = '106'  # 经度上限
    if minLon == '':
        minLon = '97'  # 经度下限
    if maxLat == '':
        maxLat = '29'  # 纬度上限
    if minLat == '':
        minLat = '21'  # 纬度下限
    if maxMag == '':
        maxMag = '9.9'  # 震级上限
    if minMag == '':
        minMag = '1.0'  # 震级下限
    # if endDate == '':
    #     endDate = pd.to_datetime('today').strftime('%Y-%m-%d')  # 结束时间
    # if startDate == '':
    #     startDate = endDate[0:4] + "-01-01"
        # startDate = str(int(endDate.split('-', 2)[0]) - 1) + "-01-01"
    # region = [minLon, maxLon, minLat, maxLat]
    # ------------------------------------------------------------------------------------------------------------
    # --- 设置访问目录种类 ---
    tag = "9"  # 访问目录种类
    # --- 请求目录 ---
    data1 = earthquakeDataRequest(tag, startDate1, endDate1, maxMag, minMag, maxLat, minLat, maxLon, minLon).json()
    data2 = earthquakeDataRequest(tag, startDate2, endDate2, maxMag, minMag, maxLat, minLat, maxLon, minLon).json()
    # ------------------------------------------------------------------------------------------------------------
    magThreshold = 3.0
    catalog_statistic(data2, para, magThreshold)
    # --- 画图 ---
    fig = pygmt.Figure()
    fig.basemap(
        region=[minLon, maxLon, minLat, maxLat],
        projection="M15c",
        frame=True,
    )
    # ---plot boundaries---
    fig.plot(data="data/prov.txt", pen="1.5p,black")  # ,label="Province boundary"
    # ---plot faults---
    fig.plot(data="data/ynfault.txt", pen="0.5p,gray")  # ,label="Faults")
    doubleTimeRangePlot(startDate1, endDate1, startDate2, endDate2, fig, data1, data2)
    # ---plot mag symbol---
    with fig.inset(position="jBL+w4c/1.4c+o0.2c/-1.6c", box="+pblack+gwhite"):
        fig.basemap(
            region=[0, 5, 0, 2],
            projection="X4c/1.4c",
            frame='+t" "'
        )
        fig.plot(
            x=[1.5, 2.5, 3.5, 4.5],
            y=[1.4, 1.4, 1.4, 1.4],
            size=[0.3, 0.4, 0.5, 0.6],
            style="cc",
            color="white",
            pen="black"
        )
        fig.text(
            text=['ML', '3.0', '4.0', '5.0', '6.0'],
            x=[0.5, 1.5, 2.5, 3.5, 4.5],
            y=[0.2, 0.2, 0.2, 0.2, 0.2],
            font="12p,4,black",
            justify="CB"
        )
    # --- 保存图片 ---
    # fig.savefig(figName)
    # figPath = (os.getcwd() + "\\" +figName)
    # print("本次做图成功，图件位置：%s" % figPath)
    figPath = "static/Yunnan/" + figName
    fig.savefig(figPath)
    figLoc = {'figLoc': figPath}
    para.append(figLoc)
    return para

def plotEDF_Tibet_single(startDate, endDate, maxLon, minLon, maxLat, minLat, maxMag,minMag, figName, para):
    # ----------------------------------------------------------------------------------------------------------
    # --- 读取作图指令 ---
    if maxLon == '':
        maxLon = '94.5'  # 经度上限
    if minLon == '':
        minLon = '82'  # 经度下限
    if maxLat == '':
        maxLat = '32'  # 纬度上限
    if minLat == '':
        minLat = '26.5'  # 纬度下限
    if maxMag == '':
        maxMag = '9.9'  # 震级上限
    if minMag == '':
        minMag = '3.0'  # 震级下限
    if endDate == '':
        endDate = pd.to_datetime('today').strftime('%Y-%m-%d')  # 结束时间
    if startDate == '':
        startDate = time.strftime("%Y-%m-%d", time.localtime(
            time.mktime(time.strptime(endDate, "%Y-%m-%d")) - 30 * 24 * 60 * 60))  # 开始时间
    # region = [minLon, maxLon, minLat, maxLat]
    # ------------------------------------------------------------------------------------------------------------
    # --- 设置访问目录种类 ---
    tag = "5"  # 访问目录种类
    # --- 请求目录 ---
    data = earthquakeDataRequest(tag, startDate, endDate, maxMag, minMag, maxLat, minLat, maxLon, minLon).json()
    # ------------------------------------------------------------------------------------------------------------
    magThreshold = 3.0
    catalog_statistic(data, para, magThreshold)
    # --- 画图 ---
    fig = pygmt.Figure()
    fig.basemap(
        region=[minLon, maxLon, minLat, maxLat],
        projection="M15c",
        frame=True,
    )
    fig.coast(
        land='lightblue',
    )
    # ---plot boundaries---
    fig.plot(data="data/Tibet_boundary.txt", pen="1.5p,red")  # ,label="Province boundary"
    # ---plot faults---
    fig.plot(data="data/CN-faults.dat", pen="0.5p,gray")  # ,label="Faults")
    singleTimeRangePlot(startDate, endDate, fig, data)
    # #---plot mag symbol---
    with fig.inset(position="jBL+w4c/1.4c+o0.2c/0.2c", box="+pblack+gwhite"):
        fig.basemap(
            region=[0, 5, 0, 2],
            projection="X4c/1.4c",
            frame='+t" "'
        )
        fig.plot(
            x=[1.5, 2.5, 3.5, 4.5],
            y=[1.4, 1.4, 1.4, 1.4],
            size=[0.24, 0.32, 0.4, 0.48],
            style="cc",
            color="white",
            pen="black"
        )
        fig.text(
            text=['M', '3.0', '4.0', '5.0', '6.0'],
            x=[0.5, 1.5, 2.5, 3.5, 4.5],
            y=[0.2, 0.2, 0.2, 0.2, 0.2],
            font="12p,4,black",
            justify="CB"
        )
    # --- Plot colorbar and time label ---
    fig.colorbar(
        frame=["a1000000000"],
        position="g84/25.5+w10.5c/0.5c+h",
    )
    plot_time_label_for_single_time_range(startDate, endDate, fig)

    # --- 保存图片 ---
    # fig.savefig(figName)
    # figPath = (os.getcwd() + "\\" +figName)
    # print("本次做图成功，图件位置：%s" % figPath)
    figPath = "static/Tibet/" + figName
    fig.savefig(figPath)
    figLoc = {'figLoc': figPath}
    para.append(figLoc)
    return para

def plotEDF_Tibet_double(startDate1, endDate1, maxLon, minLon, maxLat, minLat, maxMag,minMag, startDate2, endDate2, figName, para):
    # ----------------------------------------------------------------------------------------------------------
    # --- 读取作图指令 ---
    if maxLon == '':
        maxLon = '94.5'  # 经度上限
    if minLon == '':
        minLon = '82'  # 经度下限
    if maxLat == '':
        maxLat = '32'  # 纬度上限
    if minLat == '':
        minLat = '26.5'  # 纬度下限
    if maxMag == '':
        maxMag = '9.9'  # 震级上限
    if minMag == '':
        minMag = '3.0'  # 震级下限
    # if endDate1 == '':
    #     print('Error: please input endDate1 !')
    #     return
        # endDate = pd.to_datetime('today').strftime('%Y-%m-%d')  # 结束时间
    # if startDate == '':
    #     startDate = time.strftime("%Y-%m-%d", time.localtime(
    #         time.mktime(time.strptime(endDate, "%Y-%m-%d")) - 30 * 24 * 60 * 60))  # 开始时间
    # region = [minLon, maxLon, minLat, maxLat]
    # ------------------------------------------------------------------------------------------------------------
    # --- 设置访问目录种类 ---
    tag = "5"  # 访问目录种类
    # --- 请求目录 ---
    data1 = earthquakeDataRequest(tag, startDate1, endDate1, maxMag, minMag, maxLat, minLat, maxLon, minLon).json()
    data2 = earthquakeDataRequest(tag, startDate2, endDate2, maxMag, minMag, maxLat, minLat, maxLon, minLon).json()
    # ------------------------------------------------------------------------------------------------------------
    magThreshold = 3.0
    catalog_statistic(data2, para, magThreshold)
    # --- 画图 ---
    fig = pygmt.Figure()
    fig.basemap(
        region=[minLon, maxLon, minLat, maxLat],
        projection="M15c",
        frame=True,
    )
    fig.coast(
        land='lightblue',
    )
    # ---plot boundaries---
    fig.plot(data="data/Tibet_boundary.txt", pen="1.0p,black")  # ,label="Province boundary"
    # ---plot faults---
    fig.plot(data="data/CN-faults.dat", pen="0.5p,gray")  # ,label="Faults")
    doubleTimeRangePlot(startDate1, endDate1, startDate2, endDate2, fig, data1, data2)
    # ---plot mag symbol---
    with fig.inset(position="jBL+w4c/1.4c+o0.2c/-1.6c", box="+pblack+gwhite"):
        fig.basemap(
            region=[0, 5, 0, 2],
            projection="X4c/1.4c",
            frame='+t" "'
        )
        fig.plot(
            x=[1.5, 2.5, 3.5, 4.5],
            y=[1.4, 1.4, 1.4, 1.4],
            size=[0.3, 0.4, 0.5, 0.6],
            style="cc",
            color="white",
            pen="black"
        )
        fig.text(
            text=['M', '3.0', '4.0', '5.0', '6.0'],
            x=[0.5, 1.5, 2.5, 3.5, 4.5],
            y=[0.2, 0.2, 0.2, 0.2, 0.2],
            font="12p,4,black",
            justify="CB"
        )
    # --- 保存图片 ---
    # fig.savefig(figName)
    # figPath = (os.getcwd() + "\\" +figName)
    # print("本次做图成功，图件位置：%s" % figPath)
    figPath = "static/Tibet/" + figName
    fig.savefig(figPath)
    figLoc = {'figLoc': figPath}
    para.append(figLoc)
    return para