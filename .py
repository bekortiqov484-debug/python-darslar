     #   Bir nechta shartlarni tekshirish

    #if = agar
    #else = aks holda
    #elif = aks holda,agar
    #if elif else =dastur davomida bir nechta shartlar tekshirish

#Python avval if shartini tekshiradi, shart bajarilmasa
#elif ga o'tadi, birinchi elif sharti bajarilmasa keyingi elif ga o'tadi va hokazo davom etaveradi.

#yosh = int(input('Yoshingiz nechida? '))
#if yosh<=4:
 #  print('Sizga kirish bepul.')elif yosh<=12:
 #  print('Sizga kirish 5000 so\'m')
#else:
    #print('Sizga kirish 10000 so\'m')

     #True = haqiyqiy yoki to'g'ri
    #False =yolg'on


#Agar yosh<=4 sharti bajarilmasa, keyingi elif yosh<=12 sharti tekshiriladi, agar shart bajarilsa quyidagi natija chiqadi:

#Avval aytganimizdek,  if-elif-else zanjirida bit nechta elif lar bo'lishi mumkin.
#Misol uchun, hayvonot bog'i qariyalar uchun chegirma e'lon qilsa, kodimizni quyidagicha o'zgartirishimiz mumkin:

#yosh = int(input('Yoshingiz nechida? '))
#if yosh<=4: # yosh bolalarga bepul
 #   price = 0
#elif yosh<=12: # 4 dan 12 yoshgacha 5000 so'm
 #   price = 5000
#elif yosh<65: # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
 #   price = 10000
#else: # qariyalarga esa 8000 so'm
 #   price = 8000
#print(f"Sizga kirish {price} so'm")


     # if elif else ketma-ketligini tekshirish


         #AND = "va"
     #shartlarning barchasi bajarilishini tekshirishda ishlatiladi.
 #AND operatori bilan yozilgan shartlarning barchasi bajarilgandagina TRUE qiymati qaytadi,
 #agar shartlardan biri bajarilmay qolsa ham FALSE qiymati qaytadi.

#kun = input("Bugun nima kun?")
#harorat = float(input("Havo harorati qanday?"))
#if kun.lower()=='yakshanba' and harorat>=30:
  #  print("Cho'milgani ketdik!")
#elif kun.lower()=='yakshanba' and harorat<30:
   # print("Uyda dam olamiz!")



       #OR  ="yoki"
 #ikki va undan ko'p shartlardan biri bajarilishini tekshirishda ishlatiladi.

#kun = input("Bugun nima kun?>>>")
#if kun.lower()=='shanba' or kun.lower()=='yakshanba':
 #   print('Bugun dam olish kuni.')
#else:
 #  print('Bugun ish kuni.')

 #2-qatrodagi or operatoriga e'tibor qiling, bu operator kun.lower()=='shanba'
   #yoki kun.lower()=='yakshanba' shartlaridan biri bajarilsa TRUE qiymatini qaytaradi


    #bolen =turli ifodalar solishtirishda True yoki False qiymatlaring qaytishi "boolen"(mantiqiy)
    # qiymat deb ataladi.

#narh = 15000 # mijoz 15000 so'mga taom oldi.
#choy = True # mijoz choy ham oldi
#salat = False # mijoz salat olmadi

#if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
 #   narh = narh + 10000 # narhga 10000 so'm qo'shamiz
#elif choy or salat: # agar choy yoki salat olgan bo'lsa
   # narh = narh + 5000 # narhga 5000 so'm qo'shamiz

#print(f"Jami {narh} so'm") # yakuniy narxni chiqaramiz


       # in - operatori yordamida bir royxat tarkibida ma'lum bir element borligini tekshiramiz.

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#'manti' in menu # menu da manti bormi?


menu = ['osh','qazonkabob','shashlik','norin','somsa']
ovqat = input('Nima ovqat yeysiz?>>>')
if ovqat.lower() in menu:
 print('Buyurtma qabul qilindi.')
else:
 print('Afsuski bizda bunday ovqat yo\'q')


     # not in = operatori yordamida bir elemant ro'yxatda yo'ligini tekshiramiz


#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#ovqat = input('Nima ovqat yeysiz?>>>')
#if ovqat.lower() not in menu:
 #   print('Afsuski bizda bunday ovqat yo\'q')
#else:
 #   print('Buyurtma qabul qilindi.')



#print("Hello World")