import pandas as pd
import numpy as np
from sklearn import linear_model

class mlpotong:
    def __init__(self):
        self.reg = linear_model.LinearRegression()
        df = pd.DataFrame({'tekanan': [23, 39, 24, 45],
                        'jarak': [22, 27, 42, 34],
                        'tachometer': [5872, 9495, 6303, 8749],
                        'gunting': [28, 67, 24, 67]})
        self.reg.fit(df[['tekanan', 'jarak', 'tachometer']], df.gunting)

    
    def hitungml(self, tekanan, jarak, tachometer):
        return self.reg.predict([[tekanan, jarak, tachometer]])[0]
    
class mljahit:
    def __init__(self):
        self.reg = linear_model.LinearRegression()
        df = pd.DataFrame({'suhu': [64, 114, 37, 5],
                        'optik': [7339, 8594, 9204, 6764],
                        'kelembaban': [70, 95, 69, 25],
                        'jahitan': [300, 0, 500, 1000]})
        self.reg.fit(df[['suhu', 'optik', 'kelembaban']], df.jahitan)

    
    def hitungml(self, suhu, optik, kelembaban):
        return self.reg.predict([[suhu, optik, kelembaban]])[0]
    
class mlbenang:
    def __init__(self):
        self.reg = linear_model.LinearRegression()
        df = pd.DataFrame({'penggerakan': [2325, 1522, 163, 3397],
                        'suara': [875, 787, 220, 342],
                        'getaran': [198, 883, 992, 454],
                        'benang': [200, 50, 700, 600]})
        self.reg.fit(df[['penggerakan', 'suara', 'getaran']], df.benang)

    
    def hitungml(self, penggerakan, suara, getaran):
        return self.reg.predict([[penggerakan, suara, getaran]])[0]

# ---------------------------------------------------------------------

class mlbahan:
    def __init__(self):
        self.reg = linear_model.LinearRegression()
        df = pd.DataFrame({'kapas': [1655, 5415, 18749, 23491],
                        'benang': [67482, 842, 35041, 38750],
                        'poliester': [45065, 4224, 33671, 7950],
                        'bahan': [400, 100, 1480, 600]})
        self.reg.fit(df[['kapas', 'benang', 'poliester']], df.bahan)

    
    def hitungml(self, kapas, benang, poliester):
        return self.reg.predict([[kapas, benang, poliester]])[0]
    
class mlkain:
    def __init__(self):
        self.reg = linear_model.LinearRegression()
        df = pd.DataFrame({'kain': [8439, 1362, 4438, 9009],
                        'pemintalan': [544, 557, 116, 67],
                        'pencelupan': [1, 5, 7, 3],
                        'kain': [8000, 1000, 4000, 9000]})
        self.reg.fit(df[['kain', 'pemintalan', 'pencelupan']], df.kain)

    
    def hitungml(self, kain, pemintalan, pencelupan):
        return self.reg.predict([[kain, pemintalan, pencelupan]])[0]

class mlketahanan:
    def __init__(self):
        self.reg = linear_model.LinearRegression()
        df = pd.DataFrame({'tarik': [52, 107, 76, 129],
                        'spektrofotometer': [80, 93, 85, 59],
                        'kerutan': [382, 133, 34, 546],
                        'ketahanan': [45, 90, 75, 5]})
        self.reg.fit(df[['tarik', 'spektrofotometer', 'kerutan']], df.ketahanan)

    
    def hitungml(self, tarik, spektrofotometer, kerutan):
        return self.reg.predict([[tarik, spektrofotometer, kerutan]])[0]

# ---------------------------------------------------------------------

class mlkualitas:
    def __init__(self):
        self.reg = linear_model.LinearRegression()
        df = pd.DataFrame({'label': [1, 0, 1, 1],
                        'warna': [658, 579, 448, 742],
                        'cacat': [1, 45, 25, 14],
                        'kualitas': [90, 30, 45, 75]})
        self.reg.fit(df[['label', 'warna', 'cacat']], df.kualitas)

    
    def hitungml(self, label, warna, cacat):
        return self.reg.predict([[label, warna, cacat]])[0]
    
class mlpenghalusan:
    def __init__(self):
        self.reg = linear_model.LinearRegression()
        df = pd.DataFrame({'panas': [210, 87, 86, 248],
                        'penghalus': [6, 97, 10, 6],
                        'kimia': [13, 18, 15, 11],
                        'kehalusan': [0, 85, 90, 0]})
        self.reg.fit(df[['panas', 'penghalus', 'kimia']], df.kehalusan)

    
    def hitungml(self, panas, penghalus, kimia):
        return self.reg.predict([[panas, penghalus, kimia]])[0]

class mlpembersihan:
    def __init__(self):
        self.reg = linear_model.LinearRegression()
        df = pd.DataFrame({'bau': [4142, 9249, 7188, 1231],
                        'softener': [937, 879, 535, 83],
                        'kotoran': [1, 9, 8, 2],
                        'kebersihan': [50, 5, 5, 100]})
        self.reg.fit(df[['bau', 'softener', 'kotoran']], df.kebersihan)

    
    def hitungml(self, bau, softener, kotoran):
        return self.reg.predict([[bau, softener, kotoran]])[0]

# ---------------------------------------------------------------------
# aktuator pabrik
class mlclothing:
    def __init__(self):
        self.reg = linear_model.LinearRegression()
        df = pd.DataFrame({'bahan': [210, 87, 86, 248],
                        'kain': [6, 97, 10, 6],
                        'ketahanan': [13, 18, 15, 11],
                        'clothing': [0, 85, 90, 0]})
        self.reg.fit(df[['bahan', 'kain', 'ketahanan']], df.clothing)

    
    def hitungml(self, bahan, kain, ketahanan):
        return self.reg.predict([[bahan, kain, ketahanan]])[0]
    
# aktuator tekstil
class mlteksitl:
    def __init__(self):
        self.reg = linear_model.LinearRegression()
        df = pd.DataFrame({'bahan': [210, 87, 86, 248],
                        'kain': [6, 97, 10, 6],
                        'ketahanan': [13, 18, 15, 11],
                        'hasiltekstil': [0, 85, 90, 0]})
        self.reg.fit(df[['bahan', 'kain', 'ketahanan']], df.hasiltekstil)

    
    def hitungml(self, bahan, kain, ketahanan):
        return self.reg.predict([[bahan, kain, ketahanan]])[0]
    
# aktuator finishing
class mlfinishing:
    def __init__(self):
        self.reg = linear_model.LinearRegression()
        df = pd.DataFrame({'kualitas': [210, 87, 86, 248],
                        'kehalusan': [6, 97, 10, 6],
                        'kebersihan': [13, 18, 15, 11],
                        'finishing': [0, 85, 90, 0]})
        self.reg.fit(df[['kualitas', 'kehalusan', 'kebersihan']], df.finishing)

    
    def hitungml(self, kualitas, kehalusan, kebersihan):
        return self.reg.predict([[kualitas, kehalusan, kebersihan]])[0]
    
# aktuator tailoring
class mltailoring:
    def __init__(self):
        self.reg = linear_model.LinearRegression()
        df = pd.DataFrame({'gunting': [4142, 9249, 7188, 1231],
                        'jahitan': [937, 879, 535, 83],
                        'benang': [1, 9, 8, 2],
                        'hasiljahit': [50, 5, 5, 100]})
        self.reg.fit(df[['gunting', 'jahitan', 'benang']], df.hasiljahit)

    
    def hitungml(self, gunting, jahitan, benang):
        return self.reg.predict([[gunting, jahitan, benang]])[0]
