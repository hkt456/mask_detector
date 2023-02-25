# import face-detect-masked.py 

# import 
# import os
# from colorama import init
# count=0
# while True:
#     s=input()
#     if s=='insert':
#         s2=input()
#         while count!=2:
#             if s2=="mask":
#                 os.system('face-detect-masked')
#                 count=count+1
#             elif s2=="unmasked":
#                 os.system('face-detect-unmasked')
#                 count=count+1
#         os.system('model_training.py')
#     elif s=='test':
#         os.system('model_test.py')
import time
if __name__=="__main__":
    imp=__import__("face-detect-masked")
    print(dir(imp))
    time.sleep(5)
    imp=__import__("face-detect-unmasked")
    print(dir(imp))
    imp=__import__("model_training")
    print(dir(imp))
    imp=__import__("model_test")
    print(dir(imp))
