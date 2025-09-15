import cv2


# to read image
image = cv2.imread("/home/dinamitrii/Pictures/mami/mami.jpeg")

# Edges
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 11)
edges = cv2.adaptiveThreshold (gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY, 9, 9)

# Actual cartoonization
color = cv2.bilateralFilter(image, 9, 210, 123)
cartoon = cv2.bitwise_and(color, color, mask=edges)


cv2.imshow("Image", image)
cv2.imshow("Edges", edges)
cv2.imshow("Cartoon", cartoon)


cv2.waitKey(0)
cv2.destroyAllWindows()
