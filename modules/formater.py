# -*- coding: utf8 -*-

"""
    Used to format some data to output
"""

import datetime
import constants
from hashlib import md5
import re
"""
    Define the month of the year to replace it from date
"""
MonthOfTheYear = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

"""
    Define the searchs type
"""
SearchTypes = { "1" : "RA", "2" : "Nome", "3" : "RG",  "4" : "CPF", "5" : "Data de Nascimento", "6" : "Filiação", "7" : "Código", "8" : "ID"}

def convertNumberForDay(wNumber):
    """
        Get a string number list and convert for day of week
        @param wNumber The input list
        @return A string with the week day
    """
    if ("None" in wNumber) or (wNumber==""):
        return ""
    return ((wNumber.replace('',',').replace('1',' Seg').replace('2',' Ter').replace('3',' Qua').replace('4',' Qui').replace('5',' Sex').replace('6',' Sab'))[1:])[:-1]

def formatCPF(wCPF):
    """
        Get the CPF string and convert it to Convetional CPF data
        @param wCPF The current cpf
        @return The processed CPF
    """
    if wCPF==None:
        return ''
    if len(wCPF) == 11:
        wCPF = wCPF[:3]+'.'+wCPF[3:]
        wCPF = wCPF[:7]+'.'+wCPF[7:]
        return wCPF[:11]+'-'+wCPF[11:]
    else:
        if wCPF == 'None' or wCPF == None:
            return ''
    return wCPF

def formatRG(wRG):
    """
        Get the RG string and convert it to Convetional RG data
        @param wRG The current RG
        @return The processed RG
    """
    if wRG == 'None' or wRG == None:
        return ''
    if len(wRG) < 7:
        return wRG
    wRG = wRG[:2]+'.'+wRG[2:]
    wRG = wRG[:6]+'.'+wRG[6:]
    if len(wRG) == 11:
        wRG = wRG[:10]+'-'+wRG[10:]
    return wRG

def formatPhone(wPhone):
    """
        Get a phone and return the best presented string
        @param wPhone The 
    """
    if wPhone=='None' or wPhone==None or wPhone=='':
        return ''
    l_phone = len(wPhone)
    wPhone = re.sub(r'[ +()-]','',wPhone,flags = re.MULTILINE)
    
    if  l_phone<8:
        return wPhone
    if l_phone>=11:
        return '({0}) {1}-{2}'.format(wPhone[:2],wPhone[2:7],wPhone[7:])
    if l_phone>=10:
        return '({0}) {1}-{2}'.format(wPhone[:2],wPhone[2:6],wPhone[6:])
    if l_phone>=9:
        return '{0}-{1}'.format(wPhone[:5],wPhone[5:])
    if l_phone>=8:
        return '{0}-{1}'.format(wPhone[:4],wPhone[4:])
    return wPhone

def getDataOnly(wDateTime):
    """
        Get a date time string and convert it to Date only
        @param wDateTime The input date time
        @return The processed date or nothing
    """
    if type(wDateTime) == datetime.datetime:
        return wDateTime.strftime("%d/%m/%Y")
    elif wDateTime == 'None' or wDateTime == None:
        return ''
    return wDateTime

def getFixDate(wDateTime):
    """
        Get a date time string and convert the Date only
        @param wDateTime The input date time
        @return The processed date as string
    """
    if type(wDateTime) == datetime.datetime:
        return wDateTime.strftime("%d/%m/%Y %H:%M:%S")
    elif wDateTime == 'None' or wDateTime == None:
        return ''
    return wDateTime

def getDataFromTable(wRows,wTable,wFieldRet,wFieldComp,wCompare):
    """
        Get a database row and search for some field inside
        @param wDateTime The input date time
        @return The desired field
    """
    try:
        for item in wRows:
            if item[wTable][wFieldComp] == wCompare:
                return item[wTable][wFieldRet]
    except:
        return ''

def getTypeSearchByCode(wCode, wOld = None):
    """
        Get the search name by the code
        @param wCode The code to search in the dictionary
        return The text of the search
    """
    if wCode == None or wCode == '':
        return None
    try:
        if wCode=='8':
            return wOld
        return SearchTypes[wCode]
    except:
        return ''


def getUsableAddress(wAddress, wNumber, wNeigh, wCity):
    """
        Process the address to get it fixed to presentation and 
        google searchs
        @param wAddress The street name
        @param wNumber The number in the street
        @param wNeigh The neighborhood of the street
        @param wCity The Address city
        @return The process address
    """
    ret = ''
    if wNumber==None:
        wNumber = ''  
    if wAddress==None:
        wAddress = ''
    else:
        ret+=wAddress
        if wNumber!= '':
            ret+=', N° '+str(wNumber)
    if wNeigh==None:
        wNeigh = ''
    else:
        if ret!= '':
            ret+=' - '+wNeigh
        else:
            ret=wNeigh
    valid_address = ret
    if wCity==None:
        wCity = ''
    else:
        if ret!= '':
            ret+=', '+wCity
        else:
            ret=wCity
    return ret,valid_address

def decodeDict(wData, wCoding):
    """
        Run the decoding into a dictionary from 
        @param wData The current dictionary
        @param wCoding The current coding that shall be converted
        @return The new dictionary
    """
    rv = {}
    for key, value in wData.iteritems():
        if isinstance(key, unicode):
            key = key.encode(wCoding)
        if isinstance(value, unicode):
            value = value.encode(wCoding)
        elif isinstance(value, list):
            value = decodeDict(value,wCoding)
        elif isinstance(value, dict):
            value = decodeDict(value,wCoding)
        rv[key] = value
    return rv

