import cv2 as cv

indir = 'specify input directory'
outdir = 'specify ouput directory'

# Read in the image and convert to grayscale
image = cv.imread(indir)
cv.imshow('Image',image)
cv.waitKey()
gray = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
cv.imshow('Gray',gray)
cv.waitKey()
cv.imwrite(outdir + '/' + 'gray.jpg',gray)

# Define a kernel size for Gaussian smoothing / blurring
kernel_size = 5
blur_gray = cv.GaussianBlur(gray,(kernel_size, kernel_size),0)

# Define our parameters for Canny
low_threshold = 100
high_threshold = 200
edges = cv.Canny(blur_gray, low_threshold, high_threshold)

# Display the image
cv.imshow('Gray',edges)
cv.waitKey()
cv.imwrite(outdir + '/' + 'edges.jpg',edges)