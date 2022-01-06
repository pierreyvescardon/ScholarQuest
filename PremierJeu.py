from typing import Union
def sun_angle(time: str):
    list=time.split(":")

    if int(list[0])<6 or int(list[0])>18 or ((int(list[0])==18) and (int(list[1])>0)):
        reponse="I don't see the sun!"
        return reponse
    else:
        reponse=float(((float(list[0])-6)*15)+(float(list[1])*0.25))
        return reponse


a="18:01"

print(sun_angle(a))
