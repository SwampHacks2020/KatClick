# USAGE
# python cnn_regression.py --dataset Houses-dataset/Houses\ Dataset/

from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import datasets as f1
import models as f2
import numpy as np
import argparse
import locale
import os

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", type=str, required=True,
	help="path to input dataset of house images")
args = vars(ap.parse_args())

print("[INFO] loading cat attributes...")
inputPath = os.path.sep.join([args["dataset"], "cat_data.txt"])
df = f1.load_cat_attributes(inputPath)
print(df)

print("[INFO] loading cat images...")
images = f1.load_cat_images(df, args["dataset"])
images = images / 255.0

split = train_test_split(df, images, test_size=0.10, random_state=42)
(trainAttrX, testAttrX, trainImagesX, testImagesX) = split

maxPrice = trainAttrX["engagement"].max()
trainY = trainAttrX["engagement"] / maxPrice
testY = testAttrX["engagement"] / maxPrice

model = f2.create_cnn(64, 64, 3, regress=True)
opt = Adam(lr=1e-3, decay=1e-3 / 200)
model.compile(loss="mean_absolute_percentage_error", optimizer=opt)

print("[INFO] training model...")
model.fit(trainImagesX, trainY, validation_data=(testImagesX, testY),
	epochs=50, batch_size=8)

print("[INFO] predicting engagement...")
preds = model.predict(testImagesX)

diff = preds.flatten() - testY
percentDiff = (diff / testY) * 100
absPercentDiff = np.abs(percentDiff)

mean = np.mean(absPercentDiff)
std = np.std(absPercentDiff)

locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
print("[INFO] avg. engagement: " + df["engagement"].mean() + ", std engagement: " + df["engagement"].std())
print("[INFO] mean: {:.2f}%, std: {:.2f}%".format(mean, std))