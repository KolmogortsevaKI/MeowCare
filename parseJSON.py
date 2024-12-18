from petdb import dbPet
import os
import json
import datetime

def scandir(basedir,func):
    for fname in os.listdir(basedir):  # для каждого файла в директории
        if os.path.isfile(basedir+fname):
            func(basedir,fname)
        elif os.path.isdir(basedir+fname):
            scandir(basedir+fname+"/",func)
    
def loaddata(dir,fn):
    if fn.split(".")[-1].lower()!="json": return
    try:
        f=open(dir+fn,"r",encoding="cp866") # cp437 # cp866
        jstr=f.read().replace("\\","/")
        jsd=json.loads(jstr)
        
        iwidth=jsd["images"]["meta"]["width_height"][0]
        iheight=jsd["images"]["meta"]["width_height"][1]
        idev=jsd["images"]["meta"]["device"]
        idate=datetime.datetime.strptime(jsd["images"]["meta"]["date_time"], '%Y-%m-%d %H:%M:%S')
        breed=jsd["images"]["meta"]["breed"]
        age=jsd["images"]["meta"]["age"]
        gender=jsd["images"]["meta"]["gender"]
        imgname=jsd["label"]["label_filename"]
        path=jsd["label"]["label_path"]
        lev1=jsd["label"]["label_disease_lv_1"]=="yes"
        lev2=jsd["label"]["label_disease_lv_2"]=="yes"
        lev3=jsd["label"]["label_disease_lv_3"]=="yes"
        dn=jsd["label"]["label_disease_nm"]
        fimg=open(dir+imgname,"rb")
        # fimg=open(path,"rb")
        img=fimg.read()
        fimg.close()

        res=dbPet.one("Diseases",f"title='{dn}'","id")                                  # Add desease
        if res==None:
            desID=dbPet.insert("Diseases","title",(dn,))
        else:
            desID=int(res[0])

        res=dbPet.one("Breed",f"title='{breed}'","id")       # Add Breed
        if res==None:
            breedID=dbPet.insert("Breed","title",(breed,))
        else:
            breedID=int(res[0])

        catID=dbPet.insert("Cats","user_id,breed_id,nick,age,gender",(1,breedID,"Coteyka",age,gender)) # Add cat

        diagID=dbPet.insert("Diagnostics","cat_id,flag,d_date",(catID,0,idate))    # Add diagnostics

        imgID=dbPet.insert("Image","diagnostics_id,path,device,pos_left,pos_top,height,width,img",     # Add image
                           (diagID,path,idev,0,0,iheight,iwidth,img))

        resID=dbPet.insert("Result","disease_id,diagnostics_id,presence,probability,class_type",    # Add results 1
                           (desID,diagID,lev1,1,1))             
        resID=dbPet.insert("Result","disease_id,diagnostics_id,presence,probability,class_type",    # Add results 2
                           (desID,diagID,lev2,1,2))             
        resID=dbPet.insert("Result","disease_id,diagnostics_id,presence,probability,class_type",    # Add results 3
                           (desID,diagID,lev3,1,3))             
    except Exception as e:
        print(f"{fn} fail with {str(e)}")


#basedir="D:/RemoteJob/_Cheburina/VisCats/TestJson/"
basedir="D:/RemoteJob/_Cheburina/VisCats/Model/"
scandir(basedir,loaddata)
