import json
import mysql
#from models import db, Post
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_restful import Api, Resource
import os
import json
import app 


@app.route('/product', methods = ['GET'])
# def product():
#     if(request.method == 'GET'):
  
#         data = "#get from mysql"
#         return jsonify({'products': data})
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products GROUP BY categoryType")
    products = cur.fetchall()
    cur.close()

def show():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products WHERE uniqueId") #params[id]
    products = cur.fetchone()
    cur.close()

@app.route('/men', methods=["GET"])
def men():
    cur = mysql.connection.cursor()
    values = 'men'
    cur.exceute("SELECT * FROM products WHERE catlevel1Name=%s ORDER BY uniqueId", (values,))
    products = cur.fetchall()
    cur.close()

@app.route('/women', methods=["GET"])
def women():
    cur = mysql.connection.cursor()
    values = 'women'
    cur.exceute("SELECT * FROM products WHERE catlevel1Name=%s ORDER BY uniqueId", (values,))
    products = cur.fetchall()
    cur.close()

@app.route('/shirts', methods=['GET'])
def shirts():
    cur = mysql.connection.cursor()
    # Get message
    values = 'Shirts'
    cur.execute("SELECT * FROM products WHERE categoryType=%s ORDER BY uniqueId ASC", (values,))
    products = cur.fetchall()
    # Close Connection
    cur.close()

@app.route('/bottoms', methods=['GET'])
def bottoms():
        cur = mysql.connection.cursor()
        # Get message
        values = 'Bottoms'
        cur.execute("SELECT * FROM products WHERE categoryType=%s ORDER BY uniqueId ASC", (values,))
        products = cur.fetchall()
        # Close Connection
        cur.close()

@app.route('/accessories', methods=['GET'])
def accessories():
    cur = mysql.connection.cursor()
    # Get message
    values = 'Accessories'
    cur.execute("SELECT * FROM products WHERE categoryType=%s ORDER BY uniqueId ASC", (values,))
    products = cur.fetchall()
    # Close Connection
    cur.close() 


