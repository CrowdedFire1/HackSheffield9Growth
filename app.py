import streamlit as st
import replicate
import os
from collections import deque
from PIL import Image

pathList = []


api = replicate.Client(api_token=os.getenv('REPLICATE_API_KEY'))

def storeImage(output, cnt):
    with open("output" + cnt + ".jpg", "wb") as file:
        file.write(output.read())
        findURL(output)
    #=> output.jpg written to disk

def generateImage(input):
    cnt = 0
    for itm in input:
        st.write(itm)
        output = replicate.run("black-forest-labs/flux-1.1-pro-ultra", input=itm)
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

input1 = {
    "prompt": "Illustration of a large, majestic oak tree. The tree stands tall with a thick, sturdy trunk featuring rough, exaggerated textures to show its age. Wide branches spread outward, filled with clusters of bright, rounded green leaves that appear lively and vibrant.",
    "aspect_ratio": "3:2"
}
input2 = {
    "prompt": "branches of a tree, without the trunk",
    "aspect_ratio": "3:2"
}


initialInputPrompts = [input1,input2]

generateImage(initialInputPrompts)
st.write("loaded..")


#display images
for itm in pathList:
    st.image = (itm)

st.write("done")









