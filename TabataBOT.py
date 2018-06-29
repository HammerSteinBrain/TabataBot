import telepot
from telepot.namedtuple import ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from random import *
import sys
import os

#-----------------------instancia inicial do bot
bot = telepot.Bot("537641293:AAElQXZ0B_T1X3JXnsspop_Qq5xL_eSwwGE")

#-----------------------funcao para reiniciar o codigo
def restart_program():
    os.system
    #sys.exit(0)
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
#-----------------limpando mensagens antigas do cache
updates = bot.getUpdates()

if updates:
    last_update_id = updates[-1]['update_id']
    bot.getUpdates(offset=last_update_id+1)
    
#-----------------------variaveis globais-------------------------------------------------
w = True
linha_escolhida = 0

#-----------------------enviando msg com botões o/ ---------------------------------------
bot.sendMessage(382662102,"Olá, eu sou a Tabata bot =)")
bot.sendMessage(382662102,"Trabalho para a secretaria de transportes"
                " do municio de Caçapava-SP...")

bot.sendMessage(382662102,"E eu odeio meu trabalho...ops, como posso te ajudar?",
    reply_markup=InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text="Horario da linha de onibus", callback_data='01')],
    [InlineKeyboardButton(text="Etinerario da linha de onibus", callback_data='02')],
    [InlineKeyboardButton(text="Reiniciar...", callback_data='03')],
    [InlineKeyboardButton(text="Sair...", callback_data='04')]
    ]))
bot.sendMessage(382662102,"E não ouse me deixar no vacuo Ò.ó' ")

