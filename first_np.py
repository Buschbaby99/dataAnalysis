from ctypes import sizeof
import numpy as np
import matplotlib.pyplot as plt



#cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 21.8, 21.3, 20.9, 20.1]
#
#C = np.array(cvalues)
#
#print(C, type(C))
#
#
#print(C * 9 / 5 + 32)
#
#
##plt.plot(C)
##plt.show()
#
#a = np.arange(1, 7)
#
#print(a)
#
#x = range(1, 7)
#print(x)
#
#print(list(x))
#
#x = np.arange(7, 15, 0.2)
#print(x)
#
#
#print("")
#
#y = (np.linspace(1, 10, 11))
#
#print(y)
#
#print(len(y))
#
#x = np.array([ [67, 63, 87],
#               [77, 69, 59],
#               [85, 87, 99],
#               [79, 72, 71],
#               [63, 89, 93],
#               [68, 92, 78]])
#
#print(np.shape(x))
#print(x)
#
#
#
#print(x.shape)
#
#x.shape = (2, 9)
#
#print(x)#




Density = np.dtype([('density',  'i4')])
x = np.array([(393,), (337,), (256,)],
             dtype=Density)

dt = np.dtype([('country', np.unicode, 25), 
               ('density', 'i4'), 
               ('area', 'i4'), 
               ('population', 'i4')])

population_table = np.array([
    ('Netherlands', 393, 41526, 16928800),
    ('Belgium', 337, 30510, 11007020),
    ('United Kingdom', 256, 243610, 62262000),
    ('Germany', 233, 357021, 81799600),
    ('Liechtenstein', 205, 160, 32842),
    ('Italy', 192, 301230, 59715625),
    ('Switzerland', 177, 41290, 7301994),
    ('Luxembourg', 173, 2586, 512000),
    ('France', 111, 547030, 63601002),
    ('Austria', 97, 83858, 8169929),
    ('Greece', 81, 131940, 11606813),
    ('Ireland', 65, 70280, 4581269),
    ('Sweden', 20, 449964, 9515744),
    ('Finland', 16, 338424, 5410233),
    ('Norway', 13, 385252, 5033675)],
                            dtype=dt)

#print(population_table['country'][2:5])



##np.savetxt("population_table.csv",
##           population_table,
##           fmt="%s;%d;%d;%d", 
##           delimiter=";")
##
##
##dt = np.dtype([('country', np.unicode, 20), 
##               ('density', 'i4'), 
##               ('area', 'i4'), 
##               ('population', 'i4')])
##x = np.genfromtxt("population_table.csv",
##               dtype=dt,
##               delimiter=";")

population_table.dtype.names = ('Land', 
                                'Bevölkerungsdichte', 
                                'Fläche', 
                                'Bevölkerung')

print(population_table.dtype.names)

print("\n")



lands = ['Niederlande', 'Belgien', 'Vereinigtes Königreich', 
         'Deutschland', 'Liechtenstein', 'Italien', 'Schweiz', 
         'Luxemburg', 'Frankreich', 'Österreich', 'Griechenland', 
         'Irland', 'Schweden', 'Finnland', 'Norwegen']

population_table['Land'] = np.array(lands, dtype='<U25')

print(population_table)