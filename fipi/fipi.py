def passtojson(noz,z):
    z=z.replace('"',"'")
    a=open("fipi/fipi.json").read()[:-1]
    open("fipi/fipi.json","w").write(a+',\n    "'+noz+'" : "'+z+'"}')