def clearPhoneString(wPhone):
    """
        Remove some parts of the phone as string
        @param wPhone The phone data
        @return The phone string clears
    """
    if wPhone=='':
        return ''
    if wPhone=='None' or wPhone==None:
        return ''
    return constants.REP_REG_PHONE.sub('',wPhone)

def clearPointsString(wString):
    """
        Clear parts of string that is not wanted, mostly for numbers
        @param wString The input string, rg, cpf...
        @return The clear string
    """
    if wString=='':
        return ''
    if wString=='None' or wString==None:
        return ''
    return constants.REP_REG_CLEARPOINTS.sub('',wString)

def formatInfo(wPart):
    keys = wPart.keys()
    for item in keys:
        wPart[item] =  str(wPart[item]).strip()
    return wPart

def formatFileSize(wSize):
    """
        Show the file size as text
        @param wSize the enter size
        @return The size converted, the measured value and the combining of those
    """
    if wSize<1024:
        return str(wSize),"Bytes", str(wSize)+" Bytes",
    if wSize<102400:
        wSize = wSize/1024
        return str(wSize),"KB", str(wSize)+" KB",
    else:
        wSize = (wSize/1024)/1000
        return str(wSize),"MB", str(wSize)+" MB",

def buildFileName(wFileName,wVariant = ''):
    """
        Build a new file name to avoid the non-update file because of the name
    """
    pos = len(wFileName)/2-1
    comp = constants.REP_REG_CLEARALL.sub('',str(datetime.datetime.now()))+wVariant
    return wFileName[:pos]+comp+wFileName[pos:]

def exporeError(wParam, wType):
    """
        Present the error message. Building a through parameters
        @param wParam Can be any thing but the error must support it
        @param wType The type of error
    """
    # for all empty field items
    if wType=='custom':
        return wParam
    elif wType=='empty_field':
        return 'O campo '+str(wParam)+' não pode ser vazio!'
    elif wType=='larger_field':
        return 'O campo '+str(wParam[0])+' não pode conter mais de '+str(wParam[1])+' caracteres!'
    elif wType=='search_field':
        return 'A busca '+wParam[0]+' não suporta os caracteres '+wParam[1]+'.'
    elif wType=='search_field_date':
        return 'A busca '+wParam[0]+' não suporta '+wParam[1]+'.'
    elif wType=='larger_field_tag':
        return 'O campo '+str(wParam)+' está muito grande, remova algum conteúdo!';
    elif wType=='quotation_field':
        return 'O campo '+str(wParam)+' não aceita os caracteres \' ou \"!'
    elif wType=='invalid_field':
        return 'O campo '+str(wParam)+' é inválido!'
    elif wType=='number_field':
        return 'O campo '+str(wParam)+' aceita somente n&uacute;meros!'
    elif wType=='duplicated_field':
        return 'Já existe um registro de '+str(wParam[0])+' com '+str(wParam[1])+'!'
    elif wType=='invalid_file_name':
        return 'O nome do arquivo carregado não é válido para o campo '+str(wParam)+'!'
    elif wType=='invalid_file_name_size':
        return 'No campo '+str(wParam[0])+', o tamanho do nome do arquivo deve ser menor que '+str(wParam[1])+' caracteres!'
    elif wType=='file_size':
        return 'No campo '+str(wParam[0])+', o tamanho do arquivo deve estar entre '+str(wParam[1])+' e '+str(wParam[2])+'!'
    elif wType=='invalid_file':
        return 'O tipo de arquivo carregado não é válido para o campo '+str(wParam)+'!'
    elif wType=='invalid_selection':
        return 'Nenhuma opçãoo foi selecionado no campo '+wParam+'!'

    return 'Erro desconhecido ou não descrito!'

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
    
def formatMaxSizeName(wName):
    """
        Shrink the name of the file
        @param wName of file
        @return The new name, maybe 50 character only
    """
    return wName[:75]+wName[len(wName)-75:] if len(wName)>150 else wName

def formatSessionId(wSessionId):
    """
        try to put $ back, because the args take $ from the URL
        Shall be used when the session id is passed via args
        @param wSessionId The text that shall be session id
        @return The clean sesson id
    """
    # 
    if not ('$' in wSessionId):
        try:
            part = wSessionId.split('_')
            return part[0]+'$'+part[1]+' '+part[2]+':'+part[3]+':'+part[4]
        except:
            return 'None'
    else:
        return wSessionId

def formatZipCode(wZipCode):
    """
        Get the zip code string and put it with dots and trace
        Return empty if nothing exists, never return None
        @param wZipCode The input text, empty or none thing
        @return The zipcode for show or empty
    """
    if wZipCode != '' and wZipCode != None and len(wZipCode)>=8:
        return wZipCode[0:2]+"."+wZipCode[2:5]+"-"+wZipCode[5:8]
    if wZipCode==None:
        return '';
    return wZipCode;

def buildMD5(wName,wBirth,wNow):
    """
        Compile the MD5 code base on name and birth date
        @param wName The person name
        @param wBirth The person birth date
        @return The MD5 in upper case
    """
    if type(wBirth) == str:
        wBirth = wBirth.split(' ')[0]
    else:
        wBirth = str(getDataOnly(wBirth))
    
    name = str(wNow)+str(wName)
    for_build = ((name[:100].ljust(100,' ')+constants.REP_REG_CLEARALL.sub('',wBirth)).lower())[:119]
    return md5(for_build).hexdigest().upper()