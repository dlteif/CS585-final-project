### Blind Deconvolution Using a Normalized Sparsity Measure: [Paper [5]](https://dilipkay.files.wordpress.com/2019/04/priors_cvpr11.pdf) [Code](https://www.dropbox.com/s/wy0yr9zfix3o9xi/norm_sparsity_code.zip?dl=0)
This work uses a regularization function which is the ratio of the <i>l1</i> norm to the <i>l2</i> norm on the high frequencies of an image.
This ratio is inversely proportional to blur in the image, so the stronger the blur, the lower the ratio is. On the other hand, added noise increases the ratio. The <i>l1/l2</i> function is considered a sparsity measure, and it is a normalized version of <i>l1</i>, making it scale invariant. <br/>
The overall algorithm of this method is described below:
<div style="width:800px; margin:0 auto;">
<img src="https://user-images.githubusercontent.com/57039745/115951501-0d0b2b80-a4af-11eb-9bb5-948ad7a74e93.png" width="400" height="300" />
</div>
<br/>

#### Result
To the left is the original data and to the right is the deblurred.

![output](https://github.com/dlteif/CS585-final-project/blob/master/data/ms_blind_deconv.gif)

To process and deblur a video run: [test_blind_deconv.m](https://github.com/dlteif/CS585-final-project/blob/master/norm_sparsity_code/test_blind_deconv.m)

To process and deblur a set of images/frames run: [test_blind_deconv_frames.m](https://github.com/dlteif/CS585-final-project/blob/master/norm_sparsity_code/test_blind_deconv_frames.m) 

Since the method is robust to the choice of parameters, we use the same parameter values across all samples.

