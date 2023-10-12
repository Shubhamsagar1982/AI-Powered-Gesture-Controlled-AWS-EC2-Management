#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3


# In[2]:


myec2 = boto3.resource(
    "ec2",
    region_name="ap-south-1",
    aws_access_key_id="",
    aws_secret_access_key=""
)


# In[3]:


def launchOS():
    response=myec2.create_instances(
        ImageId="ami-0da59f1af71ea4ad2",
        InstanceType="t2.micro",
        MaxCount=1,
        MinCount=1
    )


# In[4]:


import cv2


# In[5]:


# !pip install opencv-python


# In[5]:


from cvzone.HandTrackingModule import HandDetector


# In[6]:


cap = cv2.VideoCapture(0)


# In[7]:


# detector=HandDetector()
detector = HandDetector()


# In[8]:


while True:
    status , photo = cap.read()
    cv2.imshow("mylivephoto" , photo)
    if cv2.waitKey(100) == 13:
        break

    handphoto= detector.findHands(photo , draw=False)
    if handphoto:
        lmlist=handphoto[0]
        fingerstatus=detector.fingersUp(lmlist)

        if fingerstatus == [1,1,1,1,1]:
            print("ALL UP")
            launchOS()
            launchOS()
            launchOS()
            launchOS()
            launchOS()
    
        elif fingerstatus == [1,0,0,0,0]:
            print("index")
            launchOS()
    
        elif fingerstatus == [0,1,1,0,0]:
            print("two UP")
            launchOS()
            launchOS()
    
        elif fingerstatus == [0,1,1,1,0]:
            print("3 UP")
            launchOS()
            launchOS()
            launchOS()
    
        elif fingerstatus == [0,1,1,1,1]:
            print("4 UP")
            launchOS()
            launchOS()
            launchOS()
            launchOS()
    
        else:
            print("idk")
        
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




