---
layout: post
title: GPT-2: 6-Month Follow-Up
tags: unknown
url: https://openai.com/blog/gpt-2-6-month-follow-up/
id: 5d5237ca81cf770044605ced
authors: [{'name': 'Jack Clark'}]
published: Tue, 20 Aug 2019 16:00:59 GMT
---


# GPT-2: 6-Month Follow-Up

## Summary

<!--kg-card-begin: markdown--><div class="js-excerpt">
<p>We’re releasing the 774 million parameter GPT-2 language model after the release of our small <a href="https://openai.com/blog/better-language-models/">124M model</a> in February, staged release of our medium <a href="https://openai.com/blog/better-language-models/#update">355M model</a> in May, and subsequent research with partners and the AI community into the model’s potential for misuse and societal benefit. We’re</p></div>

## Content


<!--kg-card-begin: markdown--><div class="js-excerpt">
<img alt="GPT-2: 6-Month Follow-Up" src="images/gpt-2_update_8-14a-40.jpg"/><p>We’re releasing the 774 million parameter GPT-2 language model after the release of our small <a href="https://openai.com/blog/better-language-models/">124M model</a> in February, staged release of our medium <a href="https://openai.com/blog/better-language-models/#update">355M model</a> in May, and subsequent research with partners and the AI community into the model’s potential for misuse and societal benefit. We’re also releasing an open-source legal agreement to make it easier for organizations to initiate model-sharing partnerships with each other, and are publishing a technical report about our experience in coordinating with the wider AI research community on publication norms.</p>
</div>
<section class="btns"><a class="btn btn-padded icon-paper" href="https://arxiv.org/abs/1908.09203" target="blank">Read Report</a><a class="btn btn-padded icon-code" href="https://github.com/openai/gpt-2" target="blank">View Code</a><a class="btn btn-padded icon-download" href="https://cdn.openai.com/Software+Access+Agreement+Template.docx" target="blank">Legal Agreement</a></section>
<h2 id="keythingswevelearned">Key things we’ve learned</h2>
<p><strong>1. Coordination is difficult, but possible.</strong> To date, there hasn’t been a public release of a 1558M parameter language model, though multiple organizations have developed the systems to train them, or have publicly discussed how to train larger models. For example, teams from both NLP developer <a href="https://medium.com/huggingface/ethical-analysis-of-the-open-sourcing-of-a-state-of-the-art-conversational-ai-852113c324b2">Hugging Face</a> and the <a href="https://allenai.org/">Allen Institute for Artificial Intelligence</a> (AI2) with the University of Washington <a href="https://arxiv.org/abs/1905.12616">have explicitly adopted similar staged release approaches to us</a>. Since February, we’ve spoken with more than five groups who have replicated GPT-2.<sup class="footnote-ref"><a href="#fn1" id="fnref1">[1]</a></sup></p>
<p><strong>2. Humans can be convinced by synthetic text.</strong> Research from our research partners Sarah Kreps and Miles McCain at Cornell <a href="https://www.foreignaffairs.com/articles/2019-08-02/not-your-fathers-bots">published in <em>Foreign Affairs</em></a> says people find GPT-2 synthetic text samples almost as convincing (72% in one cohort judged the articles to be credible) as real articles from the New York Times (83%).<sup class="footnote-ref"><a href="#fn2" id="fnref2">[2]</a></sup> Additionally, research from AI2/UW has shown that news written by a system called "GROVER" can be <a href="https://arxiv.org/abs/1905.12616">more plausible than human-written propaganda</a>. These research results make us generally more cautious about releasing language models.</p>
<p><strong>3. Detection isn’t simple.</strong> In practice, we expect detectors to need to detect a significant fraction of generations with very few false positives. Malicious actors may use a variety of sampling techniques (including rejection sampling) or fine-tune models to evade detection methods. A deployed system likely needs to be highly accurate (99.9%–99.99%) on a variety of generations. Our research suggests that current ML-based methods only achieve low to mid–90s accuracy, and that fine-tuning the language models decreases accuracy further. There are promising paths forward (see especially those advocated by the developers of "<a href="https://arxiv.org/abs/1905.12616">GROVER</a>") but it's a genuinely difficult research problem. We believe that statistical detection of text needs to be supplemented with human judgment and metadata related to the text in order to effectively combat misuse of language models.</p>
<h2 id="partnerships">Partnerships</h2>
<p>We’ve partnered with four leading research organizations to analyze both the newly-released 774M parameter GPT-2 model and the unreleased full-size GPT-2 model. We’ve included some preliminary results from them in our technical report, and their ongoing analysis will factor into the potential release of the 1558M model. We’ve also developed a non-commercial legal agreement to facilitate the sharing of models between organizations and are publishing it here to help others initiate such sharing schemes.</p>
<ul>
<li><strong>Cornell University</strong> is studying human susceptibility to digital disinformation generated by language models.</li>
<li><strong>The Middlebury Institute of International Studies</strong> Center on Terrorism, Extremism, and Counterterrorism (CTEC) is exploring how GPT-2 could be misused by terrorists and extremists online.</li>
<li><strong>The University of Oregon</strong> is developing a series of “bias probes” to analyze bias within GPT-2.</li>
<li><strong>The University of Texas at Austin</strong> is studying the statistical detectability of GPT-2 outputs after fine-tuning the model on domain-specific datasets, as well as the extent of detection transfer across different language models.</li>
</ul>
<h2 id="futurereleasedecisions">Future release decisions</h2>
<p>Research from these partners will factor into our future release decisions, as will observing how the 774M model is used, and discussing language models with researchers and policymakers to understand the considerations around larger models. As part of our staged release strategy, our current plan is to release the 1558M parameter model in a few months, but it's plausible that findings from a partner, or malicious usage of our 774M model, could change this.</p>
<p>We think that a combination of staged release and partnership-based model sharing is likely to be a key foundation of responsible publication in AI, particularly in the context of powerful generative models. The issues inherent to large models are going to grow, rather than diminish, over time. We hope that our work on GPT-2, discussed further in the <a href="https://cdn.openai.com/GPT_2_August_Report.pdf">technical report</a> we're publishing, will help provide evidence the AI community can draw on when thinking about the publication challenges inherent to some parts of AI research.</p>
<div class="full bg-shadow mb-2">
<div class="container">
<div class="row">
<div class="content">
<ul class="timeline pb-1.5" id="timeline">
<h4>Timeline</h4>
<li data-date="February 2019">
<p>OpenAI publishes a <a href="https://openai.com/blog/better-language-models/">blog post</a> and <a href="https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf">paper</a> on GPT-2.</p>
<p>Released small parameter (124M) GPT-2 model.</p>
</li>
<li data-date="March 2019">
<p>The Partnership on AI co-hosts a dinner with OpenAI to <a href="https://www.partnershiponai.org/when-is-it-appropriate-to-publish-high-stakes-ai-research/">discuss publication norms</a>, then publishes a blog summarizing the discussion.</p>
</li>
<li data-date="May 2019">
<p>Released medium parameter (355M) model.</p>
<p>Released dataset of outputs from large-scale models.</p>
<p>Released a detection baseline to help people understand how to detect outputs of models like GPT-2.</p>
<p>The original blog post is <a href="https://openai.com/blog/better-language-models/#update">updated</a> to reflect these changes.</p>
<p>Adam King <a href="https://twitter.com/adamdanielking/status/1125831730848571392?lang=en">launches</a> "TalktoTransformer.com", giving people an interface to play with the newly released models.</p>
<p>Hugging Face releases a conversational AI demo based on GPT-2 models, discusses some of the ethical considerations in the release decision, and <a href="https://medium.com/huggingface/ethical-analysis-of-the-open-sourcing-of-a-state-of-the-art-conversational-ai-852113c324b2">decides not to release the large GPT-2 model</a>.</p>
<p>Researchers with the University of Washington and Allen Institute for AI Research <a href="https://arxiv.org/abs/1905.12616">reveal GROVER</a>, a GPT-2–style language model; they do not release the large versions of the model, and conduct research into the detection of the outputs of such models.</p>
</li>
<li data-date="June 2019">
<p><a href="https://www.youtube.com/watch?v=tdLS9MlIWOk">OpenAI testifies in Congress</a> about the implications of synthetic media, including a discussion of synthetic text.</p>
<p>DeepMind discusses GPT-2 and the importance of appropriate publication norms for generative models in their recent <a href="https://deepmind.com/blog/article/unsupervised-learning">discussion</a> of unsupervised learning.</p>
<p>OpenAI commences a research collaboration with the <a href="https://www.partnershiponai.org/">Partnership on AI</a> for publication norms in AI research. We're trying to work with a diverse set of AI research organizations to come up with questions scientists may want to ask ahead of publication, and potential frameworks they can use to make publication decisions.</p>
</li>
<li data-date="July 2019">
<p><a href="https://tabnine.com/blog/deep">DeepTabNine develops a code autocompleter</a> based on GPT-2.</p>
<p><a href="https://arxiv.org/abs/1908.01841">Multi-turn Dialogue Response Generation with Autoregressive Transformer Models</a></p>
<p><a href="https://www.aclweb.org/anthology/P19-3019">GLTR: Statistical Detection and Visualization of Generated Text</a></p>
</li>
<li data-date="August 2019">
<p>Researchers with the Thoughtful Technology Project and the University of Cambridge published a working paper on “<a href="https://arxiv.org/abs/1907.11274">Reducing malicious use of synthetic media research: Considerations and potential release practices for machine learning</a>”.</p>
<p><a href="https://arxiv.org/abs/1907.05774">Hello, It's GPT-2—How Can I Help You? Towards the Use of Pretrained Language Models for Task-Oriented Dialogue Systems</a></p>
<p>AI startup AI21 Labs releases <a href="https://www.ai21.com/haim-post">HAIM</a>, a neural text generator; they only release a 345M variant of the model, "equivalent in size to the publicly released versions of Grover and GPT-2."</p>
<p>NVIDIA Research <a href="https://nv-adlr.github.io/MegatronLM">trains</a> 8.3 billion parameter GPT-2 model.</p>
<p>Released larger parameter (774M) model.</p>
</li>
</ul>
</div><!-- end .content -->
</div><!-- end .row -->
</div><!-- end .container -->
</div><!-- end .full -->
<footer class="post-footer js-post-footer">
<!-- footer item -->
<div><hr/><div class="row">
<div class="col">Acknowledgments</div>
<div class="col">Thanks to the following for feedback on this post: Yura Burda, Daniela Amodei, Josh Tobin, Christopher Olah, Jeff Wu, Alec Radford, Ashley Pilipiszyn, Greg Brockman, Rowan Zellers, and Dario Amodei.
</div>
</div></div>
<!-- special footer item for footnotes -->
<div data-order="-1"><hr/><div class="row">
<div class="col">Footnotes</div>
<div class="col"><hr class="footnotes-sep"/>
<section class="footnotes">
<ol class="footnotes-list">
<li class="footnote-item" id="fn1"><p>Having these conversations is difficult, as it involves talking candidly about proprietary systems and it’s unclear who to reach out to in specific organizations to discuss such models and what the appropriate processes are for inter-org discussion about unreleased research. <a class="footnote-backref" href="#fnref1">↩︎</a></p>
</li>
<li class="footnote-item" id="fn2"><p>These samples were generated via a “human-in-the-loop” process meant to simulate contemporary disinformation operations, where a human generated samples and periodically selected some for exposure to people. <a class="footnote-backref" href="#fnref2">↩︎</a></p>
</li>
</ol>
</section>
<!--kg-card-end: markdown--></div></div></div></footer>