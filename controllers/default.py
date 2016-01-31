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
<<<<<<< HEAD
    


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
=======
>>>>>>> c9d12f6ffaaf671181260c9e7192f5fafd865297
    
def login():
    #verification_person()
    return dict()


def close_session():
    session.verification_person = False
    return XML(response.json({'info':'OK'}))    
<<<<<<< HEAD
=======





#python gluon/contrib/websocket_messaging.py -k mykey -p 8888



#SELECT similarity(keypoints2, '603c9d5dd8231afbf3e96ca6dd355fa9,055d462e7bd0f546bcd4d0c4dcc76141,055d462e7bd0f546bcd4d0c4dcc76141,256c3a0598dcdc72acc1afc633cfc197,256c3a0598dcdc72acc1afc633cfc197,e47ad45424fd03ce9832fa6810ea532a,e47ad45424fd03ce9832fa6810ea532a,890dc476eeb55cfce43f600cebc56ce5,67444b71beff3eb842a6cfdfb5ab7154,c303380d7aa16ed802f9ab0bd4a7a09f,c752c0fe99151f41574f12fb2dff747d,c303380d7aa16ed802f9ab0bd4a7a09f,19fd8a0ad9afedc37b88f6e7c1c2e648,f19f70a42198a41f08f5e1ee5f6d6a42,3ca8586ad6b40ceb9f740bed0269e548,add8be4fcf6cad6ef18ee29d78ba392b,5219a976d42d0ec6d1496242b3b4ba29,5219a976d42d0ec6d1496242b3b4ba29,3e81ac70bd0328331c649584e0d2f7da,2a526501cb6cb57cf3840022d728a4f9,07d6821ea2f83a21a58c8573112f9dbc,94ec6263bb2c09841bbb297473dd133d,94ec6263bb2c09841bbb297473dd133d,07a5cac8abc4448eadc1871c7334379f,07a5cac8abc4448eadc1871c7334379f,8644da0415a02132336c888d4a011420,fde4a1f9508388c24c8db68119e20743,db469f60c647d1dd87d4e28b12ad5f33,fde4a1f9508388c24c8db68119e20743,613e02754b25060e0c9010ba06259f30,613e02754b25060e0c9010ba06259f30,3e1d74dfc7b45e01fe3dcd3bb944a7bb,db5cc89cd7cc730a3fb4d677071ba926,6729158e3845311633915e2f621c18e4,96984dbfa4ae6215acfaa543c9e6b0cc,c4cff773e160344e2a06c5dc84d02cd0,c4cff773e160344e2a06c5dc84d02cd0,6729158e3845311633915e2f621c18e4,578e2fb1e066fee291dd98271649dbf2,578e2fb1e066fee291dd98271649dbf2,578e2fb1e066fee291dd98271649dbf2,85d095a77065d436332f8a1bb718baed,b3bef8ca20c781c8cd682b2ffe3af234,b3bef8ca20c781c8cd682b2ffe3af234,0780558926857801a07903df405c148d,860e74cc9e97d302687225a4b3c176b4,db5cc89cd7cc730a3fb4d677071ba926,45291f2a90e82f42801124ec313d9b12,61745376e295c346708d61252966830a,4e1779dc2ca8aea050699ace34332697,ee4d5a360d9ab3d578b3804c89711dee,ee4d5a360d9ab3d578b3804c89711dee,61745376e295c346708d61252966830a,e2f99890e2e875eea1a9c65ca40f313c,6379f99b7ffb7ebbe2b056f152c01930,45291f2a90e82f42801124ec313d9b12,561160d9a63910762fcb162475469e55,561160d9a63910762fcb162475469e55,a2d5aebd03a6b123dcd51d554a7bd414,de2a0457e1635da6c6b3260e440ddd53,de2a0457e1635da6c6b3260e440ddd53,3686cb0088c47b6bb6aabcd964d8b894,3a17e1bc1d57f2b99afe72f07cbee734,709eac12db5578afa24787f6842e0c2d,f3005e7bfa3f902327795546eb1d7507,df73e08ff4f9ba3aa73cbb31bed7b7c6,9edb3fbf70a9953ae0c5891a7a61c625,7bd945ac4aea4565038c6101347831d4,a7dca855bd81435c24f94189c38e15a1,f4c0ae14848fa794d92f00ea896f2cfd,a7dca855bd81435c24f94189c38e15a1,2f2e3e7c2baca550b2edc8457beaf89b,0274e203458f83de08c74237b28d255a,3b68854d63a4de0cf5e21dc2d1537f2d,3e1683baff39db61bb5a6d7fc821f3de,bf5bbae23fc291c9203b5b8dfb0bf11f,663da6023d757fdeb5482c946ae43717,b117a39c2212b85932728f90b672ec6f,b117a39c2212b85932728f90b672ec6f,50c8b06a4980a6c6a07ae59c76c05a99,fdd75dbd6e5ba0ab3b84ff5e508d08be,8fd188beff032b3695214f7d97800245,af5cc42aea7083a7232eac837661ebdb,a48627dcc22915b909205f84b5b66acc,a48627dcc22915b909205f84b5b66acc,af5cc42aea7083a7232eac837661ebdb,8d20c6fda14b3bc9319da5e915feacc9,fdd75dbd6e5ba0ab3b84ff5e508d08be,8fd188beff032b3695214f7d97800245,8d20c6fda14b3bc9319da5e915feacc9,e0b14256d215ea629dbeabcd8d7bba18,c92145d8ae4e7d172be54bc9a7804fb4,e024f9590c647840979c6e11a66f4c5f,0d85726d643d90f4c6ae33099be637f9,e024f9590c647840979c6e11a66f4c5f,533c6bb5b6b59c1c9604080d8850bdcf,3c758cafb08429ea4d04fbf228ecc97e,3c758cafb08429ea4d04fbf228ecc97e,eb08569328b72af6d8f9d76ae0d57035,f7d00216369ae869782861eea5ad30ff')
#FROM person 
#WHERE keypoints1 % '603c9d5dd8231afbf3e96ca6dd355fa9,055d462e7bd0f546bcd4d0c4dcc76141,055d462e7bd0f546bcd4d0c4dcc76141,256c3a0598dcdc72acc1afc633cfc197,256c3a0598dcdc72acc1afc633cfc197,e47ad45424fd03ce9832fa6810ea532a,e47ad45424fd03ce9832fa6810ea532a,890dc476eeb55cfce43f600cebc56ce5,67444b71beff3eb842a6cfdfb5ab7154,c303380d7aa16ed802f9ab0bd4a7a09f,c752c0fe99151f41574f12fb2dff747d,c303380d7aa16ed802f9ab0bd4a7a09f,19fd8a0ad9afedc37b88f6e7c1c2e648,f19f70a42198a41f08f5e1ee5f6d6a42,3ca8586ad6b40ceb9f740bed0269e548,add8be4fcf6cad6ef18ee29d78ba392b,5219a976d42d0ec6d1496242b3b4ba29,5219a976d42d0ec6d1496242b3b4ba29,3e81ac70bd0328331c649584e0d2f7da,2a526501cb6cb57cf3840022d728a4f9,07d6821ea2f83a21a58c8573112f9dbc,94ec6263bb2c09841bbb297473dd133d,94ec6263bb2c09841bbb297473dd133d,07a5cac8abc4448eadc1871c7334379f,07a5cac8abc4448eadc1871c7334379f,8644da0415a02132336c888d4a011420,fde4a1f9508388c24c8db68119e20743,db469f60c647d1dd87d4e28b12ad5f33,fde4a1f9508388c24c8db68119e20743,613e02754b25060e0c9010ba06259f30,613e02754b25060e0c9010ba06259f30,3e1d74dfc7b45e01fe3dcd3bb944a7bb,db5cc89cd7cc730a3fb4d677071ba926,6729158e3845311633915e2f621c18e4,96984dbfa4ae6215acfaa543c9e6b0cc,c4cff773e160344e2a06c5dc84d02cd0,c4cff773e160344e2a06c5dc84d02cd0,6729158e3845311633915e2f621c18e4,578e2fb1e066fee291dd98271649dbf2,578e2fb1e066fee291dd98271649dbf2,578e2fb1e066fee291dd98271649dbf2,85d095a77065d436332f8a1bb718baed,b3bef8ca20c781c8cd682b2ffe3af234,b3bef8ca20c781c8cd682b2ffe3af234,0780558926857801a07903df405c148d,860e74cc9e97d302687225a4b3c176b4,db5cc89cd7cc730a3fb4d677071ba926,45291f2a90e82f42801124ec313d9b12,61745376e295c346708d61252966830a,4e1779dc2ca8aea050699ace34332697,ee4d5a360d9ab3d578b3804c89711dee,ee4d5a360d9ab3d578b3804c89711dee,61745376e295c346708d61252966830a,e2f99890e2e875eea1a9c65ca40f313c,6379f99b7ffb7ebbe2b056f152c01930,45291f2a90e82f42801124ec313d9b12,561160d9a63910762fcb162475469e55,561160d9a63910762fcb162475469e55,a2d5aebd03a6b123dcd51d554a7bd414,de2a0457e1635da6c6b3260e440ddd53,de2a0457e1635da6c6b3260e440ddd53,3686cb0088c47b6bb6aabcd964d8b894,3a17e1bc1d57f2b99afe72f07cbee734,709eac12db5578afa24787f6842e0c2d,f3005e7bfa3f902327795546eb1d7507,df73e08ff4f9ba3aa73cbb31bed7b7c6,9edb3fbf70a9953ae0c5891a7a61c625,7bd945ac4aea4565038c6101347831d4,a7dca855bd81435c24f94189c38e15a1,f4c0ae14848fa794d92f00ea896f2cfd,a7dca855bd81435c24f94189c38e15a1,2f2e3e7c2baca550b2edc8457beaf89b,0274e203458f83de08c74237b28d255a,3b68854d63a4de0cf5e21dc2d1537f2d,3e1683baff39db61bb5a6d7fc821f3de,bf5bbae23fc291c9203b5b8dfb0bf11f,663da6023d757fdeb5482c946ae43717,b117a39c2212b85932728f90b672ec6f,b117a39c2212b85932728f90b672ec6f,50c8b06a4980a6c6a07ae59c76c05a99,fdd75dbd6e5ba0ab3b84ff5e508d08be,8fd188beff032b3695214f7d97800245,af5cc42aea7083a7232eac837661ebdb,a48627dcc22915b909205f84b5b66acc,a48627dcc22915b909205f84b5b66acc,af5cc42aea7083a7232eac837661ebdb,8d20c6fda14b3bc9319da5e915feacc9,fdd75dbd6e5ba0ab3b84ff5e508d08be,8fd188beff032b3695214f7d97800245,8d20c6fda14b3bc9319da5e915feacc9,e0b14256d215ea629dbeabcd8d7bba18,c92145d8ae4e7d172be54bc9a7804fb4,e024f9590c647840979c6e11a66f4c5f,0d85726d643d90f4c6ae33099be637f9,e024f9590c647840979c6e11a66f4c5f,533c6bb5b6b59c1c9604080d8850bdcf,3c758cafb08429ea4d04fbf228ecc97e,3c758cafb08429ea4d04fbf228ecc97e,eb08569328b72af6d8f9d76ae0d57035,f7d00216369ae869782861eea5ad30ff' 
#AND similarity(keypoints1, '603c9d5dd8231afbf3e96ca6dd355fa9,055d462e7bd0f546bcd4d0c4dcc76141,055d462e7bd0f546bcd4d0c4dcc76141,256c3a0598dcdc72acc1afc633cfc197,256c3a0598dcdc72acc1afc633cfc197,e47ad45424fd03ce9832fa6810ea532a,e47ad45424fd03ce9832fa6810ea532a,890dc476eeb55cfce43f600cebc56ce5,67444b71beff3eb842a6cfdfb5ab7154,c303380d7aa16ed802f9ab0bd4a7a09f,c752c0fe99151f41574f12fb2dff747d,c303380d7aa16ed802f9ab0bd4a7a09f,19fd8a0ad9afedc37b88f6e7c1c2e648,f19f70a42198a41f08f5e1ee5f6d6a42,3ca8586ad6b40ceb9f740bed0269e548,add8be4fcf6cad6ef18ee29d78ba392b,5219a976d42d0ec6d1496242b3b4ba29,5219a976d42d0ec6d1496242b3b4ba29,3e81ac70bd0328331c649584e0d2f7da,2a526501cb6cb57cf3840022d728a4f9,07d6821ea2f83a21a58c8573112f9dbc,94ec6263bb2c09841bbb297473dd133d,94ec6263bb2c09841bbb297473dd133d,07a5cac8abc4448eadc1871c7334379f,07a5cac8abc4448eadc1871c7334379f,8644da0415a02132336c888d4a011420,fde4a1f9508388c24c8db68119e20743,db469f60c647d1dd87d4e28b12ad5f33,fde4a1f9508388c24c8db68119e20743,613e02754b25060e0c9010ba06259f30,613e02754b25060e0c9010ba06259f30,3e1d74dfc7b45e01fe3dcd3bb944a7bb,db5cc89cd7cc730a3fb4d677071ba926,6729158e3845311633915e2f621c18e4,96984dbfa4ae6215acfaa543c9e6b0cc,c4cff773e160344e2a06c5dc84d02cd0,c4cff773e160344e2a06c5dc84d02cd0,6729158e3845311633915e2f621c18e4,578e2fb1e066fee291dd98271649dbf2,578e2fb1e066fee291dd98271649dbf2,578e2fb1e066fee291dd98271649dbf2,85d095a77065d436332f8a1bb718baed,b3bef8ca20c781c8cd682b2ffe3af234,b3bef8ca20c781c8cd682b2ffe3af234,0780558926857801a07903df405c148d,860e74cc9e97d302687225a4b3c176b4,db5cc89cd7cc730a3fb4d677071ba926,45291f2a90e82f42801124ec313d9b12,61745376e295c346708d61252966830a,4e1779dc2ca8aea050699ace34332697,ee4d5a360d9ab3d578b3804c89711dee,ee4d5a360d9ab3d578b3804c89711dee,61745376e295c346708d61252966830a,e2f99890e2e875eea1a9c65ca40f313c,6379f99b7ffb7ebbe2b056f152c01930,45291f2a90e82f42801124ec313d9b12,561160d9a63910762fcb162475469e55,561160d9a63910762fcb162475469e55,a2d5aebd03a6b123dcd51d554a7bd414,de2a0457e1635da6c6b3260e440ddd53,de2a0457e1635da6c6b3260e440ddd53,3686cb0088c47b6bb6aabcd964d8b894,3a17e1bc1d57f2b99afe72f07cbee734,709eac12db5578afa24787f6842e0c2d,f3005e7bfa3f902327795546eb1d7507,df73e08ff4f9ba3aa73cbb31bed7b7c6,9edb3fbf70a9953ae0c5891a7a61c625,7bd945ac4aea4565038c6101347831d4,a7dca855bd81435c24f94189c38e15a1,f4c0ae14848fa794d92f00ea896f2cfd,a7dca855bd81435c24f94189c38e15a1,2f2e3e7c2baca550b2edc8457beaf89b,0274e203458f83de08c74237b28d255a,3b68854d63a4de0cf5e21dc2d1537f2d,3e1683baff39db61bb5a6d7fc821f3de,bf5bbae23fc291c9203b5b8dfb0bf11f,663da6023d757fdeb5482c946ae43717,b117a39c2212b85932728f90b672ec6f,b117a39c2212b85932728f90b672ec6f,50c8b06a4980a6c6a07ae59c76c05a99,fdd75dbd6e5ba0ab3b84ff5e508d08be,8fd188beff032b3695214f7d97800245,af5cc42aea7083a7232eac837661ebdb,a48627dcc22915b909205f84b5b66acc,a48627dcc22915b909205f84b5b66acc,af5cc42aea7083a7232eac837661ebdb,8d20c6fda14b3bc9319da5e915feacc9,fdd75dbd6e5ba0ab3b84ff5e508d08be,8fd188beff032b3695214f7d97800245,8d20c6fda14b3bc9319da5e915feacc9,e0b14256d215ea629dbeabcd8d7bba18,c92145d8ae4e7d172be54bc9a7804fb4,e024f9590c647840979c6e11a66f4c5f,0d85726d643d90f4c6ae33099be637f9,e024f9590c647840979c6e11a66f4c5f,533c6bb5b6b59c1c9604080d8850bdcf,3c758cafb08429ea4d04fbf228ecc97e,3c758cafb08429ea4d04fbf228ecc97e,eb08569328b72af6d8f9d76ae0d57035,f7d00216369ae869782861eea5ad30ff') > 0.1
#OR keypoints2 % '603c9d5dd8231afbf3e96ca6dd355fa9,055d462e7bd0f546bcd4d0c4dcc76141,055d462e7bd0f546bcd4d0c4dcc76141,256c3a0598dcdc72acc1afc633cfc197,256c3a0598dcdc72acc1afc633cfc197,e47ad45424fd03ce9832fa6810ea532a,e47ad45424fd03ce9832fa6810ea532a,890dc476eeb55cfce43f600cebc56ce5,67444b71beff3eb842a6cfdfb5ab7154,c303380d7aa16ed802f9ab0bd4a7a09f,c752c0fe99151f41574f12fb2dff747d,c303380d7aa16ed802f9ab0bd4a7a09f,19fd8a0ad9afedc37b88f6e7c1c2e648,f19f70a42198a41f08f5e1ee5f6d6a42,3ca8586ad6b40ceb9f740bed0269e548,add8be4fcf6cad6ef18ee29d78ba392b,5219a976d42d0ec6d1496242b3b4ba29,5219a976d42d0ec6d1496242b3b4ba29,3e81ac70bd0328331c649584e0d2f7da,2a526501cb6cb57cf3840022d728a4f9,07d6821ea2f83a21a58c8573112f9dbc,94ec6263bb2c09841bbb297473dd133d,94ec6263bb2c09841bbb297473dd133d,07a5cac8abc4448eadc1871c7334379f,07a5cac8abc4448eadc1871c7334379f,8644da0415a02132336c888d4a011420,fde4a1f9508388c24c8db68119e20743,db469f60c647d1dd87d4e28b12ad5f33,fde4a1f9508388c24c8db68119e20743,613e02754b25060e0c9010ba06259f30,613e02754b25060e0c9010ba06259f30,3e1d74dfc7b45e01fe3dcd3bb944a7bb,db5cc89cd7cc730a3fb4d677071ba926,6729158e3845311633915e2f621c18e4,96984dbfa4ae6215acfaa543c9e6b0cc,c4cff773e160344e2a06c5dc84d02cd0,c4cff773e160344e2a06c5dc84d02cd0,6729158e3845311633915e2f621c18e4,578e2fb1e066fee291dd98271649dbf2,578e2fb1e066fee291dd98271649dbf2,578e2fb1e066fee291dd98271649dbf2,85d095a77065d436332f8a1bb718baed,b3bef8ca20c781c8cd682b2ffe3af234,b3bef8ca20c781c8cd682b2ffe3af234,0780558926857801a07903df405c148d,860e74cc9e97d302687225a4b3c176b4,db5cc89cd7cc730a3fb4d677071ba926,45291f2a90e82f42801124ec313d9b12,61745376e295c346708d61252966830a,4e1779dc2ca8aea050699ace34332697,ee4d5a360d9ab3d578b3804c89711dee,ee4d5a360d9ab3d578b3804c89711dee,61745376e295c346708d61252966830a,e2f99890e2e875eea1a9c65ca40f313c,6379f99b7ffb7ebbe2b056f152c01930,45291f2a90e82f42801124ec313d9b12,561160d9a63910762fcb162475469e55,561160d9a63910762fcb162475469e55,a2d5aebd03a6b123dcd51d554a7bd414,de2a0457e1635da6c6b3260e440ddd53,de2a0457e1635da6c6b3260e440ddd53,3686cb0088c47b6bb6aabcd964d8b894,3a17e1bc1d57f2b99afe72f07cbee734,709eac12db5578afa24787f6842e0c2d,f3005e7bfa3f902327795546eb1d7507,df73e08ff4f9ba3aa73cbb31bed7b7c6,9edb3fbf70a9953ae0c5891a7a61c625,7bd945ac4aea4565038c6101347831d4,a7dca855bd81435c24f94189c38e15a1,f4c0ae14848fa794d92f00ea896f2cfd,a7dca855bd81435c24f94189c38e15a1,2f2e3e7c2baca550b2edc8457beaf89b,0274e203458f83de08c74237b28d255a,3b68854d63a4de0cf5e21dc2d1537f2d,3e1683baff39db61bb5a6d7fc821f3de,bf5bbae23fc291c9203b5b8dfb0bf11f,663da6023d757fdeb5482c946ae43717,b117a39c2212b85932728f90b672ec6f,b117a39c2212b85932728f90b672ec6f,50c8b06a4980a6c6a07ae59c76c05a99,fdd75dbd6e5ba0ab3b84ff5e508d08be,8fd188beff032b3695214f7d97800245,af5cc42aea7083a7232eac837661ebdb,a48627dcc22915b909205f84b5b66acc,a48627dcc22915b909205f84b5b66acc,af5cc42aea7083a7232eac837661ebdb,8d20c6fda14b3bc9319da5e915feacc9,fdd75dbd6e5ba0ab3b84ff5e508d08be,8fd188beff032b3695214f7d97800245,8d20c6fda14b3bc9319da5e915feacc9,e0b14256d215ea629dbeabcd8d7bba18,c92145d8ae4e7d172be54bc9a7804fb4,e024f9590c647840979c6e11a66f4c5f,0d85726d643d90f4c6ae33099be637f9,e024f9590c647840979c6e11a66f4c5f,533c6bb5b6b59c1c9604080d8850bdcf,3c758cafb08429ea4d04fbf228ecc97e,3c758cafb08429ea4d04fbf228ecc97e,eb08569328b72af6d8f9d76ae0d57035,f7d00216369ae869782861eea5ad30ff' 
#AND similarity(keypoints2, '603c9d5dd8231afbf3e96ca6dd355fa9,055d462e7bd0f546bcd4d0c4dcc76141,055d462e7bd0f546bcd4d0c4dcc76141,256c3a0598dcdc72acc1afc633cfc197,256c3a0598dcdc72acc1afc633cfc197,e47ad45424fd03ce9832fa6810ea532a,e47ad45424fd03ce9832fa6810ea532a,890dc476eeb55cfce43f600cebc56ce5,67444b71beff3eb842a6cfdfb5ab7154,c303380d7aa16ed802f9ab0bd4a7a09f,c752c0fe99151f41574f12fb2dff747d,c303380d7aa16ed802f9ab0bd4a7a09f,19fd8a0ad9afedc37b88f6e7c1c2e648,f19f70a42198a41f08f5e1ee5f6d6a42,3ca8586ad6b40ceb9f740bed0269e548,add8be4fcf6cad6ef18ee29d78ba392b,5219a976d42d0ec6d1496242b3b4ba29,5219a976d42d0ec6d1496242b3b4ba29,3e81ac70bd0328331c649584e0d2f7da,2a526501cb6cb57cf3840022d728a4f9,07d6821ea2f83a21a58c8573112f9dbc,94ec6263bb2c09841bbb297473dd133d,94ec6263bb2c09841bbb297473dd133d,07a5cac8abc4448eadc1871c7334379f,07a5cac8abc4448eadc1871c7334379f,8644da0415a02132336c888d4a011420,fde4a1f9508388c24c8db68119e20743,db469f60c647d1dd87d4e28b12ad5f33,fde4a1f9508388c24c8db68119e20743,613e02754b25060e0c9010ba06259f30,613e02754b25060e0c9010ba06259f30,3e1d74dfc7b45e01fe3dcd3bb944a7bb,db5cc89cd7cc730a3fb4d677071ba926,6729158e3845311633915e2f621c18e4,96984dbfa4ae6215acfaa543c9e6b0cc,c4cff773e160344e2a06c5dc84d02cd0,c4cff773e160344e2a06c5dc84d02cd0,6729158e3845311633915e2f621c18e4,578e2fb1e066fee291dd98271649dbf2,578e2fb1e066fee291dd98271649dbf2,578e2fb1e066fee291dd98271649dbf2,85d095a77065d436332f8a1bb718baed,b3bef8ca20c781c8cd682b2ffe3af234,b3bef8ca20c781c8cd682b2ffe3af234,0780558926857801a07903df405c148d,860e74cc9e97d302687225a4b3c176b4,db5cc89cd7cc730a3fb4d677071ba926,45291f2a90e82f42801124ec313d9b12,61745376e295c346708d61252966830a,4e1779dc2ca8aea050699ace34332697,ee4d5a360d9ab3d578b3804c89711dee,ee4d5a360d9ab3d578b3804c89711dee,61745376e295c346708d61252966830a,e2f99890e2e875eea1a9c65ca40f313c,6379f99b7ffb7ebbe2b056f152c01930,45291f2a90e82f42801124ec313d9b12,561160d9a63910762fcb162475469e55,561160d9a63910762fcb162475469e55,a2d5aebd03a6b123dcd51d554a7bd414,de2a0457e1635da6c6b3260e440ddd53,de2a0457e1635da6c6b3260e440ddd53,3686cb0088c47b6bb6aabcd964d8b894,3a17e1bc1d57f2b99afe72f07cbee734,709eac12db5578afa24787f6842e0c2d,f3005e7bfa3f902327795546eb1d7507,df73e08ff4f9ba3aa73cbb31bed7b7c6,9edb3fbf70a9953ae0c5891a7a61c625,7bd945ac4aea4565038c6101347831d4,a7dca855bd81435c24f94189c38e15a1,f4c0ae14848fa794d92f00ea896f2cfd,a7dca855bd81435c24f94189c38e15a1,2f2e3e7c2baca550b2edc8457beaf89b,0274e203458f83de08c74237b28d255a,3b68854d63a4de0cf5e21dc2d1537f2d,3e1683baff39db61bb5a6d7fc821f3de,bf5bbae23fc291c9203b5b8dfb0bf11f,663da6023d757fdeb5482c946ae43717,b117a39c2212b85932728f90b672ec6f,b117a39c2212b85932728f90b672ec6f,50c8b06a4980a6c6a07ae59c76c05a99,fdd75dbd6e5ba0ab3b84ff5e508d08be,8fd188beff032b3695214f7d97800245,af5cc42aea7083a7232eac837661ebdb,a48627dcc22915b909205f84b5b66acc,a48627dcc22915b909205f84b5b66acc,af5cc42aea7083a7232eac837661ebdb,8d20c6fda14b3bc9319da5e915feacc9,fdd75dbd6e5ba0ab3b84ff5e508d08be,8fd188beff032b3695214f7d97800245,8d20c6fda14b3bc9319da5e915feacc9,e0b14256d215ea629dbeabcd8d7bba18,c92145d8ae4e7d172be54bc9a7804fb4,e024f9590c647840979c6e11a66f4c5f,0d85726d643d90f4c6ae33099be637f9,e024f9590c647840979c6e11a66f4c5f,533c6bb5b6b59c1c9604080d8850bdcf,3c758cafb08429ea4d04fbf228ecc97e,3c758cafb08429ea4d04fbf228ecc97e,eb08569328b72af6d8f9d76ae0d57035,f7d00216369ae869782861eea5ad30ff') > 0.1
#LIMIT 1
>>>>>>> c9d12f6ffaaf671181260c9e7192f5fafd865297
