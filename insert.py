# import os

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# import django
# django.setup()
# from project.models import District, Genre, Region

# from accounts.models import User
# from faker import Faker



# fake = Faker()

# genres = ["Horror", "Tarixiy", "Fantastika", "Adabiyot", "Biografiya", "San'at", "Sayohat", "Detektiv", "Qo'llanma", "Din", "Texnologiya", "Komiks", "She'riyat ", "Psixologiya", "Komediya"]

# for x in District.objects.all():
    
#     x.name = ' '.join(x.name.split(' ').pop())
    
#     x.save()
    
    
import sys
sys.dont_write_bytecode = True

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()


from project.models import *




data = [
    {
        "name": "Farg'ona",
        "districts": [
            {
                "name": "Buvayda tumani"
            },
            {
                "name": "Oltiariq tumani"
            },
            {
                "name": "Bag'dod tumani"
            },
            {
                "name": "Beshariq tumani"
            },
            {
                "name": "Dang'ara tumani"
            },
            {
                "name": "Farg'ona tumani"
            },
            {
                "name": "Furqat tumani"
            },
            {
                "name": "Qo'shtepa tumani"
            },
            {
                "name": "Quva tumani"
            },
            {
                "name": "Rishton tumani"
            },
            {
                "name": "So'x tumani"
            },
            {
                "name": "Toshloq tumani"
            },
            {
                "name": "Uchko'prik tumani"
            },
            {
                "name": "O'zbekiston tumani"
            },
            {
                "name": "Yozyovon tumani"
            },
            {
                "name": "Farg'ona shahar"
            },
            {
                "name": "Marg'ilon shahar"
            },
            {
                "name": "Qo'qon shahar"
            },
            {
                "name": "Quvasoy shahar"
            }
        ]
    },
    {
        "name": "Andijon",
        "districts": [
            {
                "name": "Asaka tumani"
            },
            {
                "name": "Andijon shahar"
            },
            {
                "name": "Andijon tumani"
            },
            {
                "name": "Bo'ston tumani"
            },
            {
                "name": "Buloqboshi tumani"
            },
            {
                "name": "Izboskan tuman"
            },
            {
                "name": "Jalaquduq tumani"
            },
            {
                "name": "Marhamat tumani"
            },
            {
                "name": "Oltinko'l tuman"
            },
            {
                "name": "Paxtaobod tumani"
            },
            {
                "name": "Shahrixon tuman"
            },
            {
                "name": "Ulug'nor tumani"
            },
            {
                "name": "Xo'jaobod tumani"
            }
        ]
    },
    {
        "name": "Namangan",
        "districts": [
            {
                "name": "Pop tumani"
            },
            {
                "name": "Namangan shahar"
            },
            {
                "name": "Chortoq tumani"
            },
            {
                "name": "Chust tumani"
            },
            {
                "name": "Kosonsoy tumani"
            },
            {
                "name": "Mingbuloq tumani"
            },
            {
                "name": "Namangan tumani"
            },
            {
                "name": "Norin tumani"
            },
            {
                "name": "To'raqo'rg'on tumani"
            },
            {
                "name": "Uchqo'rg'on tumani"
            },
            {
                "name": "Uychi tumani"
            },
            {
                "name": "Yangiqo'rg'on tumani"
            },
            {
                "name": "Davlatobod tumani"
            },
            {
                "name": "Yangiqo'rg'on tumani"
            }
        ]
    },
    {
        "name": "Jizzax",
        "districts": [
            {
                "name": "Arnasoy tumani"
            },
            {
                "name": "Baxmal tumani"
            },
            {
                "name": "Do'stlik tumani"
            },
            {
                "name": "Forish tumani"
            },
            {
                "name": "G'allaorol tumani"
            },
            {
                "name": "Sharof Rashidov tumani"
            },
            {
                "name": "Mirzacho'l tumani"
            },
            {
                "name": "Paxtakor tumani"
            },
            {
                "name": "Yangiobod tumani"
            },
            {
                "name": "Zomin tumani"
            },
            {
                "name": "Zafarobod tumani"
            },
            {
                "name": "Zarbdor tumani"
            },
            {
                "name": "Jizzax shahri"
            }
        ]
    },
    {
        "name": "Samarqand",
        "districts": [
            {
                "name": "Bulung'ur tumani"
            },
            {
                "name": "Ishtixon tumani"
            },
            {
                "name": "Jomboy tumani"
            },
            {
                "name": "Kattaqo'rg'on tumani"
            },
            {
                "name": "Qo'shrabot tumani"
            },
            {
                "name": "Narpay tumani"
            },
            {
                "name": "Nurobod tumani"
            },
            {
                "name": "Oqdaryo tumani"
            },
            {
                "name": "Paxtachi tumani"
            },
            {
                "name": "Payariq tumani"
            },
            {
                "name": "Pastdarg'om tumani"
            },
            {
                "name": "Samarqand tumani"
            },
            {
                "name": "Toyloq tumani"
            },
            {
                "name": "Urgut tumani"
            },
            {
                "name": "Samarqand shahri"
            }
        ]
    },
    {
        "name": "Qashqadaryo",
        "districts": [
            {
                "name": "Qarshi shahar"
            },
            {
                "name": "Dehqonobod tumani"
            },
            {
                "name": "Kitob tumani"
            },
            {
                "name": "Chiroqchi tumani"
            },
            {
                "name": "G'uzor tumani"
            },
            {
                "name": "Qamashi tumani"
            },
            {
                "name": "Qarshi tumani"
            },
            {
                "name": "Koson tumani"
            },
            {
                "name": "Kasbi tumani"
            },
            {
                "name": "Mirishkor tumani"
            },
            {
                "name": "Muborak tumani"
            },
            {
                "name": "Nishon tumani"
            },
            {
                "name": "Shahrisabz tumani"
            },
            {
                "name": "Yakkabog' tumani"
            },
            {
                "name": "Ko'kdala tumani"
            }
        ]
    },
    {
        "name": "Surxondaryo",
        "districts": [
            {
                "name": "Angor tumani"
            },
            {
                "name": "Boysun tumani"
            },
            {
                "name": "Denov tumani"
            },
            {
                "name": "Jarqo'rg'on tumani"
            },
            {
                "name": "Qiziriq tumani"
            },
            {
                "name": "Qiziriq tumani"
            },
            {
                "name": "Qumqo'rg'on tumani"
            },
            {
                "name": "Muzrabot tumani"
            },
            {
                "name": "Oltinsoy tumani"
            },
            {
                "name": "Sariosiyo tumani"
            },
            {
                "name": "Sherobod tumani"
            },
            {
                "name": "Sho'rchi tumani"
            },
            {
                "name": "Termiz tumani"
            },
            {
                "name": "Uzun tumani"
            }
        ]
    },
    {
        "name": "Xorazm",
        "districts": [
            {
                "name": "Bog'ot tumani"
            },
            {
                "name": "Gurlan tumani"
            },
            {
                "name": "Xonqa tumani"
            },
            {
                "name": "Hazorasp tumani"
            },
            {
                "name": "Xiva tumani"
            },
            {
                "name": "Qo'shko'pir tumani"
            },
            {
                "name": "Shovot tumani"
            },
            {
                "name": "Urganch tumani"
            },
            {
                "name": "Yangiariq tumani"
            },
            {
                "name": "Yangibozor tumani"
            },
            {
                "name": "Tuproqqal'a tumani"
            },
            {
                "name": "Xiva shahri"
            }
        ]
    },
    {
        "name": "Buxoro",
        "districts": [
            {
                "name": "Olot tumani"
            },
            {
                "name": "Buxoro tumani"
            },
            {
                "name": "G'ijduvon tumani"
            },
            {
                "name": "Jondor tumani"
            },
            {
                "name": "Kogon tumani"
            },
            {
                "name": "Qorako'l tumani"
            },
            {
                "name": "Qorovulbozor tumani"
            },
            {
                "name": "Peshku tumani"
            },
            {
                "name": "Romitan tumani"
            },
            {
                "name": "Shofirkon tumani"
            },
            {
                "name": "Vobkent tumani"
            },
            {
                "name": "Buxoro shahri"
            }
        ]
    },
    {
        "name": "Navoiy",
        "districts": [
            {
                "name": "Konimex tumani"
            },
            {
                "name": "Karmana tumani"
            },
            {
                "name": "Qiziltepa tumani"
            },
            {
                "name": "Xatirchi tumani"
            },
            {
                "name": "Navbahor tumani"
            },
            {
                "name": "Nurota tumani"
            },
            {
                "name": "Tomdi tumani"
            },
            {
                "name": "Uchquduq tumani"
            }
        ]
    },
    {
        "name": "Qoraqalpog'iston",
        "districts": [
            {
                "name": "Amudaryo tumani"
            },
            {
                "name": "Beruniy tumani"
            },
            {
                "name": "Chimboy tumani"
            },
            {
                "name": "Ellikqal'a tumani"
            },
            {
                "name": "Kegeyli tumani"
            },
            {
                "name": "Mo'ynoq tumani"
            },
            {
                "name": "Nukus tumani"
            },
            {
                "name": "Qanliko'l tumani"
            },
            {
                "name": "Qo'ng'irot tumani"
            },
            {
                "name": "Qorao'zak tumani"
            },
            {
                "name": "Shumanay tumani"
            },
            {
                "name": "Taxtako'pir tumani"
            },
            {
                "name": "To'rtko'l tumani"
            },
            {
                "name": "Xo'jayli tumani"
            },
            {
                "name": "Taxiatosh tumani"
            },
            {
                "name": "Bo'zatov tumani"
            },
            {
                "name": "Boyovut tumani"
            }
        ]
    },
    {
        "name": "Sirdaryo",
        "districts": [
            {
                "name": "Oqoltin tumani"
            },
            {
                "name": "Guliston tumani"
            },
            {
                "name": "Xovos tumani"
            },
            {
                "name": "Mirzaobod tumani"
            },
            {
                "name": "Sayxunobod tumani"
            },
            {
                "name": "Sardoba tumani"
            },
            {
                "name": "Sirdaryo tumani"
            },
            {
                "name": "Yangiyer shahri"
            },
            {
                "name": "Shirin shahri"
            },
            {
                "name": "Guliston shahri"
            }
        ]
    },
    {
        "name": "Toshkent",
        "districts": [
            {
                "name": "Bekobod tumani"
            },
            {
                "name": "Bo'stonliq tumani"
            },
            {
                "name": "Bo'ka tumani"
            },
            {
                "name": "Chinoz tumani"
            },
            {
                "name": "Qibray tumani"
            },
            {
                "name": "Ohangaron tumani"
            },
            {
                "name": "Oqqo'rg'on tumani"
            },
            {
                "name": "Parkent tumani"
            },
            {
                "name": "Piskent tumani"
            },
            {
                "name": "Quyi chirchiq tumani"
            },
            {
                "name": "O'rta Chirchiq tumani"
            },
            {
                "name": "Yangiyo'l tumani"
            },
            {
                "name": "Yuqori Chirchiq tumani"
            },
            {
                "name": "Zangiota tumani"
            },
            {
                "name": "Yunusobod tumani"
            }
        ]
    }
]


for region in data:
    rname = region['name'] + ' viloyati'

    rg = Region.objects.create(name=rname)

    for district in region['districts']:
        dname = district['name']

        District.objects.create(region=rg, name=dname)

