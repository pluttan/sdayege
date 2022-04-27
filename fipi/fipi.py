def passtojson(noz,z):
    z=z.replace('"',"'")
    a=open("fipi.json").read()[:-1]
    open("fipi.json","w").write(a+',\n    "'+noz+'" : "'+z+'"}')