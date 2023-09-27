from nicegui import ui
import requests
import subprocess
import os
from lxml.html import fromstring

basepath = os.getcwd()
p = subprocess.Popen(["pwd"])

def enable_items():
    k.set_text("")
    i.enable()
    j.enable()
    os.chdir(basepath)

def download(url, title):
    newTitle = title.replace(" ", "_")
    try:
        os.mkdir(newTitle)
        print("Created folder: " + newTitle)
    except OSError as error:
        print(str(error))

    try:
        os.chdir(newTitle)
        k.set_text("Running")
        i.disable()
        j.disable()
        print("Started downloading: " + title)
        ui.notify("Downloading: " + title)
        p = subprocess.Popen(["spotdl",url])
    except Exception as e:
        ui.notify("Error: " + str(e))
        print("Exception: " + str(e))
        enable_items()

def url_ok(url):
    try:
        response = requests.head(url)
        r = requests.get(url)
        tree = fromstring(r.content)
        title = tree.findtext('.//title')
        if response.status_code == 200:
            download(url, title)
        else:
            ui.notify("Error: url status code error: " + str(response.status_code))
            return False
    except requests.ConnectionError as e:
        ui.notify("Error: check url")
        return e

with ui.column().classes('fixed-center').style('align-items: center;'):
    with ui.card().style('align-items: center;'):
        ui.label("Spoty Downloader")
        i = ui.input(placeholder='Enter spoty url').props('rounded outlined dense').props('clearable')
        j = ui.button('Start Download', on_click=lambda: [url_ok(i.value)])
        k = ui.label()

poll = p.poll()
if poll is not None:
    print("Download finished")
    enable_items()

ui.run(port=3344, title="SpotWebDL", dark=None)
