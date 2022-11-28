import cv2

def get_center(rectangles):
    centers = []
    for i in rectangles:
        x = int(i[0]+((i[2]-i[0])/2))
        y = int(i[1]+((i[3]-i[1])/2))
        centers.append([x, y])
        #print(centers)
    return centers


def get_rectangles(results):
    rectangles = []
    x = results.xyxy[0].tolist()
    for i in x:
        rectangles.append(i[:-2])
    return rectangles


def toggle_vision(vision_status, frame):
    if vision_status:
        #resized = cv2.resize(frame, (720,480), interpolation = cv2.INTER_AREA)
        cv2.imshow("Matches", resized)
    else:
        cv2.destroyAllWindows()

