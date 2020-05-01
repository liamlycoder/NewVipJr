import cv2 as cv


def face_detect_demo():
    # 将图片转换为灰度图片
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 加载特征数据
    faceCascade = cv.CascadeClassifier(r'D:\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
    faces = faceCascade.detectMultiScale(gray)
    for x, y, w, h in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)
    cv.imshow('result', img)


# 加载图片
img = cv.imread('lena.jpg')
face_detect_demo()
cv.waitKey(0)
cv.destroyAllWindows()
