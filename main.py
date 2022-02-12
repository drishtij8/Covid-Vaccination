import requests
import json
import push
import otp

url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"

res = requests.get(url = url)
email= input("Enter your email-id:")

get_otp = otp.generateOTP()
push.push_notification(email=email,title="OTP",msg=str(get_otp))
put_otp = input("Enter the otp:")

if put_otp == get_otp:
    data = res.json()  #returns dict
    print(data)
    state_name = input("Enter the state name:")
    for i in data["states"]:
        if state_name == i["state_name"]:
            val = i["state_id"]

    state_id = str(val)

    url2 = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/" + state_id

    res2 = requests.get(url = url2)

    data2 = res2.json()  #returns dict
    print(data2)

    district_name = input("Enter the district name:")
    for i in data2["districts"]:
        if district_name == i["district_name"]:
            val2 = i["district_id"]

    district_id = str(val2)

    d = input("Enter the date:")
    date = "&date="+str(d)

    url3 = "https://cdn-api.co-vin.in/" \
           "api/v2/appointment/sessions/public/findByDistrict?" \
           "district_id=" + district_id + date

    res3 = requests.get(url = url3)

    data3 = res3.json()
    centers = data3["sessions"]
    for i in centers :
        if i["available_capacity"] > 0 and i["vaccine"] == "COVISHIELD":
            push.push_notification(email=email,title="slots",msg=i["name"]+ i["address"] + str(i["available_capacity"]))
            print(i)

else:
    print("OTP is wrong.")