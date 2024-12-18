from petdb import dbPet

for i in range(1,7):
    fimg=open(f"Import/{i}.jpg","rb")
    img=fimg.read()
    fimg.close()

    dbPet.update("Diseases",["img"],(img,),f"id={i}")
