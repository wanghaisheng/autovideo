#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# here put the import lib
import json
import tkinter as tk
from tkinter import OptionMenu, filedialog
from tkinter import colorchooser
from tkinter import ttk
from PIL import Image, ImageFont, ImageDraw
import os
import itertools
from itertools import groupby
from datetime import datetime
import base64
from moviepy.editor import *
import random
import os
import time
import textwrap
import numpy as np
import platform
from datetime import timedelta, date
import multiprocessing.dummy as mp
import concurrent
from functools import partial
from glob import glob
import itemdb
from PIL import Image

import multiprocessing as mp
from moviepy.editor import VideoFileClip, AudioFileClip
import moviepy.video.fx.all as vfx
from ytb_up.upload import Upload


import requests


ytb_path = os.path.join(os.getcwd()+os.sep, "ytb.db")

# dbname = "reddit_popular"
# Open the database and make sure there is a table with appopriate indices
ytb = itemdb.ItemDB(ytb_path)
print('database started', 'ytb')


def url_ok(url):


    try:
        response = requests.head(url)
    except Exception as e:
        # print(f"NOT OK: {str(e)}")
        return False
    else:
        if response.status_code == 200:
            # print("OK")
            return True
        else:
            print(f"NOT OK: HTTP response code {response.status_code}")

            return False


def isfilenamevalid(filename):
    # print(imagename)
    invalid = '…,<>:."/\|?*!$\'\"#'

    for char in invalid:

        filename = filename.replace(char, '')
    if len(filename) > 260:
        filename = filename[:259]
    return filename


