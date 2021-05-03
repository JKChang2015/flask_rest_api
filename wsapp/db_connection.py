# -*- coding: UTF-8 -*-
# File name: db_connection
# Created by JKChang
# 30/04/2021, 11:00
# Tag:
# Description:

import mysql.connector
from flask import abort

import config


def get_connection():
    try:
        params = config.DB_PARAMS
        db = mysql.connector.connect(**params)
        return db
    except Exception as e:
        print(("Could not query the database " + str(e)))
        abort(500)


def gene_suggest(species, query, lim=None):
    db = get_connection()
    cursor = db.cursor()

    q = f"""select display_label 
            from gene_autocomplete 
            where species = '{species}' 
              and display_label like '{query}%'; """
    if lim != None:
        q = q.replace(';', f'limit {lim};')
    cursor.execute(q)
    result = cursor.fetchall()
    result = [i[0] for i in result]
    db.close()
    return result

def species_suggest(query,lim=None):
    db = get_connection()
    cursor = db.cursor()

    q = f"""select distinct(species) 
            from gene_autocomplete
            where species like '{query}%'; """
    if lim != None:
        q = q.replace(';', f'limit {lim};')
    cursor.execute(q)
    result = cursor.fetchall()
    result = [i[0] for i in result]
    db.close()
    return result