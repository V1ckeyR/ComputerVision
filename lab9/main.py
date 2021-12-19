import cv2
import os

import numpy as np


def math_with_db(filename):
    img = cv2.imread(filename)
    img_to_draw = cv2.resize(img, None, fx=1, fy=1)

    counter_matches = 0

    for file in [file for file in os.listdir("database")]:
        fingerprint_database_image = cv2.imread("./database/" + file)

        sift = cv2.xfeatures2d.SIFT_create()

        key_points_1, descriptors_1 = sift.detectAndCompute(img, None)
        key_points_2, descriptors_2 = sift.detectAndCompute(fingerprint_database_image, None)

        matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10),
                                        dict()).knnMatch(descriptors_1, descriptors_2, k=2)

        match_points = []
        for p, q in matches:
            if p.distance < 0.1 * q.distance:
                match_points.append(p)

        if len(key_points_1) <= len(key_points_2):
            key_points = len(key_points_1)
        else:
            key_points = len(key_points_2)

        if (len(match_points) / key_points) > 0.95:
            counter_matches += 1
            print("% match: ", len(match_points) / key_points * 100)
            print("Fingerprint ID: " + str(file))
            image_stack = np.hstack((img_to_draw, cv2.resize(cv2.imread("database/" + file), None, fx=1, fy=1)))
            cv2.imshow("Result", image_stack)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break

    if not counter_matches:
        print("No matches! :(")


if __name__ == "__main__":
    math_with_db("Finger-Print.tif")
