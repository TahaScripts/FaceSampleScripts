import requests
from credentials import getHuggingFace
from utils import parseArgs
import io
import os
from PIL import Image
from datetime import datetime

"""
----------------------------------
Model API URLs

(StableAI) StableDiffusion
stabilityai/stable-diffusion-2
stabilityai/stable-diffusion-2-1
----------------------------------
"""

args = parseArgs()

def imageQuery(url, headers, payload):
	response = requests.post("https://api-inference.huggingface.co/models/"+url, headers=headers, json=payload)
	return response.content

def getImage(modelURL, query, save):
	image_bytes = imageQuery(modelURL, {"Authorization": args.auth if args.auth else getHuggingFace()},{ "inputs": query })
	if save:
		image = Image.open(io.BytesIO(image_bytes))
		currentTime = datetime.now().strftime("%H:%M:%S")	
		imageName = currentTime + (query if len(query) < 12 else query[0:12]) # Image name created by time + (up-to) first 12 chars of query
		imageSave = image.save(imageName+'.jpg')
	else:
		return image_bytes

if args.compare:
	subjects = args.model.split(',')
	currentTime = datetime.now().strftime("%H:%M:%S")	
	folderName = currentTime + (args.query if len(args.query) < 12 else args.query[0:12]) # Image name created by time + (up-to) first 12 chars of query
	os.mkdir('export/' + folderName) # Makes folder for full output of each query within /export directory
	for i in subjects:
		temp = getImage(i, args.query, False)
		image = Image.open(io.BytesIO(temp))
		tempSave = image.save('export/' + folderName + '/' + i.replace('/', '--')+'.jpg') # Saves each image by model name in the folder
else:
	if args.query:
		getImage(args.model if args.model else "stabilityai/stable-diffusion-2-1",args.query, True)
	else:
		print("\nError. Query required. Canceling script.\n")

