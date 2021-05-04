DeblurGANv2: [Paper [1]](https://arxiv.org/abs/1908.03826) [Code](https://github.com/VITA-Group/DeblurGANv2)

This work uses an pix2pix[2] style Generative Adverserial Network. They take a pre-trained network, and apply a Feature Pyramid Network [3] on top of it, as shown below. They use  perceptual,adverserial, and mean-squared error losses to train on the Go-Pro dataset, where they have high-resolution/blurry pairs. Additionally, they use local and global discriminators. We take such a pretrained network and apply it to the recycling data, using the code provided by the authors linked above.  

![](./doc_images/pipeline.jpg)

#### Result
To the left is the original data and to the right is the deblurred.We note that GIF's introduce their own artifacts. 
![output](./results/recycle_deblur.gif)

If you'd like to view an mp4 of the results, click [here](https://github.com/dlteif/CS585-final-project/blob/master/deblur_gan/results/recycle_deblur.mp4?raw=true). 

#### How to Run

```
   bash setup_deblurgan.sh
   ipython deblur.py
```
This clones the original repo, downloads needed data, and runs an inference script.
