# -*- coding: utf8 -*-
from gluon.http import HTTP
import searchs
import constants
from datetime import datetime
from random import random


db = None
session = None
auth = None
request = None

def checkDuplicatedLogin(wSessionId, wGroup, wCompanyType):
    """
        This function checks if the current user as more than five minutes of log and 
        than check if it is the same IP, if not, logout
        @param wCalledFunction The function called before the analysis of IP
        @return The function return
    """
    if auth.user:
        # check if the user was removed from the system
        if auth.user.actived_user == False:
            from gluon.utils import simple_hash
            if 'session_id_legislator' in request.cookies.keys():
                cookey_key = str(request.cookies['session_id_legislator'])
            else:
                cookey_key = str(random()*1000000000)
            db(db.auth_user.id==auth.user.id).update(last_ip=request.env.remote_addr,
                last_session=wSessionId,password=simple_hash(cookey_key,digest_alg='sha512')[:299])
            session.clear()
            raise HTTP(1001)
        if (session.current_state==None or session.current_company_name==None or
            session.current_city==None):
            searchs.setSessionCompanyInfo(request.env.remote_addr,wSessionId,request.now)
        #ups you cannot access this function 
        if not (session.current_role in wGroup):
            session.clear()
            raise HTTP(401)
        if not (session.current_company_type in wCompanyType):
            session.clear()
            raise HTTP(401)
        # fill the session
        if type(session.current_user_lastcheck) != datetime:
            #avoid break when the session is not correctly filled
            session.current_user_lastcheck = request.now
        if (((request.now-session.current_user_lastcheck).seconds) > 300):
            if session.current_user_id!=None and session.current_user_ip!=None and session.current_user_session!=None:
                ret = db.executesql("SELECT id FROM auth_user WHERE id={0} AND last_ip='{1}' AND last_session='{2}'".format(
                     session.current_user_id,session.current_user_ip,session.current_user_session))
            else:
                # clear the session to avoid any access to the system, guarantee logout
                session.clear()
                raise HTTP(1000)
            if len(ret)>0:# ok the last ip is the current ip
                session.current_user_lastcheck = request.now
                return True
            else:
                # clear the session to avoid any access to the system, guarantee logout
                session.clear()
                raise HTTP(1002)
        else:
            return True
    return True
 
def getAndCheckKeyId(wAction, wData =None, wIdForSession = None):
    """
         This function generates and check the key existence
         @param wData The data that shall be stored
         @param wAction The action over the key
         @param wStatus If it shall be created or used
         @param wIdForSession The session id 
    """
    if wAction == constants.CREATE_KEY:
        # create unique code for student
        date = datetime.now()
        id_for_session = str(random()*100000)+'$'+str(date)
        # create the main session communication handle
        if session.key_of_data==None:
            session.key_of_data = {} 
        # Delete old id_session
        for key in session.key_of_data.keys():
            if key == None or key == 'None' or key == '':
                session.key_of_data.pop(key)
            else:  
                if '$' in key: # check if the key can be broken
                    key_time = datetime.strptime(key.split('$')[1], "%Y-%m-%d %H:%M:%S.%f")
                    if (date-key_time).seconds > 13600: # if the item has more then 12 hours try to avoid problems
                        session.key_of_data.pop(key)
                else:# through key problem away
                    session.key_of_data.pop(key)
        session.key_of_data[id_for_session] = {}
        return id_for_session
    elif wAction == constants.INSERT_RAW:
        session.key_of_data[wIdForSession] = wData
        return ''
    elif wAction == constants.RETRIAVE_KEY:
        if type(session.key_of_data) != dict:
            return 'Ocorreu um erro, tente novamente!'
        # check if the unique code was passed throught the system
        if not (wIdForSession in session.key_of_data.keys()):
            return 'Ocorreu um erro, tente novamente!'
        # return the session ids
        return session.key_of_data[wIdForSession]
    return 'Opção Inválida na chave de sessão!'
 
