---
layout: post
title: Procgen Benchmark
tags: unknown
url: https://openai.com/blog/procgen-benchmark/
id: 5dd5ddafb142d6003858b037
authors: [{'name': 'Karl Cobbe'}]
published: Tue, 03 Dec 2019 17:00:16 GMT
---

# Procgen Benchmark
## Summary
We’re releasing Procgen Benchmark, 16 simple-to-use procedurally-generated environments which provide a direct measure of how quickly a reinforcement learning agent learns generalizable skills.
## Content
We’re releasing Procgen Benchmark, 16 simple-to-use procedurally-generated environments which provide a direct measure of how quickly a reinforcement learning agent learns generalizable skills.
<!--kg-card-begin: markdown--><div class="medium-copy color-fg-80 mt-n0.5">
<img alt="Procgen Benchmark" src="images/og-image.jpg"/><p>We’re releasing Procgen Benchmark, 16 simple-to-use <a href="https://en.wikipedia.org/wiki/Procedural_generation">procedurally-generated</a> environments which provide a direct measure of how quickly a reinforcement learning agent learns generalizable skills.</p>
</div>
<section class="btns">
<a class="btn btn-padded icon-paper" href="https://arxiv.org/abs/1912.01588">Paper</a>
<a class="btn btn-padded icon-code" href="https://github.com/openai/procgen">Environment Code</a>
<a class="btn btn-padded icon-code" href="https://github.com/openai/train-procgen">Training Code</a>
</section>
<!-- carousel -->
<div class="full my-0 pt-0.5 pb-2 position-relative overflow-hidden">
<div class="container">
<div class="js-carousel-videos carousel-videos">
<div class="js-carousel-video carousel-video">
<div class="small-copy mb-0.2">CoinRun</div>
<video autoplay="" class="w-100 mb-0" loop="" muted="" playsinline="" poster="https://cdn.openai.com/procgen-benchmark/assets/env_coinrun.jpg" src="https://cdn.openai.com/procgen-benchmark/assets/env_coinrun.mp4"></video>
</div>
<div class="js-carousel-video carousel-video">
<div class="small-copy mb-0.2">StarPilot</div>
<video autoplay="" class="w-100 mb-0" loop="" muted="" playsinline="" poster="https://cdn.openai.com/procgen-benchmark/assets/env_starpilot.jpg" src="https://cdn.openai.com/procgen-benchmark/assets/env_starpilot.mp4"></video>
</div>
<div class="js-carousel-video carousel-video">
<div class="small-copy mb-0.2">CaveFlyer</div>
<video autoplay="" class="w-100 mb-0" loop="" muted="" playsinline="" poster="https://cdn.openai.com/procgen-benchmark/assets/env_caveflyer.jpg" src="https://cdn.openai.com/procgen-benchmark/assets/env_caveflyer.mp4"></video>
</div>
<div class="js-carousel-video carousel-video">
<div class="small-copy mb-0.2">Dodgeball</div>
<video autoplay="" class="w-100 mb-0" loop="" muted="" playsinline="" poster="https://cdn.openai.com/procgen-benchmark/assets/env_dodgeball.jpg" src="https://cdn.openai.com/procgen-benchmark/assets/env_dodgeball.mp4"></video>
</div>
<div class="js-carousel-video carousel-video">
<div class="small-copy mb-0.2">FruitBot</div>
<video autoplay="" class="w-100 mb-0" loop="" muted="" playsinline="" poster="https://cdn.openai.com/procgen-benchmark/assets/env_fruitbot.jpg" src="https://cdn.openai.com/procgen-benchmark/assets/env_fruitbot.mp4"></video>
</div>
<div class="js-carousel-video carousel-video">
<div class="small-copy mb-0.2">Chaser</div>
<video autoplay="" class="w-100 mb-0" loop="" muted="" playsinline="" poster="https://cdn.openai.com/procgen-benchmark/assets/env_chaser.jpg" src="https://cdn.openai.com/procgen-benchmark/assets/env_chaser.mp4"></video>
</div>
<div class="js-carousel-video carousel-video">
<div class="small-copy mb-0.2">Miner</div>
<video autoplay="" class="w-100 mb-0" loop="" muted="" playsinline="" poster="https://cdn.openai.com/procgen-benchmark/assets/env_miner.jpg" src="https://cdn.openai.com/procgen-benchmark/assets/env_miner.mp4"></video>
</div>
<div class="js-carousel-video carousel-video">
<div class="small-copy mb-0.2">Jumper</div>
<video autoplay="" class="w-100 mb-0" loop="" muted="" playsinline="" poster="https://cdn.openai.com/procgen-benchmark/assets/env_jumper.jpg" src="https://cdn.openai.com/procgen-benchmark/assets/env_jumper.mp4"></video>
</div>
<div class="js-carousel-video carousel-video">
<div class="small-copy mb-0.2">Leaper</div>
<video autoplay="" class="w-100 mb-0" loop="" muted="" playsinline="" poster="https://cdn.openai.com/procgen-benchmark/assets/env_leaper.jpg" src="https://cdn.openai.com/procgen-benchmark/assets/env_leaper.mp4"></video>
</div>
<div class="js-carousel-video carousel-video">
<div class="small-copy mb-0.2">Maze</div>
<video autoplay="" class="w-100 mb-0" loop="" muted="" playsinline="" poster="https://cdn.openai.com/procgen-benchmark/assets/env_maze.jpg" src="https://cdn.openai.com/procgen-benchmark/assets/env_maze.mp4"></video>
</div>
<div class="js-carousel-video carousel-video">
<div class="small-copy mb-0.2">BigFish</div>
<video autoplay="" class="w-100 mb-0" loop="" muted="" playsinline="" poster="https://cdn.openai.com/procgen-benchmark/assets/env_bigfish.jpg" src="https://cdn.openai.com/procgen-benchmark/assets/env_bigfish.mp4"></video>
</div>
<div class="js-carousel-video carousel-video">
<div class="small-copy mb-0.2">Heist</div>
<video autoplay="" class="w-100 mb-0" loop="" muted="" playsinline="" poster="https://cdn.openai.com/procgen-benchmark/assets/env_heist.jpg" src="https://cdn.openai.com/procgen-benchmark/assets/env_heist.mp4"></video>
</div>
<div class="js-carousel-video carousel-video">
<div class="small-copy mb-0.2">Climber</div>
<video autoplay="" class="w-100 mb-0" loop="" muted="" playsinline="" poster="https://cdn.openai.com/procgen-benchmark/assets/env_climber.jpg" src="https://cdn.openai.com/procgen-benchmark/assets/env_climber.mp4"></video>
</div>
<div class="js-carousel-video carousel-video">
<div class="small-copy mb-0.2">Plunder</div>
<video autoplay="" class="w-100 mb-0" loop="" muted="" playsinline="" poster="https://cdn.openai.com/procgen-benchmark/assets/env_plunder.jpg" src="https://cdn.openai.com/procgen-benchmark/assets/env_plunder.mp4"></video>
</div>
<div class="js-carousel-video carousel-video">
<div class="small-copy mb-0.2">Ninja</div>
<video autoplay="" class="w-100 mb-0" loop="" muted="" playsinline="" poster="https://cdn.openai.com/procgen-benchmark/assets/env_ninja.jpg" src="https://cdn.openai.com/procgen-benchmark/assets/env_ninja.mp4"></video>
</div>
<div class="js-carousel-video carousel-video">
<div class="small-copy mb-0.2">BossFight</div>
<video autoplay="" class="w-100 mb-0" loop="" muted="" playsinline="" poster="https://cdn.openai.com/procgen-benchmark/assets/env_bossfight.jpg" src="https://cdn.openai.com/procgen-benchmark/assets/env_bossfight.mp4"></video>
</div>
</div><!-- end .js-carousel-videos -->
</div><!-- end .container -->
</div><!-- end .full -->
<h3 id="gettingstarted">Getting started</h3>
<p>Using the environment is easy whether you’re a human or AI:</p>
<pre><code class="language-bash">$ pip install procgen # install
$ python -m procgen.interactive --env-name starpilot # human
$ python &lt;&lt;EOF # random AI agent
import gym
env = gym.make('procgen:procgen-coinrun-v0')
obs = env.reset()
while True:
    obs, rew, done, info = env.step(env.action_space.sample())
    env.render()
    if done:
        break
