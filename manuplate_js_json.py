# from selenium import webdriver
import xlsxwriter

from selenium.webdriver.chrome.options import Options
from openpyxl import Workbook
import pandas as pd
import csv

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

import os
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random
import time


options = Options()
options.accept_untrusted_certs = True
options.assume_untrusted_cert_issuer = True
options.add_argument("window-size=1920,1080")
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
options.add_argument(f"user-agent={user_agent}")
options.add_argument("headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-session-crashed-bubble")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-dev-shm-using")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-ipv6")
m_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
print("Sucessfully the webdriver runned.")

# m_driver = webdriver.Chrome(
#     executable_path="{0}/chromedriver/chromedriver.exe".format(os.getcwd())
# )  # , options=options)
# m_driver.maximize_window()
# m_driver.implicitly_wait(10)
m_driver.get("http://qd.ieprint.cc/#/waleng")

js_sample_album = """
    let body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "封面", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": true, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 7 }, "ZhiZhang": { "LeiXing": 14, "KeZhong": 102 }, "Width": { "Value": 420 }, "Height": { "Value": "285" }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "亮膜", "Enable": true }, "MoQie": { "Enable": false, "MoQieZhongLei": "" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": false, "HeXing": "" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "", "Enable": false } }, "P": 4, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false }, { "MingCheng": "内页", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": true, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 7 }, "ZhiZhang": { "LeiXing": 14, "KeZhong": 111 }, "Width": { "Value": 420 }, "Height": { "Value": "285" }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": false, "MoQieZhongLei": "" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": false, "HeXing": "" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "", "Enable": false } }, "P": 16, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": true, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "", "QiMaDing": true }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 210, "ChengPinHeight": 285, "ChengPinHou": 0, "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 420, "ZhanKaiHeight": "285", "ShuLiang": 1000, "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "" }'); 
    //body_json.BuJians[0].MingCheng = '';m_Width, m_Height, m_ShuLiang
    const m_Width = arguments[1];
    const m_Height = arguments[2];
    const m_ShuLiang = arguments[3];
    body_json.BuJians[0].Width.Value = m_Width * 2;
    body_json.BuJians[0].Height.Value = m_Height;
    body_json.BuJians[1].Width.Value = m_Width * 2;
    body_json.BuJians[1].Height.Value = m_Height;
    body_json.ChengPinWidth = m_Width;
    body_json.ChengPinHeight = m_Height
    body_json.ZhangKaiWidth = m_Width * 2
    body_json.ZhangKaiHeight = m_Height
    body_json.ShuLiang = m_ShuLiang
    let body_txt = JSON.stringify(body_json);
    let urls = "http://qd.ieprint.cc/api/BaoJiaApi/DanyeBaojia?CiShu="+arguments[0]+"&pageCode=pageCode";
    let response = await fetch(
        urls,
        {
        headers: {
            accept: "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9,ko;q=0.8,zh;q=0.7,ko;q=0.6,und;q=0.5",
            "bj-guid": "2847c4d4-5363-4dc8-9b42-b520e999e7bf",
            "content-type": "application/json;charset=UTF-8",
        },
        referrer: "http://qd.ieprint.cc/",
        referrerPolicy: "no-referrer-when-downgrade",
        body: body_txt,
        method: "POST",
        mode: "cors",
        credentials: "omit",
        }
    );

    let myJson = await response.json(); //extract JSON from the http response
    // do something with myJson
    //console.log(myJson);
    //console.log(arguments[0])

    return myJson;
"""
js_color_pill_box = """
    let body_json;
    //body_json.BuJians[0].MingCheng = '';m_Width, m_Height, m_ShuLiang
    const params = arguments[1];
    switch (parseInt(params.m_box_variety)) {
        case 1://"Siamese display box":
            body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": true, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 0 }, "ZhiZhang": { "LeiXing": 16, "KeZhong": 117 }, "Width": { "Value": 0 }, "Height": { "Value": 0 }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": true, "MoQieZhongLei": "彩盒" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "单面", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "单面", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": true, "HeXing": "" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "", "Enable": false } }, "P": 1, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false, "MingChen": "彩盒" }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": true, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": false, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "" }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 80, "ChengPinHeight": 40, "ChengPinHou": "120", "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 0, "ZhanKaiHeight": 0, "ShuLiang": "1000", "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "", "DanPinGongSiHeight": "宽*2+高*4+5", "DanPinGongSiWidth": "长+高*4+5*2", "ShuangPinGongSiHeight": "宽*2+高*2+5", "ShuangPinGongSiWidth": "长+高*4+5*2", "HeXing": "连体展示盒" }'); 
            break;
        case 2://"Insert the bottom box":
            body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": true, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 0 }, "ZhiZhang": { "LeiXing": 16, "KeZhong": 117 }, "Width": { "Value": 0 }, "Height": { "Value": 0 }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": true, "MoQieZhongLei": "彩盒" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "单面", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "单面", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": true, "HeXing": "" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "", "Enable": false } }, "P": 1, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false, "MingChen": "彩盒" }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": true, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": false, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "" }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 80, "ChengPinHeight": 40, "ChengPinHou": "120", "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 0, "ZhanKaiHeight": 0, "ShuLiang": "1000", "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "", "DanPinGongSiHeight": "(长+宽)*2+25", "DanPinGongSiWidth": "宽/2+30+高+宽+25", "ShuangPinGongSiHeight": "长+宽+25", "ShuangPinGongSiWidth": "宽/2+30+高+宽+25", "HeXing": "上盖下插底盒" }'); 
            break;
        case 3://"Upper and lower cover":
            body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": true, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 0 }, "ZhiZhang": { "LeiXing": 16, "KeZhong": 117 }, "Width": { "Value": 0 }, "Height": { "Value": 0 }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": true, "MoQieZhongLei": "彩盒" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "单面", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "单面", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": true, "HeXing": "" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "", "Enable": false } }, "P": 1, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false, "MingChen": "彩盒" }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": true, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": false, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "" }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 80, "ChengPinHeight": 40, "ChengPinHou": "120", "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 0, "ZhanKaiHeight": 0, "ShuLiang": "1000", "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "", "DanPinGongSiHeight": "(宽+高*4+30)*2", "DanPinGongSiWidth": "长+高*4+30", "ShuangPinGongSiHeight": "宽+高*4+30", "ShuangPinGongSiWidth": "长+高*4+30", "HeXing": "上下盖（衬衣盒）" }'); 
            break;
        case 4://"Hook bottom box":
            body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": true, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 0 }, "ZhiZhang": { "LeiXing": 16, "KeZhong": 117 }, "Width": { "Value": 0 }, "Height": { "Value": 0 }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": true, "MoQieZhongLei": "彩盒" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "单面", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "单面", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": true, "HeXing": "" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "", "Enable": false } }, "P": 1, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false, "MingChen": "彩盒" }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": true, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": false, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "" }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 80, "ChengPinHeight": 40, "ChengPinHou": "120", "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 0, "ZhanKaiHeight": 0, "ShuLiang": "1000", "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "", "DanPinGongSiHeight": "长*2+宽*2+15", "DanPinGongSiWidth": "高+宽*2+15+15", "ShuangPinGongSiHeight": "长+宽+20", "ShuangPinGongSiWidth": "高+宽*2+20+20", "HeXing": "钩底盒" }'); 
            break;
        case 5://"Hanging box":
            body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": true, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 0 }, "ZhiZhang": { "LeiXing": 16, "KeZhong": 117 }, "Width": { "Value": 0 }, "Height": { "Value": 0 }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": true, "MoQieZhongLei": "彩盒" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "单面", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "单面", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": true, "HeXing": "" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "", "Enable": false } }, "P": 1, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false, "MingChen": "彩盒" }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": true, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": false, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "" }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 80, "ChengPinHeight": 40, "ChengPinHou": "120", "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 0, "ZhanKaiHeight": 0, "ShuLiang": "1000", "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "", "DanPinGongSiHeight": "长*2+宽*2+15", "DanPinGongSiWidth": "高+宽*2+20+20", "ShuangPinGongSiHeight": "长+宽+20", "ShuangPinGongSiWidth": "长+高*2+10*2", "HeXing": "挂盒" }'); 
            break;
        case 6://"Self-forming box":
            body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": true, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 0 }, "ZhiZhang": { "LeiXing": 16, "KeZhong": 117 }, "Width": { "Value": 0 }, "Height": { "Value": 0 }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": true, "MoQieZhongLei": "彩盒" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "单面", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "单面", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": true, "HeXing": "" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "", "Enable": false } }, "P": 1, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false, "MingChen": "彩盒" }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": true, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": false, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "" }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 80, "ChengPinHeight": 40, "ChengPinHou": "120", "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 0, "ZhanKaiHeight": 0, "ShuLiang": "1000", "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "", "DanPinGongSiHeight": "高*2+宽*2+40+30", "DanPinGongSiWidth": "长+高*2+10*2", "ShuangPinGongSiHeight": "长+高*2+10*2", "ShuangPinGongSiWidth": "高+宽+40", "HeXing": "自成形盒" }'); 
            break;
        case 7:// "Isert bottom box up and down":
            body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": true, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 0 }, "ZhiZhang": { "LeiXing": 16, "KeZhong": 117 }, "Width": { "Value": 0 }, "Height": { "Value": 0 }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": true, "MoQieZhongLei": "彩盒" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "单面", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "单面", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": true, "HeXing": "" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "", "Enable": false } }, "P": 1, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false, "MingChen": "彩盒" }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": true, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": false, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "" }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 80, "ChengPinHeight": 40, "ChengPinHou": "120", "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 0, "ZhanKaiHeight": 0, "ShuLiang": "1000", "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "", "DanPinGongSiHeight": "(长+宽)*2+20", "DanPinGongSiWidth": "高+宽*2+15+15", "ShuangPinGongSiHeight": "长+宽+20", "ShuangPinGongSiWidth": "高+宽*2+15+15", "HeXing": "上下插底盒" }'); 
            break;
        default:
            body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": true, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 0 }, "ZhiZhang": { "LeiXing": 16, "KeZhong": 117 }, "Width": { "Value": 0 }, "Height": { "Value": 0 }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": true, "MoQieZhongLei": "彩盒" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "单面", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "单面", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": true, "HeXing": "" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "", "Enable": false } }, "P": 1, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false, "MingChen": "彩盒" }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": true, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": false, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "" }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 80, "ChengPinHeight": 40, "ChengPinHou": "120", "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 0, "ZhanKaiHeight": 0, "ShuLiang": "1000", "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "", "DanPinGongSiHeight": "宽*2+高*4+5", "DanPinGongSiWidth": "长+高*4+5*2", "ShuangPinGongSiHeight": "宽*2+高*2+5", "ShuangPinGongSiWidth": "长+高*4+5*2", "HeXing": "连体展示盒" }'); 

    }

    body_json.BuJians[0].P = params.m_PinZhong;
    body_json.BuJians[0].PinZhong = params.m_PinZhong;
    body_json.ChengPinWidth = params.m_ChengPinWidth;
    body_json.ChengPinHeight = params.m_ChengPinHeight;
    body_json.ChengPinHou = params.m_ChengPinHou;
    body_json.ShuLiang = params.m_ShuLiang;
    body_json.PinZhong = params.m_PinZhong;
    //material gram
    body_json.BuJians[0].ZhiZhang.LeiXing = params.m_LeiXing;
    body_json.BuJians[0].ZhiZhang.KeZhong = params.m_KeZhong;
    // if kezhong = 200 then 162
    //Color
    body_json.BuJians[0].ZhengMianColor.ZhuanSe = params.m_ZhengMianColor;

    //binding Parameters
    body_json.BuJians[0].HouGong.HuHe.Enable = params.Formed_a_box;
    if(params.FuMo_Enable){
        body_json.BuJians[0].HouGong.FuMo.Enable = params.FuMo_Enable;
        body_json.BuJians[0].HouGong.FuMo.FuMoZhongLei = params.FuMo_FuMoZhongLei 
    }
    if(params.ShouTiSheng_Enable){
        body_json.BuJians[0].HouGong.ShouTiSheng.Enable = true;
        body_json.BuJians[0].HouGong.ShouTiSheng.CaiLiao = params.ShouTiSheng_CaiLiao;
    }
    if(params.TiBa_Enable){
        body_json.BuJians[0].HouGong.ShouTiSheng.Enable = false;
        body_json.BuJians[0].HouGong.TiBa.Enable = true;
    }
    if(params.DanMianTangYin_Enable){
        body_json.BuJians[0].HouGong.DanMianTangYin.Enable = true;
        body_json.BuJians[0].HouGong.DanMianTangYin.Width = params.DanMianTangYin_Width;
        body_json.BuJians[0].HouGong.DanMianTangYin.Height = params.DanMianTangYin_Height;
    }
    if(params.DanMianTangJin_Enable){
        body_json.BuJians[0].HouGong.DanMianTangJin.Enable = true;
        body_json.BuJians[0].HouGong.DanMianTangJin.Width = params.DanMianTangJin_Width;
        body_json.BuJians[0].HouGong.DanMianTangJin.Height = params.DanMianTangJin_Height;
    }
    if(params.KaiTianChuang_Enable){
        body_json.BuJians[0].HouGong.KaiTianChuang.Enable = true;
        body_json.BuJians[0].HouGong.KaiTianChuang.Width = params.KaiTianChuang_Width;
        body_json.BuJians[0].HouGong.KaiTianChuang.Height = params.KaiTianChuang_Height;
    }
    if(params.DanMianJiTu_Enable){
        body_json.BuJians[0].HouGong.DanMianJiTu.Enable = true;
        body_json.BuJians[0].HouGong.DanMianJiTu.Width = params.DanMianJiTu_Width;
        body_json.BuJians[0].HouGong.DanMianJiTu.Height = params.DanMianJiTu_Height;
    }
    if(params.DanMianJiTu_Enable){
        body_json.BuJians[0].HouGong.JuBuUV.Enable = true;
        body_json.BuJians[0].HouGong.JuBuUV.Width = params.JuBuUV_Width;
        body_json.BuJians[0].HouGong.JuBuUV.Height = params.JuBuUV_Height;
        body_json.BuJians[0].HouGong.JuBuUV.UVCaiLiao = params.JuBuUV_UVCaiLiao;
    }
    if(params.GuoYou_Enable){
        body_json.BuJians[0].HouGong.GuoYou.Enable = true;
        body_json.BuJians[0].HouGong.GuoYou.CaiLiao = params.GuoYou_CaiLiao;
    }


    let body_txt = JSON.stringify(body_json);
    let urls = "http://qd.ieprint.cc/api/BaoJiaApi/DanyeBaojia?CiShu="+arguments[0]+"&pageCode=pageCode";
    let response = await fetch(
        urls,
        {
        headers: {
            accept: "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9,ko;q=0.8,zh;q=0.7,ko;q=0.6,und;q=0.5",
            "bj-guid": "11824be6-bf4e-463e-b7e2-cdc02c806498",
            "content-type": "application/json;charset=UTF-8",
        },
        referrer: "http://qd.ieprint.cc/",
        referrerPolicy: "no-referrer-when-downgrade",
        body: body_txt,
        method: "POST",
        mode: "cors",
        credentials: "omit",
        }
    );

    let myJson = await response.json(); //extract JSON from the http response
    // do something with myJson
    //console.log(myJson);
    //console.log(arguments[0])

    return myJson;
"""
js_corrugated_box = """
    let body_json;
    //body_json.BuJians[0].MingCheng = '';m_Width, m_Height, m_ShuLiang
    const params = arguments[1];
    switch (parseInt(params.m_box_variety)) {
        case 1://"Insert the bottom box under the upper cover":
            body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": true, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 0 }, "ZhiZhang": { "LeiXing": 16, "KeZhong": 116 }, "Width": { "Value": 0 }, "Height": { "Value": 0 }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": true, "MoQieZhongLei": "小包装" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "单面", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "单面", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": true, "HeXing": "其他" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "三层高强度瓦楞板", "Enable": true } }, "P": 1, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false, "MingChen": "小包装" }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": true, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": false, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "" }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 350, "ChengPinHeight": 260, "ChengPinHou": "320", "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 0, "ZhanKaiHeight": 0, "ShuLiang": "1000", "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "", "DanPinGongSiHeight": "(长+宽)*2+25", "DanPinGongSiWidth": "宽/2+30+高+宽+25", "ShuangPinGongSiHeight": "长+宽+25", "ShuangPinGongSiWidth": "宽/2+30+高+宽+25", "HeXing": "上盖下插底盒" }'); 
            break;
        case 2://"suitcase":
            body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": true, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 0 }, "ZhiZhang": { "LeiXing": 16, "KeZhong": 116 }, "Width": { "Value": 0 }, "Height": { "Value": 0 }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": true, "MoQieZhongLei": "小包装" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "单面", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "单面", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": true, "HeXing": "其他" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "三层高强度瓦楞板", "Enable": true } }, "P": 1, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false, "MingChen": "小包装" }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": true, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": false, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "" }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 350, "ChengPinHeight": 260, "ChengPinHou": "320", "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 0, "ZhanKaiHeight": 0, "ShuLiang": "1000", "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "", "DanPinGongSiHeight": "(长+宽)*2+30", "DanPinGongSiWidth": "宽/2+30+高+宽/2+25+80", "ShuangPinGongSiHeight": "长+宽+30", "ShuangPinGongSiWidth": "宽/2+30+高+宽/2+25+80", "HeXing": "手提箱" }'); 
            break;
        case 3://"Promotion box":
            body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": true, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 0 }, "ZhiZhang": { "LeiXing": 16, "KeZhong": 116 }, "Width": { "Value": 0 }, "Height": { "Value": 0 }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": true, "MoQieZhongLei": "小包装" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "单面", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "单面", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": true, "HeXing": "其他" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "三层高强度瓦楞板", "Enable": true } }, "P": 1, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false, "MingChen": "小包装" }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": true, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": false, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "" }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 350, "ChengPinHeight": 260, "ChengPinHou": "320", "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 0, "ZhanKaiHeight": 0, "ShuLiang": "1000", "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "", "DanPinGongSiHeight": "(长+宽)*2+25", "DanPinGongSiWidth": "宽/2+30+高+宽+25", "ShuangPinGongSiHeight": "长+宽+25", "ShuangPinGongSiWidth": "宽/2+30+高+宽+25", "HeXing": "提拔盒" }'); 
            break;
        case 4://"Counterpart box":
            body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": true, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 0 }, "ZhiZhang": { "LeiXing": 16, "KeZhong": 116 }, "Width": { "Value": 0 }, "Height": { "Value": 0 }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": true, "MoQieZhongLei": "小包装" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "单面", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "单面", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": true, "HeXing": "其他" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "三层高强度瓦楞板", "Enable": true } }, "P": 1, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false, "MingChen": "小包装" }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": true, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": false, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "" }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 350, "ChengPinHeight": 260, "ChengPinHou": "320", "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 0, "ZhanKaiHeight": 0, "ShuLiang": "1000", "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "", "DanPinGongSiHeight": "(长+宽)*2+30", "DanPinGongSiWidth": "高+宽", "ShuangPinGongSiHeight": "(长+宽)+30", "ShuangPinGongSiWidth": "宽+高", "HeXing": "对口箱" }'); 
            break;
        case 7://"Insert bottom box up and down":
            body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": true, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 0 }, "ZhiZhang": { "LeiXing": 16, "KeZhong": 116 }, "Width": { "Value": 0 }, "Height": { "Value": 0 }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": true, "MoQieZhongLei": "小包装" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "单面", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "单面", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": true, "HeXing": "其他" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "三层高强度瓦楞板", "Enable": true } }, "P": 1, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false, "MingChen": "小包装" }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": true, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": false, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "" }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 350, "ChengPinHeight": 260, "ChengPinHou": "320", "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 0, "ZhanKaiHeight": 0, "ShuLiang": "1000", "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "", "DanPinGongSiHeight": "(长+宽)*2+20", "DanPinGongSiWidth": "高+宽*2+15+15", "ShuangPinGongSiHeight": "长+宽+20", "ShuangPinGongSiWidth": "高+宽*2+15+15", "HeXing": "上下插底盒" }'); 
            break;
        case 9://"Inclined box":
            body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": true, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 0 }, "ZhiZhang": { "LeiXing": 16, "KeZhong": 116 }, "Width": { "Value": 0 }, "Height": { "Value": 0 }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": true, "MoQieZhongLei": "小包装" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "单面", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "单面", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": true, "HeXing": "其他" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "三层高强度瓦楞板", "Enable": true } }, "P": 1, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false, "MingChen": "小包装" }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": true, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": false, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "" }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 350, "ChengPinHeight": 260, "ChengPinHou": "320", "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 0, "ZhanKaiHeight": 0, "ShuLiang": "1000", "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "", "DanPinGongSiHeight": " 长*2+宽*2+25", "DanPinGongSiWidth": "宽/2+30+高+宽+宽/2+25", "ShuangPinGongSiHeight": "宽/2+30+高+宽+宽/2+25", "ShuangPinGongSiWidth": "长+宽+25", "HeXing": "斜面盒" }'); 
            break;
        case 10://"Hanging box":
            body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": true, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 0 }, "ZhiZhang": { "LeiXing": 16, "KeZhong": 116 }, "Width": { "Value": 0 }, "Height": { "Value": 0 }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": true, "MoQieZhongLei": "小包装" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "单面", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "单面", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": true, "HeXing": "其他" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "三层高强度瓦楞板", "Enable": true } }, "P": 1, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false, "MingChen": "小包装" }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": true, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": false, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "" }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 350, "ChengPinHeight": 260, "ChengPinHou": "320", "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 0, "ZhanKaiHeight": 0, "ShuLiang": "1000", "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "", "DanPinGongSiHeight": "长*2+宽*2+20", "DanPinGongSiWidth": "高+宽*2+20+20", "ShuangPinGongSiHeight": "长+宽+20", "ShuangPinGongSiWidth": "高+宽*2+20+20", "HeXing": "挂盒" }'); 
            break;
        case 11://"Hook bottom box":
            body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": true, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 0 }, "ZhiZhang": { "LeiXing": 16, "KeZhong": 116 }, "Width": { "Value": 0 }, "Height": { "Value": 0 }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": true, "MoQieZhongLei": "小包装" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "单面", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "单面", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": true, "HeXing": "其他" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "三层高强度瓦楞板", "Enable": true } }, "P": 1, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false, "MingChen": "小包装" }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": true, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": false, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "" }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 350, "ChengPinHeight": 260, "ChengPinHou": "320", "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 0, "ZhanKaiHeight": 0, "ShuLiang": "1000", "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "", "DanPinGongSiHeight": "长*2+宽*2+20", "DanPinGongSiWidth": "高+宽*2+20+20", "ShuangPinGongSiHeight": "长+宽+20", "ShuangPinGongSiWidth": "高+宽*2+20+20", "HeXing": "钩底盒" }'); 
            break;
        default:
            body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": true, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 0 }, "ZhiZhang": { "LeiXing": 16, "KeZhong": 116 }, "Width": { "Value": 0 }, "Height": { "Value": 0 }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": true, "MoQieZhongLei": "小包装" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "单面", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "单面", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": true, "HeXing": "其他" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "三层高强度瓦楞板", "Enable": true } }, "P": 1, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false, "MingChen": "小包装" }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": true, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": false, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": false, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "" }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 350, "ChengPinHeight": 260, "ChengPinHou": "320", "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 0, "ZhanKaiHeight": 0, "ShuLiang": "1000", "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "", "DanPinGongSiHeight": "(长+宽)*2+25", "DanPinGongSiWidth": "宽/2+30+高+宽+25", "ShuangPinGongSiHeight": "长+宽+25", "ShuangPinGongSiWidth": "宽/2+30+高+宽+25", "HeXing": "上盖下插底盒" }'); 

    }

    body_json.BuJians[0].P = params.m_PinZhong;
    body_json.BuJians[0].PinZhong = params.m_PinZhong;
    body_json.ChengPinWidth = params.m_ChengPinWidth;
    body_json.ChengPinHeight = params.m_ChengPinHeight;
    body_json.ChengPinHou = params.m_ChengPinHou;
    body_json.ShuLiang = params.m_ShuLiang;
    body_json.PinZhong = params.m_PinZhong;
    //material gram
    body_json.BuJians[0].ZhiZhang.LeiXing = params.m_LeiXing;
    body_json.BuJians[0].ZhiZhang.KeZhong = params.m_KeZhong;
    // if kezhong = 200 then 162
    //Color
    body_json.BuJians[0].ZhengMianColor.ZhuanSe = params.m_ZhengMianColor;
    //material type
    body_json.BuJians[0].HouGong.XiaoBaoZhuang.CaiLiao = params.m_XiaoBaoZhuang_CaiLiao;
    //binding Parameters
    body_json.BuJians[0].HouGong.HuHe.Enable = params.Formed_a_box;
    if(params.FuMo_Enable){
        body_json.BuJians[0].HouGong.FuMo.Enable = params.FuMo_Enable;
        body_json.BuJians[0].HouGong.FuMo.FuMoZhongLei = params.FuMo_FuMoZhongLei 
    }
    if(params.ShouTiSheng_Enable){
        body_json.BuJians[0].HouGong.ShouTiSheng.Enable = true;
        body_json.BuJians[0].HouGong.ShouTiSheng.CaiLiao = params.ShouTiSheng_CaiLiao;
    }
    if(params.TiBa_Enable){
        body_json.BuJians[0].HouGong.ShouTiSheng.Enable = false;
        body_json.BuJians[0].HouGong.TiBa.Enable = true;
    }
    if(params.DanMianTangYin_Enable){
        body_json.BuJians[0].HouGong.DanMianTangYin.Enable = true;
        body_json.BuJians[0].HouGong.DanMianTangYin.Width = params.DanMianTangYin_Width;
        body_json.BuJians[0].HouGong.DanMianTangYin.Height = params.DanMianTangYin_Height;
    }
    if(params.DanMianTangJin_Enable){
        body_json.BuJians[0].HouGong.DanMianTangJin.Enable = true;
        body_json.BuJians[0].HouGong.DanMianTangJin.Width = params.DanMianTangJin_Width;
        body_json.BuJians[0].HouGong.DanMianTangJin.Height = params.DanMianTangJin_Height;
    }
    if(params.KaiTianChuang_Enable){
        body_json.BuJians[0].HouGong.KaiTianChuang.Enable = true;
        body_json.BuJians[0].HouGong.KaiTianChuang.Width = params.KaiTianChuang_Width;
        body_json.BuJians[0].HouGong.KaiTianChuang.Height = params.KaiTianChuang_Height;
    }
    if(params.DanMianJiTu_Enable){
        body_json.BuJians[0].HouGong.DanMianJiTu.Enable = true;
        body_json.BuJians[0].HouGong.DanMianJiTu.Width = params.DanMianJiTu_Width;
        body_json.BuJians[0].HouGong.DanMianJiTu.Height = params.DanMianJiTu_Height;
    }
    if(params.DanMianJiTu_Enable){
        body_json.BuJians[0].HouGong.JuBuUV.Enable = true;
        body_json.BuJians[0].HouGong.JuBuUV.Width = params.JuBuUV_Width;
        body_json.BuJians[0].HouGong.JuBuUV.Height = params.JuBuUV_Height;
        body_json.BuJians[0].HouGong.JuBuUV.UVCaiLiao = params.JuBuUV_UVCaiLiao;
    }
    if(params.GuoYou_Enable){
        body_json.BuJians[0].HouGong.GuoYou.Enable = true;
        body_json.BuJians[0].HouGong.GuoYou.CaiLiao = params.GuoYou_CaiLiao;
    }

    let body_txt = JSON.stringify(body_json);
    let urls = "http://qd.ieprint.cc/api/BaoJiaApi/DanyeBaojia?CiShu="+arguments[0]+"&pageCode=pageCode";
    let response = await fetch(
        urls,
        {
        headers: {
            accept: "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9,ko;q=0.8,zh;q=0.7,ko;q=0.6,und;q=0.5",
            "bj-guid": "2847c4d4-5363-4dc8-9b42-b520e999e7bf",
            "content-type": "application/json;charset=UTF-8",
        },
        referrer: "http://qd.ieprint.cc/",
        referrerPolicy: "no-referrer-when-downgrade",
        body: body_txt,
        method: "POST",
        mode: "cors",
        credentials: "omit",
        }
    );

    let myJson = await response.json(); //extract JSON from the http response
    // do something with myJson
    //console.log(myJson);
    //console.log(arguments[0])

    return myJson;
"""
js_tag = """
    let body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": true, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 7 }, "ZhiZhang": { "LeiXing": 14, "KeZhong": 102 }, "Width": { "Value": 0 }, "Height": { "Value": 0 }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": true, "MoQieZhongLei": "吊牌" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": false, "HeXing": "" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "", "Enable": false } }, "P": 2, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false, "MingChen": "吊牌" }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": true, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": false, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "" }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 90, "ChengPinHeight": 54, "ChengPinHou": 0, "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 0, "ZhanKaiHeight": 0, "ShuLiang": "1000", "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "" }'); 
    //body_json.BuJians[0].MingCheng = '';m_Width, m_Height, m_ShuLiang
    const params = arguments[1];

    body_json.BuJians[0].PinZhong = params.m_PinZhong
    body_json.BuJians[0].P = params.m_PinZhong * 2

    body_json.ChengPinWidth = params.m_ChengPinWidth
    body_json.ChengPinHeight = params.m_ChengPinHeight
    body_json.ShuLiang = params.m_ShuLiang
    body_json.PinZhong = params.m_PinZhong

    body_json.BuJians[0].ZhiZhang.LeiXing = params.m_LeiXing
    body_json.BuJians[0].ZhiZhang.KeZhong = params.m_KeZhong


    body_json.BuJians[0].ZhengMianColor.ZhuanSe = params.m_ZhengMianColor
    body_json.BuJians[0].FanMianColor.ZhuanSe = params.m_FanMianColor

    //params Parameters
    if(params.FuMo_Enable > 0){
        body_json.BuJians[0].HouGong.FuMo.Enable = true;
        body_json.BuJians[0].HouGong.FuMo.FuMoZhongLei = params.FuMo_FuMoZhongLei 
        body_json.BuJians[0].HouGong.FuMo.ShuangMianFuMo = params.FuMo_ShuangMianFuMo=="single"  ? false:true;
    }
    if(params.YaWen_Enable > 0){
        body_json.BuJians[0].HouGong.YaWen.Enable = true;
    }
    if(params.Easytearline > 0){
        body_json.BuJians[0].HouGong.YiSiXian.Enable = true;
        body_json.BuJians[0].HouGong.YiSiXian.JiTiaoXian = params.selEasytearline;
    }
    if(params.DanMianTangYin_Enable > 0){
        body_json.BuJians[0].HouGong.DanMianTangYin.Enable = true;
        body_json.BuJians[0].HouGong.DanMianTangYin.Width = params.DanMianTangYin_Width;
        body_json.BuJians[0].HouGong.DanMianTangYin.Height = params.DanMianTangYin_Height;
    }
    if(params.DanMianTangJin_Enable > 0){
        body_json.BuJians[0].HouGong.DanMianTangJin.Enable = true;
        body_json.BuJians[0].HouGong.DanMianTangJin.Width = params.DanMianTangJin_Width;
        body_json.BuJians[0].HouGong.DanMianTangJin.Height = params.DanMianTangJin_Height;
    }
    if(params.Code > 0 ){
        body_json.BuJians[0].HouGong.DaHaoMa.Enable = true;
        body_json.BuJians[0].HouGong.DaHaoMa.ShuLiang = params.selCode2;
        body_json.BuJians[0].HouGong.DaHaoMa.DaMaLeiXing = params.selCode1;
    }
    if(params.DanMianJiTu_Enable > 0){
        body_json.BuJians[0].HouGong.DanMianJiTu.Enable = true;
        body_json.BuJians[0].HouGong.DanMianJiTu.Width = params.DanMianJiTu_Width;
        body_json.BuJians[0].HouGong.DanMianJiTu.Height = params.DanMianJiTu_Height;
    }
    if(params.JuBuUV_Enable > 0){
        body_json.BuJians[0].HouGong.JuBuUV.Enable = true;
        body_json.BuJians[0].HouGong.JuBuUV.Width = params.JuBuUV_Width;
        body_json.BuJians[0].HouGong.JuBuUV.Height = params.JuBuUV_Height;
        body_json.BuJians[0].HouGong.JuBuUV.UVCaiLiao = params.JuBuUV_UVCaiLiao;
        body_json.BuJians[0].HouGong.JuBuUV.ShuangMian = params.JuBuUV_ShuangMian;
    }

    let body_txt = JSON.stringify(body_json);
    let urls = "http://qd.ieprint.cc/api/BaoJiaApi/DanyeBaojia?CiShu="+arguments[0]+"&pageCode=pageCode";
    let response = await fetch(
        urls,
        {
        headers: {
            accept: "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9,ko;q=0.8,zh;q=0.7,ko;q=0.6,und;q=0.5",
            "bj-guid": "a26c902c-79d0-44e5-a3b2-edf3ecb8beba",
            "content-type": "application/json;charset=UTF-8",
        },
        referrer: "http://qd.ieprint.cc/",
        referrerPolicy: "no-referrer-when-downgrade",
        body: body_txt,
        method: "POST",
        mode: "cors",
        credentials: "omit",
        }
    );

    let myJson = await response.json(); //extract JSON from the http response
    return myJson;
"""
js_desk_calendar = """
    let body_json = JSON.parse('{"BuJians":[{"MingCheng":"里纸","BuJianFenLei":{"DanZhang":false,"XiaoBaoZhuang":false,"LiBaoDuiLian":false,"LiBaoHengPi":false,"LiBaoFuZi":false,"LiBaoHongBao":false,"LiBao":false,"DuiLian":false,"DuiLianHengpi":false,"DuiLianFuZi":false,"FuZi":false,"GuaLiNeiYe":false,"TaiLiNeiYe":false,"TaiLiGongYeBan":false,"TaiLiWaiBiaoZhi":false,"TailiNeiBiaoZhi":true,"MingPian":false,"CaiHe":false,"DangAnDai":false,"DiaoPai":false,"XinFeng":false,"BaoZhi":false,"BianQian":false,"FengTao":false,"BuGanJiao":false,"ShouTiDai":false,"HuaCeFengPi":false,"HuaCeNeiYe":false,"HuaCeFeiYe":false,"HuaCeLaYe":false},"ZhengMianColor":{"ZhuanSe":7},"FanMianColor":{"ZhuanSe":7},"ZhiZhang":{"LeiXing":15,"KeZhong":18},"Width":{"Value":"210"},"Height":{"Value":360},"ZiDaiZhi":false,"HouGongCanShu":[],"ShuangDaMianXiangTong":false,"ShuangCeMianXiangTong":false,"HouGong":{"YaHen":{"YaHenZhe":"","Enable":false,"JiDaoHen":1},"YiSiXian":{"JiTiaoXian":1,"Enable":false},"DanMianJiTu":{"Enable":false,"Width":"","Height":""},"DanMianTangJin":{"Enable":false,"Width":"","Height":""},"DanMianTangYin":{"Enable":false,"Width":"","Height":""},"FuMo":{"ShuangMianFuMo":"false","FuMoZhongLei":"","Enable":false},"MoQie":{"Enable":false,"MoQieZhongLei":""},"YaWen":{"Enable":false,"ShuangMianYaWen":false},"JuBuUV":{"Enable":false,"ShuangMian":"","UVCaiLiao":"","Width":"","Height":""},"KaiTianChuang":{"Enable":false,"Width":"","Height":""},"GuoYou":{"Enable":false,"ShuangMianGuoYou":"","CaiLiao":""},"DaHaoMa":{"Enable":false,"ShuLiang":1},"ZheYe":{"Enable":false,"ZheFa":""},"DaKong":{"Enable":false,"DaKongShuLiang":1},"DanMianGuaGuaYin":{"Enable":false},"HuHe":{"Enable":false,"HeXing":""},"ShouTiSheng":{"Enable":false,"CaiLiao":""},"TiBa":{"Enable":false},"DaMaoDing":{"Enable":false},"JiaoTou":{"Enable":false},"XiaoBaoZhuang":{"CaiLiao":"","Enable":false}},"P":1,"PinZhong":1,"ShuLiang":0,"ZhengFangMianNeiRongXiangTong2":false,"ZhengFangMianNeiRongXiangTong3":false,"ZhengFangMianNeiRongXiangTong4":false,"ZhengFangMianNeiRongXiangTong5":false,"ZhengFangMianNeiRongBuTong":false,"JieDiaoKou":false,"SFYinShua":false,"SFXiangTong":false},{"MingCheng":"面纸","BuJianFenLei":{"DanZhang":false,"XiaoBaoZhuang":false,"LiBaoDuiLian":false,"LiBaoHengPi":false,"LiBaoFuZi":false,"LiBaoHongBao":false,"LiBao":false,"DuiLian":false,"DuiLianHengpi":false,"DuiLianFuZi":false,"FuZi":false,"GuaLiNeiYe":false,"TaiLiNeiYe":false,"TaiLiGongYeBan":false,"TaiLiWaiBiaoZhi":true,"TailiNeiBiaoZhi":false,"MingPian":false,"CaiHe":false,"DangAnDai":false,"DiaoPai":false,"XinFeng":false,"BaoZhi":false,"BianQian":false,"FengTao":false,"BuGanJiao":false,"ShouTiDai":false,"HuaCeFengPi":false,"HuaCeNeiYe":false,"HuaCeFeiYe":false,"HuaCeLaYe":false},"ZhengMianColor":{"ZhuanSe":7},"FanMianColor":{"ZhuanSe":7},"ZhiZhang":{"LeiXing":14,"KeZhong":111},"Width":{"Value":"210"},"Height":{"Value":360},"ZiDaiZhi":false,"HouGongCanShu":[],"ShuangDaMianXiangTong":false,"ShuangCeMianXiangTong":false,"HouGong":{"YaHen":{"YaHenZhe":"","Enable":false,"JiDaoHen":1},"YiSiXian":{"JiTiaoXian":1,"Enable":false},"DanMianJiTu":{"Enable":false,"Width":"","Height":""},"DanMianTangJin":{"Enable":false,"Width":"","Height":""},"DanMianTangYin":{"Enable":false,"Width":"","Height":""},"FuMo":{"ShuangMianFuMo":"false","FuMoZhongLei":"","Enable":false},"MoQie":{"Enable":false,"MoQieZhongLei":""},"YaWen":{"Enable":false,"ShuangMianYaWen":false},"JuBuUV":{"Enable":false,"ShuangMian":"","UVCaiLiao":"","Width":"","Height":""},"KaiTianChuang":{"Enable":false,"Width":"","Height":""},"GuoYou":{"Enable":false,"ShuangMianGuoYou":"","CaiLiao":""},"DaHaoMa":{"Enable":false,"ShuLiang":1},"ZheYe":{"Enable":false,"ZheFa":""},"DaKong":{"Enable":false,"DaKongShuLiang":1},"DanMianGuaGuaYin":{"Enable":false},"HuHe":{"Enable":false,"HeXing":""},"ShouTiSheng":{"Enable":false,"CaiLiao":""},"TiBa":{"Enable":false},"DaMaoDing":{"Enable":false},"JiaoTou":{"Enable":false},"XiaoBaoZhuang":{"CaiLiao":"","Enable":false}},"P":1,"PinZhong":1,"ShuLiang":0,"ZhengFangMianNeiRongXiangTong2":false,"ZhengFangMianNeiRongXiangTong3":false,"ZhengFangMianNeiRongXiangTong4":false,"ZhengFangMianNeiRongXiangTong5":false,"ZhengFangMianNeiRongBuTong":false,"JieDiaoKou":false,"SFYinShua":true,"SFXiangTong":false},{"MingCheng":"内页","BuJianFenLei":{"DanZhang":false,"XiaoBaoZhuang":false,"LiBaoDuiLian":false,"LiBaoHengPi":false,"LiBaoFuZi":false,"LiBaoHongBao":false,"LiBao":false,"DuiLian":false,"DuiLianHengpi":false,"DuiLianFuZi":false,"FuZi":false,"GuaLiNeiYe":false,"TaiLiNeiYe":true,"TaiLiGongYeBan":false,"TaiLiWaiBiaoZhi":false,"TailiNeiBiaoZhi":false,"MingPian":false,"CaiHe":false,"DangAnDai":false,"DiaoPai":false,"XinFeng":false,"BaoZhi":false,"BianQian":false,"FengTao":false,"BuGanJiao":false,"ShouTiDai":false,"HuaCeFengPi":false,"HuaCeNeiYe":false,"HuaCeFeiYe":false,"HuaCeLaYe":false},"ZhengMianColor":{"ZhuanSe":7},"FanMianColor":{"ZhuanSe":7},"ZhiZhang":{"LeiXing":14,"KeZhong":111},"Width":{"Value":0},"Height":{"Value":0},"ZiDaiZhi":false,"HouGongCanShu":[],"ShuangDaMianXiangTong":false,"ShuangCeMianXiangTong":false,"HouGong":{"YaHen":{"YaHenZhe":"","Enable":false,"JiDaoHen":1},"YiSiXian":{"JiTiaoXian":1,"Enable":false},"DanMianJiTu":{"Enable":false,"Width":"","Height":""},"DanMianTangJin":{"Enable":false,"Width":"","Height":""},"DanMianTangYin":{"Enable":false,"Width":"","Height":""},"FuMo":{"ShuangMianFuMo":"false","FuMoZhongLei":"","Enable":false},"MoQie":{"Enable":false,"MoQieZhongLei":""},"YaWen":{"Enable":false,"ShuangMianYaWen":false},"JuBuUV":{"Enable":false,"ShuangMian":"","UVCaiLiao":"","Width":"","Height":""},"KaiTianChuang":{"Enable":false,"Width":"","Height":""},"GuoYou":{"Enable":false,"ShuangMianGuoYou":"","CaiLiao":""},"DaHaoMa":{"Enable":false,"ShuLiang":1},"ZheYe":{"Enable":false,"ZheFa":""},"DaKong":{"Enable":false,"DaKongShuLiang":1},"DanMianGuaGuaYin":{"Enable":false},"HuHe":{"Enable":false,"HeXing":""},"ShouTiSheng":{"Enable":false,"CaiLiao":""},"TiBa":{"Enable":false},"DaMaoDing":{"Enable":false},"JiaoTou":{"Enable":false},"XiaoBaoZhuang":{"CaiLiao":"","Enable":false}},"P":26,"PinZhong":1,"ShuLiang":13,"ZhengFangMianNeiRongXiangTong2":false,"ZhengFangMianNeiRongXiangTong3":false,"ZhengFangMianNeiRongXiangTong4":false,"ZhengFangMianNeiRongXiangTong5":false,"ZhengFangMianNeiRongBuTong":false,"JieDiaoKou":false,"SFYinShua":false,"SFXiangTong":false}],"ChanPinFenLei":{"DanZhang":false,"XiaoBaoZhuang":false,"DaLiBao":false,"DuiLian":false,"FuZi":false,"GuaLi":false,"TaiLi":true,"MingPian":false,"CaiHe":false,"DangAnDai":false,"DiaoPai":false,"XinFeng":false,"BaoZhi":false,"BiaoQian":false,"FengTao":false,"BuGanJiao":false,"ShouTiDai":false,"YangBenHuaCe":false,"PVC":false,"WuTanLianDan":false,"DanPinGongSiHeight":"","DanPinGongSiWidth":"","ShuangPinGongSiHeight":"","ShuangPinGongSiWidth":""},"JiaLeiKou":null,"JiaZheDou":null,"JiaLaYe":null,"ZhuangDingFangShi":"骑马钉","ChengPinWidth":140,"ChengPinHeight":210,"ChengPinHou":0,"ZheDouLeiXing":"单折兜","DianBan":false,"QiQiang":0,"ZhanKaiWidth":0,"ZhanKaiHeight":0,"ShuLiang":1000,"PinZhong":1,"MeiBenYeShu":1,"CaiChengPin":true,"ShuangDaMianXiangTong":true,"ShuangCeMianXiangTong":true,"ChuanHuanBian":"140","ChuanHuanYanSe":"彩色","ZhiJiaoHouDu":"2","ZhiJiaWidth":"210","ZhiJiaHeight":360,"SheTou":0,"XinFengYangShi":""}'); 
    //body_json.BuJians[0].MingCheng = '';m_Width, m_Height, m_ShuLiang
    const m_ChengPinWidth = arguments[1];
    const m_ChengPinHeight = arguments[2];
    const m_ZhiJiaWidth = arguments[3];
    const m_ZhiJiaHeight = arguments[4];
    const m_ZhiJiaoHouDu = arguments[5];
    const m_ShuLiang = arguments[6];
    const m_ChuanHuanBian = arguments[7];
    const m_ChuanHuanYanSe = arguments[8];

    
    body_json.BuJians[0].Width.Value = m_ZhiJiaWidth
    body_json.BuJians[0].Height.Value = m_ZhiJiaHeight
    body_json.BuJians[1].Width.Value = m_ZhiJiaWidth
    body_json.BuJians[1].Height.Value = m_ZhiJiaHeight

    body_json.ChengPinWidth = m_ChengPinWidth
    body_json.ChengPinHeight = m_ChengPinHeight
    body_json.ShuLiang = m_ShuLiang
    body_json.ZhiJiaWidth = m_ZhiJiaWidth
    body_json.ZhiJiaHeight = m_ZhiJiaHeight
    body_json.ZhiJiaoHouDu = m_ZhiJiaoHouDu
    body_json.ChuanHuanBian = m_ChuanHuanBian
    body_json.ChuanHuanYanSe = m_ChuanHuanYanSe

    let body_txt = JSON.stringify(body_json);
    let urls = "http://qd.ieprint.cc/api/BaoJiaApi/DanyeBaojia?CiShu="+arguments[0]+"&pageCode=pageCode";
    let response = await fetch(
        urls,
        {
        headers: {
            accept: "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9,ko;q=0.8,zh;q=0.7,ko;q=0.6,und;q=0.5",
            "bj-guid": "a26c902c-79d0-44e5-a3b2-edf3ecb8beba",
            "content-type": "application/json;charset=UTF-8",
        },
        referrer: "http://qd.ieprint.cc/",
        referrerPolicy: "no-referrer-when-downgrade",
        body: body_txt,
        method: "POST",
        mode: "cors",
        credentials: "omit",
        }
    );

    let myJson = await response.json(); //extract JSON from the http response
    return myJson;
"""

