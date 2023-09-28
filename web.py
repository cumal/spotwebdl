from nicegui import ui
import requests
import subprocess
import os
from lxml.html import fromstring

basepath = os.getcwd()

def download(url, title):
    newTitle = title.replace(" ", "")
    try:
        os.mkdir(newTitle)
    except OSError as error:
        False

    try:
        os.chdir(newTitle)
        i.disable()
        j.disable()
        ui.notify("Downloading: " + title)
        subprocess.run(["spotdl",url])
        ui.notify("Finished")
        i.enable()
        i.set_value("")
        j.enable()
        os.chdir(basepath)
    except Exception as e:
        ui.notify("Error: " + str(e))
        os.chdir(basepath)

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
        ui.link('Spoty', 'https://open.spotify.com/')
        i = ui.input(placeholder='Enter spoty url').props('rounded outlined dense').props('clearable')
        j = ui.button('Start Download', on_click=lambda: [url_ok(i.value)])

ui.run(port=3344, title="SpotWebDL", dark=None)
