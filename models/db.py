# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

## app configuration made easy. Look inside private/appconfig.ini
from gluon.contrib.appconfig import AppConfig
from datetime import datetime
## once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)


global teste
if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    #db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'],migrate = True)
    try:
        #db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'],migrate = True)
        db = DAL('postgres://postgres:q1w2E#R$@188.166.24.73/TG_Samara',pool_size=1,check_reserved=['all'],fake_migrate = True)
    except Exception as wE:
        print('Erro de Conexão');
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## choose a style for forms
response.formstyle = myconf.take('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.take('forms.separator')


## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()


## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.take('smtp.server')
mail.settings.sender = myconf.take('smtp.sender')
mail.settings.login = myconf.take('smtp.login')

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)


db.define_table('country',
    Field('name',requires=IS_NOT_EMPTY(),unique=True,length=128,label='Nome do Pais'),
    format='%(name)s')


db.define_table('province',
    Field('name',requires=IS_NOT_EMPTY(),unique=True,length=128,label='Nome do Estado/Provincia'),
    Field('country',db.country,writable=False,readable=True, label='Pais'),
    format='%(name)s')

db.province.country.requires = IS_IN_DB(db,'country.id', '%(name)s',
                                          zero=T('Selecione'))

db.define_table('city',
    Field('created','datetime',writable=False,readable=False,label='Criado',default=datetime.now()),
    Field('last_update','datetime',writable=False,readable=False,label='Última Atualização',default=datetime.now()),
    Field('name',requires=IS_NOT_EMPTY(),length=50,label='Nome da Cidade'),
    Field('province',db.province,writable=False,readable=True, label='Estado/Provincia'),
    Field('deleted','boolean',writable=False,readable=False,label='Deleção Lógica',default='F'),
    Field('last_user','integer',label='Último Usuario'),
    format='%(name)s')

db.city.province.requires = IS_IN_DB(db,'province.id', '%(name)s',zero=T('Selecione'))


db.define_table('company',
    Field('created','datetime',writable=False,readable=False,label='Criado',default=datetime.now()),
    Field('last_update','datetime',writable=False,readable=False,label='Última Atualização',default=datetime.now()),
    Field('name_cmp',length=256,requires=IS_NOT_EMPTY(),label='Nome'),
    Field('cnpj',length=127,requires=IS_NOT_EMPTY(),label='CNPJ'),
    Field('city_cmp',db.city,requires=IS_NOT_EMPTY(),notnull=True,label='Cidade'),
    Field('address_cmp',length=300,label='Endereço'),
    Field('address_number_cmp','integer',label='Número'),
    Field('neigh_cmp',length=50,label='Bairro'),
    Field('comp_cmp',length=50,label='Complemento'),
    Field('zipcode_cmp',length=10,label='CEP'),
    Field('actived_cmp','boolean',label='Empresa Ativa',default=True),
    Field('deleted','boolean',writable=False,readable=False,label='Deleção Lógica',default='F'),
    Field('last_user','integer',label='Último Usuario'),
    format='%(name_cmp)s')

db.company.city_cmp.requires = IS_IN_DB(db,'city.id','%(name)s',zero=T('Selecione'))


auth.settings.extra_fields['auth_user'] = [
    Field('created','datetime',writable=False,readable=False,label='Criado',default=datetime.now()),
    Field('last_update','datetime',writable=False,readable=False,label='Última Atualização',default=datetime.now()),
    Field('email',length=100,label='E-mail'),
    Field('cpf',length=50,label='CPF'),
    Field('rg',length=50,label='RG'),
    Field('birth',type='date',label='Data de Nascimento'),
    Field('address',length=300,label='Endereço'),
    Field('address_number','integer',label='Número'),
    Field('comp_user',length=50,label='Complemento'),
    Field('city_user',db.city,requires=IS_EMPTY_OR(IS_IN_DB(db, 'city.id', '%(id)s')),
              represent=lambda id, row: db.city(id).name if id else '',label='Cidade'),
    Field('neigh',length=50,label='Bairro'),
    Field('zipcode',length=10,label='CEP'),
    Field('actived_user','boolean',label='Usuário ativo',default=True),
    Field('last_user','integer',label='Último Usuario'),
    Field('company',db.company,requires=IS_EMPTY_OR(IS_IN_DB(db, 'company.id', '%(id)s')),
              represent=lambda id, row: db.company(id).name_cmp if id else '',writable=False,readable=True, label='Empresa'),
    Field('deleted','boolean',writable=False,readable=False,label='Deleção Lógica',default='F')
    
]

auth.define_tables(username=False, signature=False)

db.define_table('person',
        Field('created','datetime',writable=False,readable=False,label='Criado',default=datetime.now()),
        Field('last_update','datetime',writable=False,readable=False,label='Última Atualização',default=datetime.now()),
        Field('full_name',length=50,label='Nome'),
        Field('birth_date',type='date',label='Data de Nascimento'),
        Field('cpf',length=50,label='CPF'),
        Field('rg',length=50,label='RG'),
        Field('email',length=100,label='E-mail'),
        Field('cellphone',length=100,label='Celular'),
        Field('keypoints1',length=50000,label='keypoints 1'),
        Field('keypoints2',length=50000,label='keypoints 2'),
        Field('sex','boolean',label='Sexo'),
        Field('street_number',length=5,label='Numero'),
        Field('comp_person',length=50,label='Complemento'),
        Field('neigh',length=50,label='Bairro'),
        Field('street',length=100,label='Logradouro'),
        Field('zipcode',length=10,label='CEP'),
        Field('city_person',db.city,label='Cidade'),
        Field('marital_status',type='integer',label='Estado civil'),
        Field('deleted','boolean',writable=False,readable=False,label='Deleção Lógica',default='F'),
        Field('company',db.company,requires=IS_EMPTY_OR(IS_IN_DB(db, 'company.id', '%(id)s')),
                  represent=lambda id, row: db.company(id).name_cmp if id else '',label='Empresa'),
        Field('last_user',db.auth_user,requires=IS_EMPTY_OR(IS_IN_DB(db, 'auth_user.id', '%(id)s')),
                  represent=lambda id, row: db.auth_user(id).id if id else '',label='Usuario'),
        format='%(first_name)s')
    
db.person.company.requires = IS_IN_DB(db,'company.id','%(name_cmp)s',zero=T('Selecione'))
db.person.last_user.requires = IS_IN_DB(db,'auth_user.id','%(first_name)s',zero=T('Selecione'))

  



auth._next = None
auth.settings.login_next=URL('default','update_session')
auth.settings.logout_next = URL('default','index')
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True
auth.settings.actions_disabled.append('register')
auth.settings.actions_disabled.append('profile')
auth.settings.login_captcha = False     #adicionar captcha
auth.settings.password_min_length = 8   #tamanho do password
auth.settings.expiration = 10800 #segundos  4 horas
auth.settings.remember_me_form = False
auth.settings.retrieve_password_captcha = False
db.auth_user.email.label=T('E-mail')
db.auth_user.password.label=T('Password')