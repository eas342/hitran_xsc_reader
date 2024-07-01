import numpy as np

def read_xc(filename,xunit='micron'):
    xsc = np.loadtxt(filename,
                    skiprows=1)
    with open(filename) as f:
        xsc_head = f.readline()
        
    meta = {}
    meta['molecule'] = xsc_head[0:20]
    meta['fst'] = float(xsc_head[20:30])
    meta['fend'] = float(xsc_head[30:40])
    meta['npt'] = int(xsc_head[40:47])
    meta['T'] = float(xsc_head[47:54])
    meta['P'] = float(xsc_head[54:60])
    meta['max'] = float(xsc_head[60:70])
    meta['R'] = float(xsc_head[70:75])
    meta['name'] = str(xsc_head[75:90])
    meta['broadener'] = xsc_head[94:97]
    meta['ref'] = xsc_head[97:100]
    
    freq = np.linspace(meta['fst'],meta['fend'],meta['npt'])
    if xunit == 'micron':
        x = 1e4/freq
    else:
        x = freq
    
    y = xsc.ravel()[0:meta['npt']]
    
    return x,y,meta