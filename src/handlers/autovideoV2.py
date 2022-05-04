from tkinter import *
from PIL.ImageTk import PhotoImage, Image
import os
import subprocess as sub
# from threading import Thread
# pyinstaller --onefile -i "Exe.ico" -F --add-binary='tk86t.dll;tk' -F --add-binary='tcl86t.dll;tcl' main.py
# pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' your_script.py
from tkinter import filedialog, messagebox, Label, Tcl
import time
# import io
temp = False
def main():
    output = ''
    # /////////////////   INITIALISING THE OBJECTS   //////////////////////////
    app = Tk()
    var = IntVar()
    text1 = Text(app)
    text2 = Text(app)
    text1.config(state=DISABLED)
    text2.config(state=DISABLED)
    b1 = Button(app, text= 'install libs', command = lambda: package_installer())
    b2 = Button(app, text= 'load config', command = lambda: load_existing_config())

    words = Entry(app)
    words.config(state=DISABLED)
    file_words = Entry(app)
    file_words.config(state=DISABLED)
    file_icon = Entry(app)
    file_icon.config(state = DISABLED)
    l1 =Label(app, text = 'FILE PATH')
    l2 =Label(app, text = 'FILE NAME')
    ck = Checkbutton(app, text = 'LOGO', command = lambda: puticon())
    open_button = Button(app, text = 'OPEN FILE', command = lambda: openfile())
    icon_button = Button(app, text = 'ICON FILE', command = lambda: iconfile())
    compiling = Button(app, text = 'RUN/ TEST',command = lambda: compilation())
    video_convert_exe = Button(app, text = 'video transform', command = lambda: video_convert_exe())
    thumb_convert_exe = Button(app, text = 'thumnail transform', command = lambda: thumb_convert_exe())
    exe = Button(app, text = 'CONVERT TO EXE', command = lambda: py_exe())

    r1 = Radiobutton(app, text="WITH TERMINAL", variable=var, value=1)
    r2 = Radiobutton(app, text="WITHOUT TERMINAL", variable=var, value=2)
    panel = Label(app)
    # //////////////////   BY DEFAULT INITIALISATION ON THE SCREEN ////////////////////
    frame = Frame(app, width= 200, height = 480, bg = 'blue')
    install_module = Button(app, text = 'INSTALL MODULES', command = lambda: installer())
    load_config = Button(app, text = 'LOAD EXISTING CONFIG', command = lambda: installer())

    convert = Button(app, text = 'CONVERT TO EXE   ', command = lambda: converter())
    credit = Button(app, text = 'CREDITS   ', command = lambda: information())
    video_convert = Button(app, text = 'video transform', command = lambda: video_convert_exe())
    thumb_convert = Button(app, text = 'thumnail transform', command = lambda: thumb_convert_exe())


    # //////////////       Defining Functions        ////////////////////////
    def information():
        messagebox.showinfo("CREDITS INFORMATION", "DEVOLOPED BY\n Aaris Kazi \nPOWERED BY \n Pyinstaller")
    def iconfile():
        filename=filedialog.askopenfile(initialdir='GUI/',title="Select a ico file",filetypes=(("ICON FILES","*.ico"),("All files",'*')))
        try:
            if filename:
                filepath = os.path.abspath(filename.name)
                inp1 = words.get()
                try:
                    ic1, ic2 = filepath.split(inp1)
                except Exception:
                    ic2 = filepath
                # print(ic2)
            file_icon.config(state = NORMAL)
            file_icon.insert(0, ic2)
            file_icon.config(state = DISABLED)
            img = Image.open(filepath)
            img = img.resize((40,40), Image.ANTIALIAS)
            pimg = PhotoImage(img)
            panel.configure(image = pimg)
            panel.image =pimg
            # panel.config(image = pimg, text = 'working')
            panel.place(x= 220, y = 120)
        except Exception as e:
            file_icon.config(state = NORMAL)
            file_icon.delete(0, END)
            file_icon.config(state = DISABLED)
            panel.place_forget()
            # print(e)
                # file_icon.delete()
    def puticon():
        global temp
        if temp:
            temp =False
            file_icon.place_forget()
            icon_button.place_forget()
            panel.place_forget()
            file_icon.config(state = NORMAL)
            file_icon.delete(0, END)
            file_icon.config(state = DISABLED)
        else:
            file_icon.place(x = 290, y = 80, width = 230)
            icon_button.place(x = 524,y = 80)
            temp= True
    def statements():
        text2.config(state=NORMAL)
        text2.insert(END, 'RUNNING THE PROGRAM\n')
        text2.config(state=DISABLED)

    def py_exe():
        text2.config(state=NORMAL)
        text2.delete('1.0', END)
        text2.config(state = DISABLED)
        inp1 = words.get()
        inp2 = file_words.get()
        terminal = str(var.get())
        # print(terminal)
        icons = file_icon.get()
        # print(icons)
        if int(terminal) == 1 and len(icons) == 0:
            text2.config(state = NORMAL)
            text2.insert(END, 'CONVERTING THE PROGRAM ALONG WITH THE TERMINAL\n')
            text2.config(state = DISABLED)
            os.chdir(inp1)
            os.system('pyinstaller --onefile '+inp2)
        elif int(terminal) == 1 and len(icons) != 0:
            text2.config(state = NORMAL)
            text2.insert(END, 'CONVERTING THE PROGRAM ALONG WITH THE TERMINAL AND WITH ICON\n')
            text2.config(state = DISABLED)
            os.chdir(inp1)
            os.system('pyinstaller --onefile -i "'+icons+'" '+inp2)
            # os.system('pyinstaller --onefile -w -i "path.ico" yourfile.py'+filename)
        elif int(terminal) == 2 and len(icons) == 0:
            text2.config(state = NORMAL)
            text2.insert(END, 'CONVERTING THE PROGRAM WITHOUT THE TERMINAL\n')
            text2.config(state = DISABLED)
            os.chdir(inp1)
            os.system('pyinstaller --onefile -w '+inp2)
        elif int(terminal) == 2 and len(icons) != 0:
            text2.config(state = NORMAL)
            text2.insert(END, 'CONVERTING THE PROGRAM WITHOUT THE TERMINAL AND WITH ICON\n')
            text2.config(state = DISABLED) 
            print('pyinstaller --onefile -w -i "'+str(icons)+'" '+inp2)
            os.chdir(inp1)
            os.system('pyinstaller --onefile -w -i "'+str(icons)+'" '+inp2)
            # pyinstaller --onefile -w -i "Coffee.ico" add_data "Exe.ico" main.py
        else:
            text2.insert(END, 'PLEASE DO NOT EDIT THE FILE\n')
                
    def openfile():
        words.config(state=NORMAL)
        words.delete(0, END)
        words.config(state=DISABLED)
        filename=filedialog.askopenfile(initialdir='GUI/',title="Select a Python file",filetypes=(("Python files","*.py"),("All files",'*')))
        try:
            if filename:
                filepath = os.path.abspath(filename.name)
            new_filename = os.path.basename(filepath)
            fp = filepath.split(new_filename)
            filep = fp[0]
            words.config(state=NORMAL)
            words.insert(0, filep)
            words.config(state=DISABLED)
            file_words.config(state=NORMAL)
            file_words.insert(0, new_filename)
            file_words.config(state=DISABLED)
            
            r1.select()
            r1.place( x = 600, y = 80)
            r2.place( x = 750, y = 80)
            ck.place(x = 220, y = 80)
            text2.place(x = 220, y = 170, height = 250)
            compiling.place(x = 700, y = 450)
            exe.place(x = 800, y = 450)
            thumb_convert_exe.place(x = 800, y = 500)
            video_convert_exe.place(x = 800, y = 550)         
        except Exception as e:
            words.config(state=NORMAL)
            words.delete(0, END)
            words.config(state=DISABLED)
            file_words.config(state=NORMAL)
            file_words.delete(0, END)
            file_words.config(state=DISABLED)
            compiling.place_forget()
            exe.place_forget()
            thumb_convert_exe.place_forget()
            video_convert_exe.place_forget()            
            text2.place_forget()
            r1.place_forget()
            r2.place_forget()
            ck.place_forget()
            # ////// for icon
            file_icon.place_forget()
            icon_button.place_forget()
            panel.place_forget()
            # ck.deselect()
            # temp = False
    def compilation():
        text2.config(state=NORMAL)
        text2.delete('1.0', END)
        text2.config(state = DISABLED)
        inp1 = words.get()
        inp2 = file_words.get()
        print(inp1, inp2)
        print(str(var.get()))
        text2.config(state=NORMAL)
        text2.insert(END, 'RUNNING THE PROGRAM\n')
        text2.insert(END, 'COMPILED SUCCESSFULLY!\n')
        text2.config(state=DISABLED)
        os.chdir(inp1)
        os.system('python '+inp2)
    def load_existing_config():
        text1.config(state=NORMAL)
        p = sub.Popen('pip install pyinstaller',stdout=sub.PIPE,stderr=sub.PIPE, shell= True)
        output, errors = p.communicate()
        text1.insert(END, output)
        text1.config(state=DISABLED)
    def package_installer():
        text1.config(state=NORMAL)
        p = sub.Popen('pip install pyinstaller',stdout=sub.PIPE,stderr=sub.PIPE, shell= True)
        output, errors = p.communicate()
        text1.insert(END, output)
        text1.config(state=DISABLED)
    def installer():
        words.config(state=NORMAL)
        words.delete(0, END)
        words.config(state=DISABLED)
        file_words.config(state=NORMAL)
        file_words.delete(0, END)
        file_words.config(state=DISABLED)
        icon_button.place_forget()
        file_icon.place_forget()
        r1.place_forget()
        r2.place_forget()
        ck.place_forget()
        compiling.place_forget()
        exe.place_forget()
        thumb_convert_exe.place_forget()
        video_convert_exe.place_forget()
        l1.place_forget()
        l2.place_forget()
        words.place_forget()
        file_words.place_forget()
        open_button.place_forget()
        text2.place_forget()
        panel.place_forget()
        text1.place(x = 220, y = 10)
        b1.place(x = 460, y = 400)
        b2.place(x = 460, y = 450)
        thumb_convert_exe.place(x = 460, y = 500)
        video_convert_exe.place(x = 460, y = 550)            
    def converter():
        text1.place_forget()
        b1.place_forget()
        b2.place_forget()
        thumb_convert_exe.place_forget()
        video_convert_exe.place_forget()  
        l1.place(x= 220, y = 10)
        l2.place(x= 650, y = 10)
        open_button.place(x = 800, y = 40)
        words.place(x = 220, y = 40, width = 400)
        file_words.place(x = 650, y = 40, width = 140)
    def move2(i):
        if i<=50:
            credit.place(x=i, y=400)
            credit.after(31, lambda: move2(i)) #after every 100ms
            i = i+1
    def move(i):
        if i<=50:
            convert.place(x=i, y=70)
            convert.after(20, lambda: move(i)) #after every 100ms
            i = i+1
    def move1(i):
        if i<=50:
            install_module.place(x=i, y=20)
            b1.after(24, lambda: move1(i)) #after every 100ms
            i = i+1
    def move5(i):
        if i<=50:
            load_config.place(x=i, y=120)
            b2.after(24, lambda: move5(i)) #after every 100ms
            i = i+1
    def move3(i):
        if i<=50:
            video_convert.place(x=i, y=300)
            b1.after(24, lambda: move3(i)) #after every 100ms
            i = i+1
    def move4(i):
        if i<=50:
            thumb_convert.place(x=i, y=200)
            b1.after(24, lambda: move4(i)) #after every 100ms
            i = i+1



    frame.place(x = 0, y = 0)
    move(20)
    move1(20)
    move2(20)
    move3(20)
    move4(20)    
    move5(20)    

    # app.attributes('-alpha', 0.85)
    # app.iconbitmap('Exe.ico')
    app.title('batch auto upload videos to youtube demo')
    app.geometry('920x480')
    app.resizable(width = False, height = False)
    app.mainloop()



