# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
import constants
import processor
import security
import searchs
import formater
import validator
import datetime


searchs.db = db
searchs.session = session
searchs.auth = auth
processor.db = db
processor.session = session
processor.auth = auth
processor.request = request
processor.mail = mail
security.db = db
security.session = session
security.auth = auth
security.request = request 

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    if request.args(0) == 'register_ok':
        return dict(message=T('Cadastro confirmado com sucesso!'))
    elif request.args(0) == 'reset_ok':
        return dict(message=T('Senha alterada com sucesso!'))
    else: 
        return dict(message=T(''))


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
	return response.download(request,db,attachment=False)

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


@auth.requires_login()
def create_person():
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
        ret = searchs.getPersonForEdition(request.vars.id,session.current_company_id)
        if len(ret)==0:
            session.flash_msg = 'error Não foi possível editar o cliente!'
            return redirect(URL('search_person'))
        else:
            fromData=ret
            
    insert_update='Inserir' if insert else 'Atualizar'    
    cities = searchs.searchCity()
    return dict(cities=cities, insertUpdate=insert_update,formData=fromData)

@auth.requires_login()
def search_person():       
    action = request.vars.action
    option = request.vars.option
    if action=='delete':
        if request.vars.id!=None and request.vars.id.isdigit():
            ret = processor.deletePerson(request.vars.id,session.current_company_id)
            session.flash_msg = 'error '+ret if len(ret) != 0 else 'success Cliente removido com sucesso!'
            return redirect(URL('search_person'))
        else:
            session.flash_msg = 'error O Cliente é inválido e não pode ser processado!'
    elif action=='update':
        return redirect(URL('create_person',args=['update'],
                vars={'id': request.vars.id}))
    formData = searchs.searchPerson(request.vars.option, request.vars.value,session.current_company_id)
    return dict(option=option,value=request.vars.value,formData=formData)



    



