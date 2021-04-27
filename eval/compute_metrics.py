import cv2
from glob import glob
import os

ground_truth_imgs = sorted(x for x in glob('../deblur_gan/results/ground_truth/*'))
deblurred_imgs = sorted(x for x in glob('../deblur_gan/results/deblurred/*'))
deblurred_normed = sorted(x for x in glob('../norm_sparsity_code/results/deblurred/*'))

dl_metric = []
norm_metric_list = []

for imgs in zip(ground_truth_imgs,deblurred_imgs, deblurred_normed):
    gt_img_path, deblurred_img_path, norm_img_path = imgs
    gt = cv2.imread(gt_img_path)
    db = cv2.imread(deblurred_img_path)
    norm = cv2.imread(norm_img_path)
    gray_gt = cv2.cvtColor(gt, cv2.COLOR_BGR2GRAY)
    gray_db = cv2.cvtColor(db, cv2.COLOR_BGR2GRAY)
    gray_norm = cv2.cvtColor(norm, cv2.COLOR_BGR2GRAY)
    gt_metric = cv2.Laplacian(gray_gt, cv2.CV_64F).var()
    db_metric = cv2.Laplacian(gray_db, cv2.CV_64F).var()
    norm_metric = cv2.Laplacian(gray_norm, cv2.CV_64F).var()
    dl_metric.append(db_metric - gt_metric)
    norm_metric_list.append(norm_metric - gt_metric)


#gt_laplacian = cv2.Laplacian(gray_gt, cv2.CV_64F)
#db_laplacian = cv2.Laplacian(gray_db, cv2.CV_64F)


#cv2.imwrite('../doc_images/gt_laplacian.png', gt_laplacian)
#cv2.imwrite('../doc_images/db_laplacian.png', db_laplacian)

dl_metric_avg = sum(dl_metric)/len(dl_metric)
norm_metric_avg = sum(norm_metric_list)/len(norm_metric_list)



print('DL Average Improvement: {}'.format(dl_metric_avg))
print('Norm Average Improvement: {}'.format(norm_metric_avg))
