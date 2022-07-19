#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Bibliotecas:
from selenium.webdriver.chrome.options import Options
from datetime import timedelta, datetime, date
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver import chrome
from selenium import webdriver

import time as pytm


def captura_data_e_horario():
    # Data:
    data = date.today();
    data = data.strftime('%d/%m/%Y');
    dia_da_semana = datetime.today().weekday();

    # Horário:
    hora = datetime.now().hour;
    minuto = datetime.now().minute;
    segundo = datetime.now().second

    return data, hora, minuto, segundo, dia_da_semana

def bater_ponto():
    # Opções do navegador - visibilidade e tamanho:
    chrome_options = Options();

    # chrome_options.add_argument("--headless");
    chrome_options.add_argument("--window-size=1920x1080");

    # Acessando o navegador:
    navegador = webdriver.Chrome(options = chrome_options);

    # Acessando página de login:
    pytm.sleep(1);
    navegador.get('http://webponto.norber.com.br/webpontoindra/');

    # Selecionando Empresa
    pytm.sleep(1);
    navegador.find_element(by = By.XPATH, value = '/html/body/form/div[3]/div/div[1]/div[2]/input').send_keys('2');

    # Digitando Usuàrio
    pytm.sleep(1);
    navegador.find_element(by = By.XPATH, value = '/html/body/form/div[3]/div/div[2]/div[2]/input').send_keys('857537');

    # Digitando Senha
    pytm.sleep(1);
    navegador.find_element(by = By.XPATH, value = '/html/body/form/div[3]/div/div[3]/div[2]/input[1]').send_keys('Chinixy123');

    # Clicando em OK
    pytm.sleep(1);
    navegador.find_element(by = By.XPATH, value = '/html/body/form/div[3]/div/div[3]/div[2]/input[2]').click();

    # Acessando página de login:
    pytm.sleep(5);
    navegador.get('https://webponto.norber.com.br/webpontoindra/just_user/IncluirMarcacaoOnLine.asp');

    # Clicando em OK
    pytm.sleep(1); 
    navegador.find_element(by = By.XPATH, value = '/html/body/form/table[2]/tbody/tr[11]/td/input[1]').click();

    # Fechar navegador
    pytm.sleep(10);
    navegador.close();

    pytm.sleep (62);

while True:
    
    data, hora, minuto, segundo, dia_da_semana = captura_data_e_horario();
    
    pytm.sleep(20);
    
    if (dia_da_semana == 0 or dia_da_semana == 1 or dia_da_semana == 2 or dia_da_semana == 3):
        if (hora==8 and minuto ==0) or (hora==12 and minuto ==0) or (hora==13 and minuto ==0) or (hora==18 and minuto ==0):
            bater_ponto();
    else:
        if (dia_da_semana == 4):
            if (hora==8 and minuto ==0) or (hora==12 and minuto ==0) or (hora==14 and minuto ==0) or (hora==18 and minuto ==0):
                bater_ponto();


# In[ ]:




