import numpy as np

def read_xc(filename,xunit='wave'):
    xsc = np.loadtxt(xscfile,
                    skiprows=1)
    with open(xscfile) as f:
        xsc_head = f.readline()
        
    meta = {}
    meta['molecule'] = xsc_head[0:20]
    meta['fst'] = float(xsc_head[20:30])
    meta['fend'] = float(xsc_head[30:40])
    meta['npt'] = int(xsc_head[40:47])
    meta['T'] = xsc_head[47:54]
    meta['P'] = xsc_head[54:60]
    meta['max'] = xsc_head[60:70]
    meta['R'] = xsc_head[70:75]
    meta['name'] = xsc_head[75:90]
    meta['broadener'] = xsc_head[94:97]
    meat['ref'] = xsc_head[97:100]
    
    
    return x,y,meta