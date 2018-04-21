# -*- coding: gbk -*-
'''
Created on 2018年4月21日
@author: Administrator
'''
name = ['kyo','iori','ryo']
name.sort()
name.remove('ryo')
print(name)
last_name=name.pop()
print("winner is "+last_name)
print("The rest of player is ")
for i in name:
 print(i)
    
    