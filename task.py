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

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="",
  database="package"
)

mycursor = mydb.cursor()

package_ids = list()

sql = "SELECT * FROM packages WHERE status = 'progress'"
mycursor.execute(sql)
records = mycursor.fetchall()
#Get Ids
for x in records:
    package_ids.append(x[0])

def analysis_result(full_text):
    price = full_text.split()[-1]
    return re.findall(r'\d+', price)[0] 



class webcapture():
    def __init__(self, path):
        self.source_path = path
        # options = Options()
        # prefs = {"download.default_directory" : r'{0}\pdfs'.format(path), "plugins.always_open_pdf_externally":True}
        # options.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(executable_path='{0}/chromedriver/chromedriver.exe'.format(self.source_path))#, options=options)
        self.driver.maximize_window() 
        self.driver.implicitly_wait(10)
        self.driver.get("http://qd.ieprint.cc/#/waleng")
        time.sleep(3)
         
        
    def setParameters(self, c_id):
        self.c_id = c_id
        sql = "UPDATE packages SET status = 'Running' WHERE id = '"+str(c_id)+"'"
        mycursor.execute(sql)
        mydb.commit()

        sql = "SELECT * FROM packages WHERE id = '"+str(c_id)+"'"
        mycursor.execute(sql)
        records = mycursor.fetchall()

        for row in records:
            id = row[0]
            package_type = row[1]
            product_size1 = row[2]
            product_size2 = row[3]
            product_size3 = row[4]
            print_quantity1 = row[5]
            print_quantity2 = row[6]
            # facial_paper1 = row[7]
            # facial_paper2 = row[8]
            if (package_type == '上盖下插底盒'):
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/section/main/div/div[1]/div[1]/div/div/div[1]').click()
            elif (package_type == '手提箱'):
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/section/main/div/div[1]/div[1]/div/div/div[2]').click()
            elif(package_type == '提拔盒'):
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/section/main/div/div[1]/div[1]/div/div/div[3]').click()
            else:
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

            time.sleep(3)
            tk = Tk()
            # tk.selection_clear()
            price_result = []
            result_text = ''
            result = ''
            for numbers in range(5):
                for kinds in range(2):
                    time.sleep(0.2)
                    tk.selection_clear()
                    xPath = '//*[@id="xxxl"]/div[1]/div/div[2]/table/tr['+str(numbers+2)+']/td['+str(kinds+2)+']/i'
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xPath)))
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
                    # sql = "UPDATE getStatus SET run_sta = 'Running' WHERE loanID = '" + loanId + "'"
                    # mycursor.execute(sql)
            sql = "INSERT INTO `results` VALUES ("+str(id)+","+str(id)+","+str(price_result[0])+","+str(price_result[1])+","+str(price_result[2])+","+str(price_result[3])+\
                        ","+str(price_result[4])+","+str(price_result[5])+","+str(price_result[6])+","+str(price_result[7])+","+str(price_result[8])+\
                            ","+str(price_result[9])+",'"+result_text+"',NULL,NULL)"
            print(sql)
            mycursor.execute(sql)
            mydb.commit()

            sql = "UPDATE packages SET status = 'update' WHERE id = '" + str(id) + "'"
            print(sql)
            mycursor.execute(sql)
            mydb.commit()

    def quit(self, ):
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
    #Get Ids
    for x in records:
        package_ids.append(x[0])

    if len(package_ids) > 0:

        print('There are  {0} tasks.'.format(len(package_ids)))

        for current_id in package_ids:
            try:
                print(current_id)
                automation.setParameters(current_id)
            except:
                sql = "UPDATE packages SET status = 'Error' WHERE id = '"+str(current_id)+"'"
                mycursor.execute(sql)
                mydb.commit()
                pass
    else:
        time.sleep(0.3)
    
# automation.setParameters()
# automation.getResult()
automation.quit()

