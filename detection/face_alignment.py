import sys
import dlib
import cv2
import time
predictor_path = './detection/shape_predictor_68_face_landmarks.dat'
#face_file_path = './classe.jpg'
date=time.strftime("%Y-%m-%d-%H-%M")
def face_ali_detec(face_file_path):
    print(face_file_path)
    #Loading models we need , predictor for landmarks used for face alignment
    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor(predictor_path)


    img = cv2.imread(face_file_path)
    img_raw=img.copy()
    # Ask the detector to find the bounding boxes of each face. The 1 in the
    # second argument indicates that we should upsample the image 1 time. This
    # will make everything bigger and allow us to detect more faces.
    dets = detector(img, 1)

    num_faces = len(dets)
    if num_faces == 0:
        print("Sorry, there were no faces found in '{}'".format(face_file_path))
        exit()

    # Find the 5 face landmarks we need to do the alignment.
    faces = dlib.full_object_detections()
    rects = dlib.rectangles()
    for detection in dets:
        faces.append(sp(img, detection))
        rects.append(detection)
    


    # Get the aligned face images
    images = dlib.get_face_chips(img, faces, size=227)

    for i,image  in enumerate(images):
        outfile_1= './detection/images/aligned/aligned- {} --'.format(i)+date+'.png'
        print(outfile_1)
        cv2.imwrite(outfile_1,image)
    

    return rects






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