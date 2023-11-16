import datetime
stunda = datetime.datetime.now().hour

if 8 <= stunda < 12:
    print("labrit!")
elif 12 <= stunda < 17:
    print("labdien!")
else:
    print("labvakar!")
