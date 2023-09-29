from nicegui import ui
import requests
import asyncio
import os
from lxml.html import fromstring

basepath = os.getcwd()

async def url_ok(url):
    try:
        response = requests.head(url)
        r = requests.get(url)
        tree = fromstring(r.content)
        title = tree.findtext('.//title')
    except requests.ConnectionError as e:
        ui.notify("Error: check url")
        return

    newTitle = title.replace(" ", "")
    try:
        os.mkdir(newTitle)
    except OSError as error:
        False

    try:
        os.chdir(newTitle)
    except OSError as error:
        ui.notify("Error changing dir: " + str(error))
        os.chdir(basepath)
        return

    if response.status_code == 200:
        ui.notify("Downloading: " + title)
        await asyncio.create_subprocess_shell("spotdl " + url)
        i.set_value("")
    else:
        ui.notify("Error: url status code error: " + str(response.status_code))
    os.chdir(basepath)

with ui.card().classes('fixed-center').style('align-items: center;'):
    ui.label("Spoty Downloader")
    ui.link('Spoty', 'https://open.spotify.com/')
    i = ui.input(placeholder='Enter spoty url').props('rounded outlined dense').props('clearable')
    j = ui.button('Start Download', on_click=lambda: url_ok(i.value))

ui.run(port=3344, title="SpotWebDL", dark=None, reload=False)
