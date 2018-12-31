import os
import config
import requests
import tasks
import configparser

from xml.etree import ElementTree as ET
from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_httpauth import HTTPBasicAuth


tapi = Flask(__name__)
api = Api(tapi)
auth = HTTPBasicAuth()

url = os.environ['TALLY_URL']
# url = 'http://192.168.1.125:9002'
config = configparser.ConfigParser()
config.read('config.ini')
config['Tally']['Url'] = url
with open('config.ini', 'w') as configfile:
    config.write(configfile)


# view to ping tally server and check if running or not
@tapi.route('/tally/api/v1.0/pingserver')
def ping_tally():
    try:
        p = tasks.ping_tally()
        return(p)
    except Exception as e:
        return(str(e))


# view to import vouchers from csv using dataframe and send to taly
@tapi.route('/tally/api/v1.0/voucherimport/<path:filename>')
def batch_voucher_import(filename):
    try:
        request_xml = tasks.create_voucher_request(filename)
        result = tasks.send_tally_request(tally_req=request_xml)
        return(result)
    except Exception as e:
        return(str(e))


# view to import stock items from dataframe and send to tally
@tapi.route('/tally/api/v1.0/stockitemsimport/<path:filename>')
def batch_import_stockitems(filename):
    try:
        request_xml = tasks.create_stockitem_request(filename, chunksize=10)
        result = tasks.send_tally_request(tally_req=request_xml)
        return(result)
    except Exception as e:
        return(str(e))


if __name__ == '__main__':
    tapi.run(host=config['Flask']['host'], port=config['Flask']['port'], debug=True)  # set debug=True for development
