from skimage.metrics import structural_similarity
import cv2


# Works well with images of different dimensions
def orb_sim(img1, img2):
    # SIFT is no longer available in cv2 so using ORB
    orb = cv2.ORB_create()

    # detect keypoints and descriptors
    kp_a, desc_a = orb.detectAndCompute(img1, None)
    kp_b, desc_b = orb.detectAndCompute(img2, None)

    # define the bruteforce matcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # perform matches.
    matches = bf.match(desc_a, desc_b)
    # Look for similar regions with distance < 50. Goes from 0 to 100 so pick a number between.
    similar_regions = [i for i in matches if i.distance < 50]
    if len(matches) == 0:
        return 0
    return len(similar_regions) / len(matches)




img1 = cv2.imread('full.png', 0)  # 714 x 901 pixels

img3 = cv2.imread('full1.png', 0)  # 203 x 256 pixels


orb_similarity = orb_sim(img1, img3)  # 1.0 means identical. Lower = not similar

print("Similarity using ORB is: ", orb_similarity*100)



def structural_similarity_find():
    from skimage.metrics import structural_similarity
    from skimage.transform import resize
    import cv2
    import numpy as np

    first = cv2.imread('full.png')
    second = cv2.imread('full1.png')

    # Convert images to grayscale
    first_gray = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
    second_gray = cv2.cvtColor(second, cv2.COLOR_BGR2GRAY)

    # Compute SSIM between two images
    score, diff = structural_similarity(first_gray, second_gray, full=True)
    print("Similarity Score: {:.3f}%".format(score * 100))

structural_similarity_find()