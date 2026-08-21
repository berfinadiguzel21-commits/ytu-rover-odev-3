from ultralytics import YOLO
import cv2


model = YOLO("best.pt")

results = model.predict(source="Photo-6.png", save=True)

cizilmis_resim = results[0].plot()

cv2.imshow("Dur Tabelasi Tespiti - YTU Rover", cizilmis_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
