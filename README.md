# CS585-final-project: Image Deblurring Applied to Recycling Data
### Team: Diala Lteif, Piotr Teterwak, Kubra Eryilmaz

We run and compare available non-DL and DL methods for image deblurring on a video of recycling garbage on a conveyer belt.

![Original](https://github.com/dlteif/CS585-final-project/blob/master/data/original.gif)

## Non-DL Methods
### 1. Blind Deconvolution Using a Normalized Sparsity Measure: [Paper [5]](https://dilipkay.files.wordpress.com/2019/04/priors_cvpr11.pdf) [Code](https://www.dropbox.com/s/wy0yr9zfix3o9xi/norm_sparsity_code.zip?dl=0)
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

### 2. Wiener Deconvolution: [Definition](https://en.wikipedia.org/wiki/Wiener_deconvolution) [Code] (https://github.com/michal2229/dft-wiener-deconvolution-with-psf/blob/master/deconv_cv.py)
The Wiener filter is the MSE-optimal stationary linear filter for images degraded by additive noise and blurring. Calculation of the Wiener filter requires the assumption that the signal and noise processes are second-order stationary (in the random process sense).[1] 

Wiener filters are usually applied in the frequency domain. Given a degraded image g(x,y), one takes the Discrete Fourier Transform (DFT) to obtain G(u,v). The original image spectrum is estimated by taking the product of G(u,v) with the Wiener filter W(u,v):

<img src="./wiener_deconvolution/images/filter1.png" >

The inverse DFT is then used to obtain the image estimate from its spectrum. The Wiener filter is defined in terms of these spectra:

```math
H(u,v): Fourier Transform of the Point Spread Function(PSF)
P_s(u,v): Power specturum of the signal process, obtained by taking the Fourier Transform of the signal autocorrection
P_n(u,v): Power specturum of the noise process, obtained by taking the Fourier Transform of the noise autocorrection
```
The Wiener Filter is:

<img src="./wiener_deconvolution/images/filter2.png" >

```math
K(u,v) = P_n(u,v)/P_s(u,v)
```

#### Result
To the left is the original data and to the right is the deblurred.
![original](https://github.com/dlteif/CS585-final-project/blob/master/wiener_deconvolution/original.gif)
![output](https://github.com/dlteif/CS585-final-project/blob/master/wiener_deconvolution/output.gif)

### References
[1]https://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/VELDHUIZEN/node15.html


## DL Methods
### 1. DeblurGANv2: [Paper [1]](https://arxiv.org/abs/1908.03826) [Code](https://github.com/VITA-Group/DeblurGANv2)

This work uses an pix2pix[2] style Generative Adverserial Network. They take a pre-trained network, and apply a Feature Pyramid Network [3] on top of it, as shown below. They use  perceptual,adverserial, and mean-squared error losses to train on the Go-Pro dataset, where they have high-resolution/blurry pairs. Additionally, they use local and global discriminators. We take such a pretrained network and apply it to the recycling data, using the code provided by the authors linked above.  

![](./doc_images/pipeline.jpg)

#### Result
To the left is the original data and to the right is the deblurred.We note that GIF's introduce their own artifacts. 
![output](./deblur_gan/results/recycle_deblur.gif)

If you'd like to view an mp4 of the results, click [here](https://github.com/dlteif/CS585-final-project/blob/master/deblur_gan/results/recycle_deblur.mp4?raw=true). 


## Evaluation

We do both a qualitative and quantitative evaluation of the methods. 

### Quantitative Evaluation

We use a simple method to evaluate the sharpness of the resulting image; we simply compute the variance of the Laplacian of the image [4,5]. The laplacian of an image is given below, for image intensity I:

![](./doc_images/eqnlog1.gif)

As you can see, it's simply the sum of image second derivatives in the horizontal and vertical dirctions. In areas where the image is uniform, the second derivatives of the image are 0. However, where the image has edges, the second derivatives of the image are changing very quickly. Therefore, near edges the Laplacian will have non-zero values. Therefore, when there are sharper edges, the variance of the Laplacian will be larger than with an image which has blurry outputs. 

We show laplacians of two sample images below. 

First, we show the laplacian of the blurry input.

<img src="./doc_images/gt_laplacian.png" >

Next, we show the laplacian of the deblurred output.

<img src="./doc_images/db_laplacian.png">

It's clear that edges are sharper in the deblurred output, though both are fairly subtle and you need to look closely.

Finally, for each input, output pair, we compute the difference of the variance of the Laplacian between blurry and deblurred images. See the pseudocode below for a sample of how it's done:

``` 
compute_laplacian(output).variance() - compute_laplacian(input).variance().
```

We do this for 20 input-output pairs, and then take the average. Although we would have liked to run it on more frames, some of our methods are extremely slow. 

We report numbers for all the methods below:

| Model       | Increase in Variance of Laplacian |
| ----------- | ----------- |
| DeblurGANv2      | 7.89       |
| Blind Deconvolution   | 27.16        |
| Wiener Deconvolution w/Motion Blur kernel | **34.24** | 

### Qualitative Evaluation

To further compare the tested methods, we conduct a user study where users are presented with outputs of the 3 different methods side by side along with the ground truth over 20 frames and asked to choose the method that they think gave the best output according to sharpness, artifacts,. Below is an example figure in which the users can easily compare the methods.

<img src='./compared_results/2_out.jpg' width="125%" height="125%">

We do this for 3 users only, given the limited time frame we had. One should take into consideration that all inputs are sampled from the same video, which means that a user is most likely to give the same vote for all presented outputs. We summarize the results in the table below, where the number of votes is tallied for the total frames over all users. There are 60 frames in total.  

| Quality | DeblurGANv2 | Blind Deconvolution | Wiener Deconvolution |
|---------|-------------|---------------------|----------------------|
| Sharpness |           |                     |                      |
| Artifacts |           |                     |                      |



### References
[1] Kupyn, Orest, et al. "Deblurgan-v2: Deblurring (orders-of-magnitude) faster and better." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2019.

[2] Isola, Phillip, et al. "Image-to-image translation with conditional adversarial networks." Proceedings of the IEEE conference on computer vision and pattern recognition. 2017.

[3] Lin, Tsung-Yi, et al. "Feature pyramid networks for object detection." Proceedings of the IEEE conference on computer vision and pattern recognition. 2017.

[4] https://www.pyimagesearch.com/2015/09/07/blur-detection-with-opencv/

[5] D. Krishnan, T. Tay and R. Fergus, "Blind deconvolution using a normalized sparsity measure," CVPR 2011, 2011, pp. 233-240, doi: 10.1109/CVPR.2011.5995521. 

[6] Pech-Pacheco, José Luis, et al. "Diatom autofocusing in brightfield microscopy: a comparative study." Proceedings 15th International Conference on Pattern Recognition. ICPR-2000. Vol. 3. IEEE, 2000. 
