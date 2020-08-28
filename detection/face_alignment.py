import sys
import dlib
import cv2
import time
import os
predictor_path = 'detection\\shape_predictor_68_face_landmarks.dat'
#face_file_path = './classe.jpg'

def face_ali_detec(face_file_path):
    date=time.strftime("%Y-%m-%d-%H-%M")
    print(face_file_path)
    #Loading models we need , predictor for landmarks used for face alignment
    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor(resource_path(predictor_path))


    img = cv2.imread(face_file_path)
    img_raw=img.copy()
    print(img_raw.shape)
    # Ask the detector to find the bounding boxes of each face. The 1 in the
    # second argument indicates that we should upsample the image 1 time. This
    # will make everything bigger and allow us to detect more faces.
    dets = detector(img, 1)

    num_faces = len(dets)
    if num_faces == 0:
        print("Sorry, there were no faces found in '{}'".format(face_file_path))
        raise Exception

    # Find the 5 face landmarks we need to do the alignment.
    faces = dlib.full_object_detections()
    rects = dlib.rectangles()
    for detection in dets:
        faces.append(sp(img, detection))
        rects.append(detection)
    


    # Get the aligned face images
    images = dlib.get_face_chips(img, faces, size=227)

    for i,image  in enumerate(images):
        outfile_1= 'detection\\images\\aligned\\tmp\\aligned-{}--'.format(i)+date+'.png'
        cv2.imwrite(resource_path(outfile_1),image)
    

    return rects



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


'''
a = face_ali_detec('m.jpg')
print(len(a))
print(a[0].left(),a[0].top())

'''



'''
    for k, d in enumerate(dets):
        cv2.rectangle(img_raw, (d.left(), d.top()), (d.right(), d.bottom()), (255, 0, 0), 2)

        #cv2.putText(img_raw, 'Fedex', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)

    outfile_2= './images/detected/im-'+date+'.png'
    cv2.imwrite(outfile_2,img_raw)
'''
