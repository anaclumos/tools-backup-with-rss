---
layout: post
title: OpenAI → PyTorch
tags: unknown
url: https://openai.com/blog/openai-pytorch/
id: 5e21ffa76fce7300445cd7ed
authors: [{'name': 'OpenAI'}]
published: Thu, 30 Jan 2020 16:57:01 GMT
---

# OpenAI → PyTorch
###### <!--kg-card-begin: markdown--><p>We are standardizing OpenAI’s deep learning framework on <a href="https://pytorch.org/">PyTorch</a>. In the past, we implemented projects in many frameworks depending on their relative strengths. We’ve now chosen to standardize to make it easier for our team to create and share optimized implementations of our models.</p>
<p><img alt="openai-pytorch" src="images/openai-pytorch.png"/></p>
<p>As part of this</p>
<!--kg-card-begin: markdown--><img alt="OpenAI → PyTorch" src="images/openai-pytorch-vertical.png"/><p>We are standardizing OpenAI’s deep learning framework on <a href="https://pytorch.org/">PyTorch</a>. In the past, we implemented projects in many frameworks depending on their relative strengths. We’ve now chosen to standardize to make it easier for our team to create and share optimized implementations of our models.</p>
<p><img alt="OpenAI → PyTorch" src="images/openai-pytorch.png"/></p>
<p>As part of this move, we’ve just released a <a href="https://github.com/openai/spinningup">PyTorch-enabled version</a> of <a href="https://openai.com/blog/spinning-up-in-deep-rl/">Spinning Up in Deep RL</a>, an open-source educational resource produced by OpenAI that makes it easier to learn about deep reinforcement learning. We are also in the process of writing PyTorch bindings for our highly-optimized <a href="https://openai.com/blog/block-sparse-gpu-kernels/">blocksparse kernels</a>, and will open-source those bindings in upcoming months.</p>
<p>The main reason we've chosen PyTorch is to increase our research productivity at scale on GPUs. It is very easy to try and execute new research ideas in PyTorch; for example, switching to PyTorch decreased our iteration time on research ideas in generative modeling from weeks to days. We’re also excited to be joining a rapidly-growing developer community, including organizations like Facebook and Microsoft, in pushing scale and performance on GPUs.</p>
<p>Going forward we'll primarily use PyTorch as our deep learning framework but sometimes use other ones when there's a specific technical reason to do so. Many of our teams have already made the switch, and we look forward to contributing to the PyTorch community in upcoming months.</p>
<!--kg-card-end: markdown-->