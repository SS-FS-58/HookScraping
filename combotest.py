from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
import glob
import os, time, shutil
import re
import mysql.connector
import time, threading

from tkinter import Tk

source_path = os.getcwd()
keywords = list()

#Class information
# str1 = '瓦楞箱 5000个 成品长350x宽200x高200  展开575*555 灰底白板250g 单面 彩色  模切+糊成品+瓦楞(三层高强度瓦楞板) #印码VLB3p1# 14314元'

# str2 = '瓦楞箱 5000个 成品长350x宽200x高200  展开575*555 灰底白板250g 单面 彩色  模切+糊成品+瓦楞(三层高强度瓦楞板) #印码VLB3p2# 含税15459元'

# mydb = mysql.connector.connect(
#   host="127.0.0.1",
#   user="root",
#   passwd="",
#   database="package"
# )

# mycursor = mydb.cursor()

package_ids = list()

# sql = "SELECT * FROM packages WHERE status = 'progress'"
# mycursor.execute(sql)
# records = mycursor.fetchall()
#Get Ids
# for x in records:
#     package_ids.append(x[0])




def analysis_result(full_text):
    price = full_text.split()[-1]
    return re.findall(r'\d+', price)[0] 



class webcapture():
    def __init__(self, path):
        self.source_path = path
        # options = Options()
        # prefs = {"download.default_directory" : r'{0}\pdfs'.format(path), "plugins.always_open_pdf_externally":True}
        # options.add_experimental_option("prefs",prefs)
        
        # Read config.json file 
        with open('config.json','r') as inf:
            # c = eval(inf.read())
            self.urls =eval(inf.read())['urls']
        self.driver = webdriver.Chrome(executable_path='{0}/chromedriver/chromedriver.exe'.format(self.source_path))#, options=options)
        self.driver.maximize_window() 
        self.driver.implicitly_wait(10)
        self.driver.get(self.urls['Corrugated box'])

        # time.sleep(3)
         
        
    def setParameters(self, c_id):
        self.c_id = c_id
        # sql = "UPDATE packages SET status = 'Running' WHERE id = '"+str(c_id)+"'"
        # mycursor.execute(sql)
        # mydb.commit()

        # sql = "SELECT * FROM packages WHERE id = '"+str(c_id)+"'"
        # mycursor.execute(sql)
        # records = mycursor.fetchall()

        # for row in records:
            # id = 'c_id'
        package_type = '手提箱'
        product_size1 = 100
        product_size2 = 200
        product_size3 = 200
        print_quantity1 = 2000
        print_quantity2 = 2
        # facial_paper1 = row[7]
        # facial_paper2 = row[8]
        # //*[@id="app"]/div[1]/section/section/main/div/div[1]/div[2]/div/div/form/div[1]/div/div/div[3]/div/input
        if (package_type == '上盖下插底盒'):
            # pass
            if not "active" in self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/section/main/div/div[1]/div[1]/div/div/div[1]').get_attribute("class"):
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/section/main/div/div[1]/div[1]/div/div/div[1]').click()
        elif (package_type == '手提箱'):
            if not "active" in self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/section/main/div/div[1]/div[1]/div/div/div[2]').get_attribute("class"):
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/section/main/div/div[1]/div[1]/div/div/div[2]').click()
        elif(package_type == '提拔盒'):
            if not "active" in self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/section/main/div/div[1]/div[1]/div/div/div[3]').get_attribute("class"):
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/section/main/div/div[1]/div[1]/div/div/div[3]').click()
        else:
            if not "active" in self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/section/main/div/div[1]/div[1]/div/div/div[4]').get_attribute("class"):
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/section/main/div/div[1]/div[1]/div/div/div[4]').click()
            
        
        
        # WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'userNameInput'))).send_keys(emailID)
        # self.product_size_length = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(By.XPATH, '//*[@id="app"]/div[1]/section/section/main/div/div[1]/div[2]/div/div/form/div[1]/div/div/div[3]/div/input'))
        self.product_size_length = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/section/main/div/div[1]/div[2]/div/div/form/div[1]/div/div/div[3]/div/input')
        self.product_size_length.clear()
        self.product_size_length.send_keys(product_size1)
    
        self.product_size_width = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/section/main/div/div[1]/div[2]/div/div/form/div[1]/div/div/div[4]/div/input')
        self.product_size_width.clear()
        self.product_size_width.send_keys(product_size2)


        self.product_size_height = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/section/main/div/div[1]/div[2]/div/div/form/div[1]/div/div/div[5]/div/input')
        self.product_size_height.clear()
        self.product_size_height.send_keys(product_size3)

        self.ele_print_quantity1 = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/section/main/div/div[1]/div[2]/div/div/form/div[2]/div/div[1]/div/input')
        self.ele_print_quantity1.clear()
        self.ele_print_quantity1.send_keys(print_quantity1)

        self.ele_print_quantity2 = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/section/main/div/div[1]/div[2]/div/div/form/div[2]/div/div[2]/div/input')
        self.ele_print_quantity2.clear()
        self.ele_print_quantity2.send_keys(print_quantity2)

        script = """
        
        const response = await fetch(
            "http://qd.ieprint.cc/api/BaoJiaApi/DanyeBaojia?CiShu=1&pageCode=pageCode",
            {
            headers: {
                accept: "application/json, text/plain, */*",
                "accept-language": "en-US,en;q=0.9,ko;q=0.8",
                "bj-guid": "a26c902c-79d0-44e5-a3b2-edf3ecb8beba",
                "content-type": "application/json;charset=UTF-8",
            },
            referrer: "http://qd.ieprint.cc/",
            referrerPolicy: "no-referrer-when-downgrade",
            body:
                '{"BuJians":[{"MingCheng":"","BuJianFenLei":{"DanZhang":false,"XiaoBaoZhuang":true,"LiBaoDuiLian":false,"LiBaoHengPi":false,"LiBaoFuZi":false,"LiBaoHongBao":false,"LiBao":false,"DuiLian":false,"DuiLianHengpi":false,"DuiLianFuZi":false,"FuZi":false,"GuaLiNeiYe":false,"TaiLiNeiYe":false,"TaiLiGongYeBan":false,"TaiLiWaiBiaoZhi":false,"TailiNeiBiaoZhi":false,"MingPian":false,"CaiHe":false,"DangAnDai":false,"DiaoPai":false,"XinFeng":false,"BaoZhi":false,"BianQian":false,"FengTao":false,"BuGanJiao":false,"ShouTiDai":false,"HuaCeFengPi":false,"HuaCeNeiYe":false,"HuaCeFeiYe":false,"HuaCeLaYe":false},"ZhengMianColor":{"ZhuanSe":7},"FanMianColor":{"ZhuanSe":0},"ZhiZhang":{"LeiXing":16,"KeZhong":116},"Width":{"Value":0},"Height":{"Value":0},"ZiDaiZhi":false,"HouGongCanShu":[],"ShuangDaMianXiangTong":false,"ShuangCeMianXiangTong":false,"HouGong":{"YaHen":{"YaHenZhe":"","Enable":false,"JiDaoHen":1},"YiSiXian":{"JiTiaoXian":1,"Enable":false},"DanMianJiTu":{"Enable":false,"Width":"","Height":""},"DanMianTangJin":{"Enable":false,"Width":"","Height":""},"DanMianTangYin":{"Enable":false,"Width":"","Height":""},"FuMo":{"ShuangMianFuMo":"false","FuMoZhongLei":"","Enable":false},"MoQie":{"Enable":true,"MoQieZhongLei":"小包装"},"YaWen":{"Enable":false,"ShuangMianYaWen":false},"JuBuUV":{"Enable":false,"ShuangMian":"单面","UVCaiLiao":"","Width":"","Height":""},"KaiTianChuang":{"Enable":false,"Width":"","Height":""},"GuoYou":{"Enable":false,"ShuangMianGuoYou":"单面","CaiLiao":""},"DaHaoMa":{"Enable":false,"ShuLiang":1},"ZheYe":{"Enable":false,"ZheFa":""},"DaKong":{"Enable":false,"DaKongShuLiang":1},"DanMianGuaGuaYin":{"Enable":false},"HuHe":{"Enable":true,"HeXing":"其他"},"ShouTiSheng":{"Enable":false,"CaiLiao":""},"TiBa":{"Enable":false},"DaMaoDing":{"Enable":false},"JiaoTou":{"Enable":false},"XiaoBaoZhuang":{"CaiLiao":"三层高强度瓦楞板","Enable":true}},"P":1,"PinZhong":1,"ShuLiang":0,"ZhengFangMianNeiRongXiangTong2":false,"ZhengFangMianNeiRongXiangTong3":false,"ZhengFangMianNeiRongXiangTong4":false,"ZhengFangMianNeiRongXiangTong5":false,"ZhengFangMianNeiRongBuTong":false,"JieDiaoKou":false,"SFYinShua":false,"SFXiangTong":false,"MingChen":"小包装"}],"ChanPinFenLei":{"DanZhang":false,"XiaoBaoZhuang":true,"DaLiBao":false,"DuiLian":false,"FuZi":false,"GuaLi":false,"TaiLi":false,"MingPian":false,"CaiHe":false,"DangAnDai":false,"DiaoPai":false,"XinFeng":false,"BaoZhi":false,"BiaoQian":false,"FengTao":false,"BuGanJiao":false,"ShouTiDai":false,"YangBenHuaCe":false,"PVC":false,"WuTanLianDan":false,"DanPinGongSiHeight":"","DanPinGongSiWidth":"","ShuangPinGongSiHeight":"","ShuangPinGongSiWidth":""},"JiaLeiKou":null,"JiaZheDou":null,"JiaLaYe":null,"ZhuangDingFangShi":"骑马钉","ChengPinWidth":350,"ChengPinHeight":260,"ChengPinHou":"320","ZheDouLeiXing":"单折兜","DianBan":false,"QiQiang":0,"ZhanKaiWidth":0,"ZhanKaiHeight":0,"ShuLiang":"1000","PinZhong":1,"MeiBenYeShu":1,"CaiChengPin":true,"ShuangDaMianXiangTong":true,"ShuangCeMianXiangTong":true,"ChuanHuanBian":0,"ChuanHuanYanSe":"","ZhiJiaoHouDu":0,"ZhiJiaWidth":0,"ZhiJiaHeight":0,"SheTou":0,"XinFengYangShi":"","DanPinGongSiHeight":"(长+宽)*2+25","DanPinGongSiWidth":"宽/2+30+高+宽+25","ShuangPinGongSiHeight":"长+宽+25","ShuangPinGongSiWidth":"宽/2+30+高+宽+25"}',
            method: "POST",
            mode: "cors",
            credentials: "omit",
            }
        );

        const myJson = await response.json(); //extract JSON from the http response
        // do something with myJson
        console.log(myJson);
        console.log(arguments[0])
        return myJson;
        
        """
        print(self.driver.execute_script(script, "test"))
        #combobox
        # self.ele_test_combo = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div[1]/ul/li[4]')
