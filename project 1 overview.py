# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:10:45 2020

@author: sophi
"""

class Hospital:
    def __init__(self, name, dob, ocr):
        self.name = name
        self.dob = dob
        self.ocr = ocr
        pass
    
    def add(self):
        pass
    
    def remove(self):
        pass

class Quarantine:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    
    def remove(self):
        pass
    
    def add(self):
        pass
    
    def display(self):
        pass
    pass

####################################################################
    
class Staff:
    def __init__(self,hospital,quarantine):
        Hospital.name = hospital
        Quarantine.name = quarantine
        pass
    
    def add(self):
        pass
    
    def remove(self):
        pass
    
    def move(self):
        pass
    pass

####################################################################
    
class Diagnosis:
    def __init__(self):
        return
    pass

class Isolation:
    def __init__(self):
        return
    pass

class Patients:
    def __init__(self, name, medication, monitoring):
        self.name = name
        Diagnosis.status = diagnosis
        Isolation.status = isolation
        self.medication = medication
        self.monitoring = monitoring
        Diagnosis.negative = deathdate
        pass
    
    def add(self):
        pass
    
    def remove(self):
        pass
    pass