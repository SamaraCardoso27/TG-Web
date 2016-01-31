# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
import constants
import processor
import security
import searchs
import formater
import validator
import datetime
from serializers import json

from requests import session

searchs.db = db
searchs.session = session
searchs.auth = auth
processor.db = db
processor.session = session
processor.auth = auth
processor.request = request
processor.mail = mail

session.current_company_id = 1



def index():
    try:
        if session.verification_person != False:
            print str(session.verification_person)
            session.verification_person = True
            return dict()
        else:
            return dict()
    except Exception as wE:
        session.verification_person = False
        return dict()
        
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html
    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    if request.args(0) == 'login':
        request.vars._next = URL('update_session')
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

def downloads():
    """
        Allows downloading of uploaded files as pure
        URL without Content-Disposition in the HTTP header
        http://..../[app]/default/downloads/[filename]
    """
    return dict()

def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


def update_session():
    if auth.user_id:
        # vai para o menu principal
        if (session.current_state==None or session.current_company_name==None or
            session.current_city==None):
            searchs.setSessionCompanyInfo()
        if session.current_company_type==constants.TYPE_CMP_ADMIN:
            return redirect(URL('default','index'))
        else:
            return redirect(URL('default','index'))



def create_person():
    #if session.verification_person == True or session.verification_person == None:
    insert = True
    first_args = request.args(0)
    fromData = request.vars
    wType =  request.vars.type
    wId = request.vars.id
    if wType == 'Atualizar':
        insert = False
        ret = processor.insertUpdatePerson(request.vars,insert)
        if ret=='':
            session.flash_msg = 'success,Cliente {0} com sucesso!'.format('criado' if insert else 'atualizado')
            return redirect(URL('create_person'))
        else:
            session.flash_msg = 'error '+ret
            return redirect(URL('create_person'))
    elif first_args == 'submit':
    #if wType == 'Inserir':
        insert = True
        ret = processor.insertUpdatePerson(request.vars,insert)
        if ret=='':
            session.flash_msg = 'success,Cliente {0} com sucesso!'.format('criado' if insert else 'atualizado')
            return redirect(URL('create_person'))
        else:
            session.flash_msg = 'error '+ret
            return redirect(URL('create_person'))
    #if wType == 'Atualizar':
    elif first_args == 'update':
        insert = False
        ret = searchs.getPersonForEdition(int(request.vars.id),session.current_company_id)
        if len(ret)==0:
            session.flash_msg = 'error Não foi possível editar o cliente!'
            return redirect(URL('search_person'))
        else:
            fromData=ret
            
    insert_update='Inserir' if insert else 'Atualizar'    
    cities = searchs.searchCity()
    return dict(cities=cities, insertUpdate=insert_update,formData=fromData)
    #else:
    #    session.flash_msg = 'Autentique-se'
    #    return redirect(URL('index'))

def search_person():
    #if session.verification_person == True:       
    action = request.vars.action
    option = request.vars.option
    if action=='delete':
        if request.vars.id!=None and request.vars.id.isdigit():
            ret = processor.deletePerson(request.vars.id,1)
            session.flash_msg = 'error '+ret if len(ret) != 0 else 'success Cliente removido com sucesso!'
            return redirect(URL('search_person'))
        else:
            session.flash_msg = 'error O Cliente é inválido e não pode ser processado!'
    elif action=='update':
        return redirect(URL('create_person',args=['update'],
                vars={'id': request.vars.id}))
    formData = searchs.searchPerson(request.vars.option, request.vars.value,session.current_company_id)
    return dict(option=option,value=request.vars.value,formData=formData)
    #else:
    #    session.flash_msg = 'Autentique-se'
    #    return redirect(URL('index'))

def verification_person():
    keypoint = request.vars.keypoints
    session.current_company_id = 1
    query = """
        SELECT id,created, last_update, full_name, birth_date,cpf,rg,email,keypoints1,keypoints2,sex,street_number,
        comp_person,neigh,street,zipcode,marital_status,deleted,cellphone,city_person
        FROM auth_user
        WHERE deleted='F'"""
    
    person_data = db.executesql(query,as_dict=True)
    if person_data != None or person_data != '':
        for i in range(0,len(person_data)):
            get_person = authentication(person_data[i]['keypoints1'],person_data[i]['keypoints2'],keypoint)
            if get_person == 1:
                session.full_name = person_data[0]['full_name']
                return XML(json({'info':'OK', 'person':person_data[0]}))
            else:
                return XML(json({'info':'Ocorreu um erro! Tente Novamente!', 'person':''}))
    else:
        return XML(json({'info':'Ocorreu um erro! Tente Novamente!', 'person':''}))
    


def func_diff(wVetor,wList1,wList2):
    keyPoint_equal = []
    keyPoint_diff = []
    search_point = []
    for i in range(0,len(wVetor)):
        slt = wVetor[i].split(',')
        x = float(slt[0])
        y = float(slt[1])
        
        percent_x = (x * 0.05) / 100 + x
        percent_Y = (y * 0.05) / 100 + y
    
        
        search_point.append(str(percent_x) + ',' + str(percent_Y))
        
        if len(search_point) > 0:
            for val in search_point:
                if val in wList1:
                    keyPoint_equal.append(val)
                else:
                    keyPoint_diff.append(val)
                    
        if len(keyPoint_equal) == 0:
            for val in search_point:
                if val in wList2:
                    keyPoint_equal.append(val)
                else:
                    keyPoint_diff.append(val)
    
    if len(keyPoint_equal):
        return len(keyPoint_equal)
    else:
        return 0

def authentication(wList1,wList2,wList3):
    keyPoint_equal = []
    keyPoint_diff = []
    for val in wList3:
        if val in wList1:
            keyPoint_equal.append(val)
        else:
            keyPoint_diff.append(val)
    
    if len(keyPoint_equal) == 0:
        for val in wList3:
            if val in wList2:
                keyPoint_equal.append(val)
            else:
                keyPoint_diff.append(val)

    
    percentual = (len(keyPoint_equal) * 100 / 100)
    
    if percentual >= 70:
        return 1
    else:
        if len(keyPoint_diff) > 0:
            search_diff = func_diff(keyPoint_diff,wList1,wList2)
            if  search_diff != 0:
                if (percentual  + search_diff) >= 70:
                    return 1
                else:
                    return 2
    
def login():
    #verification_person()
    return dict()


def close_session():
    session.verification_person = False
    return XML(response.json({'info':'OK'}))    
