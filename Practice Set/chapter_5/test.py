# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
s="janhavi jayram rane"
dis={}
for ch in s:
    if ch in dis:
        dis[ch]+=1
    else:
        dis[ch]=1
        
print(dis)