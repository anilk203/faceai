from collections import OrderedDict 
from flask import jsonify 
import logging
import pymysql 
import pymysql.cursors



class DatabaseConnection:
    def __init__(self):
        pass
    
    def get_database_connection(self):
        try:
            con = pymysql.connect(host='faceaidb',
            user='root',
            password='mysql',
            db='faceaidb',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
            return con
        except Exception as e:
            print(e)
            return None
    
class MySQLDatasource:
    def __init__(self):
        pass
    
    def save(self, data):
        dc  =  None 
        try: 
            dc  =  DatabaseConnection()
            con = dc.get_database_connection()
            
            if con != None: 
                with con: 
                    cur = con.cursor()
                    sql = "insert into registrations (registration_id, user_id,user_name, l_file_name, l_file_path, l_file_size_in_kb) values (%s, %s,%s,%s,%s, %s)" 
                    count = cur.execute(sql, (data['registration_id'], data['user_id'], data['user_name'], data['l_file_name'], data['l_file_path'], data['l_file_size_in_kb']))
                    con.commit()
        except pymysql.InternalError as error:
            code, message = error.args 
            return None
        
    def save_params(self, user_id, params): 
        dc  =  None 
        try: 
            dc  =  DatabaseConnection()
            con = dc.get_database_connection()
            if con != None: 
                with con: 
                    cur = con.cursor()
                    for key,value in params.items():
                        sql = "insert into registration_params (user_id,param_name, param_value) values (%s,%s,%s)" 
                        count = cur.execute(sql, (user_id, key, value))
                        con.commit()
                 
        
        except pymysql.InternalError as error:
            code, message = error.args 
            return None
        
    def get_registrations(self): 
        dc  =  None 
        rows = []
        try: 
            dc  =  DatabaseConnection()
            con = dc.get_database_connection()
            
            if con != None: 
                with con: 
                    cur = con.cursor()                  
                    sql = "select * from registrations order by created_at desc" 
                    count = cur.execute(sql)
                    rows = cur.fetchall()
        
        except pymysql.InternalError as error:
            code, message = error.args 
            return None        
        
        return rows
    
            
    def user_exists(self, facename, filename, file_size): 
        dc  =  None 
        try: 
            dc  =  DatabaseConnection()
            con = dc.get_database_connection()
            
            if con != None: 
                with con: 
                    cur = con.cursor()                  
                    sql = "select user_id from registrations where user_name=%s and l_file_name=%s and l_file_size_in_kb=%s" 
                    count = cur.execute(sql, (facename, filename, file_size))
                    user_id = cur.fetchone()
                    return user_id
                 
        
        except pymysql.InternalError as error:
            code, message = error.args 
            return None        
        
        return None
        
    def save_recognize_params(self, recongize_id, file_name,  params): 
        dc  =  None 
        try: 
            dc  =  DatabaseConnection()
            con = dc.get_database_connection()
            
            if con != None: 
                with con: 
                    cur = con.cursor()
                    for key, value in params.items():
                        sql = "insert into recognize_params (recongize_id,file_name, param_name, param_value) values (%s,%s,%s, %s)" 
                        cur.execute(sql, (recongize_id , file_name, key, value))
                    con.commit()
                 
        
        except pymysql.InternalError as error:
            code, message = error.args 
            print(error)
            return None                 
        
       