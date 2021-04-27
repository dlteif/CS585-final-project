import cv2
from glob import glob
import os

ground_truth_imgs = sorted(x for x in glob('../deblur_gan/results/ground_truth/*'))
deblurred_imgs = sorted(x for x in glob('../deblur_gan/results/deblurred/*'))

metric = []

for imgs in zip(ground_truth_imgs,deblurred_imgs):
    gt_img_path, deblurred_img_path = imgs
    gt = cv2.imread(gt_img_path)
    db = cv2.imread(deblurred_img_path)
    gray_gt = cv2.cvtColor(gt, cv2.COLOR_BGR2GRAY)
    gray_db = cv2.cvtColor(db, cv2.COLOR_BGR2GRAY)
    gt_metric = cv2.Laplacian(gray_gt, cv2.CV_64F).var()
    db_metric = cv2.Laplacian(gray_db, cv2.CV_64F).var()
    metric.append(db_metric - gt_metric)


gt_laplacian = cv2.Laplacian(gray_gt, cv2.CV_64F)
db_laplacian = cv2.Laplacian(gray_db, cv2.CV_64F)

gt_laplacian = cv2.normalize(gt_laplacian, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
db_laplacian = cv2.normalize(db_laplacian, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

cv2.imwrite('../doc_images/gt_laplacian.png', gt_laplacian)
cv2.imwrite('../doc_images/db_laplacian.png', db_laplacian)

average_metric = sum(metric)/len(metric)

print('Average Improvement: {}'.format(average_metric))
