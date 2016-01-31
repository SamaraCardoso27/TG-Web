# -*- coding: utf8 -*-
from validator import sanatizeItem
import constants
import formater

db = None
session = None
auth = None

def setSessionCompanyInfo():
    session.current_user_id        = auth.user.id
    session.current_user_name      = auth.user.first_name 
    session.current_company_id     = auth.user.company



def searchCity(wFull=False):
    query = ''
    query = """SELECT city.id, city.name
                          FROM city WHERE city.deleted='F';"""
    return db.executesql(query,as_dict=True)



def searchPerson(wOption,wValue,wCompany):
    if wOption=='1':
        part = "full_name LIKE '%%"+wValue+"%%'"
    elif wOption=='2':
        part = "cpf LIKE '%%"+wValue+"%%'"
    else:
        part = "id>0"
    
    query = """SELECT * FROM person WHERE """+part+""" ORDER BY id DESC"""
    print query
    search_person = db.executesql(query,as_dict=True)
    return search_person

def getPersonForEdition(wId,wCompany):
    query = """
        SELECT id,created, last_update, full_name, birth_date,cpf,rg,email,keypoints1,keypoints2,sex,street_number,
        comp_person,neigh,street,zipcode,marital_status,deleted,cellphone,city_person,company,last_user
        FROM person
        WHERE id={0} AND deleted='F' AND company={1};""".format(wId,wCompany)
    person_data = db.executesql(query,as_dict=True)
    return person_data

def getPerson(wCompany):
    query = """
        SELECT id,created, last_update, full_name, birth_date,cpf,rg,email,keypoints1,keypoints2,sex,street_number,
        comp_person,neigh,street,zipcode,marital_status,deleted,cellphone,city_person,company,last_user
        FROM person
        WHERE deleted='F' AND company={0};""".format(wCompany)
    person_data = db.executesql(query,as_dict=True)
    
    #if len(person_data)==0:
    #    return {},{}
    
    #if person_data['birth_date']!='' and person_data['birth_date']!=None:
    #    person_data['birth_date'] = formater.formatDateToDB(str(person_data['birth_date']), False)
    #else:
    #    person_data['birth_date']=''
    #person_data['sex'] = 1 if person_data['sex']=='T' else 2
    #person_data['last_update'] = str(person_data['last_update']) 
    
    return person_data#, {'id' : person_data['id']}


            

