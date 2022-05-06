""" Earthquakes Magnitude Counts Module"""

import requests

def earthquakeDataRequest(tag, startDate, endDate, maxMag, minMag, maxLat, minLat, maxLon, minLon):
    # --- 服务器请求模块 ---
    # --- 固定参数含义 ---
    # -----------------------------------------------------------------
    # 表的索引标签  表名
    # tag = 0:   autokbdzml_d - -自动编目的速报目录(局内ftp, 每五分钟更新一次)
    # tag = 1:   dzml_china_ms5 - -全国M5.0以上地震目录(每天更新两次)
    # tag = 2:   dzml_eqim_p01 - -全国小震目录，震级为MS(每天更新两次)
    # tag = 3:   dzml_M3 - -全国3级以上地震目录（MS）(每天更新两次)
    # tag = 4:   dzml_M5 - -全国5级以上地震目录（MS）(每天更新两次)
    # tag = 5:   dzml_new - -全国小震目录，震级为ML(每天更新两次)
    # tag = 6:   dzml_W7 - -全球7级地震目录（MS）(每天更新两次)
    # tag = 7:   dzml_world_ms7 - -全球M7.0以上地震目录(每天更新两次)
    # tag = 8:   earthquakes - -地震短信速报地震目录(正式报, 自动触发)
    # tag = 9:   sbml_d - -云南速报地震目录(局内ftp, 每五分钟更新一次)

    params = ("tag=" + tag + "&startDate=" + startDate + "&endDate=" + endDate + "&minMag="
              + minMag + "&maxMag=" + maxMag + "&maxLat=" + maxLat + "&minLat="
              + minLat + "&maxLon=" + maxLon + "&minLon=" + minLon)
    url = "http://10.53.204.152:8080/seis"  # webserver address
    response = requests.get(url, params=params)
    return response