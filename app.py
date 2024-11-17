import streamlit as st
import replicate
import os
from collections import deque
from PIL import Image

pathList = []
print(os.environ.get("REPLICATE_API_TOKEN"))
api = replicate.Client(api_token=os.environ.get("REPLICATE_API_TOKEN"))

def storeImage(output, cnt):
    with open("output" + cnt + ".jpg", "wb") as file:
        file.write(output.read())
        findURL(output)
    #=> output.jpg written to disk

def generateImage(input):
    cnt = 0
    for itm in input:
        output = api.run("black-forest-labs/flux-1.1-pro-ultra", input=input)
        storeImage(output, cnt)
        cnt += 1


def generateQueue(initialInputs):
    q = deque()
    for itm in initialInputs:
        q.append(itm)

#url expires after an hour for this
def findURL(image):
    path = image.url
    pathList.add(path)


#main

st.write("loading...")
initialInputPrompts = ["Illustration of a large, majestic oak tree. The tree stands tall with a thick, sturdy trunk featuring rough, exaggerated textures to show its age. Wide branches spread outward, filled with clusters of bright, rounded green leaves that appear lively and vibrant.",
                 "branches of a tree, without the trunk",""]

generateImage(initialInputPrompts)
st.write("loaded..")
for i in range (0,len(initialInputPrompts)):
    path = find("output"+i+".jpg", "/")
    pathList.add(path)

#display images
for itm in pathList:
    st.image = (itm)

st.write("done")









