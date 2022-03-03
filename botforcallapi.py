from selenium import webdriver
import json

import glob
import os, shutil
import re
import mysql.connector
import time, threading


source_path = os.getcwd()

mydb = mysql.connector.connect(
    host="127.0.0.1", user="root", passwd="", database="package"
)

mycursor = mydb.cursor()

package_ids = list()

sql = "SELECT * FROM packages WHERE status = 'progress'"
mycursor.execute(sql)
records = mycursor.fetchall()
# Get Ids
for x in records:
    package_ids.append(x[0])


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
    // do something with myJson
    console.log(myJson);
    console.log(arguments[0])

    return myJson;
"""
js_color_pill_box = """
    let body_json;
    //body_json.BuJians[0].MingCheng = '';m_Width, m_Height, m_ShuLiang
    const m_box_variety = arguments[1];
    switch (parseInt(m_box_variety)) {
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
    const m_ChengPinWidth = arguments[2];
    const m_ChengPinHeight = arguments[3];
    const m_ChengPinHou = arguments[4];
    const m_ShuLiang = arguments[5];
    const m_PinZhong = arguments[6];
    const m_LeiXing = arguments[7];
    const m_KeZhong = arguments[8];
    const m_ZhengMianColor = arguments[9];
    const m_binding = arguments[10];
    // const m_ChengPinHou = arguments[9];

    body_json.BuJians[0].P = m_PinZhong;
    body_json.BuJians[0].PinZhong = m_PinZhong;
    body_json.ChengPinWidth = m_ChengPinWidth;
    body_json.ChengPinHeight = m_ChengPinHeight;
    body_json.ChengPinHou = m_ChengPinHou;
    body_json.ShuLiang = m_ShuLiang;
    body_json.PinZhong = m_PinZhong;
    //material gram
    body_json.BuJians[0].ZhiZhang.LeiXing = m_LeiXing;
    body_json.BuJians[0].ZhiZhang.KeZhong = m_KeZhong;
    // if kezhong = 200 then 162
    //Color
    body_json.BuJians[0].ZhengMianColor.ZhuanSe = m_ZhengMianColor;

    //binding Parameters
    body_json.BuJians[0].HouGong.HuHe.Enable = m_binding.Formed_a_box > 0?true:false;
    if(m_binding.FuMo_Enable > 0){
        body_json.BuJians[0].HouGong.FuMo.Enable = true;
        body_json.BuJians[0].HouGong.FuMo.FuMoZhongLei = m_binding.FuMo_FuMoZhongLei 
    }
    if(m_binding.ShouTiSheng_Enable > 0){
        body_json.BuJians[0].HouGong.ShouTiSheng.Enable = true;
        body_json.BuJians[0].HouGong.ShouTiSheng.CaiLiao = m_binding.ShouTiSheng_CaiLiao;
    }
    if(m_binding.TiBa_Enable > 0){
        body_json.BuJians[0].HouGong.ShouTiSheng.Enable = false;
        body_json.BuJians[0].HouGong.TiBa.Enable = true;
    }
    if(m_binding.DanMianTangYin_Enable > 0){
        body_json.BuJians[0].HouGong.DanMianTangYin.Enable = true;
        body_json.BuJians[0].HouGong.DanMianTangYin.Width = m_binding.DanMianTangYin_Width;
        body_json.BuJians[0].HouGong.DanMianTangYin.Height = m_binding.DanMianTangYin_Height;
    }
    if(m_binding.DanMianTangJin_Enable > 0){
        body_json.BuJians[0].HouGong.DanMianTangJin.Enable = true;
        body_json.BuJians[0].HouGong.DanMianTangJin.Width = m_binding.DanMianTangJin_Width;
        body_json.BuJians[0].HouGong.DanMianTangJin.Height = m_binding.DanMianTangJin_Height;
    }
    if(m_binding.KaiTianChuang_Enable > 0){
        body_json.BuJians[0].HouGong.KaiTianChuang.Enable = true;
        body_json.BuJians[0].HouGong.KaiTianChuang.Width = m_binding.KaiTianChuang_Width;
        body_json.BuJians[0].HouGong.KaiTianChuang.Height = m_binding.KaiTianChuang_Height;
    }
    if(m_binding.DanMianJiTu_Enable > 0){
        body_json.BuJians[0].HouGong.DanMianJiTu.Enable = true;
        body_json.BuJians[0].HouGong.DanMianJiTu.Width = m_binding.DanMianJiTu_Width;
        body_json.BuJians[0].HouGong.DanMianJiTu.Height = m_binding.DanMianJiTu_Height;
    }
    if(m_binding.JuBuUV_Enable > 0){
        body_json.BuJians[0].HouGong.JuBuUV.Enable = true;
        body_json.BuJians[0].HouGong.JuBuUV.Width = m_binding.JuBuUV_Width;
        body_json.BuJians[0].HouGong.JuBuUV.Height = m_binding.JuBuUV_Height;
        body_json.BuJians[0].HouGong.JuBuUV.UVCaiLiao = m_binding.JuBuUV_UVCaiLiao;
    }
    if(m_binding.GuoYou_Enable > 0){
        body_json.BuJians[0].HouGong.GuoYou.Enable = true;
        body_json.BuJians[0].HouGong.GuoYou.CaiLiao = m_binding.GuoYou_CaiLiao;
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
    console.log(myJson);
    console.log(arguments[0])

    return myJson;
"""
js_corrugated_box = """
    let body_json;
    //body_json.BuJians[0].MingCheng = '';m_Width, m_Height, m_ShuLiang
    const m_box_variety = arguments[1];
    switch (parseInt(m_box_variety)) {
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
    const m_ChengPinWidth = arguments[2];
    const m_ChengPinHeight = arguments[3];
    const m_ChengPinHou = arguments[4];
    const m_ShuLiang = arguments[5];
    const m_PinZhong = arguments[6];
    const m_LeiXing = arguments[7];
    const m_KeZhong = arguments[8];
    const m_ZhengMianColor = arguments[9];
    const m_XiaoBaoZhuang_CaiLiao = arguments[10];
    const m_binding = arguments[11];
    //const m_binding = arguments[12];

    body_json.BuJians[0].P = m_PinZhong;
    body_json.BuJians[0].PinZhong = m_PinZhong;
    body_json.ChengPinWidth = m_ChengPinWidth;
    body_json.ChengPinHeight = m_ChengPinHeight;
    body_json.ChengPinHou = m_ChengPinHou;
    body_json.ShuLiang = m_ShuLiang;
    body_json.PinZhong = m_PinZhong;
    //material gram
    body_json.BuJians[0].ZhiZhang.LeiXing = m_LeiXing;
    body_json.BuJians[0].ZhiZhang.KeZhong = m_KeZhong;
    // if kezhong = 200 then 162
    //Color
    body_json.BuJians[0].ZhengMianColor.ZhuanSe = m_ZhengMianColor;
    //material type
    body_json.BuJians[0].HouGong.XiaoBaoZhuang.CaiLiao = m_XiaoBaoZhuang_CaiLiao;
    //binding Parameters
    body_json.BuJians[0].HouGong.HuHe.Enable = m_binding.Formed_a_box > 0?true:false;
    if(m_binding.FuMo_Enable > 0){
        body_json.BuJians[0].HouGong.FuMo.Enable = true;
        body_json.BuJians[0].HouGong.FuMo.FuMoZhongLei = m_binding.FuMo_FuMoZhongLei 
    }
    if(m_binding.ShouTiSheng_Enable > 0){
        body_json.BuJians[0].HouGong.ShouTiSheng.Enable = true;
        body_json.BuJians[0].HouGong.ShouTiSheng.CaiLiao = m_binding.ShouTiSheng_CaiLiao;
    }
    if(m_binding.TiBa_Enable > 0){
        body_json.BuJians[0].HouGong.ShouTiSheng.Enable = false;
        body_json.BuJians[0].HouGong.TiBa.Enable = true;
    }
    if(m_binding.DanMianTangYin_Enable > 0){
        body_json.BuJians[0].HouGong.DanMianTangYin.Enable = true;
        body_json.BuJians[0].HouGong.DanMianTangYin.Width = m_binding.DanMianTangYin_Width;
        body_json.BuJians[0].HouGong.DanMianTangYin.Height = m_binding.DanMianTangYin_Height;
    }
    if(m_binding.DanMianTangJin_Enable > 0){
        body_json.BuJians[0].HouGong.DanMianTangJin.Enable = true;
        body_json.BuJians[0].HouGong.DanMianTangJin.Width = m_binding.DanMianTangJin_Width;
        body_json.BuJians[0].HouGong.DanMianTangJin.Height = m_binding.DanMianTangJin_Height;
    }
    if(m_binding.KaiTianChuang_Enable > 0){
        body_json.BuJians[0].HouGong.KaiTianChuang.Enable = true;
        body_json.BuJians[0].HouGong.KaiTianChuang.Width = m_binding.KaiTianChuang_Width;
        body_json.BuJians[0].HouGong.KaiTianChuang.Height = m_binding.KaiTianChuang_Height;
    }
    if(m_binding.DanMianJiTu_Enable > 0){
        body_json.BuJians[0].HouGong.DanMianJiTu.Enable = true;
        body_json.BuJians[0].HouGong.DanMianJiTu.Width = m_binding.DanMianJiTu_Width;
        body_json.BuJians[0].HouGong.DanMianJiTu.Height = m_binding.DanMianJiTu_Height;
    }
    if(m_binding.JuBuUV_Enable > 0){
        body_json.BuJians[0].HouGong.JuBuUV.Enable = true;
        body_json.BuJians[0].HouGong.JuBuUV.Width = m_binding.JuBuUV_Width;
        body_json.BuJians[0].HouGong.JuBuUV.Height = m_binding.JuBuUV_Height;
        body_json.BuJians[0].HouGong.JuBuUV.UVCaiLiao = m_binding.JuBuUV_UVCaiLiao;
    }
    if(m_binding.GuoYou_Enable > 0){
        body_json.BuJians[0].HouGong.GuoYou.Enable = true;
        body_json.BuJians[0].HouGong.GuoYou.CaiLiao = m_binding.GuoYou_CaiLiao;
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
    // do something with myJson
    console.log(myJson);
    console.log(arguments[0])

    return myJson;
"""
js_tag = """
    let body_json = JSON.parse('{ "BuJians": [{ "MingCheng": "", "BuJianFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "LiBaoDuiLian": false, "LiBaoHengPi": false, "LiBaoFuZi": false, "LiBaoHongBao": false, "LiBao": false, "DuiLian": false, "DuiLianHengpi": false, "DuiLianFuZi": false, "FuZi": false, "GuaLiNeiYe": false, "TaiLiNeiYe": false, "TaiLiGongYeBan": false, "TaiLiWaiBiaoZhi": false, "TailiNeiBiaoZhi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": true, "XinFeng": false, "BaoZhi": false, "BianQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "HuaCeFengPi": false, "HuaCeNeiYe": false, "HuaCeFeiYe": false, "HuaCeLaYe": false }, "ZhengMianColor": { "ZhuanSe": 7 }, "FanMianColor": { "ZhuanSe": 7 }, "ZhiZhang": { "LeiXing": 14, "KeZhong": 102 }, "Width": { "Value": 0 }, "Height": { "Value": 0 }, "ZiDaiZhi": false, "HouGongCanShu": [], "ShuangDaMianXiangTong": false, "ShuangCeMianXiangTong": false, "HouGong": { "YaHen": { "YaHenZhe": "", "Enable": false, "JiDaoHen": 1 }, "YiSiXian": { "JiTiaoXian": 1, "Enable": false }, "DanMianJiTu": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangJin": { "Enable": false, "Width": "", "Height": "" }, "DanMianTangYin": { "Enable": false, "Width": "", "Height": "" }, "FuMo": { "ShuangMianFuMo": "false", "FuMoZhongLei": "", "Enable": false }, "MoQie": { "Enable": true, "MoQieZhongLei": "吊牌" }, "YaWen": { "Enable": false, "ShuangMianYaWen": false }, "JuBuUV": { "Enable": false, "ShuangMian": "", "UVCaiLiao": "", "Width": "", "Height": "" }, "KaiTianChuang": { "Enable": false, "Width": "", "Height": "" }, "GuoYou": { "Enable": false, "ShuangMianGuoYou": "", "CaiLiao": "" }, "DaHaoMa": { "Enable": false, "ShuLiang": 1 }, "ZheYe": { "Enable": false, "ZheFa": "" }, "DaKong": { "Enable": false, "DaKongShuLiang": 1 }, "DanMianGuaGuaYin": { "Enable": false }, "HuHe": { "Enable": false, "HeXing": "" }, "ShouTiSheng": { "Enable": false, "CaiLiao": "" }, "TiBa": { "Enable": false }, "DaMaoDing": { "Enable": false }, "JiaoTou": { "Enable": false }, "XiaoBaoZhuang": { "CaiLiao": "", "Enable": false } }, "P": 2, "PinZhong": 1, "ShuLiang": 0, "ZhengFangMianNeiRongXiangTong2": false, "ZhengFangMianNeiRongXiangTong3": false, "ZhengFangMianNeiRongXiangTong4": false, "ZhengFangMianNeiRongXiangTong5": false, "ZhengFangMianNeiRongBuTong": false, "JieDiaoKou": false, "SFYinShua": false, "SFXiangTong": false, "MingChen": "吊牌" }], "ChanPinFenLei": { "DanZhang": false, "XiaoBaoZhuang": false, "DaLiBao": false, "DuiLian": false, "FuZi": false, "GuaLi": false, "TaiLi": false, "MingPian": false, "CaiHe": false, "DangAnDai": false, "DiaoPai": true, "XinFeng": false, "BaoZhi": false, "BiaoQian": false, "FengTao": false, "BuGanJiao": false, "ShouTiDai": false, "YangBenHuaCe": false, "PVC": false, "WuTanLianDan": false, "DanPinGongSiHeight": "", "DanPinGongSiWidth": "", "ShuangPinGongSiHeight": "", "ShuangPinGongSiWidth": "" }, "JiaLeiKou": null, "JiaZheDou": null, "JiaLaYe": null, "ZhuangDingFangShi": "骑马钉", "ChengPinWidth": 90, "ChengPinHeight": 54, "ChengPinHou": 0, "ZheDouLeiXing": "单折兜", "DianBan": false, "QiQiang": 0, "ZhanKaiWidth": 0, "ZhanKaiHeight": 0, "ShuLiang": "1000", "PinZhong": 1, "MeiBenYeShu": 1, "CaiChengPin": true, "ShuangDaMianXiangTong": true, "ShuangCeMianXiangTong": true, "ChuanHuanBian": 0, "ChuanHuanYanSe": "", "ZhiJiaoHouDu": 0, "ZhiJiaWidth": 0, "ZhiJiaHeight": 0, "SheTou": 0, "XinFengYangShi": "" }'); 
    //body_json.BuJians[0].MingCheng = '';m_Width, m_Height, m_ShuLiang
    const m_ChengPinWidth = arguments[1];
    const m_ChengPinHeight = arguments[2];
    const m_ShuLiang = arguments[3];
    const m_PinZhong = arguments[4];
    const m_LeiXing = arguments[5];
    const m_KeZhong = arguments[6];
    const m_ZhengMianColor = arguments[7];
    const m_FanMianColor = arguments[8];
    const m_binding = arguments[9];

    body_json.BuJians[0].PinZhong = m_PinZhong
    body_json.BuJians[0].P = m_PinZhong * 2

    body_json.ChengPinWidth = m_ChengPinWidth
    body_json.ChengPinHeight = m_ChengPinHeight
    body_json.ShuLiang = m_ShuLiang
    body_json.PinZhong = m_PinZhong

    body_json.BuJians[0].ZhiZhang.LeiXing = m_LeiXing
    body_json.BuJians[0].ZhiZhang.KeZhong = m_KeZhong


    body_json.BuJians[0].ZhengMianColor.ZhuanSe = m_ZhengMianColor
    body_json.BuJians[0].FanMianColor.ZhuanSe = m_FanMianColor

    //binding Parameters
    if(m_binding.FuMo_Enable > 0){
        body_json.BuJians[0].HouGong.FuMo.Enable = true;
        body_json.BuJians[0].HouGong.FuMo.FuMoZhongLei = m_binding.FuMo_FuMoZhongLei 
        body_json.BuJians[0].HouGong.FuMo.ShuangMianFuMo = m_binding.FuMo_ShuangMianFuMo=="single"  ? false:true;
    }
    if(m_binding.YaWen_Enable > 0){
        body_json.BuJians[0].HouGong.YaWen.Enable = true;
    }
    if(m_binding.Easytearline > 0){
        body_json.BuJians[0].HouGong.YiSiXian.Enable = true;
        body_json.BuJians[0].HouGong.YiSiXian.JiTiaoXian = m_binding.selEasytearline;
    }
    if(m_binding.DanMianTangYin_Enable > 0){
        body_json.BuJians[0].HouGong.DanMianTangYin.Enable = true;
        body_json.BuJians[0].HouGong.DanMianTangYin.Width = m_binding.DanMianTangYin_Width;
        body_json.BuJians[0].HouGong.DanMianTangYin.Height = m_binding.DanMianTangYin_Height;
    }
    if(m_binding.DanMianTangJin_Enable > 0){
        body_json.BuJians[0].HouGong.DanMianTangJin.Enable = true;
        body_json.BuJians[0].HouGong.DanMianTangJin.Width = m_binding.DanMianTangJin_Width;
        body_json.BuJians[0].HouGong.DanMianTangJin.Height = m_binding.DanMianTangJin_Height;
    }
    if(m_binding.Code > 0 ){
        body_json.BuJians[0].HouGong.DaHaoMa.Enable = true;
        body_json.BuJians[0].HouGong.DaHaoMa.ShuLiang = m_binding.selCode2;
        body_json.BuJians[0].HouGong.DaHaoMa.DaMaLeiXing = m_binding.selCode1;
    }
    if(m_binding.DanMianJiTu_Enable > 0){
        body_json.BuJians[0].HouGong.DanMianJiTu.Enable = true;
        body_json.BuJians[0].HouGong.DanMianJiTu.Width = m_binding.DanMianJiTu_Width;
        body_json.BuJians[0].HouGong.DanMianJiTu.Height = m_binding.DanMianJiTu_Height;
    }
    if(m_binding.JuBuUV_Enable > 0){
        body_json.BuJians[0].HouGong.JuBuUV.Enable = true;
        body_json.BuJians[0].HouGong.JuBuUV.Width = m_binding.JuBuUV_Width;
        body_json.BuJians[0].HouGong.JuBuUV.Height = m_binding.JuBuUV_Height;
        body_json.BuJians[0].HouGong.JuBuUV.UVCaiLiao = m_binding.JuBuUV_UVCaiLiao;
        body_json.BuJians[0].HouGong.JuBuUV.ShuangMian = m_binding.JuBuUV_ShuangMian;
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
    const m_binding = arguments[9];

    
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

    body_json.BuJians[2].P = m_binding.selText * 2;
    body_json.BuJians[2].ShuLiang = m_binding.selText;

    body_json.BuJians[2].ZhengMianColor.ZhuanSe = m_binding.printColor1;
    body_json.BuJians[2].FanMianColor.ZhuanSe = m_binding.printColor2;
    body_json.BuJians[2].ZhiZhang.LeiXing = m_binding.material1;
    body_json.BuJians[2].ZhiZhang.KeZhong = m_binding.material2;

    if(m_binding.innerPrinting > 0){
        body_json.BuJians[0].ZhiZhang.LeiXing = m_binding.innerMaterial1;
        body_json.BuJians[0].ZhiZhang.KeZhong = m_binding.innerMaterial2;
        body_json.BuJians[0].SFYinShua = true;
        body_json.BuJians[0].ZhengMianColor.ZhuanSe = m_binding.innerPrintingcolor1;
    }
    if(m_binding.outerPrinting > 0){
        body_json.BuJians[1].ZhiZhang.LeiXing = m_binding.outerMaterial1;
        body_json.BuJians[1].ZhiZhang.KeZhong = m_binding.outerMaterial2;
        body_json.BuJians[1].SFYinShua = true;
        body_json.BuJians[1].ZhengMianColor.ZhuanSe = m_binding.outerPrintingcolor1;
    }
    if(m_binding.FuMo_Enable > 0){
        body_json.BuJians[1].HouGong.FuMo.Enable = true;
        body_json.BuJians[1].HouGong.FuMo.FuMoZhongLei = m_binding.FuMo_FuMoZhongLei 
    }
    if(m_binding.DanMianTangYin_Enable > 0){
        body_json.BuJians[1].HouGong.DanMianTangYin.Enable = true;
        body_json.BuJians[1].HouGong.DanMianTangYin.Width = m_binding.DanMianTangYin_Width;
        body_json.BuJians[1].HouGong.DanMianTangYin.Height = m_binding.DanMianTangYin_Height;
    }
    if(m_binding.DanMianTangJin_Enable > 0){
        body_json.BuJians[1].HouGong.DanMianTangJin.Enable = true;
        body_json.BuJians[1].HouGong.DanMianTangJin.Width = m_binding.DanMianTangJin_Width;
        body_json.BuJians[1].HouGong.DanMianTangJin.Height = m_binding.DanMianTangJin_Height;
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


class webcapture:
    def __init__(self, path):
        self.source_path = path
        # options = Options()
        # prefs = {"download.default_directory" : r'{0}\pdfs'.format(path), "plugins.always_open_pdf_externally":True}
        # options.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(
            executable_path="{0}/chromedriver/chromedriver.exe".format(self.source_path)
        )  # , options=options)
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(10)
        self.driver.get("http://qd.ieprint.cc/#/waleng")
        # time.sleep(3)

    def setParameters(self, c_id):
        self.c_id = c_id
        sql = "UPDATE packages SET status = 'Running' WHERE id = '" + str(c_id) + "'"
        mycursor.execute(sql)
        mydb.commit()

        sql = "SELECT * FROM packages WHERE id = '" + str(c_id) + "'"
        mycursor.execute(sql)
        records = mycursor.fetchall()

        for row in records:
            id = row[0]
            boxType = row[1]
            packageType = row[2]
            productSize1 = row[3]
            productSize2 = row[4]
            productSize3 = row[5]
            tripodSize1 = row[6]
            tripodSize2 = row[7]
            bracket = row[8]
            piercing = row[9]
            colorRing = row[10]
            printQuantity1 = row[11]
            printQuantity2 = row[12]

            material1 = row[13]
            material2 = row[14]

            printColor1 = row[15]
            printColor2 = row[16]

            printsBook = row[17]
            thickness = row[18]
            corrugatedBoard = row[19]

            Formedabox = row[20]
            Lamination = row[21]
            selLamination1 = row[22]
            selLamination2 = row[23]
            HandRope = row[24]
            selHandRope = row[25]
            Handle = row[26]
            StampingSliver = row[27]
            StampingSliverL = row[28]
            StampingSliverW = row[29]
            StampingGold = row[30]
            StampingGoldL = row[31]
            StampingGoldW = row[32]
            PVCWindows = row[33]
            PVCWindowsL = row[34]
            PVCWindowsW = row[35]
            Embossed = row[36]
            EmbossedL = row[37]
            EmbossedW = row[38]
            SpotUV = row[39]
            selSpotUV1 = row[40]
            SpotUVL = row[41]
            SpotUVW = row[42]
            Varnishing = row[43]

            selText = row[44]
            outerPrinting = row[45]
            outerMaterial1 = row[46]
            outerMaterial2 = row[47]
            outerPrintingcolor1 = row[48]

            innerPrinting = row[49]
            innerMaterial1 = row[50]
            innerMaterial2 = row[51]
            innerPrintingcolor1 = row[52]

            selVarnishing = row[53]

            LinenTexture = row[54]
            Indentation = row[55]
            selIndentation1 = row[56]
            selIndentation2 = row[57]
            Easytearline = row[58]
            selEasytearline = row[59]
            Code = row[60]
            selCode1 = row[61]
            selCode2 = row[62]
            PunchHole = row[63]
            selPunchHole = row[64]
            selSpotUV2 = row[65]

            # Get Parameters

            m_type = boxType
            # m_type = "color_pill_box"
            # m_type = "tag"
            # m_type = "Desk calendar"
            m_driver = self.driver
            error_code = "ok"
            if m_type == "sampleAlbum":
                m_Width = productSize1
                m_Height = productSize2
                m_ShuLiang = printsBook
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
            elif m_type == "corrugatedBox":
                m_box_variety = packageType
                m_ChengPinWidth = productSize1
                m_ChengPinHeight = productSize2
                m_ChengPinHou = productSize3
                m_ShuLiang = printQuantity1
                m_PinZhong = printQuantity2
                # [
                #     "SBS": 16,
                #     "Kraft Paper": 17,
                #     "White Kraft Paper": 28,
                #     "C2S": 14,
                #     "CCNB": 278,
                # ]
                m_LeiXing = material1
                # "SBS": [
                #     "210": 114,
                #     "230": 115,
                #     "250": 116,
                #     "300": 117,
                #     "350": 26,

                # ],
                # "Kraft Paper": [
                #     "200": 162,
                #     "250": 166,
                #     "300": 104,
                # ],
                # "White Kraft Paper": [
                #     "250": 86
                # ],
                # "C2S": [
                #     "250": 102,
                #     "300": 103,
                #     "350": 14,
                # ]
                # "CCNB": [
                #     "250": 316,
                #     "300": 317,
                #     "350": 318,
                # ]
                m_KeZhong = material2
                # color 7~15
                m_ZhengMianColor = printColor1  # 单黑
                # price list
                # "CaiLiag": [
                #     "Three-layer high-strength corrugated cardboard": "三层高强度瓦楞板",
                #     "Three-layer high-strength corrugated cardboard (inner white)": "三层高强度瓦楞(内白)",
                #     "Three-layer (ordinary) corrugated cardboard": "三层(普通)瓦楞板",
                #     "Five-layer (ordinary) corrugated cardboard": "五层(普通)瓦楞纸板",
                # ]
                m_XiaoBaoZhuang_CaiLiao = corrugatedBoard

                # m_binding = {
                #     "Formed_a_box": Formedabox,
                #     "FuMo_Enable": Lamination,
                #     "FuMo_FuMoZhongLei": selLamination2,
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

                m_binding = {
                    "Formed_a_box": Formedabox,
                    "FuMo_Enable": Lamination,
                    "FuMo_FuMoZhongLei": selLamination2,
                    "ShouTiSheng_Enable": HandRope,
                    "ShouTiSheng_CaiLiao": selHandRope,
                    "TiBa_Enable": Handle,
                    "DanMianTangYin_Enable": StampingSliver,
                    "DanMianTangYin_Width": StampingSliverL,
                    "DanMianTangYin_Height": StampingSliverW,
                    "DanMianTangJin_Enable": StampingGold,
                    "DanMianTangJin_Width": StampingGoldL,
                    "DanMianTangJin_Height": StampingGoldW,
                    "KaiTianChuang_Enable": PVCWindows,
                    "KaiTianChuang_Width": PVCWindowsL,
                    "KaiTianChuang_Height": PVCWindowsW,
                    "DanMianJiTu_Enable": Embossed,
                    "DanMianJiTu_Width": EmbossedL,
                    "DanMianJiTu_Height": EmbossedW,
                    "JuBuUV_Enable": SpotUV,
                    "JuBuUV_Width": SpotUVL,
                    "JuBuUV_Height": SpotUVW,
                    "JuBuUV_UVCaiLiao": selSpotUV1,
                    "GuoYou_Enable": Varnishing,
                    "GuoYou_CaiLiao": selVarnishing,
                }

                price_result = []

                return_json = m_driver.execute_script(
                    js_corrugated_box,
                    1,
                    m_box_variety,
                    m_ChengPinWidth,
                    m_ChengPinHeight,
                    m_ChengPinHou,
                    m_ShuLiang,
                    m_PinZhong,
                    m_LeiXing,
                    m_KeZhong,
                    m_ZhengMianColor,
                    m_XiaoBaoZhuang_CaiLiao,
                    m_binding,
                )
                if return_json["success"]:
                    price_result.append(return_json["response"]["list"][0]["zushu"])
                    price_result.append(return_json["response"]["list"][0]["hanshui"])

                    return_json = m_driver.execute_script(
                        js_corrugated_box,
                        2,
                        m_box_variety,
                        m_ChengPinWidth,
                        m_ChengPinHeight,
                        m_ChengPinHou,
                        m_ShuLiang,
                        m_PinZhong,
                        m_LeiXing,
                        m_KeZhong,
                        m_ZhengMianColor,
                        m_XiaoBaoZhuang_CaiLiao,
                        m_binding,
                    )
                    if return_json["success"]:
                        for re_json_list in return_json["response"]["list"]:
                            price_result.append(re_json_list["zushu"])
                            price_result.append(re_json_list["hanshui"])
                    else:
                        error_code = "error 2 request"
                else:
                    error_code = "error 1 request"
            elif m_type == "Paper Box":
                m_box_variety = packageType
                m_ChengPinWidth = productSize1
                m_ChengPinHeight = productSize2
                m_ChengPinHou = productSize3
                m_ShuLiang = printQuantity1
                m_PinZhong = printQuantity2
                # [
                #     "SBS": 16,
                #     "Kraft Paper": 17,
                #     "White Kraft Paper": 28,
                #     "C2S": 14,
                #     "CCNB": 278,
                # ]
                m_LeiXing = material1
                # "SBS": [
                #     "210": 114,
                #     "230": 115,
                #     "250": 116,
                #     "300": 117,
                #     "350": 26,

                # ],
                # "Kraft Paper": [
                #     "200": 162,
                #     "250": 166,
                #     "300": 104,
                # ],
                # "White Kraft Paper": [
                #     "250": 86
                # ],
                # "C2S": [
                #     "250": 102,
                #     "300": 103,
                #     "350": 14,
                # ]
                # "CCNB": [
                #     "250": 316,
                #     "300": 317,
                #     "350": 318,
                # ]
                m_KeZhong = material2
                # color 7~15
                m_ZhengMianColor = printColor1  # 单黑
                # price list
                m_binding = {
                    "Formed_a_box": Formedabox,
                    "FuMo_Enable": Lamination,
                    "FuMo_FuMoZhongLei": selLamination2,
                    "ShouTiSheng_Enable": HandRope,
                    "ShouTiSheng_CaiLiao": selHandRope,
                    "TiBa_Enable": Handle,
                    "DanMianTangYin_Enable": StampingSliver,
                    "DanMianTangYin_Width": StampingSliverL,
                    "DanMianTangYin_Height": StampingSliverW,
                    "DanMianTangJin_Enable": StampingGold,
                    "DanMianTangJin_Width": StampingGoldL,
                    "DanMianTangJin_Height": StampingGoldW,
                    "KaiTianChuang_Enable": PVCWindows,
                    "KaiTianChuang_Width": PVCWindowsL,
                    "KaiTianChuang_Height": PVCWindowsW,
                    "DanMianJiTu_Enable": Embossed,
                    "DanMianJiTu_Width": EmbossedL,
                    "DanMianJiTu_Height": EmbossedW,
                    "JuBuUV_Enable": SpotUV,
                    "JuBuUV_Width": SpotUVL,
                    "JuBuUV_Height": SpotUVW,
                    "JuBuUV_UVCaiLiao": selSpotUV1,
                    "GuoYou_Enable": Varnishing,
                    "GuoYou_CaiLiao": selVarnishing,
                }
                price_result = []

                return_json = m_driver.execute_script(
                    js_color_pill_box,
                    1,
                    m_box_variety,
                    m_ChengPinWidth,
                    m_ChengPinHeight,
                    m_ChengPinHou,
                    m_ShuLiang,
                    m_PinZhong,
                    m_LeiXing,
                    m_KeZhong,
                    m_ZhengMianColor,
                    m_binding,
                )
                if return_json["success"]:
                    price_result.append(return_json["response"]["list"][0]["zushu"])
                    price_result.append(return_json["response"]["list"][0]["hanshui"])

                    return_json = m_driver.execute_script(
                        js_color_pill_box,
                        2,
                        m_box_variety,
                        m_ChengPinWidth,
                        m_ChengPinHeight,
                        m_ChengPinHou,
                        m_ShuLiang,
                        m_PinZhong,
                        m_LeiXing,
                        m_KeZhong,
                        m_ZhengMianColor,
                        m_binding,
                    )
                    if return_json["success"]:
                        for re_json_list in return_json["response"]["list"]:
                            price_result.append(re_json_list["zushu"])
                            price_result.append(re_json_list["hanshui"])
                    else:
                        error_code = "error 2 request"
                else:
                    error_code = "error 1 request"

            elif m_type == "Tag":
                m_ChengPinWidth = productSize1
                m_ChengPinHeight = productSize2
                m_ShuLiang = printQuantity1
                m_PinZhong = printQuantity2
                # 14:Coated paper,16:White cardboard,19:Matte paper
                # 15:Double offset paper, 22:Oxue, 18:New beauty
                # 21:Sense of elegance, 24:Dutch White Card
                # 17:Kraft paper, 25:Pearlescent ice white star colored paper
                # 28: White cowhide,29:High school movie,
                # 32: Athens pattern,33:Fine pear pattern,
                m_LeiXing = material1
                # Coated paper 250: 102, 200: 11
                # White cardboard 210: 114, 230:115
                # Matte paper 128:46,157:41, 200:42

                m_KeZhong = material2  # 250
                # color:7,Single black:8, Double spot color:9,Single spot color:10
                # Color +1 Special:12, Color +2 special:13
                # Color+glazing : 14, Glazing:15, reverse color no:0
                m_ZhengMianColor = printColor1  # 单黑
                m_FanMianColor = printColor2

                m_binding = {
                    "FuMo_Enable": Lamination,
                    "FuMo_FuMoZhongLei": selLamination2,
                    "FuMo_ShuangMianFuMo": selLamination1,
                    "YaWen_Enable": LinenTexture,
                    "Easytearline": Easytearline,
                    "selEasytearline": selEasytearline,
                    "DanMianTangYin_Enable": StampingSliver,
                    "DanMianTangYin_Width": StampingSliverL,
                    "DanMianTangYin_Height": StampingSliverW,
                    "DanMianTangJin_Enable": StampingGold,
                    "DanMianTangJin_Width": StampingGoldL,
                    "DanMianTangJin_Height": StampingGoldW,
                    "Code": Code,
                    "selCode1": selCode1,
                    "selCode2": selCode2,
                    "DanMianJiTu_Enable": Embossed,
                    "DanMianJiTu_Width": EmbossedL,
                    "DanMianJiTu_Height": EmbossedW,
                    "JuBuUV_Enable": SpotUV,
                    "JuBuUV_Width": SpotUVL,
                    "JuBuUV_Height": SpotUVW,
                    "JuBuUV_UVCaiLiao": selSpotUV1,
                    "JuBuUV_ShuangMian": selSpotUV2,
                }

                # price list
                price_result = []

                return_json = m_driver.execute_script(
                    js_tag,
                    1,
                    m_ChengPinWidth,
                    m_ChengPinHeight,
                    m_ShuLiang,
                    m_PinZhong,
                    m_LeiXing,
                    m_KeZhong,
                    m_ZhengMianColor,
                    m_FanMianColor,
                    m_binding,
                )
                if return_json["success"]:
                    price_result.append(return_json["response"]["list"][0]["zushu"])
                    price_result.append(return_json["response"]["list"][0]["hanshui"])

                    return_json = m_driver.execute_script(
                        js_tag,
                        2,
                        m_ChengPinWidth,
                        m_ChengPinHeight,
                        m_ShuLiang,
                        m_PinZhong,
                        m_LeiXing,
                        m_KeZhong,
                        m_ZhengMianColor,
                        m_FanMianColor,
                        m_binding,
                    )
                    if return_json["success"]:
                        for re_json_list in return_json["response"]["list"]:
                            price_result.append(re_json_list["zushu"])
                            price_result.append(re_json_list["hanshui"])
                    else:
                        error_code = "error 2 request"
                else:
                    error_code = "error 1 request"
            elif m_type == "Desk calendar":
                m_ChengPinWidth = productSize2
                m_ChengPinHeight = productSize1
                m_ZhiJiaWidth = tripodSize1
                m_ZhiJiaHeight = tripodSize2
                m_ZhiJiaoHouDu = bracket
                m_ShuLiang = printsBook
                # Piercing
                if piercing == 1:
                    if m_ChengPinWidth > m_ChengPinHeight:
                        m_ChuanHuanBian = m_ChengPinHeight
                    else:
                        m_ChuanHuanBian = m_ChengPinWidth
                else:
                    if m_ChengPinWidth < m_ChengPinHeight:
                        m_ChuanHuanBian = m_ChengPinHeight
                    else:
                        m_ChuanHuanBian = m_ChengPinWidth
                if colorRing == 1:
                    m_ChuanHuanYanSe = "黑白色"  # "彩色"
                else:
                    m_ChuanHuanYanSe = "彩色"

                m_binding = {
                    "selText": selText,
                    "material1": material1,
                    "material2": material2,
                    "printColor1": printColor1,
                    "printColor2": printColor2,
                    "outerPrinting": outerPrinting,
                    "outerMaterial1": outerMaterial1,
                    "outerMaterial2": outerMaterial2,
                    "outerPrintingcolor1": outerPrintingcolor1,
                    "innerPrinting": innerPrinting,
                    "innerMaterial1": innerMaterial1,
                    "innerMaterial2": innerMaterial2,
                    "innerPrintingcolor1": innerPrintingcolor1,
                    "FuMo_Enable": Lamination,
                    "FuMo_FuMoZhongLei": selLamination2,
                    "DanMianTangYin_Enable": StampingSliver,
                    "DanMianTangYin_Width": StampingSliverL,
                    "DanMianTangYin_Height": StampingSliverW,
                    "DanMianTangJin_Enable": StampingGold,
                    "DanMianTangJin_Width": StampingGoldL,
                    "DanMianTangJin_Height": StampingGoldW,
                }
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
                    m_binding,
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
                        m_binding,
                    )
                    if return_json["success"]:
                        for re_json_list in return_json["response"]["list"]:
                            price_result.append(re_json_list["zushu"])
                            price_result.append(re_json_list["hanshui"])
                    else:
                        error_code = "error 2 request"
                else:
                    error_code = "error 1 request"
            if error_code == "ok":
                print(price_result)
                # print("test")

            sql = (
                "INSERT INTO `results` VALUES ("
                + str(id)
                + ","
                + str(id)
                + ","
                + str(price_result[0])
                + ","
                + str(price_result[1])
                + ","
                + str(price_result[2])
                + ","
                + str(price_result[3])
                + ","
                + str(price_result[4])
                + ","
                + str(price_result[5])
                + ","
                + str(price_result[6])
                + ","
                + str(price_result[7])
                + ","
                + str(price_result[8])
                + ","
                + str(price_result[9])
                + ",'"
                + "result_text"
                + "',NULL,NULL)"
            )
            # print(sql)
            mycursor.execute(sql)
            mydb.commit()

            sql = "UPDATE packages SET status = 'update' WHERE id = '" + str(id) + "'"
            # print(sql)
            mycursor.execute(sql)
            mydb.commit()

    def quit(self,):
        self.driver.quit()


automation = webcapture(source_path)
while True:
    # initialize all task id list
    mycursor = mydb.cursor()
    mydb.commit()
    sql = "SELECT * FROM packages WHERE status = 'progress'"
    mycursor.execute(sql)
    records = mycursor.fetchall()
    del package_ids[:]
    # Get Ids
    for x in records:
        package_ids.append(x[0])

    if len(package_ids) > 0:

        print("There are  {0} tasks.".format(len(package_ids)))

        for current_id in package_ids:
            try:
                print("Task Id is :" + str(current_id))
                automation.setParameters(current_id)
            except:
                sql = (
                    "UPDATE packages SET status = 'Error' WHERE id = '"
                    + str(current_id)
                    + "'"
                )
                mycursor.execute(sql)
                mydb.commit()
                pass
    else:
        time.sleep(0.2)

# automation.setParameters()
# automation.getResult()
automation.quit()

