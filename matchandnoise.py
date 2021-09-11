# Shivam Chourey
# Computer Vision - ECE5554
# Template matching using OpenCV function
# Various levels of noise are added to the image
# For all the noisy images, Gaussian blurring is performed with various 'Sigma'
# The highest value returned by template matching function for each case is written in an Excel file


import numpy as np
import cv2
import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet = wb.add_sheet('Sheet 1')

# Using the recommended function
################################
# noisy - modified from Shubham Pachori on Stackoverflow
def noisy(image, noise_type, sigma):
    if noise_type == "gauss":
        row, col = image.shape
        mean = 0
        gauss = np.random.normal(mean, sigma, (row, col))
        gauss = gauss.reshape(row, col)
        noisy = image + gauss
        return noisy

    elif noise_type == "s&p":
        row, col = image.shape
        s_vs_p = 0.5
        amount = 0.004
        out = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt))
                  for i in image.shape]
        out[coords] = 1

        # Pepper mode
        num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
                  for i in image.shape]
        out[coords] = 0
        return out

    elif noise_type == "poisson":
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.random.poisson(image * vals) / float(vals)
        return noisy

    elif noise_type == "speckle":
        row, col = image.shape
        gauss = np.random.randn(row, col)
        gauss = gauss.reshape(row, col)
        noisy = image + image * gauss
        return noisy


img = cv2.imread("SavedImages\\imageCap.jpg", cv2.IMREAD_GRAYSCALE)
print(img.shape)
temp = cv2.imread("7W82995\B\\b.jpg", cv2.IMREAD_GRAYSCALE)
print(temp.shape)

# cv2.imshow("Original",img)
# cv2.imshow("Template",temp)

file = open("result.xls", "w")

for noiselevel in range(11):
    for sigma in range(6):
        noisyimg = np.uint8(noisy(img, 'gauss', noiselevel))
        # noisytemp = np.uint8(noisy(temp, 'gauss', noiselevel))
        smoothimg = cv2.GaussianBlur(noisyimg, (5, 5), sigma)

        res = cv2.matchTemplate(smoothimg, temp, cv2.TM_CCORR_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # print the Maximum correlation value and location
        print(noiselevel, sigma, max_val, " Max Loc: ", max_loc)  # 'Noiselevel ', 'Sigma ', max_loc)
        sheet.write(noiselevel + 1, sigma + 1, max_val)

        if noiselevel == 10 and sigma == 5:
            cv2.imwrite("Noisy.png", noisyimg)
            cv2.imshow("Noisy", noisyimg)
            cv2.imwrite("Smoothed.png", smoothimg)

            # Highlight result in image
            bgr = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            cv2.rectangle(bgr, (max_loc[0], max_loc[1]), (max_loc[0]+temp.shape[0], max_loc[1]+temp.shape[1]), (0,255,0), 2)
            cv2.imwrite("MatchTemplateResHighlight.png", bgr)
            cv2.imshow("Result", bgr)

            # Result image
            tmpres = res * 255
            cv2.imwrite("MatchTemplateRes.png", tmpres)
            cv2.imshow("Res", res)
            # print(res)

wb.save("result.xls")
cv2.waitKey(0)
cv2.destroyAllWindows()