from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import glob
import cv2
import os

def load_cat_attributes(inputPath):
	cols = ["engagement"]
	df = pd.read_csv(inputPath, sep=" ", header=None, names=cols)
	return df

def load_cat_images(df, inputPath):
	images = []
	data_path = os.path.join(inputPath, "*_CROP.jpg")
	files = glob.glob(data_path)

	data = []
	for f1 in files:
		if "BAD" not in f1:
			img = cv2.imread(f1)
			img = cv2.resize(img, (256, 256))
			data.append(img)

	return np.array(data)