# -*- coding: utf8 -*-
from datetime import datetime, date
from validator import clearPointsString,sanatizeItem,formatDateToDB
import searchs
import time


def deletePerson(wId, wCompany):
    wCompany = 1
    query = """UPDATE person SET deleted='T' 
               WHERE id={0} AND company={1} RETURNING id;""".format(wId,wCompany)
    ret = db.executesql(query)
    if ret != '':
        return ''
    else:
        return ret


def insertUpdatePerson(wVars,wInsert):
    session.current_company_id = 1
    session.current_user_id = 1
    wVars.street_number = clearPointsString(sanatizeItem(wVars.street_number))
    wVars.zipcode       = clearPointsString(sanatizeItem(wVars.zipcode))
    wVars.cpf           = clearPointsString(sanatizeItem(wVars.cpf))
    wVars.rg            = sanatizeItem(wVars.rg)
    wVars.birth_date    = sanatizeItem(wVars.birth_date)
    if wInsert:
        ini = time.time()
        try:
            query = """ INSERT INTO person(created, last_update, full_name, birth_date,cpf,rg,email,keypoints1,keypoints2,sex,
                                street_number,comp_person,neigh,street,zipcode,marital_status,deleted,cellphone,city_person,company,last_user)
                                VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}',{18},{19},{20});
                                """.format(datetime.now(),datetime.now(),wVars.full_name,formatDateToDB(wVars.birth_date,True),wVars.cpf,wVars.rg,wVars.email,wVars.keypoints1,wVars.keypoints2,
                                'T' if wVars.sex=='1' else 'F',wVars.street_number,wVars.comp_person,wVars.neigh,wVars.street,wVars.zipcode,wVars.marital_status,
                                'F',wVars.cellphone,wVars.city_person,int(session.current_company_id),int(session.current_user_id))
            db.executesql(query)
        except Exception as wE:
            db.rollback()
            return 'Não foi possível {0} o cliente, tente novamente mais tarde!'.format('inserir' if wInsert else 'atualizar')
    else:
        try:
            query = """ UPDATE person SET last_update = '{0}',full_name = '{1}',birth_date = '{2}',cpf = '{3}',rg = '{4}',email = '{5}',keypoints1 = '{6}',keypoints2 = '{7}',sex = '{8}',
                                street_number = '{9}',comp_person = '{10}',neigh = '{11}',street = '{12}',zipcode = '{13}',marital_status = '{14}',deleted = '{15}',cellphone = '{16}',city_person = '{17}',company = '{18}',last_user = '{19}' WHERE id = {20}""".format(
                                datetime.now(),wVars.full_name,formatDateToDB(wVars.birth_date,True),wVars.cpf,wVars.rg,wVars.email,wVars.keypoints1,wVars.keypoints2,
                                'T' if wVars.sex=='1' else 'F',wVars.street_number,wVars.comp_person,wVars.neigh,wVars.street,wVars.zipcode,wVars.marital_status,
                                'F',wVars.cellphone,wVars.city_person,int(session.current_company_id),int(session.current_user_id),int(wVars.id))
            db.executesql(query)
        except Exception as wE:
            db.rollback()
            return 'Não foi possível {0} o cliente, tente novamente mais tarde!'.format('inserir' if wInsert else 'atualizar')
    db.commit()
    return ''