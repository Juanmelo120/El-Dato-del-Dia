import json,sys
d=json.load(open('src/data/carruseles.json'))
a,b=int(sys.argv[1]),int(sys.argv[2])
for c in d[a-1:b]:
  print('##',c['n'],c['tema'],'|',c['titulo'])
  for x in c['datos']: print(x['n'],x['titular'],'|',x['gancho'])
