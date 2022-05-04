# -*- coding:utf-8 -*-
from contextlib import closing
import requests, json, re, os, sys, random, qrcode, pygame, shutil
from ipaddress import ip_address
from subprocess import Popen, PIPE
import urllib, math
import time
from PIL import Image,ImageDraw,ImageFont,ImageFilter
from io import BytesIO


music_path = "./0/"           #音乐文件夹
source_path = "./1/"          #图片来源路径
save_path = "./2/"            #图片修改后的保存路径
    


class ShaDiao(object):
    def run(self):
        


        
        if not os.path.exists(save_path):
            os.mkdir(save_path)

        file_names=os.listdir(source_path)

        #fl = open(os.path.join(save_path,'list.txt'),'w+')

        for i in range(len(file_names)):
            x=self.com_pic3(source_path + file_names[i])
            new_pic_name = int(round(time.time() * 1000))
            str_new_pic_name = str(new_pic_name)
            x.save(os.path.join(save_path, str_new_pic_name+'.jpg'), quality=100)
            print(file_names[i]+' 处理完毕！')
            #self.tran_single(os.path.join(save_path, str_new_pic_name), str_new_pic_name)
            #var = 'file '+'Fragment_'+str_new_pic_name+'.mp4'
            #fl.writelines(var)
            #fl.write('\n')

        #fl.close()
        #self.tran_all()
        #filepath_0 = os.path.join(save_path)#确定TEMP目录
        #shutil.rmtree(filepath_0)#执行删除目录操作
        #timemark = str(round(time.time() * 1000))
        #shutil.move(os.path.join('output.mp4'),os.path.join('video_temp',timemark+'.mp4'))#执行将视频移动到video_temp的操作
        

    def com_pic3(self, img_url):#合并图片3，这个是处理封面的，优化完成
        img = Image.open(img_url)
        w, h = img.size
        if(w>=h*16/9):
                re_bg_w=math.ceil(1080*w/h)
                re_bg_h=1080
                re_fg_w=1920
                re_fg_h=math.ceil(1920*h/w)
        else:
                re_bg_w=1920
                re_bg_h=math.ceil(1920*h/w)
                re_fg_h=1080
                re_fg_w=math.ceil(1080*w/h)

        back_img_tmp = img.resize((re_bg_w,re_bg_h),Image.ANTIALIAS)#把原图放大为背景图
        img2 = img.resize((re_fg_w,re_fg_h),Image.ANTIALIAS)#把原图处理成前景图
        bg_pointx = int((re_bg_w-1920)/2)
        bg_pointy = int((re_bg_h-1080)/2)
        back_img_tmp2 = back_img_tmp.crop([bg_pointx,bg_pointy,bg_pointx+1920,bg_pointy+1080])#裁切背景图
        img = back_img_tmp2.filter(ImageFilter.GaussianBlur(radius=18))#模糊背景图
        fg_pointx = int((1920-re_fg_w)/2)
        fg_pointy = int((1080-re_fg_h)/2)
        img.paste(img2, (fg_pointx,fg_pointy,fg_pointx+re_fg_w,fg_pointy+re_fg_h))#拼合
        bg = Image.new("RGB", img.size, (255,255,255))#这两步是用来转换的
        bg.paste(img)
        
        return bg
        
    def tran_single(self, input, new_pic_name):
        output = os.path.join(save_path,"Fragment_"+new_pic_name)
        finishcode = "ffmpeg -loop 1 -i "+input+".jpg -r 25 -t 5 -y "+output+".mp4"
        os.system(finishcode)
        os.remove(input+".jpg")

    def tran_all(self):
        music_names=os.listdir(music_path)
        pick = random.randint(0,len(music_names))
        os.rename(os.path.join(music_path, music_names[pick]),os.path.join(music_path, "input_music.mp3"))
        


        
        music = os.path.join(music_path, "input_music.mp3")
        list_txt = os.path.join(save_path, "list.txt")
        #output = os.path.join(save_path,"output_no_audio")
        #input_mp3 = os.path.join(source_path,"input.mp3")
        
        finishcode2 = "ffmpeg -f concat -i "+list_txt+" -ss 00:00:00 -t 00:03:20"+" -i "+music+" -c copy "+"output.mp4"
        os.system(finishcode2)
        os.remove(music)

        

if __name__ == '__main__':
        shadiao = ShaDiao()
        shadiao.run()