# body_param = {"BuJians":[{"MingCheng":"","BuJianFenLei":{"DanZhang":false,"XiaoBaoZhuang":true,"LiBaoDuiLian":false,"LiBaoHengPi":false,"LiBaoFuZi":false,"LiBaoHongBao":false,"LiBao":false,"DuiLian":false,"DuiLianHengpi":false,"DuiLianFuZi":false,"FuZi":false,"GuaLiNeiYe":false,"TaiLiNeiYe":false,"TaiLiGongYeBan":false,"TaiLiWaiBiaoZhi":false,"TailiNeiBiaoZhi":false,"MingPian":false,"CaiHe":false,"DangAnDai":false,"DiaoPai":false,"XinFeng":false,"BaoZhi":false,"BianQian":false,"FengTao":false,"BuGanJiao":false,"ShouTiDai":false,"HuaCeFengPi":false,"HuaCeNeiYe":false,"HuaCeFeiYe":false,"HuaCeLaYe":false},"ZhengMianColor":{"ZhuanSe":7},"FanMianColor":{"ZhuanSe":0},"ZhiZhang":{"LeiXing":16,"KeZhong":116},"Width":{"Value":0},"Height":{"Value":0},"ZiDaiZhi":false,"HouGongCanShu":[],"ShuangDaMianXiangTong":false,"ShuangCeMianXiangTong":false,"HouGong":{"YaHen":{"YaHenZhe":"","Enable":false,"JiDaoHen":1},"YiSiXian":{"JiTiaoXian":1,"Enable":false},"DanMianJiTu":{"Enable":false,"Width":"","Height":""},"DanMianTangJin":{"Enable":false,"Width":"","Height":""},"DanMianTangYin":{"Enable":false,"Width":"","Height":""},"FuMo":{"ShuangMianFuMo":"false","FuMoZhongLei":"","Enable":false},"MoQie":{"Enable":true,"MoQieZhongLei":"小包装"},"YaWen":{"Enable":false,"ShuangMianYaWen":false},"JuBuUV":{"Enable":false,"ShuangMian":"单面","UVCaiLiao":"","Width":"","Height":""},"KaiTianChuang":{"Enable":false,"Width":"","Height":""},"GuoYou":{"Enable":false,"ShuangMianGuoYou":"单面","CaiLiao":""},"DaHaoMa":{"Enable":false,"ShuLiang":1},"ZheYe":{"Enable":false,"ZheFa":""},"DaKong":{"Enable":false,"DaKongShuLiang":1},"DanMianGuaGuaYin":{"Enable":false},"HuHe":{"Enable":true,"HeXing":"其他"},"ShouTiSheng":{"Enable":false,"CaiLiao":""},"TiBa":{"Enable":false},"DaMaoDing":{"Enable":false},"JiaoTou":{"Enable":false},"XiaoBaoZhuang":{"CaiLiao":"三层高强度瓦楞板","Enable":true}},"P":1,"PinZhong":1,"ShuLiang":0,"ZhengFangMianNeiRongXiangTong2":false,"ZhengFangMianNeiRongXiangTong3":false,"ZhengFangMianNeiRongXiangTong4":false,"ZhengFangMianNeiRongXiangTong5":false,"ZhengFangMianNeiRongBuTong":false,"JieDiaoKou":false,"SFYinShua":false,"SFXiangTong":false,"MingChen":"小包装"}],"ChanPinFenLei":{"DanZhang":false,"XiaoBaoZhuang":true,"DaLiBao":false,"DuiLian":false,"FuZi":false,"GuaLi":false,"TaiLi":false,"MingPian":false,"CaiHe":false,"DangAnDai":false,"DiaoPai":false,"XinFeng":false,"BaoZhi":false,"BiaoQian":false,"FengTao":false,"BuGanJiao":false,"ShouTiDai":false,"YangBenHuaCe":false,"PVC":false,"WuTanLianDan":false,"DanPinGongSiHeight":"","DanPinGongSiWidth":"","ShuangPinGongSiHeight":"","ShuangPinGongSiWidth":""},"JiaLeiKou":null,"JiaZheDou":null,"JiaLaYe":null,"ZhuangDingFangShi":"骑马钉","ChengPinWidth":350,"ChengPinHeight":260,"ChengPinHou":"320","ZheDouLeiXing":"单折兜","DianBan":false,"QiQiang":0,"ZhanKaiWidth":0,"ZhanKaiHeight":0,"ShuLiang":"1000","PinZhong":1,"MeiBenYeShu":1,"CaiChengPin":true,"ShuangDaMianXiangTong":true,"ShuangCeMianXiangTong":true,"ChuanHuanBian":0,"ChuanHuanYanSe":"","ZhiJiaoHouDu":0,"ZhiJiaWidth":0,"ZhiJiaHeight":0,"SheTou":0,"XinFengYangShi":"","DanPinGongSiHeight":"(长+宽)*2+25","DanPinGongSiWidth":"宽/2+30+高+宽+25","ShuangPinGongSiHeight":"长+宽+25","ShuangPinGongSiWidth":"宽/2+30+高+宽+25"}
# m_type = "color_pill_box"
# m_type = "tag"
# m_type = "Paper Box"
m_type = "Lavel"


