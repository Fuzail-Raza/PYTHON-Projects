import cv2


def resize(source,destination,scale_percent):
   

    image=cv2.imread(source,cv2.IMREAD_UNCHANGED)

    cv2.imshow("Title",image)

    cv2.waitKey(0)
    width=int(image.shape[1] * scale_percent /100)
    height=int(image.shape[0] * scale_percent /100)

    dsize=(width,height)
    output=cv2.resize(image,dsize)

    cv2.imwrite(destination,output)
    cv2.waitKey(0)

if __name__=="main":
    source=r"E:\Programms\PYTHON\Projects\images\resize.jpg"
    destination=r"E:\Programms\PYTHON\Projects\images\new.jpg"
    scale_percent=50
    resize(source,destination,scale_percent)