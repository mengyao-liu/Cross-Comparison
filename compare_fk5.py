import numpy as np


me = np.loadtxt('coreid_fk5.dat',usecols=(0,1,2),dtype={'names': ('source','ra','dec'), 'formats': ('|S4',np.float,np.float)})

shuo = np.loadtxt('outflow.txt',usecols=(0,2,4),dtype={'names': ('source','ra','dec'), 'formats': ('|S6',np.float,np.float)})

for i in np.arange(len(me['ra'])):
    for j in np.arange(len(shuo['ra'])):
        if abs(me['ra'][i]-shuo['ra'][j])<0.00027 and abs(me['dec'][i]-shuo['dec'][j])<0.00027:
            print me['source'][i], me['ra'][i], shuo['source'][j], shuo['ra'][j]