# yt-dlp "bilisearch100:雷电将军" --config-location config.txt
#config.txt
# -o "./%(extractor_key)s/[%(channel_id)s] %(uploader)s/[%(upload_date)s] %(title)s [%(id)s].%(ext)s"
# -ciw
# --console-title
# --extractor-args "youtube:player_client=android,web;comment_sort=top;max_comments=1000"
# --yes-playlist
# --remux-video flv>mp4
# --merge-output-format mp4
# --no-embed-sub
# --no-clean-infojson
# --write-thumbnail
# --sub-lang all
# --convert-subtitles srt
# --write-description
# --write-info-json
# --convert-thumbnails png
# --no-write-comments
# --embed-metadata
# --parse-metadata "title:(?s)(?P<meta_title>.+)"
# --parse-metadata "uploader:(?s)(?P<meta_artist>.+)"
# --parse-metadata " : (?P<meta_synopsis>.*)"
# --parse-metadata " : (?P<meta_album>.*)"
# --abort-on-unavailable-fragment
# --no-write-playlist-metafiles



# def get_compilation_keyword(context):



#     results =[]


#     session = requests.session()



#     topic =context['keyword']
#     duration=context['duration']

#     with open('assets/cookies/bilibili.json') as f:
#         cookie_list: list = json.load(f)
#         # create the cookie jar from the first cookie
#         cookie_jar = requests.utils.cookiejar_from_dict(stringify(cookie_list[0]))
#         # append the rest of the cookies
#         for cookie in cookie_list[1:]:
#             requests.utils.add_dict_to_cookiejar(cookie_jar, stringify(cookie))
#         session.cookies = cookie_jar
#         idlist=[]    

