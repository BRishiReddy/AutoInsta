from tkinter import *
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import warnings

warnings.filterwarnings('ignore')


tk=Tk()

tk.title('Instabot')
tk.geometry('500x300')


class college:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def prints(self):
        label3.config(text='Sender username is: '+self.name,)
        label4.config(text='Sender password is: '+str(self.age))

def display():
    a=name.get()
    b=password.get()
    c=college(a,b)
    c.prints()


name=StringVar()
label1=Label(tk,text='Enter the senders username: ')
label1.pack()

entry1=Entry(tk,textvariable=name)
entry1.pack()

password=StringVar()
label2=Label(tk,text='Enter the senders password: ')
label2.pack()

entry2=Entry(tk,textvariable=password,show='*')
entry2.pack()


start_button=Button(command=display,text='Display Details')
start_button.pack()

ruser=StringVar()

label5=Label(tk,text='Enter the receivers username: ')
label5.pack()

entry3=Entry(tk,textvariable=ruser)
entry3.pack()

message=StringVar()

label6=Label(tk,text='Enter the message you want to send: ')
label6.pack()

entry4=Entry(tk,textvariable=message)
entry4.pack()

label3=Label(tk)
label3.pack()

label4=Label(tk)
label4.pack()


class bot:
    def __init__(self, username, password, user, message):
        self.username = username
        self.password = password
        self.user = user
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        self.bot =webdriver.Chrome(ChromeDriverManager().install())
        self.login()

    def login(self):
        self.bot.get(self.base_url)
        l=[str(item) for item in self.user.split()]
        enter_username = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)

        # first pop-up
        self.bot.find_element_by_xpath(
            '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()
        time.sleep(3)

        # 2nd pop-up
        self.bot.find_element_by_xpath(
            '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
        time.sleep(4)

        # direct button
        self.bot.find_element_by_xpath(
            '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/a/div/div[1]').click()
        time.sleep(3)

        # clicks on pencil icon
        self.bot.find_element_by_xpath(
            '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[1]/div/div[3]/button').click()
        time.sleep(2)
        for i in l:

            # enter the username
            self.bot.find_element_by_xpath(
                '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
            time.sleep(2)

            # click on the username
            self.bot.find_element_by_xpath(
                '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)

            # next button
            self.bot.find_element_by_xpath(
                '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button').click()
            time.sleep(4)

            # click on message area
            send =self.bot.find_element_by_xpath(
                '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

            # types message
            send.send_keys(self.message)
            time.sleep(1)

            # send message
            send.send_keys(Keys.RETURN)
            time.sleep(2)

        self.bot.quit()
        label7.config(text='Message successfully sent')


def bro():
    try:
        b=bot(name.get(),password.get(), ruser.get(), message.get())
        b.login()
    except:
        print()

ibot=Button(command=bro,text='SpiceItUp')
ibot.pack() 

label7=Label(tk)
label7.pack()

tk.mainloop()