#         self.driver.execute_script('window.onload = async () => {\
#             const response = await fetch(\
#                 "http://qd.ieprint.cc/api/BaoJiaApi/DanyeBaojia?CiShu=1&pageCode=pageCode",\
#                 {
#                 headers: {
#                     accept: "application/json, text/plain, */*",
#                     "accept-language": "en-US,en;q=0.9,ko;q=0.8",
#                     "bj-guid": "a26c902c-79d0-44e5-a3b2-edf3ecb8beba",
#                     "content-type": "application/json;charset=UTF-8",
#                 },
#                 referrer: "http://qd.ieprint.cc/",
#                 referrerPolicy: "no-referrer-when-downgrade",
#                 body:
#                     '{"BuJians":[{"MingCheng":"","BuJianFenLei":{"DanZhang":false,"XiaoBaoZhuang":true,"LiBaoDuiLian":false,"LiBaoHengPi":false,"LiBaoFuZi":false,"LiBaoHongBao":false,"LiBao":false,"DuiLian":false,"DuiLianHengpi":false,"DuiLianFuZi":false,"FuZi":false,"GuaLiNeiYe":false,"TaiLiNeiYe":false,"TaiLiGongYeBan":false,"TaiLiWaiBiaoZhi":false,"TailiNeiBiaoZhi":false,"MingPian":false,"CaiHe":false,"DangAnDai":false,"DiaoPai":false,"XinFeng":false,"BaoZhi":false,"BianQian":false,"FengTao":false,"BuGanJiao":false,"ShouTiDai":false,"HuaCeFengPi":false,"HuaCeNeiYe":false,"HuaCeFeiYe":false,"HuaCeLaYe":false},"ZhengMianColor":{"ZhuanSe":7},"FanMianColor":{"ZhuanSe":0},"ZhiZhang":{"LeiXing":16,"KeZhong":116},"Width":{"Value":0},"Height":{"Value":0},"ZiDaiZhi":false,"HouGongCanShu":[],"ShuangDaMianXiangTong":false,"ShuangCeMianXiangTong":false,"HouGong":{"YaHen":{"YaHenZhe":"","Enable":false,"JiDaoHen":1},"YiSiXian":{"JiTiaoXian":1,"Enable":false},"DanMianJiTu":{"Enable":false,"Width":"","Height":""},"DanMianTangJin":{"Enable":false,"Width":"","Height":""},"DanMianTangYin":{"Enable":false,"Width":"","Height":""},"FuMo":{"ShuangMianFuMo":"false","FuMoZhongLei":"","Enable":false},"MoQie":{"Enable":true,"MoQieZhongLei":"小包装"},"YaWen":{"Enable":false,"ShuangMianYaWen":false},"JuBuUV":{"Enable":false,"ShuangMian":"单面","UVCaiLiao":"","Width":"","Height":""},"KaiTianChuang":{"Enable":false,"Width":"","Height":""},"GuoYou":{"Enable":false,"ShuangMianGuoYou":"单面","CaiLiao":""},"DaHaoMa":{"Enable":false,"ShuLiang":1},"ZheYe":{"Enable":false,"ZheFa":""},"DaKong":{"Enable":false,"DaKongShuLiang":1},"DanMianGuaGuaYin":{"Enable":false},"HuHe":{"Enable":true,"HeXing":"其他"},"ShouTiSheng":{"Enable":false,"CaiLiao":""},"TiBa":{"Enable":false},"DaMaoDing":{"Enable":false},"JiaoTou":{"Enable":false},"XiaoBaoZhuang":{"CaiLiao":"三层高强度瓦楞板","Enable":true}},"P":1,"PinZhong":1,"ShuLiang":0,"ZhengFangMianNeiRongXiangTong2":false,"ZhengFangMianNeiRongXiangTong3":false,"ZhengFangMianNeiRongXiangTong4":false,"ZhengFangMianNeiRongXiangTong5":false,"ZhengFangMianNeiRongBuTong":false,"JieDiaoKou":false,"SFYinShua":false,"SFXiangTong":false,"MingChen":"小包装"}],"ChanPinFenLei":{"DanZhang":false,"XiaoBaoZhuang":true,"DaLiBao":false,"DuiLian":false,"FuZi":false,"GuaLi":false,"TaiLi":false,"MingPian":false,"CaiHe":false,"DangAnDai":false,"DiaoPai":false,"XinFeng":false,"BaoZhi":false,"BiaoQian":false,"FengTao":false,"BuGanJiao":false,"ShouTiDai":false,"YangBenHuaCe":false,"PVC":false,"WuTanLianDan":false,"DanPinGongSiHeight":"","DanPinGongSiWidth":"","ShuangPinGongSiHeight":"","ShuangPinGongSiWidth":""},"JiaLeiKou":null,"JiaZheDou":null,"JiaLaYe":null,"ZhuangDingFangShi":"骑马钉","ChengPinWidth":350,"ChengPinHeight":260,"ChengPinHou":"320","ZheDouLeiXing":"单折兜","DianBan":false,"QiQiang":0,"ZhanKaiWidth":0,"ZhanKaiHeight":0,"ShuLiang":"1000","PinZhong":1,"MeiBenYeShu":1,"CaiChengPin":true,"ShuangDaMianXiangTong":true,"ShuangCeMianXiangTong":true,"ChuanHuanBian":0,"ChuanHuanYanSe":"","ZhiJiaoHouDu":0,"ZhiJiaWidth":0,"ZhiJiaHeight":0,"SheTou":0,"XinFengYangShi":"","DanPinGongSiHeight":"(长+宽)*2+25","DanPinGongSiWidth":"宽/2+30+高+宽+25","ShuangPinGongSiHeight":"长+宽+25","ShuangPinGongSiWidth":"宽/2+30+高+宽+25"}',
#                 method: "POST",
#                 mode: "cors",
#                 credentials: "omit",
#                 }
#   );

