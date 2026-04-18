import threading
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import csv
from io import StringIO

def parse_csv(line):
    try:
        reader = csv.reader(StringIO(line))
        row = next(reader)
        return [float(i) for i in row]
    
"""
üldiselt pärast seda:
    row = parse_csv(line)
    temp = row[0]
    rohk = row[1]
    lat = row[2]
    lon = row[3]
"""

def handle_data(data):
    temp = data[0]
    rohk = data[1]
    lat = data[2]
    lon = data[3]

    #siia tuleb graafiku uuendamine pg abil.



def read_serial():
    while True: 
        line = ser.readline().decode().strip()
        if line:
            data = parse_csv(line)
            if data:
                handle_data(data)

thread = threading.Thread(target=read_serial)
thread.daemon = True
thread.start()