EOF
</code></pre>
<p>We’ve found that all of the Procgen environments require training on 500–1000 different levels before they can generalize to new levels, which suggests that standard RL benchmarks need much more diversity within each environment. Procgen Benchmark has become the standard research platform used by the OpenAI RL team, and we hope that it accelerates the community in creating better RL algorithms.</p>
<h3 id="environmentdiversityiskey">Environment diversity is key</h3>
<p><a href="https://arxiv.org/abs/1804.06893">In</a> <a href="https://openai.com/blog/quantifying-generalization-in-reinforcement-learning/">several</a> <a href="https://arxiv.org/abs/1806.10729">environments</a>, it has been observed that agents can overfit to remarkably large training sets. This evidence raises the possibility that overfitting pervades classic benchmarks like the <a href="https://arxiv.org/abs/1207.4708">Arcade Learning Environment</a>, which has long served as a gold standard in reinforcement learning (RL). While the diversity between different games in the ALE is one of the benchmark's greatest strengths, the low emphasis on generalization presents a significant drawback. In each game the question must be asked: are agents robustly learning a relevant skill, or are they approximately memorizing specific trajectories?</p>
<p><a href="https://openai.com/blog/quantifying-generalization-in-reinforcement-learning/">CoinRun</a> was designed to address precisely this issue, by using procedural generation to construct distinct sets of training levels and test levels. While CoinRun has helped us better quantify generalization in RL, it is still only a single environment. It’s likely that CoinRun is not fully representative of the many challenges RL agents must face. We want the best of both worlds: a benchmark comprised of many diverse environments, each of which fundamentally requires generalization. To fulfill this need, we have created Procgen Benchmark. CoinRun now serves as the inaugural environment in Procgen Benchmark, contributing its diversity to a greater whole.</p>
<p>Previous work, including the <a href="https://arxiv.org/abs/1902.01378">Obstacle Tower Challenge</a> and the <a href="https://arxiv.org/abs/1802.10363">General Video Game AI framework</a>, has also encouraged using procedural generation to better evaluate generalization in RL. We've designed environments in a similar spirit, with two Procgen environments drawing direct inspiration from <a href="https://arxiv.org/abs/1806.10729">GVGAI-based work</a>. Other environments like Dota and StarCraft also provide lots of per-environment complexity, but these environments are hard to rapidly iterate with (and it's even harder to use more than one such environment at a time). With Procgen Benchmark, we strive for all of the following: experimental convenience, high diversity within environments, and high diversity across environments.</p>
<h3 id="procgenbenchmark">Procgen Benchmark</h3>
<p>Procgen Benchmark consists of 16 unique environments designed to measure both sample efficiency and generalization in reinforcement learning. This benchmark is ideal for evaluating generalization since distinct training and test sets can be generated in each environment. This benchmark is also well-suited to evaluate sample efficiency, since all environments pose diverse and compelling challenges for RL agents. The environments' intrinsic diversity demands that agents learn robust policies; overfitting to narrow regions in state space will not suffice. Put differently, the ability to generalize becomes an integral component of success when agents are faced with ever-changing levels.</p>
<h3 id="designprinciples">Design principles</h3>
<p>We’ve designed all Procgen environments to satisfy the following criteria:</p>
<ul>
<li>
<p><strong>High Diversity</strong>: Environment generation logic is given maximal freedom, subject to basic design constraints. The diversity in the resulting level distributions presents agents with meaningful generalization challenges.</p>
</li>
<li>
<p><strong>Fast Evaluation</strong>: Environment difficulty is calibrated such that baseline agents make significant progress after training for 200M timesteps. Moreover, the environments are optimized to perform thousands of steps per second on a single CPU core, enabling a fast experimental pipeline.</p>
</li>
<li>
<p><strong>Tunable Difficulty</strong>: All environments support two well-calibrated difficulty settings: easy and hard. While we report results using the hard difficulty setting, we make the easy difficulty setting available for those with limited access to compute power. Easy environments require approximately an eighth of the resources to train.</p>
</li>
<li>
<p><strong>Emphasis on Visual Recognition and Motor Control</strong>: In keeping with precedent, environments mimic the style of many Atari and Gym Retro games. Performing well primarily depends on identifying key assets in the observation space and enacting appropriate low level motor responses.</p>
</li>
</ul>
<h3 id="evaluatinggeneralization">Evaluating generalization</h3>
<p>We came to appreciate how hard RL generalization can be while conducting the <a href="https://openai.com/blog/first-retro-contest-retrospective/">Retro Contest</a>, as agents continually failed to generalize from the limited data in the training set. Later, our CoinRun experiments painted an even clearer picture of our agents' struggle to generalize. We've now expanded on those results, conducting our most thorough study of RL generalization to date using all 16 environments in Procgen Benchmark.</p>
<p>We first measured how the size of the training set impacts generalization. In each environment, we generated training sets ranging in size from 100 to 100,000 levels. We trained agents for 200M timesteps on these levels using <a href="https://openai.com/blog/openai-baselines-ppo/">Proximal Policy Optimization</a>, and we measured performance on unseen test levels.</p>
<h5 class="mb-0" id="generalization">Generalization performance</h5>
<div class="medium-xsmall-copy">Score over 100k levels, log scale</div>
<div class="mt-0.5" id="levels-legend"></div>
<div class="wide mt-1.5 mb-1">
<div class="row"><div class="col-12 col-xl-10 offset-xl-1">
<div class="row align-items-end">
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">CoinRun</div>
<div id="levels-coinrun"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">StarPilot</div>
<div id="levels-starpilot"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">CaveFlyer</div>
<div id="levels-caveflyer"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Dodgeball</div>
<div id="levels-dodgeball"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">FruitBot</div>
<div id="levels-fruitbot"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Chaser</div>
<div id="levels-chaser"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Miner</div>
<div id="levels-miner"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Jumper</div>
<div id="levels-jumper"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Leaper</div>
<div id="levels-leaper"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Maze</div>
<div id="levels-maze"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">BigFish</div>
<div id="levels-bigfish"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Heist</div>
<div id="levels-heist"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Climber</div>
<div id="levels-climber"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Plunder</div>
<div id="levels-plunder"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Ninja</div>
<div id="levels-ninja"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">BossFight</div>
<div id="levels-bossfight"></div>
</div>
</div><!-- end.row -->
</div></div>
</div><!-- end .wide-->
<p>We found that agents strongly overfit to small training sets in almost all environments. In some cases, agents need access to as many as 10,000 levels to close the generalization gap. We also saw a peculiar trend emerge in many environments: past a certain threshold, training performance improves as the training sets grows! This runs counter to trends found in supervised learning, where training performance commonly decreases with the size of the training set. We believe this increase in training performance comes from an implicit curriculum provided by a diverse set of levels. A larger training set can improve training performance if the agent learns to generalize <em>even across levels in the training set</em>. We previously noticed this effect with CoinRun, and have found it often occurs in many Procgen environments as well.</p>
<h3 id="anablationwithdeterministiclevels">An ablation with deterministic levels</h3>
<p>We also conducted a simple ablation study to emphasize the importance of procedural generation. Instead of using a new level at the start of every episode, we trained agents on a fixed sequence of levels. The agent begins each episode on the first level, and when it successfully completes a level, it progresses to the next one. If the agent fails at any point, the episode terminates. The agent can reach arbitrarily many levels, though in practice it rarely progresses beyond the 20th level in any environment.</p>
<h5 class="mb-0" id="ablation">Train and test performance</h5>
<div class="medium-xsmall-copy">Score over 200M timesteps</div>
<div class="mt-0.5" id="ablation-legend"></div>
<div class="wide mt-1.5 mb-1">
<div class="row"><div class="col-12 col-xl-10 offset-xl-1">
<div class="row align-items-end">
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">CoinRun</div>
<div id="ablation-coinrun"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">StarPilot</div>
<div id="ablation-starpilot"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">CaveFlyer</div>
<div id="ablation-caveflyer"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Dodgeball</div>
<div id="ablation-dodgeball"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">FruitBot</div>
<div id="ablation-fruitbot"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Chaser</div>
<div id="ablation-chaser"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Miner</div>
<div id="ablation-miner"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Jumper</div>
<div id="ablation-jumper"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Leaper</div>
<div id="ablation-leaper"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Maze</div>
<div id="ablation-maze"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">BigFish</div>
<div id="ablation-bigfish"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Heist</div>
<div id="ablation-heist"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Climber</div>
<div id="ablation-climber"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Plunder</div>
<div id="ablation-plunder"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">Ninja</div>
<div id="ablation-ninja"></div>
</div>
<div class="col-6 col-sm-4 col-md-3 mb-0.75 mb-md-1">
<div class="small-copy">BossFight</div>
<div id="ablation-bossfight"></div>
</div>
</div><!-- end.row -->
</div></div>
</div><!-- end .wide-->
<p>At test time, we remove the determinism in the sequence of levels, instead choosing level sequences at random. We find that agents become competent over the first several training levels in most games, giving an illusion of meaningful progress. However, test performance demonstrates that the agents have in fact learned almost nothing about the underlying level distribution. We believe this vast gap between training and test performance is worth highlighting. It reveals a crucial hidden flaw in training on environments that follow a fixed sequence of levels. These results show just how essential it is to use diverse environment distributions when training and evaluating RL agents.</p>
<h3 id="nextsteps">Next steps</h3>
<p>We expect many insights gleaned from this benchmark to apply in more complex settings, and we’re excited to use these new environments to design more capable and efficient agents.</p>
<p><em>If you’re interested in helping develop diverse environments, <a href="https://openai.com/jobs/">we’re hiring</a>!</em></p>
<footer class="post-footer js-post-footer">
<!-- footer item -->
<div><hr/><div class="row">
<div class="col">Acknowledgments</div>
<div class="col">
<p>Thanks to Marc Bellemare, Julian Togelius, Carles Gelada, Jacob Jackson, Alex Ray, Lilian Weng, and Joshua Achiam for their feedback on the paper.</p>
<p>Thanks to Mira Murati, Brooke Chan, Justin Jay Wang, Greg Brockman, Ashley Pilipiszyn and Jack Clark for their work supporting, designing, writing, and providing feedback on this post.</p>
<p>Special thanks to <a href="https://www.kenney.nl">Kenney</a> for the many high quality game assets used throughout these environments.</p>
<p>Additional thanks to <a href="https://craftpix.net">CraftPix.net</a> for several game backgrounds, as well as to <a href="https://www.gameartguppy.com">GameArtGuppy</a>, and <a href="https://ansimuz.itch.io">ansimuz</a>. All asset licenses can be found <a href="https://github.com/openai/procgen/blob/master/ASSET_LICENSES.md">here</a>.</p>
</div>
</div></div>
</footer>
<!--kg-card-end: markdown-->