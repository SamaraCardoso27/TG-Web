# -*- coding: utf8 -*-

import sys;
import datetime
from re import compile
reload(sys);
sys.setdefaultencoding("utf8")

global REP_REG_CLEARPOINTS
REP_REG_CLEARPOINTS = compile(r"[\.\s\_-]")

global REP_REG_PHONE
REP_REG_PHONE = compile(r"[\.\s\_\(\)-]")

global REP_REG_CLEARALL
REP_REG_CLEARALL = compile(r"[\.\s\_\(\)\:/-]")


def clearPointsString(wString):
    if wString=='':
        return ''
    if wString=='None' or wString==None:
        return ''
    return REP_REG_CLEARPOINTS.sub('',wString)

def format_date(date_nasc, last_update):
    date = ''
    date_upd = ''
    if str(date_nasc) != 'None' or str(date_nasc) != '':
        date_list = date_nasc.split(" ")
        if len(date_list) > 1:
            date_list = date_list[0]
        else:
            date_list = date_list[0]
        date_list = date_list.split("/")
        date = datetime.datetime(int(date_list[2]), int(date_list[1]), int(date_list[0]))
    if str(last_update) != 'None' or str(last_update) != '':
        date_list = last_update.split(" ")
        if len(date_list) > 1:
            date_list = date_list[0]
        else:
            date_list = date_list[0]
        date_list = date_list.split("/")
        date_upd = datetime.datetime(int(date_list[2]), int(date_list[1]), int(date_list[0]))
    return (date, date_upd)

def sanatizeItem(wItem):
    """
        Avoid None type, none string and undefined
        to be pass through
    """
    if wItem==None:         return ''
    if wItem=='None':       return ''
    if wItem=='undefined':  return ''
    if type(wItem)==str:
        # clean left and right space, enters and tabs
        return wItem.strip(' \t\n\r')
    return wItem

def formatDateToDB(wDate,wToDB=True):
    """
        Get data into the format dd/mm/yyyy
        to yyyy-mm-dd or backward
    """
    if wToDB:
        part = wDate.split('/')
        if len(part)!=3:
            return ''
        return part[2]+'-'+part[1]+'-'+part[0]
    else:
        part = wDate.split('-')
        if len(part)!=3:
            return ''
        return part[2]+'/'+part[1]+'/'+part[0]