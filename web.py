from nicegui import ui
import requests
import asyncio
import os
from lxml.html import fromstring

basepath = os.getcwd()

def enable_ui():
    i.set_value("")
    i.enable()
    j.enable()
    k.set_visibility(False)

def disable_ui():
    i.disable()
    j.disable()
    k.set_visibility(True)

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
        disable_ui()
        p = await asyncio.create_subprocess_shell("spotdl " + url)
        await p.wait()
        ui.notify("Downloaded")
    else:
        ui.notify("Error: url status code error: " + str(response.status_code))
    enable_ui()
    os.chdir(basepath)

with ui.card().classes('fixed-center').style('align-items: center;'):
    ui.label("Spoty Downloader")
    ui.link('Spoty', 'https://open.spotify.com/', new_tab=True).style('color: inherit;')
    i = ui.input(placeholder='Enter spoty url').props('rounded outlined dense').props('clearable')
    j = ui.button('Start Download', on_click=lambda: url_ok(i.value))
    k = ui.spinner(size='lg')
    k.set_visibility(False)

ui.run(port=3344, title="SpotWebDL", dark=None, reload=False, favicon="🚀", binding_refresh_interval=0.5, show=False)
