---
layout: post
title: Deep Double Descent
tags: unknown
url: https://openai.com/blog/deep-double-descent/
id: 5dd61135b142d6003858b0ed
authors: [{'name': 'Preetum Nakkiran'}]
published: Thu, 05 Dec 2019 17:24:26 GMT
---

# Deep Double Descent
###### Summary
<!--kg-card-begin: markdown--><div class="js-excerpt">
<p>We show that the <a href="https://arxiv.org/abs/1812.11118">double</a> <a href="https://arxiv.org/abs/1710.03667">descent</a> <a href="https://arxiv.org/abs/1809.09349">phenomenon</a> occurs in CNNs, ResNets, and transformers: performance first improves, then gets worse, and then improves again with increasing model size, data size, or training time. This effect is often avoided through careful regularization. While this behavior appears to be fairly universal, we don't</p></div>
<!--kg-card-begin: markdown--><div class="js-excerpt">
<img alt="Deep Double Descent" src="images/Frame-1--3-.png"/><p>We show that the <a href="https://arxiv.org/abs/1812.11118">double</a> <a href="https://arxiv.org/abs/1710.03667">descent</a> <a href="https://arxiv.org/abs/1809.09349">phenomenon</a> occurs in CNNs, ResNets, and transformers: performance first improves, then gets worse, and then improves again with increasing model size, data size, or training time. This effect is often avoided through careful regularization. While this behavior appears to be fairly universal, we don't yet fully understand why it happens, and view further study of this phenomenon as an important research direction.</p>
</div>
<section class="btns"><a class="btn btn-padded icon-paper" href="https://arxiv.org/abs/1912.02292">Read Paper</a></section>
<p>Many classes of modern deep learning models, including CNNs, ResNets, and transformers, exhibit the previously-observed <a href="https://arxiv.org/abs/1812.11118">double</a> <a href="https://arxiv.org/abs/1710.03667">descent</a> <a href="https://arxiv.org/abs/1809.09349">phenomenon</a> when not using early stopping or regularization. The peak occurs predictably at a "critical regime," where the models are barely able to fit the training set. As we increase the number of parameters in a neural network, the test error initially decreases, increases, and, just as the model is able to fit the train set, undergoes a second descent.</p>
<p>Neither classical statisticians’ conventional wisdom that <em>too large models are worse</em> nor the modern ML paradigm that <em>bigger models are better</em> uphold. We find that double descent also occurs over train epochs. Surprisingly, we show these phenomena can lead to a regime where more data hurts, and training a deep network on a larger train set actually performs worse.</p>
<h4 class="mb-1/12" id="modelwise">Model-wise double descent</h4>
<div class="medium-copy mb-1">1. There is a regime where bigger models are worse.</div>
<figure class="mx-n0.5">
<p><img alt="Deep Double Descent" src="images/modeldd.svg"/></p>
</figure>
<p>The model-wise double descent phenomenon can lead to a regime where training on more data hurts. In the chart above, the peak in test error occurs around the interpolation threshold, when the models are just barely large enough to fit the train set.</p>
<p>In all cases we've observed, changes which affect the interpolation threshold (such as changing the optimization algorithm, the number of train samples, or the amount of label noise) also affect the location of the test error peak correspondingly. The double descent phenomena is most prominent in settings with added label noise; without it, the peak is smaller and easy to miss. Adding label noise amplifies this general behavior and allows us to easily investigate.</p>
<h4 class="mb-1/12" id="samplewise">Sample-wise non-monotonicity</h4>
<div class="medium-copy mb-1">2. There is a regime where more samples hurts.</div>
<figure class="mx-n0.5">
<p><img alt="Deep Double Descent" src="images/fig_data_hurts.svg"/></p>
</figure>
<p>The above chart shows transformers trained on a language-translation task with no added label noise. As expected, increasing the number of samples shifts the curve downwards towards lower test error. However, since more samples require larger models to fit, increasing the number of samples also shifts the interpolation threshold (and peak in test error) to the right.</p>
<p>For intermediate model sizes (red arrows), these two effects combine, and we see that training on 4.5x more samples actually hurts test performance.</p>
<h4 class="mb-1/12" id="epochwise">Epoch-wise double descent</h4>
<div class="medium-copy mb-1">3. There is a regime where training longer reverses overfitting.</div>
<div class="wide my-0">
<div class="row">
<div class="col-12 col-md-6">
<figure class="mx-n0.5">
<p><img alt="Deep Double Descent" src="images/epoch_train.png"/></p>
</figure>
</div>
<div class="col-12 col-md-6 mt-n1 mt-md-0">
<figure class="mx-n0.5">
<p><img alt="Deep Double Descent" src="images/epoch_test.png"/></p>
</figure>
</div>
</div>
</div>
<p>The charts above show test and train error as a function of both model size and number of optimization steps. For a given number of optimization steps (fixed y-coordinate), test and train error exhibit model-size double descent. For a given model size (fixed x-coordinate), as training proceeds, test and train error decreases, increases, and decreases again; we call this phenomenon epoch-wise double descent.</p>
<p><em>In general, the peak of test error appears systematically when models are just barely able to fit the train set.</em></p>
<p>Our intuition is that, for models at the interpolation threshold, there is effectively only one model that fits the train data, and forcing it to fit even slightly noisy or misspecified labels will destroy its global structure. That is, there are no "good models" which both interpolate the train set and perform well on the test set. However, in the over-parameterized regime, there are many models that fit the train set and there exist such good models. Moreover, the implicit bias of stochastic gradient descent (SGD) leads it to such good models, for reasons we don't yet understand.</p>
<p>We leave fully understanding the mechanisms behind double descent in deep neural networks as an important open question.</p>
<footer class="post-footer js-post-footer">
<!-- footer item -->
<div><hr/><div class="row">
<div class="col">Acknowledgments</div>
<div class="col">
<p>Thanks to Mikhail Belkin and Chris Olah for helpful discussions and feedback throughout this work. An expanded version of this post can also be found on Boaz Barak's blog, <a href="https://windowsontheory.org/2019/12/05/deep-double-descent/">Windows on Theory</a>.</p>
</div>
</div></div>
</footer>
<!--kg-card-end: markdown-->