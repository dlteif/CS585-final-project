# CS585-final-project: Image Deblurring Applied to Recycling Data
### Team: Diala Lteif, Piotr Teterwak, Kubra Eryilmaz

We run and compare available non-DL and DL methods for image deblurring on a video of recycling garbage on a conveyer belt.

![Original](https://github.com/dlteif/CS585-final-project/blob/master/data/original.gif)

## Non-DL Methods
### 1. Blind Deconvolution Using a Normalized Sparsity Measure: [Paper](https://dilipkay.files.wordpress.com/2019/04/priors_cvpr11.pdf) [Code](https://www.dropbox.com/s/wy0yr9zfix3o9xi/norm_sparsity_code.zip?dl=0)
This work uses a regularization function which is the ratio of the <i>l1</i> norm to the <i>l2</i> norm on the high frequencies of an image.
This ratio is inversely proportional to blur in the image, so the stronger the blur, the lower the ratio is. On the other hand, added noise increases the ratio. The <i>l1/l2</i> function is considered a sparsity measure, and it is a normalized version of <i>l1</i>, making it scale invariant. <br/>
The overall algorithm of this method is described below:
<div style="width:800px; margin:0 auto;">
<img src="https://user-images.githubusercontent.com/57039745/115951501-0d0b2b80-a4af-11eb-9bb5-948ad7a74e93.png" width="400" height="300" />
</div>
<br/>
The main script to run is [norm_sparsity_code/test_blind_deconv.m](https://github.com/dlteif/CS585-final-project/blob/master/norm_sparsity_code/test_blind_deconv.m)

#### Result
To the left is the original data and to the right is the deblurred.
![output](https://github.com/dlteif/CS585-final-project/blob/master/data/ms_blind_deconv.gif)


## DL Methods
### 1. DeblurGANv2: [Paper [1]](https://arxiv.org/abs/1908.03826) [Code](https://github.com/VITA-Group/DeblurGANv2)

This work uses an pix2pix[2] style Generative Adverserial Network. They take a pre-trained network, and apply a Feature Pyramid Network [3] on top of it, as shown below. They use  perceptual,adverserial, and mean-squared error losses to train on the Go-Pro dataset, where they have high-resolution/blurry pairs. Additionally, they use local and global discriminators. We take such a pretrained network and apply it to the recycling data, using the code provided by the authors linked above.  

![](./doc_images/pipeline.jpg)

#### Result
To the left is the original data and to the right is the deblurred.We note that GIF's introduce their own artifacts. 
![output](./deblur_gan/results/recycle_deblur.gif)

If you'd like to view an mp4 of the results, click [here](https://github.com/dlteif/CS585-final-project/blob/master/deblur_gan/results/recycle_deblur.mp4?raw=true). 


## Evaluation

We do both a qualitative and quantitative evaluation of the method. 

### Quantitative Evaluation

We use a simple method to evaluate the sharpness of the resulting image; we simply compute the variance of the Laplacian of the image [4,5]. The laplacian of an image is given below:

![](./doc_images/eqnlog1.gif)

As you can see, it's simply the sum of image second derivatives in the horizontal and vertical dirctions. In areas where the image is uniform, the second derivatives of the image are 0. However, where the image has edges, the second derivatives of the image are changing very quickly. Therefore, near edges the Laplacian will have non-zero values. Therefore, when there are sharper edges, the variance of the Laplacian will be larger than with an image which has blurry outputs. 

We show laplacians of two sample images below. 

![](./doc_images/gt_laplacian.png =250x)

![](./doc_images/db_laplacian.png)

Finally, for each input, output pair, we compute the difference of the variance of the Laplacian between blurry and deblurred images. See the pseudocode below for a sample of how it's done:

We report numbers for all the methods below:



### References
[1] Kupyn, Orest, et al. "Deblurgan-v2: Deblurring (orders-of-magnitude) faster and better." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2019.

[2] Isola, Phillip, et al. "Image-to-image translation with conditional adversarial networks." Proceedings of the IEEE conference on computer vision and pattern recognition. 2017.

[3] Lin, Tsung-Yi, et al. "Feature pyramid networks for object detection." Proceedings of the IEEE conference on computer vision and pattern recognition. 2017.