def fix_size(old_image_path, new_image_path, canvas_width=1080, canvas_height=720):
    """Edited from https://stackoverflow.com/questions/44231209/resize-rectangular-image-to-square-keeping-ratio-and-fill-background-with-black"""
    im = Image.open(old_image_path)
    x, y = im.size

    ratio = x / y
    desired_ratio = canvas_width / canvas_height

    w = max(canvas_width, x)
    h = int(w / desired_ratio)
    if h < y:
        h = y
        w = int(h * desired_ratio)

    mode = im.mode
    print(mode)
    if len(mode) == 1:  # L, 1
        new_background = (0)
    if len(mode) == 3:  # RGB
        new_background = (0, 0, 0)
    if len(mode) == 4:  # RGBA, CMYK
        new_background = (0, 0, 0, 0)
    new_im = Image.new(mode, (w, h), new_background)
    new_im.paste(im, ((w - x) // 2, (h - y) // 2))
    img = new_im.resize((canvas_width, canvas_height))
    if mode == 'RGBA':
        img = img.convert('RGB')
    img.save(new_image_path)


def load_setting():

    global setting
    try:
        print('读取配置文件', setting_file)

        fp = open(setting_file, 'r', encoding='utf-8')
        setting_json = fp.read()
        fp.close()
    except:
        print('读取配置文件失败 加载默认模版')
        fp = open("assets/config/setting-template.json", 'r', encoding='utf-8')
        setting_json = fp.read()
        fp.close()
    setting = json.loads(setting_json)
    print('当前使用的配置为：', setting)
    return setting

def reset_gui():

    load_setting()

    # 清空表格
    # 写入数据

    prefertags.set(setting['prefertags'])
    # preferdes.set(setting['preferdes'])
    preferdes.set(setting['preferdes'])

# 加载剧本


# 保存配置


def select_profile_folder():
    global firefox_profile_folder_path
    firefox_profile_folder_path = filedialog.askdirectory(
        parent=root, initialdir="/", title='Please select a directory')
    if len(firefox_profile_folder_path) > 0:
        print("You chose %s" % firefox_profile_folder_path)
        firefox_profile_folder.set(firefox_profile_folder_path)
        setting['firefox_profile_folder'] = firefox_profile_folder_path


def select_videos_folder():
    global video_folder_path
    video_folder_path = filedialog.askdirectory(
        parent=root, initialdir="/", title='Please select a directory')
    if len(video_folder_path) > 0:
        print("You chose %s" % video_folder_path)
        video_folder.set(video_folder_path)
        setting['video_folder'] = video_folder_path

def select_musics_folder():
    global music_folder_path
    music_folder_path = filedialog.askdirectory(
        parent=root, initialdir="/", title='Please select a directory')
    if len(music_folder_path) > 0:
        print("You chose %s" % music_folder_path)
        music_folder.set(music_folder_path)
        setting['music_folder'] = music_folder_path



def select_driver_file():
    global driver_file_path
    driver_file_path = filedialog.askopenfilenames(
        title="请选择gendriver 文件", filetypes=[("exe", "*.exe"), ("All Files", "*")])[0]

    driverfilepath.set(driver_file_path)
    setting['driverfilepath'] = driver_file_path


def select_setting_file():

    global setting_file
    setting_file = filedialog.askopenfilenames(title="请选择该频道配置文件", filetypes=[
        ("Json", "*.json"), ("All Files", "*")])[0]
    load_setting()
    firefox_profile_folder_path = setting['firefox_profile_folder']
    firefox_profile_folder.set(firefox_profile_folder_path)

    driverfilepath.set(setting['driverfilepath'])
    # firefox_profile_folder.set(setting['firefox_profile_folder'])
    channel_cookie.set(setting['channelcookiepath'])
    video_folder.set(setting['video_folder'])

    prefertags.set(setting['prefertags'])
    print('---', setting['preferdes'])
    preferdes.set(setting['preferdes'])
    dailycount.set(setting['dailycount'])
    channelname.set(setting['channelname'])
    music_folder_path= setting['music_folder']
    publishpolicy.set(setting['publishpolicy'])
    music_folder.set(music_folder_path)
    ratio.set(setting['ratio'])


def select_cookie_file():

    global channel_cookie_path
    channel_cookie_path = filedialog.askopenfilenames(title="请选择该频道对应cookie文件", filetypes=[
        ("Json", "*.json"), ("All Files", "*")])[0]

    channel_cookie.set(channel_cookie_path)
    setting['channelcookiepath'] = channel_cookie_path


def save_setting():

    try:
        driver_file_path =driverfilepath.get()
        print('driver file path setting',driverfilepath.get())
    except NameError:
        print('no new  driver_file_path,using existing setting',
              setting['driverfilepath'])
        driver_file_path = setting['driverfilepath']
    else:
        if driver_file_path:
            setting['driverfilepath'] = driver_file_path
    try:
        firefox_profile_folder_path =firefox_profile_folder.get()
    except NameError:
        print('no new  firefox_profile_folder,using existing setting',
              setting['firefox_profile_folder'])
        firefox_profile_folder_path = setting['firefox_profile_folder']

    else:
        if firefox_profile_folder_path:
            setting['firefox_profile_folder'] = firefox_profile_folder_path
    try:
        video_folder_path=video_folder.get()
    except NameError:
        print('no new  video_folder_path,using existing setting',
              setting['video_folder'])
        video_folder_path = setting['video_folder']
        print(video_folder_path)
    else:
        if video_folder_path:
            setting['video_folder'] = video_folder_path

    try:
        channel_cookie_path=channel_cookie.get()
    except NameError:
        print('no new  channel_cookie_path,using existing setting',
              setting['channelcookiepath'])
        channel_cookie_path = setting['channelcookiepath']
        print(channel_cookie_path)
    else:
        if channel_cookie_path:
            setting['channelcookiepath'] = channel_cookie_path

    try:
        music_folder_path=music_folder.get()
    except NameError:
        print('no new  music_folder,using existing setting',
              setting['music_folder'])
        music_folder = setting['music_folder']
        # print(music_folder)
    else:
        if music_folder_path:
            setting['music_folder'] = music_folder_path


    setting['ratio'] = ratio.get()

    setting['dailycount'] = dailycount.get()
    setting['channelname'] = channelname.get()

    setting['preferdes'] = preferdes.get()

    setting['prefertags'] = prefertags.get()
    setting['publishpolicy']=publishpolicy.get()    
    with open('assets/config/'+setting['channelname']+".json", 'w') as f:
        f.write(json.dumps(setting, indent=4, separators=(',', ': ')))
    print("配置保存成功")

# 清理残留文件

def threadusing_free_musichelper(numbers):

    using_free_music(numbers[0],numbers[1])

def using_free_music(setting,inputmp4):

    if os.path.exists(inputmp4):

        print('video exists', inputmp4)
    else:
        print('video not found')
    try:
        music_folder =setting['music_folder']
    except:
        music_folder='assets/freemusic'

    else:
        print('setting==',setting)

        music_folder = setting['music_folder']


    freemusic = []

    for ext in ('*.mp3', '*.wav','*.wma','*.ogg','*.aac','*.mp4'):
        freemusic.extend(glob(os.path.join(music_folder, ext)))
        
    if len(freemusic) > 0:    

        soundeffect = random.choice(freemusic)
        print('randomly choose a background music',soundeffect)
        ext = os.path.splitext(soundeffect)[1]
        videoext= os.path.splitext(inputmp4)[1]
        videofilename= os.path.splitext(inputmp4)[0]

        print('videoext',videoext)
        print('videofilename',videofilename)
        oldvideofiles=[]
        if not ext in ['.mp4','.wma','.aac','.ogg','.wav','.mp3']:

            print('we have not found wav,mp3 background music in this folder',freemusic)
        else:
            audioclip = AudioFileClip(soundeffect)
          
            os.rename(inputmp4, videofilename+'-old'+videoext)
            videoclip = VideoFileClip(videofilename+'-old'+videoext)
            if audioclip.duration>videoclip.duration:
                audioclip =audioclip.subclip(0,videoclip.duration)
            else:
                audioclip = vfx.loop( audioclip, duration=videoclip.duration)
            if setting['ratio']:
                pass
            else:
                setting['ratio']=1
            audioclip = audioclip.fx( afx.volumex, float(setting['ratio']))
            # audioclip = volumex(audioclip,setting['ratio'])          
            videoclip = videoclip.set_audio(audioclip)

            videoclip.write_videofile(videofilename+'.mp4', threads=0,audio=False)



def init_worker(mps, fps, cut):
    global memorizedPaths, filepaths, cutoff
    global DG

    print("process initializing", mp.current_process())
    memorizedPaths, filepaths, cutoff = mps, fps, cut
    DG = 1##nx.read_gml("KeggComplete.gml", relabel = True)
def batchchangebgmusic():
    m = mp.Manager()
    memorizedPaths = m.dict()
    filepaths = m.dict()
    cutoff = 1 ##
    # use all available CPUs
    p = mp.Pool(initializer=init_worker, initargs=(memorizedPaths,
                                                   filepaths,
                                                   cutoff))
    folder =setting['video_folder']    
    # oldvideofiles=[]
    videofiles = []

    if os.path.isdir(folder):
        print('this is a directory',folder)

        for ext in ('*.flv', '*.mp4', '*.avi'):
            videofiles.extend(glob(os.path.join(folder, ext)))
        print('detecting videos in folder',folder,videofiles)
        if len(videofiles) > 0:
            arguments=[]
            for i,f in enumerate(videofiles):
                videofilename= os.path.splitext(f)[0]
                videoext= os.path.splitext(f)[1]
                if not videofilename.endswith('-old'):
                    arguments.append((setting,f)) 
                else:
                    oldvideofiles.append(f)
            print('awaiting convert files',videofiles)                                                   
            # degreelist = range(100000) ##
            for _ in p.imap_unordered(threadusing_free_musichelper, arguments, chunksize=500):
                pass
    p.close()
    p.join()


    print('start cleaning old video files')
    oldvideofiles=[]

    if os.path.isdir(folder):

        for ext in ('*.flv', '*.mp4', '*.avi'):
            oldvideofiles.extend(glob(os.path.join(folder, ext)))
        # print('this is a directory',folder)
  
    for f in oldvideofiles:   
        videofilename= os.path.splitext(f)[0]

        if  videofilename.endswith('-old'):
            print('start cleaning old video file',f)
            os.remove( f)
    print('finish cleaning old video files')
def changebgmusic():
    folder =setting['video_folder']    
    if os.path.isdir(folder):
        print('this is a directory',folder)

        videofiles = []
        for ext in ('*.flv', '*.mp4', '*.avi'):
            videofiles.extend(glob(os.path.join(folder, ext)))
        print('detecting videos in folder',folder,videofiles)
        if len(videofiles) > 0:
            # for i,f in enumerate(videofiles):

            #     videofiles.append(f)    
            print('awaiting convert files',videofiles)
            start = time.time()
            with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
                # while True:
                tasks = [using_free_music(x) for x in videofiles]
                for task, future in [(i, executor.submit(i)) for i in tasks]:
                    try:
                        # print(future.result(timeout=1))
                        print('ok')
                    except concurrent.futures.TimeoutError:
                        print("this took too long...")
            #             # task.interrupt()
            end = time.time()
            print("批量替换took {} seconds\n".format(end-start))



def b64e(s):
    return base64.b64encode(s.encode()).decode()


def checkraw():

    save_setting()
# 文件夹下是否有视频文件

# 视频文件是否有同名的图片

    try:
        video_folder_path = setting['video_folder']

    except NameError:
        print('not found fastlane folder  file')
    else:
        if video_folder_path:
            print("sure, it was defined dir.")
            with ytb:

                check_video_thumb_pair(video_folder_path)
        else:
            print("pls choose file or folder")

def check_video_thumb_pair(folder):
    # print('detecting----------',folder)

    for r, d, f in os.walk(folder):
        with os.scandir(r) as i:
            print('detecting----------',r)

            videofiles = []
            pairedvideothumbs=[]
            for entry in i:
                if entry.is_file():
                    filename = os.path.splitext(entry.name)[0]
                    ext = os.path.splitext(entry.name)[1]
                    print(filename,'==',ext) 

                    start_index=0
                    if ext in ('.flv', '.mp4', '.avi'):
                        for image_ext in ('.jpeg', '.png', '.jpg'):
                            videopath = os.path.join(r, entry.name)
                            thumbpath = os.path.join(r, filename+image_ext)

                            if os.path.exists(thumbpath):       
                                add_video_thumb_pair_basic(thumbpath,videopath,filename,start_index)                 
                    start_index+=1
                                # print('========',videopath)
                                # print('========',thumbpath)

        # for dirs in d:
        #     print(dirs)  
        #     check_video_thumb_pair_basic(dirs)

def add_video_thumb_pair_basic(thumbpath,videopath,filename,start_index):

    tablename = setting['channelname']
    db = ytb
    db.ensure_table(tablename, "!videoid", "status")
            
              

    # filename = os.path.splitext(f)[0]

    if os.path.exists(thumbpath):
        video = db.count(
            tablename, "videoid ==?", b64e(filename))
        print('check video stauts', video)
        if video == 1:
            status = db.select_one(tablename, "videoid ==?",
                                    b64e(filename))["status"]

            if status == 1:
                print('task completed', status, video)
            else:

                print('task added but not uploaded')

        elif video == 0:
            print('task not added before')
            tags = setting['prefertags']
            des = setting['preferdes']
            filename=filename.split(os.sep)[-1]
            title = isfilenamevalid(filename)
            if len(filename) > 100:
                title = filename[:90]
            nowtime = time.time()
            update_time = int(nowtime)
            videoid = b64e(filename)
            olddata = {}
            olddata["videoid"] = videoid
            #Oct 19, 2021
            today = date.today()
            publish_date =datetime(today.year, today.month, today.day, 20, 15), 

            if start_index <int(setting['dailycount']):
                release_offset='0-1'
            else:
                release_offset=str(int(start_index)/30)+'-'+str(int(start_index)/int(setting['dailycount']))
            

            olddata["publish_date"] = release_offset
            olddata["thumbpath"] = thumbpath
            olddata["update_time"] = update_time
            olddata["title"] = title
            olddata["des"] = des
            olddata["videopath"] = videopath
            olddata["tags"] = tags
            olddata["status"] = 0
            db.put(tablename, olddata)
            print('add 1 new videos for upload', filename)
    else:
        pass



def upload():

    tablename = setting['channelname']
    db = ytb
    db.ensure_table(tablename, "!videoid", "status")

    print('starting upload process')
    with ytb:
        donevideos = db.select(tablename, "status ==?", 1)
        print('already upload videos:', len(donevideos))

        videos = db.select(tablename, "status ==?", 0)
        print('awaiting upload videos:', len(videos))
        if len(videos)>0:
            options = {
                'backend': 'mitmproxy',
                'proxy': {
                    'http': 'socks5://127.0.0.1:1080',
                    'https': 'socks5://127.0.0.1:1080',
                    'no_proxy': 'localhost,127.0.0.1'
                }
            }
            upload = Upload(
                # use r"" for paths, this will not give formatting errors e.g. "\n"
                setting['firefox_profile_folder'],
                CHANNEL_COOKIES=setting['channelcookiepath'],
                executable_path =setting['driverfilepath']
            )
            if url_ok('http://www.google.com'):
                print('network is fine,there is no need for proxy ')
            else:
                print('google can not be access ')

                print('we need for proxy ',options)

                upload = Upload(
                    # use r"" for paths, this will not give formatting errors e.g. "\n"
                    setting['firefox_profile_folder'],
                    proxy_option=options,
                    headless=False,
                    executable_path =setting['driverfilepath'],
                    CHANNEL_COOKIES=setting['channelcookiepath']
                )   
            for video in videos:
                print('checking whether need proxy setting')
             
                thumbpath = video["thumbpath"]
                des = video["des"]
                videopath = video["videopath"]
                tags = video["tags"]
                publish_date =video["publish_date"]
                title = video["title"]
                # title = os.path.splitext(os.path.basename(title)[-1])[0]
                print('release date',publish_date)
                videoid=video['videoid']
                max_retries = 3
                for retries in itertools.count():
                    try:
                        if setting['publishpolicy']=="0" or setting['publishpolicy']=="1":
                            was_uploaded, upload_video_id = upload.upload(
                                videopath,
                                title=title,
                                description=des,
                                thumbnail=thumbpath,
                                tags=tags.split(','),
                                publishpolicy=setting['publishpolicy']
                            )
                        else:

                            was_uploaded, upload_video_id = upload.upload(
                                videopath,
                                title=title,
                                description=des,
                                thumbnail=thumbpath,
                                tags=tags.split(','),
                                publishpolicy=setting['publishpolicy'],
                                release_offset=publish_date
                            )
                        if was_uploaded:

                            nowtime = time.time()
                            update_time = int(nowtime)
                            olddata = db.select_one(tablename, "videoid ==?",
                                                    videoid)
                            # print('old data',olddata)
                            olddata["status"] = 1
                            db.put(tablename, olddata)
                            print(f"{videoid} has been uploaded to YouTube")
                                                        
                    except Exception as e:
                        if  retries != max_retries:
                            print('%s. Retrying...' % str( e.msg))
                            continue
                        
                    break               
            upload.close()

        else:
            print('videos in folder',setting['video_folder'],'all uploaded')

if __name__ == '__main__':

    gui_flag = 1

    # log_file = "log.txt"

    load_setting()

    if gui_flag:

        root = tk.Tk()
        prefertags = tk.StringVar()
        prefertags.set(setting['prefertags'])
        preferdes = tk.StringVar()
        preferdes.set(setting['preferdes'])
        dailycount = tk.StringVar()
        dailycount.set(setting['dailycount'])
        music_folder = tk.StringVar()
        music_folder.set(setting['music_folder'])

        ratio = tk.StringVar()
        ratio.set(setting['ratio'])        
        video_folder = tk.StringVar()
        video_folder.set(setting['video_folder'])
        firefox_profile_folder = tk.StringVar()
        firefox_profile_folder.set(setting['firefox_profile_folder'])
        driverfilepath = tk.StringVar()
        driverfilepath.set(setting['driverfilepath'])
        channelname = tk.StringVar()
        channelname.set(setting['channelname'])
        channel_cookie = tk.StringVar()
        channel_cookie.set(setting['channelcookiepath'])
        publishpolicy = tk.StringVar()
        publishpolicy.set(setting['publishpolicy'])
        
        l3 = tk.Label(root, text="copyright free music folder")
        l3.place(x=10, y=130)
        e3 = tk.Entry(root, width=55, textvariable=music_folder)
        e3.place(x=120, y=130)

        l4 = tk.Label(root, text="标签")
        l4.place(x=10, y=70)
        e4 = tk.Entry(root, width=55, textvariable=prefertags)
        e4.place(x=120, y=70)

        l51 = tk.Label(root, text="背景音乐音量")
        l51.place(x=10, y=150)
        e51 = tk.Entry(root, width=55, textvariable=ratio)
        e51.place(x=120, y=150)

        l52 = tk.Label(root, text="发布策略")
        l52.place(x=10, y=170)
        e52 = tk.Entry(root, width=55, textvariable=publishpolicy)
        e52.place(x=120, y=170)


        l5 = tk.Label(root, text="每日公开视频数量")
        l5.place(x=10, y=200)
        e5 = tk.Entry(root, width=55, textvariable=dailycount)
        e5.place(x=120, y=200)

        l63 = tk.Label(root, text="视频描述")
        l63.place(x=10, y=100)
        e63 = tk.Entry(root, width=55, textvariable=preferdes)
        e63.place(x=120, y=100)

        l64 = tk.Label(root, text="频道名称")
        l64.place(x=10, y=230)
        e64 = tk.Entry(root, width=55, textvariable=channelname)
        e64.place(x=120, y=230)

        l65 = tk.Label(root, text="视频文件夹")
        l65.place(x=10, y=270)
        e65 = tk.Entry(root, width=55, textvariable=video_folder)
        e65.place(x=120, y=270)

        l66 = tk.Label(root, text="profile文件夹")
        l66.place(x=10, y=300)
        e66 = tk.Entry(root, width=55, textvariable=firefox_profile_folder)
        e66.place(x=120, y=300)

        l67 = tk.Label(root, text="驱动路径")
        l67.place(x=10, y=330)
        e67 = tk.Entry(root, width=55, textvariable=driverfilepath)
        e67.place(x=120, y=330)

        l68 = tk.Label(root, text="cookie json")
        l68.place(x=10, y=360)
        e68 = tk.Entry(root, width=55, textvariable=channel_cookie)
        e68.place(x=120, y=360)

        b5 = tk.Button(root, text="加载配置", command=select_setting_file)
        b5.place(x=100, y=30)

        b6 = tk.Button(root, text="保存配置", command=save_setting)
        b6.place(x=200, y=30)

        b61 = tk.Button(root, text="headless", command=save_setting)
        b61.place(x=300, y=30)

        b7 = tk.Button(root, text="开始上传", command=upload)
        b7.place(x=400, y=400)

        b8 = tk.Button(root, text="检查素材", command=checkraw)
        b8.place(x=300, y=400)
        b9 = tk.Button(root, text="批量替换背景音乐", command=batchchangebgmusic)
        b9.place(x=150, y=400)
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="浏览器配置", menu=filemenu)
        filemenu.add_command(label="选择geckodriver文件",
                             command=select_driver_file)
        filemenu.add_command(label="选择profile文件夹",
                             command=select_profile_folder)
        filemenu.add_command(label="选择cookie json",
                             command=select_cookie_file)

        filemenu2 = tk.Menu(menubar, tearoff=False)

        menubar.add_cascade(label="视频素材", menu=filemenu2)
        filemenu2.add_command(label="选择视频文件夹",
                              command=select_videos_folder)
        filemenu2.add_command(label="选择背景音樂文件夹",
                              command=select_musics_folder)

        root.config(menu=menubar)
        # root.geometry('1280x720')
        root.geometry('530x440')
        root.title("youtube video auto upload GUI")
        root.resizable(width=False, height=False)
        root.iconbitmap("assets/icon.ico")
        root.mainloop()
