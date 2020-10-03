# coding=utf8
import csv
import json
import ast

# load vehicle data
pictures = {}

victims = {}
victim_count = 0
with open('driverProperty2.csv', encoding='utf-8', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    map_job = {
        '1. ກ/ກ': 'ກ/ກ',
        '2. ນ/ຮ': 'ນ/ຮ',
        '3. ນ/ສ': 'ນ/ສ',
        '4. ພ/ງ': 'ພ/ງ',
        '5. ທ/ຫ': 'ທ/ຫ',
        '6. ຕຫຼ': 'ຕຫຼ',
        '7. ເຮັດນາ': 'ເຮັດນາ',
        '8. ຫວ່າງງານ': 'ຫວ່າງງານ',
        '9. ຄ້າຂາຍ': 'ຄ້າຂາຍ',
        '10. ນັກທຸລະກິດ': 'ນັກທຸລະກິດ',
        '11. ທາງອື່ນໆ': 'ອື່ນໆ'
    }
    for row in spamreader:
        if victim_count > 0:
            if row[0] not in victims:
                victims[row[0]] = []
            job = row[1]
            if job in map_job:
                job = map_job[job]
            victim_data = '{"_localId": "'+row[11]+'", "ຊື່": "'+row[3]+'", "ບ້ານ": "'+row[5]+'", "ອາຍຸ": '+row[6]+', "ແຂວງ":"'+row[7]+'", "ໜ່ວຍ":"'+row[8]+'", "ອາຊີບ":"'+job+'", "ເມືອງ":"'+row[9]+'", "ສັນຊາດ":"'+row[2]+'", "ລາຍເຊັນ":"", "ໂທລະສັບ":"'+row[10]+'", "ເລກທະບຽນ":"'+row[4]+'"}'
            victims[row[0]].append(victim_data)
        victim_count = victim_count + 1

judges = {}
judge_count = 0
with open('driverProperty1.csv', encoding='utf-8', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        if judge_count > 0:
            if row[0] not in judges:
                judges[row[0]] = []
            judge_data = '{"_localId": "'+row[1]+'", "ຜູ້ເຂົ້າຮ່ວມການຊັນນະສູດ": "'+row[2]+'", "ຄຳອະທິບາຍ": "'+row[3]+'"}'
            judges[row[0]].append(judge_data)
        judge_count = judge_count + 1

# load vehicle data
vehicles = {}
vehicle_count = 0
with open('vehicle.csv', encoding='utf-8', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    map_vehicle_type = {
        '1. ລົດຈີນ': 'ລົດຈີນ',
        '2. ລົດເກົ່າຫຼີ': 'ລົດເກົ່າຫຼີ',
        '3. ລົດໄທ-ຢີ່ປຸ່ນ': 'ລົດໄທ-ຢີ່ປຸ່ນ',
        '4. ລົດອເມລິກາ': 'ລົດອເມລິກາ',
        '5. ລົດລັດເຊຍ': 'ລົດລັດເຊຍ',
        '6. ລົດເຢຍລະມັນ': 'ລົດເຢຍລະມັນ',
        '7. ທາງອື່ນໆ': 'ອື່ນໆ'
    }
    map_vehicle_condition = {
        '1. ດີ': 'ດີ',
        '2. ບໍ່ດີ': 'ບໍ່ດີ',
        '3. ໄຟຕາບໍ່ຮຸ່ງ': 'ໄຟຕາບໍ່ຮຸ່ງ',
        '4. ໄຟສັນຍານ': 'ໄຟສັນຍານ',
        '5. ພວງມະໄລເສລີ': 'ພວງມະໄລເສລີ',
        '6. ເບກບໍ່ມີ': 'ເບກບໍ່ມີ',
        '7. ຢ່າງບໍໍ່ດີ': 'ຢ່າງບໍ່ດີ',
        '8. ຄັນສົ່ງບໍ່ດີ': 'ຄັນສົ່ງບໍ່ດີ',
        '9. ເຕັກນິກອື່ນໆ': 'ເຕັກນິກອື່ນໆ',
        '10. ທາງອື່ນໆ': 'ທາງອື່ນໆ',
    }
    for row in spamreader:
        if vehicle_count > 0:
            if row[0] not in vehicles:
                vehicles[row[0]] = []
            vehicle_type = row[3]
            if vehicle_type in map_vehicle_type:
                vehicle_type = map_vehicle_type[vehicle_type]
            vehicle_condition = row[1]
            if vehicle_condition in map_vehicle_condition:
                vehicle_condition = map_vehicle_condition[vehicle_condition]
            vehicle_data = '{"_localId": "'+row[2]+'", "ປະເພດລົດ": "'+ row[4] +'", "ສະພາບເຕັກນິກ": "'+vehicle_condition+'", "ຊະນິດລົດທີ່ເກີດອຸປະຕິເຫດ": "'+vehicle_type+'"}'
            vehicles[row[0]].append(vehicle_data)
        vehicle_count = vehicle_count + 1

count = 0
header = []
def construct_data(uuid, row):
    data = []

    key = "driverລົດ"
    value = '[]'
    if uuid in vehicles:
        value = '['+(",".join(vehicles[uuid]))+']'
    data.append('"'+key+'":'+value+'')

    detail_data = []
    key = '_localId'
    value = row[header.index('incidentDetails_id')]
    detail_data.append('"'+key+'": "'+value+'"')

    key = 'ບ້ານ'
    value = row[header.index(key)]
    detail_data.append('"'+key+'": "'+value+'"')

    key = 'ແຂວງ'
    value = row[header.index(key)]
    detail_data.append('"'+key+'": "'+value+'"')

    key = 'ສາຫັດ'
    value = row[header.index(key)]
    value = int(value) if value else 0
    detail_data.append('"'+key+'": '+str(value))

    key = 'ເມືອງ'
    value = row[header.index(key)]
    detail_data.append('"'+key+'": "'+value+'"')

    key = 'ສົມຄວນ'
    value = row[header.index(key)]
    value = int(value) if value else 0
    detail_data.append('"'+key+'": '+str(value))

    key = 'ເລກນ້ອຍ'
    value = row[header.index(key)]
    value = int(value) if value else 0
    detail_data.append('"'+key+'": '+str(value))

    key = 'ປະເພດທາງ'
    value = []
    if row[header.index(key)]: 
        value = ast.literal_eval(row[header.index(key)])
    detail_data.append('"'+key+'": ["'+'","'.join(value)+'"]')

    key = 'ລົດເປ່ເພ'
    value = ast.literal_eval(row[header.index(key)])
    detail_data.append('"'+key+'": ["'+'","'.join(value)+'"]')

    key = 'ເສຍຊີວິດ'
    value = row[header.index(key)]
    value = int(value) if value else 0
    detail_data.append('"'+key+'": '+str(value))

    key = 'ຮູບການຕໍາ'
    value = ast.literal_eval(row[header.index(key)])
    map_value = { 'ຕໍາຄົນຍ່າງ/': 'ຕໍາຄົນຍ່າງ', ' ດາດ': 'ດາດ' }
    temp = []
    for each in value:
        if each in map_value:
            each = map_value[each]
        temp.append(each)
    value = temp
    detail_data.append('"'+key+'": ["'+'","'.join(value)+'"]')

    key = 'ເລກທີຄະດີ'
    value = row[header.index(key)]
    detail_data.append('"'+key+'": "'+value+'"')

    key = 'ຄົນບາດເຈັບ'
    value = ast.literal_eval(row[header.index(key)])
    detail_data.append('"'+key+'": ["'+'","'.join(value)+'"]')

    key = 'ມາດຕາລະເມີດ'
    value = ast.literal_eval(row[header.index(key)])
    detail_data.append('"'+key+'": ["'+'","'.join(value)+'"]')

    key = 'ສະພາບແວດລ້ອມ'
    value = ast.literal_eval(row[header.index(key)])
    detail_data.append('"'+key+'": ["'+'","'.join(value)+'"]')

    key = 'ສະພາບຜູ້ຂັບຂີ່'
    value = row[header.index(key)]
    detail_data.append('"'+key+'": "'+value+'"')

    key = 'ບາດເຈັບ-ເສຍຊີວິດ'
    value = ast.literal_eval(row[header.index(key)])
    detail_data.append('"'+key+'": ["'+'","'.join(value)+'"]')

    key = 'ວັັນເດືອນປີເກີດເຫດ'
    value = row[header.index(key)]
    map_value = { 'ອາທິດ': 'ວັນອາທິດ', 'ພະຫັດ': 'ວັນພະຫັດ' }
    if value in map_value:
        value = map_value[value]
    detail_data.append('"ວັນເດືອນປີເກີດເຫດ": "'+value+'"')
    
    key = 'ຄຳອະທິບາຍເພີ້ມເຕີມ'
    value = row[header.index(key)]
    detail_data.append('"'+key+'": "'+value.replace("\n", "\\n")+'"')
    
    key = 'ປະເພດພາຫະນະທີ່ເກີດອຸປະຕິເຫດ'
    value = row[header.index(key)]
    detail_data.append('"'+key+'": "'+value+'"')

    key = 'driverIncidentDetails'
    value = '{'+(",".join(detail_data))+'}'
    data.append('"'+key+'":'+value+'')

    key = 'driverຮູບພາບ'
    value = '[]'
    if uuid in pictures:
        value = '['+(",".join(vehicles[uuid]))+']'
    data.append('"'+key+'": '+value+'')

    key = 'driverຜູ້ເກີດອຸປະຕິເຫດຝ່າຍ'
    value = '[]'
    if uuid in victims:
        value = '['+(",".join(victims[uuid]))+']'
    data.append('"'+key+'":'+value+'')

    key = 'driverຜູ້ເຂົ້າຮ່ວມການຊັນນະສູດ'
    value = '[]'
    if uuid in judges:
        value = '['+(",".join(judges[uuid]))+']'
    data.append('"'+key+'":'+value+'')

    return '{'+(",".join(data))+'}'

print('#!/bin/bash')
print('psql postgres postgres <<EOF')
print('SET TIMEZONE="Asia/Vientiane";')
print('delete from data_recordauditlogentry; delete from data_driverrecordcopy; delete from data_driverrecord; delete from grout_record;')
with open('records.csv', encoding='utf-8', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        if count == 0:
            header = row
        else:

            uuid = row[header.index('record_id')]
            created = row[header.index('created')]
            modified = row[header.index('modified')]
            occurred_from = row[header.index('occurred_from')]
            occurred_to = row[header.index('occurred_to')]
            geom = "ST_SetSRID(ST_MakePoint("+row[header.index('lon')]+", "+row[header.index('lat')]+"),4326)"
            data = construct_data(uuid, row)
            schema_id = '6a6822af-e1fd-48c1-adc8-c6cf09b2a0a9' #hardcode fixed with seed script
            location_text = row[header.index('location_text')].replace("'", "''")
            archived = 'false'


            print("insert into grout_record (uuid,created,modified,occurred_from,occurred_to,geom,data,schema_id,location_text,archived) \
                    values ('"+ uuid +"','"+ created +"','"+ modified +"','"+ occurred_from +"','"+ occurred_to +"', "+geom+",'"+data+"','"+schema_id+"','"+location_text+"',"+archived+");")

            weather = row[header.index('weather')]
            if weather == 'None': weather = '' 
            light = row[header.index('light')]
            city = row[header.index('city')]
            city_district = row[header.index('city_district')]
            county = row[header.index('county')]
            neighborhood = row[header.index('neighborhood')]
            road = row[header.index('road')]
            state = row[header.index('state')]
            print("insert into data_driverrecord (record_ptr_id,weather,light,city,city_district,county,neighborhood,road,state,merged_and_updated,merged_uuid) \
                    values ('"+uuid+"','"+weather+"','"+light+"','"+city+"','"+city_district+"','"+county+"','"+neighborhood+"','"+road+"','"+state+"',false,null);")

        #if count > 1: break
        count = count + 1
        print('\n')
print('EOF')
