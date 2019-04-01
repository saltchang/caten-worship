# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request, redirect, url_for, send_file

import os, dropbox

from importDB import importDB
from config import Config

app = Flask(__name__)

# App Configure
app.config.from_object(Config.Development)

# Database
db = importDB("chinese.json", "taiwanese.json")
db_sample = importDB("sample.json")

# Dropbox API
dbx = dropbox.Dropbox(os.environ.get("DROPBOX_ACCESS_TOKEN"))

# 首頁 HomePage
@app.route("/")
def index():
    return render_template("index.html", url_for_all_songs=url_for("list_all_songs"))

# 列出所有詩歌
@app.route("/allsongs")
def list_all_songs():
    return render_template("all_songs.html", songs=db, sample=db_sample)

# 下載PPT
@app.route("/download/ppt/<id_>")
def download_ppt(id_):
    try:
        result = dbx.files_get_temporary_link("/caten-worship/ppt/ppt_" + id_ + ".ppt")
        return redirect(result.link)
    except Exception as e:
        print(e)
        return "<h1>很抱歉，這首詩歌目前沒有投影片資料可供下載。<h1>", 404

# 下載歌譜
@app.route("/download/sheetmusic/<id_>")
def download_sheetmusic(id_):
    try:  
        result = dbx.files_get_temporary_link("/caten-worship/sheet-music/sheetmusic_" + id_ + ".jpg")
        link = result.link
        return render_template("img.html", link=link)
    except Exception as e:
        print(e)
        return "<h1>很抱歉，這首詩歌目前沒有歌譜資料可供下載。<h1>", 404

@app.route("/report/<id_>")
def report_song(id_):
    return "你回報了id：" + str(id_) + "的歌曲資訊。"
    

if __name__ == "__main__":
    app.run()