def getPrice(m_type, params):
    error_code = "ok"
    if m_type == "sample_album":
        m_Width = 285
        m_Height = 210
        m_ShuLiang = 1503
        # price list
        price_result = []

        return_json = m_driver.execute_script(
            js_sample_album, 1, m_Width, m_Height, m_ShuLiang
        )
        if return_json["success"]:
            price_result.append(return_json["response"]["list"][0]["zushu"])
            price_result.append(return_json["response"]["list"][0]["hanshui"])

        return_json = m_driver.execute_script(
            js_sample_album, 2, m_Width, m_Height, m_ShuLiang
        )
        for re_json_list in return_json["response"]["list"]:
            if return_json["success"]:
                price_result.append(re_json_list["zushu"])
                price_result.append(re_json_list["hanshui"])

    elif m_type == "corrugatedbox":
        # m_box_variety = params["m_box_variety"]
        # m_ChengPinWidth = params["m_ChengPinWidth"]
        # m_ChengPinHeight = params["m_ChengPinHeight"]
        # m_ChengPinHou = params["m_ChengPinHou"]
        # m_ShuLiang = params["m_ShuLiang"]
        # m_PinZhong = params["m_PinZhong"]
        # # [
        # #     "SBS": 16,
        # #     "Kraft Paper": 17,
        # #     "White Kraft Paper": 28,
        # #     "C2S": 14,
        # #     "CCNB": 278,
        # # ]
        # m_LeiXing = 16
        # # "SBS": [
        # #     "210": 114,
        # #     "230": 115,
        # #     "250": 116,
        # #     "300": 117,
        # #     "350": 26,

        # # ],
        # # "Kraft Paper": [
        # #     "200": 162,
        # #     "250": 166,
        # #     "300": 104,
        # # ],
        # # "White Kraft Paper": [
        # #     "250": 86
        # # ],
        # # "C2S": [
        # #     "250": 102,
        # #     "300": 103,
        # #     "350": 14,
        # # ]
        # # "CCNB": [
        # #     "250": 316,
        # #     "300": 317,
        # #     "350": 318,
        # # ]
        # m_KeZhong = 116
        # # color 7~15
        # m_ZhengMianColor = 7  # 单黑
        # # price list
        # # "CaiLiag": [
        # #     "Three-layer high-strength corrugated cardboard": "三层高强度瓦楞板",
        # #     "Three-layer high-strength corrugated cardboard (inner white)": "三层高强度瓦楞(内白)",
        # #     "Three-layer (ordinary) corrugated cardboard": "三层(普通)瓦楞板",
        # #     "Five-layer (ordinary) corrugated cardboard": "五层(普通)瓦楞纸板",
        # # ]
        # m_XiaoBaoZhuang_CaiLiao = "三层高强度瓦楞板"

        # # m_Formed_a_box = False
        # # m_FuMo_Enable = True
        # # m_FuMo_FuMoZhongLei = "亮膜"
        # m_binding = {
        #     "Formed_a_box": True,
        #     "FuMo_Enable": False,
        #     "FuMo_FuMoZhongLei": "亮膜",
        #     "ShouTiSheng_Enable": False,
        #     "ShouTiSheng_CaiLiao": "普通尼龙绳",
        #     "TiBa_Enable": False,
        #     "DanMianTangYin_Enable": True,
        #     "DanMianTangYin_Width": 12,
        #     "DanMianTangYin_Height": 34,
        #     "DanMianTangJin_Enable": True,
        #     "DanMianTangJin_Width": 12,
        #     "DanMianTangJin_Height": 34,
        #     "KaiTianChuang_Enable": True,
        #     "KaiTianChuang_Width": 12,
        #     "KaiTianChuang_Height": 34,
        #     "DanMianJiTu_Enable": True,
        #     "DanMianJiTu_Width": 12,
        #     "DanMianJiTu_Height": 34,
        #     "JuBuUV_Enable": True,
        #     "JuBuUV_Width": 12,
        #     "JuBuUV_Height": 34,
        #     "JuBuUV_UVCaiLiao": "亮光油",
        #     "GuoYou_Enable": True,
        #     "GuoYou_CaiLiao": "磨光油",
        # }
        # m_binding["ShouTiSheng_Enable"] = True

        price_result = []

        return_json = m_driver.execute_script(js_corrugated_box, 1, params)
        if return_json["success"]:
            price_result.append(return_json["response"]["list"][0]["zushu"])
            price_result.append(return_json["response"]["list"][0]["hanshui"])

            return_json = m_driver.execute_script(js_corrugated_box, 2, params)
            if return_json["success"]:
                for re_json_list in return_json["response"]["list"]:
                    price_result.append(re_json_list["zushu"])
                    price_result.append(re_json_list["hanshui"])
            else:
                error_code = return_json
        else:
            error_code = return_json
    elif m_type == "Paper Box":
        # m_box_variety = "Isert bottom box up and down"
        # m_ChengPinWidth = 80
        # m_ChengPinHeight = 40
        # m_ChengPinHou = 120
        # m_ShuLiang = 1000
        # m_PinZhong = 1
        # # White cardboard : 16, Coated paper :14
        # # Kraft paper: 17, White on gray: 278
        # m_LeiXing = 16
        # # White on gray(278): {250:316, 300:317, 350:318}
        # # White cardboard(16): {300:117,250:116,350:26,230:115}
        # # Coated paper(14): {300:103,350:14}
        # # Kraft paper(17): {250:166, 200:162, 300:104}
        # m_KeZhong = 116
        # # color 7~15
        # m_ZhengMianColor = 7  # 单黑
        # # price list
        # m_binding = {
        #     "Formed_a_box": True,
        #     "FuMo_Enable": False,
        #     "FuMo_FuMoZhongLei": "亮膜",
        #     "ShouTiSheng_Enable": False,
        #     "ShouTiSheng_CaiLiao": "普通尼龙绳",
        #     "TiBa_Enable": False,
        #     "DanMianTangYin_Enable": False,
        #     "DanMianTangYin_Width": 12,
        #     "DanMianTangYin_Height": 34,
        #     "DanMianTangJin_Enable": False,
        #     "DanMianTangJin_Width": 12,
        #     "DanMianTangJin_Height": 34,
        #     "KaiTianChuang_Enable": False,
        #     "KaiTianChuang_Width": 12,
        #     "KaiTianChuang_Height": 34,
        #     "DanMianJiTu_Enable": False,
        #     "DanMianJiTu_Width": 12,
        #     "DanMianJiTu_Height": 34,
        #     "JuBuUV_Enable": False,
        #     "JuBuUV_Width": 12,
        #     "JuBuUV_Height": 34,
        #     "JuBuUV_UVCaiLiao": "亮光油",
        #     "GuoYou_Enable": False,
        #     "GuoYou_CaiLiao": "磨光油",
        # }
        price_result = []

        return_json = m_driver.execute_script(js_color_pill_box, 1, params)
        if return_json["success"]:
            price_result.append(return_json["response"]["list"][0]["zushu"])
            price_result.append(return_json["response"]["list"][0]["hanshui"])

            return_json = m_driver.execute_script(js_color_pill_box, 2, params)
            if return_json["success"]:
                for re_json_list in return_json["response"]["list"]:
                    price_result.append(re_json_list["zushu"])
                    price_result.append(re_json_list["hanshui"])
            else:
                error_code = return_json
        else:
            error_code = return_json

    elif m_type == "Lavel":
        # m_ChengPinWidth = 90
        # m_ChengPinHeight = 54
        # m_ShuLiang = 1000
        # m_PinZhong = 1
        # 14:Coated paper,16:White cardboard,19:Matte paper
        # 15:Double offset paper, 22:Oxue, 18:New beauty
        # 21:Sense of elegance, 24:Dutch White Card
        # 17:Kraft paper, 25:Pearlescent ice white star colored paper
        # 28: White cowhide,29:High school movie,
        # 32: Athens pattern,33:Fine pear pattern,
        # m_LeiXing = 14
        # Coated paper 250: 102, 200: 11
        # White cardboard 210: 114, 230:115
        # Matte paper 128:46,157:41, 200:42

        # m_KeZhong = 102  # 250
        # color:7,Single black:8, Double spot color:9,Single spot color:10
        # Color +1 Special:12, Color +2 special:13
        # Color+glazing : 14, Glazing:15, reverse color no:0
        # m_ZhengMianColor = 7  # 单黑
        # m_FanMianColor = 7
        # price list
        price_result = []

        return_json = m_driver.execute_script(js_tag, 1, params)
        if return_json["success"]:
            price_result.append(return_json["response"]["list"][0]["zushu"])
            price_result.append(return_json["response"]["list"][0]["hanshui"])

            return_json = m_driver.execute_script(js_tag, 2, params)
            if return_json["success"]:
                for re_json_list in return_json["response"]["list"]:
                    price_result.append(re_json_list["zushu"])
                    price_result.append(re_json_list["hanshui"])
            else:
                error_code = return_json
        else:
            error_code = return_json
    elif m_type == "Desk calendar":
        m_ChengPinWidth = 140
        m_ChengPinHeight = 210
        m_ZhiJiaWidth = 210
        m_ZhiJiaHeight = 360
        m_ZhiJiaoHouDu = 2.5
        m_ShuLiang = 1000
        # Piercing
        if True:
            if m_ChengPinWidth > m_ChengPinHeight:
                m_ChuanHuanBian = m_ChengPinHeight
            else:
                m_ChuanHuanBian = m_ChengPinWidth
        else:
            if m_ChengPinWidth < m_ChengPinHeight:
                m_ChuanHuanBian = m_ChengPinHeight
            else:
                m_ChuanHuanBian = m_ChengPinWidth

        m_ChuanHuanYanSe = "黑白色"  # "彩色"
        # price list
        price_result = []

        return_json = m_driver.execute_script(
            js_desk_calendar,
            1,
            m_ChengPinWidth,
            m_ChengPinHeight,
            m_ZhiJiaWidth,
            m_ZhiJiaHeight,
            m_ZhiJiaoHouDu,
            m_ShuLiang,
            m_ChuanHuanBian,
            m_ChuanHuanYanSe,
        )
        if return_json["success"]:
            price_result.append(return_json["response"]["list"][0]["zushu"])
            price_result.append(return_json["response"]["list"][0]["hanshui"])

            return_json = m_driver.execute_script(
                js_desk_calendar,
                2,
                m_ChengPinWidth,
                m_ChengPinHeight,
                m_ZhiJiaWidth,
                m_ZhiJiaHeight,
                m_ZhiJiaoHouDu,
                m_ShuLiang,
                m_ChuanHuanBian,
                m_ChuanHuanYanSe,
            )
            if return_json["success"]:
                for re_json_list in return_json["response"]["list"]:
                    price_result.append(re_json_list["zushu"])
                    price_result.append(re_json_list["hanshui"])
            else:
                error_code = return_json
        else:
            error_code = return_json
    if error_code == "ok":
        print(price_result)
        return price_result
    else:
        print(error_code)
        return error_code


