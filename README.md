Tally-Gstr-API
===========
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Python:](https://img.shields.io/badge/python-3.6%20%7C%203.7-green.svg)
![Docker:](https://img.shields.io/docker/build/jrottenberg/ffmpeg.svg)

This is a API inteface for Tally Tax Software for HTTP based Import & transcode of E-Commerce Invoices into Tally Software for GST-R Tax Filling. 

This API helps Accountants,E-Commerce Sellers to convert the CSV files with the tax data provided by the E-Commerce sites into Tally Schema(Vouchers,Item Import,Inventory Tracking) directly from the browser using HTTP/1.1 requests, without the need of manual labor. 

Table of Contents
--------------------- 
 - [Feature Support](https://github.com/Pac23/Tally-Import-API/blob/master/README.md#feature-support)
 - [Installation](https://github.com/Pac23/Tally-Import-API/blob/master/README.md#installation)
	 - [Docker](https://github.com/Pac23/Tally-Import-API/blob/master/README.md#docker)
		 - [Configuration](https://github.com/Pac23/Tally-Import-API/blob/master/README.md#configuration)
		- [Deployment](https://github.com/Pac23/Tally-Import-API/blob/master/README.md#deployment)
	 - [Non-Contanarized](https://github.com/Pac23/Tally-Import-API/blob/master/README.md#non-contanarized)
		 - [Configuration](https://github.com/Pac23/Tally-Import-API/blob/master/README.md#configuration-1)
		 - [Deployment](https://github.com/Pac23/Tally-Import-API/blob/master/README.md#deployment)
 - [Sample Usage](https://github.com/Pac23/Tally-Import-API/blob/master/README.md#sample-usage)
 	- [Command-Line](https://github.com/Pac23/Tally-Import-API/blob/master/README.md#using-the-command-line)
	- [Browser](https://github.com/Pac23/Tally-Import-API/blob/master/README.md#using-the-browser)
 - [Status](https://github.com/Pac23/Tally-Import-API/blob/master/README.md#status) 
 
Feature Support
---------------------
As of Version 0.1 
 - Check Tally Server Status
 - Voucher Import
 - Stock Items Import
 
 Installation 
 -------------
 You can either deploy this in a contanarized format using docker or in a Non-Containarized Python App format. 

### Docker 
#### Configuration 
To build from the Dockerfile :

    docker build -t what_ever_you_name_it:latest .

Volume mapping/Bindmounting would be required to share the data stored on the client system with the container. 

    -v /your/system/path:/whatever_you_name_it/Data
You can read more about volume mapping [Here](https://www.digitalocean.com/community/tutorials/how-to-share-data-between-the-docker-container-and-the-host) and [Here](https://www.digitalocean.com/community/tutorials/how-to-share-data-between-docker-containers)

Tally Server URL/IP is passed as a Enviroment Variables.

    -e TALLY_URL=http://IP:PORT
#### Deployment
Example Docker container deployment would look like. 

    docker run --name=gst -d -v ~/Documents/customerdata:/tallygst/Data -e TALLY_URL=http://192.168.1.125:9002 -p 5000:50 tallygst 

 `-p` standing for port mapping with `5000` being port forwarded to `50` . 
 `-e` for passing the `TALLY_URL` enviroment variable 

### Non-Contanarized
#### Configuration 
Download 

    git clone https://github.com/Pac23/Tally-Import-API.git
Create a Virtual Enviroment inside the cloned DIR
Install the required modules using : 

    pip install -r requirements.txt 
Comment out line 17 and 21 in the tapi.py file using #
`# url = os.environ['TALLY_URL']`
`# config['Tally']['Url'] = url` 

Update the Tally Server URL in the `Config.ini` file

Note: Non-Contanarized API will be acessible at `PORT:50` you can change that from the Config.ini file 

#### Deployment 
Make sure Your python version is `3.6 or above` 
   

     python tapi.py

Sample Usage
----------------
#### Using the Command Line 

To Check the Status of the Tally Server

    $ curl http://IP:PORT/tallyapi/pingserver
 To Import Data from CSV into Voucher 
 

    $ curl http://127.0.0.1:5000/tallyapi/voucherimport/test_rows.csv

To import Data from CSV into voucher StockItems

    $ curl http://127.0.0.1:5000/tally/api/stockitemsimport/test_rows.csv

#### Using the Browser
To Check the Status of the Tally Server
   

     http://127.0.0.1:5000/tallyapi/pingserver

To Import Data from CSV into Voucher

    http://127.0.0.1:5000/tallyapi/voucherimport/test_rows.csv

To import Data from CSV into voucher StockItems

 `http://127.0.0.1:5000/tally/api/stockitemsimport/test_rows.csv`
    
Status
----------------
This project is at a very early stage right now.Please report any issues. 

