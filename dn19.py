student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4':  
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
  'id5':  
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   }
}

dict = {}

for i,j in student_data.items():
    if j not in dict.values():
        dict[i] = j

print(dict)