#         outputdir = context["outputdir"]
#         payload = {'search_type': 'video', 'keyword': topic,'order':'pubdate','duration':'0'}
#         r = session.get('http://api.bilibili.com/x/web-interface/search/type', params=payload)
#         # print(r.json())
#         numPages = r.json()['data']['numPages']
#         if numPages>=1:
#             for page in range(numPages,1,-1):
#                 payload = {'search_type': 'video', 'keyword': topic,'order':'pubdate','duration':'0','page':page}
#                 r = session.get('http://api.bilibili.com/x/web-interface/search/type', params=payload)
#                 print(os.getcwd())
#                 os.chdir(outputdir)

#                 if not os.path.exists(str(page)):
#                     os.makedirs(str(page))
#                 os.chdir(str(page))
#                 print('下载视频到目录：',os.getcwd())

#                 links =[]
#                 # print(r.json())
#                 for j,item in enumerate(r.json()["data"]["result"]):
#                     link = item['arcurl']
                    
#                     donelist=[]
#                     context['db'].ensure_table('urls',"!url")
#                     if context['db'].select("urls",'url'):  # -> list of 2 items
#                         donelist = context['db'].select("urls",'url==?',link)
#                     else:
#                         donelist =[]
#                     if len(donelist)>0:
#                         pass
#                     else:                    
#                         ydl_opts = {"retries":10}
#                         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#                             # info = ydl.extract_info(item['arcurl'])
#                             ydl.download([item['arcurl']])
#                         context['db'].ensure_table('urls',"!url")
#                         context['db'].put_one('urls', url=link)    
#                 print('start merge flv files')