if __name__ == "__main__":
    # C, P
    params_C_P = {
        "m_box_variety": 1,
        "m_ChengPinWidth": 350,
        "m_ChengPinHeight": 260,
        "m_ChengPinHou": 320,
        "m_ShuLiang": 1000,
        "m_PinZhong": 1,
        "m_LeiXing": 16,
        "m_KeZhong": 116,
        "m_ZhengMianColor": 7,
        "m_XiaoBaoZhuang_CaiLiao": "三层高强度瓦楞板",  # c
        "Formed_a_box": True,
        "FuMo_Enable": False,
        "FuMo_FuMoZhongLei": "亮膜",
        "ShouTiSheng_Enable": False,
        "ShouTiSheng_CaiLiao": "普通尼龙绳",
        "TiBa_Enable": False,
        "DanMianTangYin_Enable": False,
        "DanMianTangYin_Width": 12,
        "DanMianTangYin_Height": 34,
        "DanMianTangJin_Enable": False,
        "DanMianTangJin_Width": 12,
        "DanMianTangJin_Height": 34,
        "KaiTianChuang_Enable": False,
        "KaiTianChuang_Width": 12,
        "KaiTianChuang_Height": 34,
        "DanMianJiTu_Enable": False,
        "DanMianJiTu_Width": 12,
        "DanMianJiTu_Height": 34,
        "JuBuUV_Enable": False,
        "JuBuUV_Width": 12,
        "JuBuUV_Height": 34,
        "JuBuUV_UVCaiLiao": "亮光油",
        "GuoYou_Enable": False,
        "GuoYou_CaiLiao": "磨光油",
    }
    # Lavel
    params_L = {
        "m_ChengPinWidth": 90,
        "m_ChengPinHeight": 54,
        "m_ShuLiang": 1000,
        "m_PinZhong": 1,
        "m_LeiXing": 14,
        "m_KeZhong": 102,
        "m_ZhengMianColor": 7,
        "m_FanMianColor": 7,
        "FuMo_Enable": 0,
        "FuMo_FuMoZhongLei": "亮膜",
        "FuMo_ShuangMianFuMo": False,
        "YaWen_Enable": 0,
        "Easytearline": 0,
        "selEasytearline": 1,
        "DanMianTangYin_Enable": 0,
        "DanMianTangYin_Width": 12,
        "DanMianTangYin_Height": 13,
        "DanMianTangJin_Enable": 0,
        "DanMianTangJin_Width": 12,
        "DanMianTangJin_Height": 13,
        "Code": 0,
        "selCode1": "激光码",
        "selCode2": 1,
        "DanMianJiTu_Enable": 0,
        "DanMianJiTu_Width": 12,
        "DanMianJiTu_Height": 12,
        "JuBuUV_Enable": 0,
        "JuBuUV_Width": 12,
        "JuBuUV_Height": 13,
        "JuBuUV_UVCaiLiao": "亮光油",
        "JuBuUV_ShuangMian": "单面",
    }
    result_array = []
    with open(
        "sub_Paper_box_data_1000_DanMianTangYin_Enable_8.csv", "w", newline=""
    ) as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "No",
                "m_box_variety",
                "m_ShuLiang",
                "m_ChengPinWidth",
                "m_ChengPinWidth",
                "m_ChengPinHou",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
            ]
        )
        for count in range(1, 5001):
            # if "Paper Box":
            params_C_P["m_box_variety"] = 3
            params_C_P["m_ShuLiang"] = count
            params_C_P["DanMianTangYin_Enable"] = True
            params_C_P["m_ChengPinWidth"] = random.randrange(10, 80)
            params_C_P["m_ChengPinWidth"] = random.randrange(10, 40)
            params_C_P["m_ChengPinHou"] = random.randrange(10, 120)
            time.sleep(1)
            price_1 = getPrice("Paper Box", params_C_P)

            # writer.writerow(price)
            params_C_P["DanMianTangYin_Enable"] = False
            # params_L["FuMo_Enable"] = 1
            price_2 = getPrice("Paper Box", params_C_P)

            substract_price = [a - b for a, b in zip(price_1, price_2)]

            substract_price.insert(0, count)
            substract_price.insert(1, params_C_P["m_box_variety"])
            substract_price.insert(2, params_C_P["m_ShuLiang"])
            substract_price.insert(3, params_C_P["m_ChengPinWidth"])
            substract_price.insert(4, params_C_P["m_ChengPinWidth"])
            substract_price.insert(5, params_C_P["m_ChengPinHou"])

            result_array.append(substract_price)
            writer.writerow(substract_price)
            print(substract_price)

    # with open("innovators.csv", "w", newline="") as file:
    #     writer = csv.writer(file)
    #     writer.writerow(["SN", "Name", "Contribution"])
    #     writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    #     writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
    #     writer.writerow([3, "Guido van Rossum", "Python Programming"])
    ## convert your array into a dataframe
    workbook = xlsxwriter.Workbook(
        "sub_Paper_box_data_1000_DanMianTangYin_Enable_8.xlsx"
    )
    worksheet = workbook.add_worksheet()

    row = 0

    for col, data in enumerate(result_array):
        worksheet.write_column(row, col, data)

    workbook.close()

