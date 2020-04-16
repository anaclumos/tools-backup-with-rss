---
layout: post
title: GPT-2: 1.5B Release
tags: unknown
url: https://openai.com/blog/gpt-2-1-5b-release/
id: 5dbc942ae12baa0038833b0c
authors: [{'name': 'Irene Solaiman'}]
published: Tue, 05 Nov 2019 17:05:24 GMT
---

# GPT-2: 1.5B Release
###### As the final model release of GPT-2’s staged release, we’re releasing the largest version (1.5B parameters) of GPT-2 along with code and model weights to facilitate detection of outputs of GPT-2 models.
<!--kg-card-begin: markdown--><div class="medium-copy color-fg-80 mt-n0.5">
<img alt="GPT-2: 1.5B Release" src="images/gpt-update_11-4b.jpg"/><p>As the final model release of <a href="https://openai.com/blog/better-language-models/">GPT-2</a>’s <a href="https://openai.com/blog/gpt-2-6-month-follow-up/">staged release</a>, we’re releasing the largest version (1.5B parameters) of GPT-2 along with <a href="https://github.com/openai/gpt-2-output-dataset">code and model weights</a> to facilitate detection of outputs of GPT-2 models. While there have been larger language models released since August, we’ve continued with our original staged release plan in order to provide the community with a test case of a full staged release process. We hope that this test case will be useful to developers of future powerful models, and we’re actively continuing the conversation with the AI community on responsible publication.</p>
</div>
<section class="btns">
<a class="btn btn-padded icon-papers" href="https://arxiv.org/abs/1908.09203">Report</a>
<a class="btn btn-padded icon-code" href="https://github.com/openai/gpt-2">GPT-2 Model</a>
<a class="btn btn-padded icon-code" href="https://github.com/openai/gpt-2-output-dataset/tree/master/detector">Detector Model</a>
<a class="btn btn-padded icon-paper" href="https://github.com/openai/gpt-2/blob/master/model_card.md">Model Card</a>
</section>
<h2 id="ourfindings">Our findings</h2>
<p><strong>1. Humans find GPT-2 outputs convincing.</strong> Our partners at Cornell University surveyed people to assign GPT-2 text a credibility score across model sizes. People gave the 1.5B model a “credibility score” of 6.91 out of 10. This is marginally greater than outputs from the 774M model (6.72) and significantly above the medium 355M model (6.07). These results make us more inclined to release the 1.5B model, as the incremental increase in human-perceived credibility relative to 774M seems low.</p>
<p><strong>2. GPT-2 can be fine-tuned for misuse.</strong> Our partners at the Middlebury Institute of International Studies’ Center on Terrorism, Extremism, and Counterterrorism (CTEC) found that extremist groups can use GPT-2 for misuse, specifically by fine-tuning GPT-2 models on four ideological positions: white supremacy, Marxism, jihadist Islamism, and anarchism. CTEC demonstrated that it’s possible to create models that can generate synthetic propaganda for these ideologies. They also show that, despite having low detection accuracy on synthetic outputs, ML-based detection methods can give experts reasonable suspicion that an actor is generating synthetic text.</p>
<p><strong>3. Detection is challenging.</strong> We expect that content-based detection of synthetic text is a long-term challenge. To test whether machine learning approaches may help today, we conducted in-house detection research and developed a <a href="https://github.com/openai/gpt-2-output-dataset">detection model</a> that has detection rates of ~95% for detecting 1.5B GPT-2-generated text.<sup class="footnote-ref"><a href="#fn1" id="fnref1">[1]</a></sup> We believe this is not high enough accuracy for standalone detection and needs to be paired with metadata-based approaches, human judgment, and public education to be more effective.  We are releasing this model to aid the study of research into the detection of synthetic text, although this does let adversaries with access better evade detection.</p>
<p>While we found detection accuracy depends heavily on the sampling methods used in training and testing, we also found detection to be more reliable when training across a range of sampling techniques. As seen in the figure below, we observed that larger models’ outputs are more difficult to classify, but training on larger models’ outputs makes detection results more accurate and robust. We expect this trend to continue and that detection will be more challenging with increased model size.</p>
<h5 id="transferredmodelaccuracynucleussamples">Transferred model accuracy (nucleus samples)</h5>
<!-- copied from observable HTML output -->
<div class="mb-1.5" id="chart" style="overflow-x:auto"><style>
#matrix {
  border-collapse: collapse;
}
#matrix tr:not(:last-child) {
  border-bottom: 1px solid rgba(var(--fg), 0.0875);
}
#matrix th,
#matrix td {
  padding-left: 0.25rem;
  padding-right: 0.25rem;
  min-width: 108px;
}
#matrix th:first-child,
#matrix td:first-child {
  padding-left: 0;
}
#matrix th:last-child,
#matrix td:last-child {
  padding-right: 0;
}
#matrix td {
  padding-top: 0.25rem;
  padding-bottom: 0.25rem;
  vertical-align: middle;
}
</style><table class="table-unstyled d-block d-md-table small-copy color-fg-80" id="matrix"><thead><tr><th class="color-fg-50" style="vertical-align:bottom;width:20%">Trained on <span class="icon position-relative" style="top:0.12em">down</span></th><th style="vertical-align:bottom;width:20%"><span class="color-fg-50">Tested on <span class="icon position-relative" style="top:0.12em">right</span></span><br/>Small (124M)</th><th style="vertical-align:bottom;width:20%">Medium (355M)</th><th style="vertical-align:bottom;width:20%">Large (774M)</th><th style="vertical-align:bottom;width:20%">XL (1.5B)</th></tr></thead><thead></thead><tbody><tr><td>Small (124M)</td><td><div class="text-center py-0.125 rounded color-white" style="background-color: rgb(16, 35, 104)">99.3%</div></td><td><div class="text-center py-0.125 rounded color-white" style="background-color: rgb(34, 66, 152)">96.6%</div></td><td><div class="text-center py-0.125 rounded color-white" style="background-color: rgb(49, 164, 193)">90.9%</div></td><td><div class="text-center py-0.125 rounded color-black" style="background-color: rgb(255, 255, 217)">79.3%</div></td></tr><tr><td>Medium (355M)</td><td><div class="text-center py-0.125 rounded color-white" style="background-color: rgb(19, 38, 111)">99.0%</div></td><td><div class="text-center py-0.125 rounded color-white" style="background-color: rgb(24, 43, 121)">98.5%</div></td><td><div class="text-center py-0.125 rounded color-white" style="background-color: rgb(34, 62, 149)">96.9%</div></td><td><div class="text-center py-0.125 rounded color-white" style="background-color: rgb(39, 150, 191)">91.8%</div></td></tr><tr><td>Large (774M)</td><td><div class="text-center py-0.125 rounded color-white" style="background-color: rgb(25, 44, 124)">98.4%</div></td><td><div class="text-center py-0.125 rounded color-white" style="background-color: rgb(29, 49, 133)">97.9%</div></td><td><div class="text-center py-0.125 rounded color-white" style="background-color: rgb(29, 49, 133)">97.9%</div></td><td><div class="text-center py-0.125 rounded color-white" style="background-color: rgb(35, 80, 161)">95.7%</div></td></tr><tr><td>XL (1.5B)</td><td><div class="text-center py-0.125 rounded color-white" style="background-color: rgb(34, 62, 149)">96.9%</div></td><td><div class="text-center py-0.125 rounded color-white" style="background-color: rgb(34, 65, 151)">96.7%</div></td><td><div class="text-center py-0.125 rounded color-white" style="background-color: rgb(34, 66, 152)">96.6%</div></td><td><div class="text-center py-0.125 rounded color-white" style="background-color: rgb(35, 75, 158)">96.0%</div></td></tr></tbody></table></div>
<p><strong>4. We’ve seen no strong evidence of misuse so far.</strong> While we’ve seen some discussion around GPT-2’s potential to augment high-volume/low-yield operations like spam and phishing, we haven’t seen evidence of writing code, documentation, or instances of misuse. We think synthetic text generators have a higher chance of being misused if their outputs become more reliable and coherent. We acknowledge that we cannot be aware of all threats, and that motivated actors can replicate language models without model release.</p>
<p><strong>5. We need standards for studying bias.</strong> Language models have biases. Working out how to study these biases, discuss them, and address them, is a challenge for the AI research community. We’ve approached the challenge of bias in two ways:</p>
<ul>
<li>Publishing a <a href="https://github.com/openai/gpt-2/blob/master/model_card.md">model card</a><sup class="footnote-ref"><a href="#fn2" id="fnref2">[2]</a></sup> alongside our models on GitHub to give people a sense of the issues inherent to language models such as GPT-2.</li>
<li>Performing a qualitative, in-house evaluation of some of the biases in GPT-2: We probed GPT-2 for some gender, race, and religious biases, using those findings to inform our model card. These probes are not comprehensive and raise the need for collaboration on bias analysis frameworks.</li>
</ul>
<h2 id="nextsteps">Next steps</h2>
<p>Our experience with GPT-2 over the past 9 months has given us valuable insight into the challenges and opportunities for creating responsible publication norms in AI. We’re continuing our work on this issue via participation in the Partnership on AI’s “Responsible Publication Norms for Machine Learning” project and discussions with our colleagues in the research community.</p>
<p><em>If you’d like to develop large-scale AI systems and think about their implications, <a href="https://openai.com/jobs/">we’re hiring</a>.</em></p>
<footer class="post-footer js-post-footer">
<!-- footer item -->
<div><hr/><div class="row">
<div class="col">Acknowledgments</div>
<div class="col">Thanks to the following for feedback on this post: Greg Brockman, Jeffrey Wu, Alec Radford, Jong Wook Kim, Gretchen Krueger, Alex Newhouse, Jason Blazakis, Sarah Kreps, Miles McCain, Cody Wild, Mona Wang, Jeremy Gillula, Larissa Schiavo, Aviv Ovadya, Rebecca Crootof</div>
</div></div>
<!-- special footer item for footnotes -->
<div data-order="-1"><hr/><div class="row">
<div class="col">Footnotes</div>
<div class="col"><hr class="footnotes-sep"/>
<section class="footnotes">
<ol class="footnotes-list">
<li class="footnote-item" id="fn1"><p>Specifically, we based a sequence classifier on RoBERTa<sub>BASE</sub> (125 million parameters) and RoBERTa<sub>LARGE</sub> (355 million parameters) and fine-tuned it to classify the outputs from the 1.5B GPT-2 model versus WebText, the dataset we used to train the GPT-2 model. <a class="footnote-backref" href="#fnref1">↩︎</a></p>
</li>
<li class="footnote-item" id="fn2"><p>Which we’ve based on “<a href="https://arxiv.org/abs/1810.03993">Model Cards for Model Reporting</a>” by Mitchell et al. <a class="footnote-backref" href="#fnref2">↩︎</a></p>
</li>
</ol>
</section>
<!--kg-card-end: markdown--></div></div></div></footer>