#                 mypath=os.getcwd()

#                 cwd = os.getcwd()
#                 files = [os.path.join(cwd, f) for f in os.listdir(cwd) if 
#                 os.path.isfile(os.path.join(cwd, f))]

#                 if len(files)>0:
#                     clips=[]
#                     tmp =[]
#                     for f in files:
#                         if f.endswith('.flv'):
#                             clip = VideoFileClip(f,audio=True)
#                             tmp.append(clip)
#                     for i,item in enumerate(divide_chunks(tmp,5)):
#                         i =str(i)
#                         post_id = uuid2slug(str(uuid.uuid4()))
#                         post_id = post_id.strip('-')
#                         # isadded = getlinkduplicate(context, link)
#                         post_id = addscrapetask(context, post_id, pipelineid='20211012',
#                                             scrapestatus=0, subnsfw=0,
#                                             scrapetaskid='20211012', 
#                                             subreddit_name=topic, post_link=link)                        
#                         print('process part',i,'comment video')
#                         comment_videoclip_i = concatenate_videoclips(item,method="compose")
#                         uploadmp4=topic+i+".mp4"
#                         # uploadmp4 =outputdir+os.sep+str(page)+os.sep+uploadmp4
#                         updatescrapemetakv(context,post_id,'uploadmp4',outputdir+os.sep+str(page)+os.sep+uploadmp4)

#                         link = '\r\n'.join(links)
#                         rapidtags = getkeywordsrapidtags(topic)
#                         print(topic)
#                         print('rapidtags',rapidtags)

#                         title =topic+'合集 compilation '

#                         post_title =  title                        # predes = item['description']
#                         predes="a bot make compilation videos from internet. Any copyright issue pls contact us We will take care of your concerns.original video  from \r\n"
#                         des=predes+ link
#                         tags=rapidtags
#                         # des = predes+'\r\n'
#                         if len(post_title) > 100:
#                             formattitle = post_title[:80]+"|"+topic

#                         title=post_title
#                         description =des[:4000]
#                         type = 'harry'
#                         position = "left"
#                         fontsize = 150                    

#                         updatescrapemetakv(context,post_id,'tags',tags)
#                         updatescrapemetakv(context,post_id,'des',des)
#                         updatescrapemetakv(context,post_id,'rapidtags',rapidtags)
                                
#                         updatescrapemetakv(context, post_id, 'post_type','video')   

#                         updatescrapemetakv(context,post_id,'postnsfw',0)

#                         updatescrapemetakv(context,post_id,'post_title',post_title)

#                         if os.path.exists(uploadmp4):
#                             print('existing',uploadmp4)
#                         else:                
#                             comment_videoclip_i.write_videofile(uploadmp4,threads=8,codec="mpeg4")
#                             updatescrapemetakv(context,post_id,'scrapestatus','1')
                            

#                             gc.collect()

#                             updatescrapemetakv(context,post_id,'videostatus',1) 
#                             # os.chdir('../../../../')
#                             print('mulu--',os.getcwd())
#                             img, thumbpath = thumbnailImage(type, title, post_id, position,
#                                                     fontsize, context['outputdir'])
#                             updatescrapemetakv(context,post_id,'thumbpath',thumbpath)
#                             updatescrapemetakv(context,post_id,'metastatus','1')

                    
#                             upload(context,post_id=post_id)            


#                     print('re generate compilation is done')
#                     os.chdir('../../../../')

#                     # for f in files:
#                         # os.remove(f)

                              
if __name__ == '__main__':
    main()