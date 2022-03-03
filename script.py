# python modulespip
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from PyPDF2 import PdfFileMerger
import glob
import os, time, shutil
# import mysql.connector
import time, threading


#loanId = input('Enter your Loan Number : ')
source_path = os.getcwd()
emailID = 'nkowarsky@emortgagecapital.com'
password = 'Newport14000!'


#====== MySQL connector =====

# Ease Automation Class
class easeAutomation():
    def __init__(self, path):
        self.loanid = ''
        self.source_path = path
        self.noDownload = False
        try:
            os.mkdir('pdfs')
        except:
            pass
        
        try:
            os.mkdir('merge-pdf')
        except:
            pass
        options = Options()
        prefs = {"download.default_directory" : r'{0}\pdfs'.format(path), "plugins.always_open_pdf_externally":True}
        options.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(executable_path='{0}/chromedriver/chromedriver.exe'.format(self.source_path), options=options)
        self.driver.get("http://ease.uwm.com/")
        self.driver.maximize_window()

    def login(self, emailID, password):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'userNameInput'))).send_keys(emailID)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'passwordInput'))).send_keys(password)
        self.driver.find_element(By.ID, 'submitButton').click()
        print('Sucessfully Logged In.')

    def search(self, loanId, searchList):
        self.loanid = loanId
        sql = "UPDATE getStatus SET run_sta = 'Running' WHERE loanID = '" + loanId + "'"
        mycursor.execute(sql)
        self.driver.get('https://ease.uwm.com/Lending/Origination/PipeLine')
        if os.system(r'mkdir {0}\pdfs\{1}'.format(self.source_path ,loanId)):
            print('{0} Folder Found.'.format(loanId))
            ans = input('It may overwrite exiting pdf files, Would you still like to download pdf files : (y/n) ')
            if ans == 'y':
                pass
            else:
                raise
        else:
            print('{0} Folder created.'.format(loanId))
        
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'SearchCriteria'))).send_keys(loanId)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'btnSearchCriteria'))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'loan-number'))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'documentManager'))).click()
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'hintViewDocs'))).click()
        for i in searchList:
            time.sleep(2)
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'attached-documents-search'))).send_keys(i)
            time.sleep(3)
            try:
                self.driver.find_element(By.CLASS_NAME, 'dataTables_empty')
            except:
                self.downloadClick()
                self.noDownload = True
                time.sleep(3)
                try:
                    self.driver.find_element(By.XPATH, '//a[@id="document-table_next" and contains(@class,"disabled")]')
                except:
                    self.driver.find_element(By.XPATH, '//a[@id="document-table_next"]').click()
                    time.sleep(3)
                    self.downloadClick()
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'attached-documents-search'))).clear()

    def downloadClick(self, ):
        tmp = 1
        for link in self.driver.find_elements(By.XPATH, '//table/tbody/tr'):
                link.find_element_by_xpath('td/a').click()
                while True:
                    if os.path.isfile('pdfs/GetDocument.pdf'):
                        fileName=str(link.find_element_by_xpath('td[2]').get_attribute('title'))
                        shutil.move('pdfs/GetDocument.pdf', 'pdfs/{0}/{1}_{2}.pdf'.format(self.loanid, fileName, tmp))
                        tmp+=1
                        break
                    else:
                        time.sleep(2)

    def mergePDF(self, ):
        try:
            pdfs = glob.glob('pdfs/{0}/*.pdf'.format(self.loanid))
            merger = PdfFileMerger()
            for pdf in pdfs:
                merger.append(pdf)
            merger.write("merge-pdf/{0}.pdf".format(self.loanid))
            merger.close()
            time.sleep(5)
            print('{0} Files Merged Successfully.'.format(self.loanid))
            sql = "UPDATE getStatus SET run_sta = 'Done' WHERE loanID = '" + loanId + "'"
            mycursor.execute(sql)
            self.noDownload = False

        except:
            sql = "UPDATE getStatus SET run_sta = 'Error' WHERE loanID = '" + loanId + "'"
            mycursor.execute(sql)
            print('Error in merging the pdfs of {0} loan id.'.format(self.loanid))

    def quit(self, ):
        self.driver.quit()


# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="py_PHP"
# )

# mycursor = mydb.cursor()

loanIndex = 0
loanIDlist = list()
loanIDlist_tmp = list()

# sql = "SELECT loanID FROM getStatus WHERE run_sta = 'Queued'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()

for x in myresult:
    loanIDlist.append(x[0])
# del oanIDlist_tmp[:]


# def foo():
#     threading.Timer(WAIT_SECONDS, foo).start()
#     del loanIDlist_tmp[:]
    
# foo()  

# with open('{0}/Loan Ids.txt'.format(source_path)) as key:
#     while True:
#         line = key.readline()
#         if line == '':
#             break
#         loanIDlist.append(line.strip())
  





keywords = list()
with open('{0}/Search Keywords.txt'.format(source_path)) as key:
    while True:
        line = key.readline()
        if line == '':
            break
        keywords.append(line)

# # Initializing telegramAutomation class object.

start_automation = easeAutomation(source_path)
start_automation.login(emailID, password)
for loanIds in loanIDlist:
    # print('Loan ID : {0}'.format(loanIds))
    try:
        print(loanIds)

        start_automation.search(loanIds, keywords)
        if start_automation.noDownload:
            start_automation.mergePDF()
        else:
            print('No Pdf files found.')


        # sql = "SELECT loanID FROM getStatus WHERE run_sta = 'Queued'"
        # mycursor.execute(sql)
        # myresult = mycursor.fetchall()
        # del loanIDlist[:]
        # for x in myresult:
        #     loanIDlist.append(x[0])
        

    # except:
    #     sql = "UPDATE getStatus SET run_sta = 'Error' WHERE loanID = '" + loanId + "'"
    #     mycursor.execute(sql)
    #     pass
start_automation.quit()