#-----------------------recebendo msg // interações--------------------------------------------------------
def recebendoMsg(msg):
    global linha_escolhida
    #print(msg["text"])

    if('text' in msg):
        #----------------levantamento de exceções----------------------------------------------------------
        bot.sendMessage(382662102,"Argh, não é para digitar, apenas selecione as opções acima!")
        #------------tratamento das exceções---------------------------------------------------------------
        bot.sendMessage(382662102,"Reiniciando...")
        restart_program()
    else:
        print(msg["data"])

        #--------------------------reiniciar/desligar o programa remotamente-------------------------------
        
        if(msg["data"]=="03"):
            bot.sendMessage(382662102,"Reiniciando...")
            restart_program()
            
        if(msg["data"]== "04"):
            bot.sendMessage(382662102,"Desligando a Tabata Bot...")
            global w
            w = False
            sys.exit(0)
            
        #-----------------------------------------ESCOLHA DOS HORARIOS--------------------------------------
            
        # tabela de codigo de 01 até 04 opções de sistema
        
        # de 1 até 21 numero das linhas de onibus
        
        if((msg["data"]=="01")):
            bot.sendMessage(382662102,"Certo, você escolheu...Horario dos onibus")
            bot.sendMessage(382662102,"E qual linha de onibus você deseja? Escolha abaixo:",
                reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                [InlineKeyboardButton(text="Linha 7: Bairro do sapé x Tataúba", callback_data='7')],
                [InlineKeyboardButton(text="Linha 8: Tijuco Preto x Panorama (via Mantiqueira)", callback_data='8')],
                [InlineKeyboardButton(text="Linha 9: Nova Caçapava x Iriguassu 2", callback_data='9')],
                [InlineKeyboardButton(text="Linha 10: Caçapava x Eugenio de Mello(FATEC)", callback_data='10')]
                ]))
            bot.sendMessage(382662102,"------------------------------------------------------")
            
        if(msg["data"]=='10'): # LINHA SELECIONADA 10 = EUGENIO DE MELO
            bot.sendMessage(382662102,"EUGENIO DE MELO")
            bot.sendMessage(382662102,"E qual periodo da semana você deseja?",
                reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                [InlineKeyboardButton(text="DIAS ÚTEIS", callback_data='uteis')],
                [InlineKeyboardButton(text="SÁBADOS", callback_data='sab')],
                [InlineKeyboardButton(text="DOMINGOS E FERIADOS", callback_data='dom')]
                ]))
            bot.sendMessage(382662102,"------------------------------------------------------")
            linha_escolhida = 10 # LINHA SELECIONADA 10 = EUGENIO DE MELO
            

        if(msg["data"]=='7'): # LINHA SELECIONADA 7 = Bairro do sapé x Tataúba
            bot.sendMessage(382662102,"Bairro do sapé x Tataúba")
            bot.sendMessage(382662102,"E qual periodo da semana você deseja?",
                reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                [InlineKeyboardButton(text="DIAS ÚTEIS", callback_data='uteis')],
                [InlineKeyboardButton(text="SÁBADOS", callback_data='sab')],
                [InlineKeyboardButton(text="DOMINGOS E FERIADOS", callback_data='dom')]
                ]))
            bot.sendMessage(382662102,"------------------------------------------------------")
            linha_escolhida = 7 # LINHA SELECIONADA 10 = Bairro do sapé x Tataúba

        #-----------------------------ESCOLHA DOS DIAS DA SEMANA----------------------------------------------

        #------------------------------horarios conforme dia util - linha 7 <<<<<<<<<<<<<<<<<<<<<< 7
        if(msg["data"] == 'uteis' and linha_escolhida == 7):
                bot.sendMessage(382662102,">>>>>>>>DIAS ÚTEIS<<<<<<<")
                bot.sendMessage(382662102,"06:40")
                bot.sendMessage(382662102,"07:10 (ATÉ RODOVIÁRIA)")        
                bot.sendMessage(382662102,"07:30 (SAI DA RODOVIÁRIA)")
                bot.sendMessage(382662102,"08:30")
                bot.sendMessage(382662102,"09:30")
                bot.sendMessage(382662102,"10:30")
                bot.sendMessage(382662102,"11:30 (VIA PINHEIRINHO)")        
                bot.sendMessage(382662102,"12:30 (VIA FREI SÉRGIO,APAE)")
                bot.sendMessage(382662102,"13:30")
                bot.sendMessage(382662102,"14:30")
                bot.sendMessage(382662102,"15:30")
                bot.sendMessage(382662102,"16:30 (VIA FREI SÉRGIO)")
                bot.sendMessage(382662102,"17:30")
                bot.sendMessage(382662102,"18:30 (VIA FREI SÉRGIO,PINHEIRINHO)")
                bot.sendMessage(382662102,"20:00 (VIA BOA VISTA)")
                bot.sendMessage(382662102,"21:40")
                bot.sendMessage(382662102,"22:50")
                bot.sendMessage(382662102,"23:10 (ATÉ RODOVIÁRIA)")
                
        if(msg["data"] == 'sab' and linha_escolhida == 7):
                bot.sendMessage(382662102,">>>>>>>>>SABADO<<<<<<<<")
                bot.sendMessage(382662102,"05:50 (VIA FREI SÉRGIO/PINHEIRINHO)")
                bot.sendMessage(382662102,"06:50")        
                bot.sendMessage(382662102,"07:30")
                bot.sendMessage(382662102,"08:30")
                bot.sendMessage(382662102,"09:30")
                bot.sendMessage(382662102,"10:30")
                bot.sendMessage(382662102,"11:30 (VIA PINHEIRINHO)")        
                bot.sendMessage(382662102,"12:30")
                bot.sendMessage(382662102,"13:30")
                bot.sendMessage(382662102,"14:30")
                bot.sendMessage(382662102,"16:30 (VIA FREI SÉRGIO)")
                bot.sendMessage(382662102,"18:30 (VIA FREI SÉRGIO,PINHEIRINHO)")
                bot.sendMessage(382662102,"20:30 (VIA BOA VISTA)")
                bot.sendMessage(382662102,"22:25 (VIA BOA VISTA/FORNOVO)")
                
        if(msg["data"] == 'dom' and linha_escolhida == 7):
                bot.sendMessage(382662102,">>>>>>>>DOMINGOS E FERIADOS<<<<<<<<")
                bot.sendMessage(382662102,"07:00")
                bot.sendMessage(382662102,"09:00")        
                bot.sendMessage(382662102,"11:00 (FREI SÉRGIO,ALDEIAS DA SERRA)")
                bot.sendMessage(382662102,"13:00 (VIA ALDEIAS)")
                bot.sendMessage(382662102,"15:00")
                bot.sendMessage(382662102,"17:00 (FREI SÉRGIO)")
                bot.sendMessage(382662102,"19:00")        
                bot.sendMessage(382662102,"21:00 (FREI SÉRGIO)")


        #------------------------------horarios conforme dia util - linha 10 <<<<<<<<<<<<<<<<<<<<<<<< 10
        if(msg["data"] == 'uteis' and linha_escolhida == 10):
                bot.sendMessage(382662102,">>>>>>>>DIAS ÚTEIS<<<<<<<")
                bot.sendMessage(382662102,"07:00 (VIA ESTRAVA VELHA, FATEC)")
                bot.sendMessage(382662102,"08:10 (VIA ESTRADA VELHA)")        
                bot.sendMessage(382662102,"09:50 (VIA ESTRADA VELHA)")
                bot.sendMessage(382662102,"11:30 (VIA ESTRADA VELHA)")
                bot.sendMessage(382662102,"13:00 (ESTRADA VELHA / FATEC)")
                bot.sendMessage(382662102,"16:25 (VIA ESTRADA VELHA)")
                bot.sendMessage(382662102,"17:30 (ESTRADA VELHA/FATEC)")        
                bot.sendMessage(382662102,"18:30 (VIA ESTRADA VELHA)")
                bot.sendMessage(382662102,"19:30 (VIA ESTRADA VELHA)")
                bot.sendMessage(382662102,"21:30 (VIA ESTRADA VELHA)")
                bot.sendMessage(382662102,"23:00 (VIA ESTRADA VELHA,FATEC)")
        if(msg["data"] == 'sab' and linha_escolhida == 10):
                bot.sendMessage(382662102,">>>>>>>>>SABADO<<<<<<<<")
                bot.sendMessage(382662102,"05:55 (VIA ESTRADA VELHA)")
                bot.sendMessage(382662102,"07:00 (VIA ESTRADA VELHA)")        
                bot.sendMessage(382662102,"08:00 (VIA ESTRADA VELHA)")
                bot.sendMessage(382662102,"10:00 (VIA ESTRADA VELHA)")
                bot.sendMessage(382662102,"11:30 (VIA ESTRADA VELHA)")
                bot.sendMessage(382662102,"12:50 (VIA ESTRADA VELHA)")
                bot.sendMessage(382662102,"14:00 (VIA VILA GALVÃO)")        
                bot.sendMessage(382662102,"16:00 (VIA VILA GALVÃO)")
                bot.sendMessage(382662102,"18:00 (VIA VILA GALVÃO)")
                bot.sendMessage(382662102,"20:00 (VIA VILA GALVÃO)")
        if(msg["data"] == 'dom' and linha_escolhida == 10):
                bot.sendMessage(382662102,">>>>>>>>DOMINGOS E FERIADOS<<<<<<<<")
                bot.sendMessage(382662102,"06:30 (VIA VILA GALVÃO")
                bot.sendMessage(382662102,"12:30 (VIA VILA GALVÃO")        
                bot.sendMessage(382662102,"18:30 (VIA VILA GALVÃO")

        

#-------------------------------------ouvindo mensagens
bot.message_loop(recebendoMsg)

#------------------------------------------------------

#id chat 382662102

while w == True:
    pass
