from influxdb import InfluxDBClient
import datetime
# client=InfluxDBClient(host="localhost",port=8086)
import yfinance as yf
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

my_token = os.environ.get("INFLUXDB_TOKEN")
my_org = "ptg"
my_url = "http://192.168.122.243:8086"

client = InfluxDBClient(url=my_url, token=my_token, org=my_org)

data = yf.download("MSFT", start="2021-01-01", end="2021-10-30")
print(data.to_csv())
