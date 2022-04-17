# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 21:36:03 2022

@author: shykul
"""

bd_division_info = {}
bd_division_info["Barisal"] = {"District":6,"Upazilla":39,"Council":333}
bd_division_info["Chittagong"] = {"District":11,"Upazilla":97,"Council":336}
bd_division_info["Dhaka"] = {"District":13,"Upazilla":93,"Council":1833}
bd_division_info["Khulna"] = {"District":10,"Upazilla":59,"Council":270}
bd_division_info["Mymensingh"] = {"District":4,"Upazilla":34,"Council":350}
bd_division_info["Rajshahi"] = {"District":8,"Upazilla":70,"Council":558}
bd_division_info["Rangpur"] = {"District":8,"Upazilla":58,"Council":536}
bd_division_info["Sylhet"] = {"District":4,"Upazilla":38,"Council":334}

dist = sum(item["District"] for item in bd_division_info.values())
print("Number of district in Bangladesh is",dist)
upa = sum(item["Upazilla"] for item in bd_division_info.values())
print("Number of upazilla in Bangladesh is",upa)
coun = sum(item["Council"] for item in bd_division_info.values())
print("Number of council in Bangladesh is",coun)