#   const myJson = await response.json(); //extract JSON from the http response
#   // do something with myJson
#   console.log(myJson);
# };
# ')
        # /html/body/div[7]
        # self.ele_facial_paper1 = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/section/main/div/div[1]/div[2]/div/div/form/div[3]/div/div[1]/div/div/input')
        # self.ele_facial_paper1.click()
        # # /html/body/div[3]/div[1]/div[1]/ul/li[4]
        # # /html/body/div[3]/div[1]/div[1]/ul/li[1]
        # /html/body/div[2]/div[1]/div[1]/ul  /html/body/div[6]/div[1]/div[1]/ul/li[3]
        #/html/body/div[7]/div[1]/div[1]/ul/li[1]
        # body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul

        # self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[4]').click()
        # self.ele_facial_paper1.select_by_index(3)
    

        self.quotation = self.driver.find_element(By.XPATH,'//*[@id="xxxl"]/div[1]/div/div[1]/button')
        self.quotation.click()

        # Get Parameters

        # time.sleep(3)
        tk = Tk()
        # tk.selection_clear()
        price_result = []
        result_text = ''
        result = ''
        for numbers in range(5):
            for kinds in range(2):
                try:
                    time.sleep(0.2)
                    tk.selection_clear()
                    xPath = '//*[@id="xxxl"]/div[1]/div/div[2]/table/tr['+str(numbers+2)+']/td['+str(kinds+2)+']/i'
                    element = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, xPath)))
                    # until(EC.presence_of_element_located
                    element.click()
                    print("click get price")
                    # self.driver.find_element_by_xpath(xPath).click()
                    tk.withdraw()
                    while not tk.selection_get(selection="CLIPBOARD"): # or result == tk.selection_get(selection="CLIPBOARD"):
                        time.sleep(0.1)
                    result = tk.selection_get(selection="CLIPBOARD")
                    print('result' + result)
                    if numbers==0 & kinds==0:
                        result_text = result
                    price = analysis_result(result)
                    price_result.insert(numbers*2+kinds, price)
                    print('price'+ str(numbers+1)+'000 : '+ str(kinds) + ' : '+str(price) + ' yuan')
                except:
                    pass
                # sql = "UPDATE getStatus SET run_sta = 'Running' WHERE loanID = '" + loanId + "'"
                # mycursor.execute(sql)
        # sql = "INSERT INTO `results` VALUES ("+str(id)+","+str(id)+","+str(price_result[0])+","+str(price_result[1])+","+str(price_result[2])+","+str(price_result[3])+\
        #             ","+str(price_result[4])+","+str(price_result[5])+","+str(price_result[6])+","+str(price_result[7])+","+str(price_result[8])+\
        #                 ","+str(price_result[9])+",'"+result_text+"',NULL,NULL)"
        # print(sql)
        # mycursor.execute(sql)
        # mydb.commit()

        # sql = "UPDATE packages SET status = 'update' WHERE id = '" + str(id) + "'"
        # print(sql)
        # mycursor.execute(sql)
        # mydb.commit()

    def quit(self, ):
        self.driver.quit()


automation = webcapture(source_path)
while True:
    automation.setParameters(100)

# while True:
    # initialize all task id list
    # mycursor = mydb.cursor()
    # mydb.commit()
    # sql = "SELECT * FROM packages WHERE status = 'progress'"
    # mycursor.execute(sql)
    # records = mycursor.fetchall()
    # del package_ids[:]
    # #Get Ids
    # for x in records:
    #     package_ids.append(x[0])

    # if len(package_ids) > 0:

    #     print('There are  {0} tasks.'.format(len(package_ids)))

    #     for current_id in package_ids:
    #         try:
    #             print(current_id)
    #             automation.setParameters(current_id)
    #         except:
                # sql = "UPDATE packages SET status = 'Error' WHERE id = '"+str(current_id)+"'"
                # mycursor.execute(sql)
                # mydb.commit()
    #             pass
    # else:
    #     time.sleep(0.3)
    
# automation.setParameters()
# automation.getResult()
automation.quit()

