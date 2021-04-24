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

## DL Methods
### 1. DeblurGAN

