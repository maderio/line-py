from linepy import *
from akad.ttypes import *
from datetime import datetime
import traceback, os, sys, threading, time, json, codecs, pytz, requests, re

bot = LINE()

""" -*- # -*- """
botPoll = OEPoll(bot)

""" Def Bots """
def logError(text):
    bot.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Makassar")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("errorLog.txt","a") as error:
        error.write("\n[{}] {}".format(str(time), text))
def speed(to):start = time.time();bot.sendMessage("u00e974dabebecab357175d08d6d4ec77", "-");elapsed_time = time.time() - start;bot.sendMessage(to, "Speed : %s second"%str(round(elapsed_time)))
def SCode(op):
    try:
        if op.type == 0:return
        if op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != bot.profile.mid:
                            to = sender
                        else:
                            to = msg.to
                    elif msg.toType == 1:
                        to = msg.to
                    elif msg.toType == 2:
                        to = msg.to
                    if msg.contentType == 0:
                        if text.lower() == "speed":speed(to)
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
        saveData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

def run():
    while True:
        ops = botPoll.singleTrace(count=50)
        if ops != None:
            for op in ops:
                try:SCode(op))
                except Exception as error:logError(error)
                botPoll.setRevision(op.revision)

if __name__ == '__main__':
    run()