'''Code ini bersumber dari website 
https://realpython.com/python-send-email/#sending-multiple-personalized-emails
'''

import csv, smtplib, ssl # Mengimport modul csv, smtplib, dan ssl 
import getpass # Mengimport modul untuk menghilangkan tampilan password di layar 

message = """Subject: Basic Python Final Project 

Hi {name},

Ini adalah final project dari Indonesia AI
"""
from_address = "vansci1310@gmail.com" # Email yang digunakan untuk mengirim 
password = getpass.getpass(prompt="Masukkan Password Anda : ", stream=None) # Input nilai password 

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server: # Server yang digunakan menggunakan SMTP
    server.login(from_address, password)
    with open("test.csv") as file: # Membuka file format .csv pada 1 folder yang sama 
        reader = csv.reader(file) 
        for name, email in reader: # Loop nama dan email pada file .csv
            server.sendmail(
                from_address,
                email,
                message.format(name=name),
            )
            print(f'Email sudah terkirim ke : {name}')

