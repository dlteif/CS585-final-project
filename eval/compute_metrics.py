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

cv2.imwrite('gt_laplacian.png', gt_laplacian)
cv2.imwrite('db_laplacian.png', db_laplacian)

average_metric = sum(metric)/len(metric)

print('Average Improvement: {}'.format(average_metric))
