# FibVID
FibVID repository is to supplement the paper "Comprehensive Fake News Diffusion Dataset during COVID-19 Period". This repository (FibVID) is collected to address challenges in Fake News detection during the COVID-19 period. 

## Abstract
While the coronavirus disease 2019 (COVID-19) has rampant throughout the world, misinformation dissemination has caused various confusions. Thus, understanding the misinformation on COVID-19 and its propagation has recently become one of the important tasks in our society. To shed light on the issue, we aim to contribute a valuable dataset, which addresses three key topics. First, we provide both true and fake (T/F) claim dataset of COVID-19 and non-COVID issues, which are labeled and validated by several fact-checking journalism platforms (e.g. Snopes and Politifact). Second, we collect the claim-related tweets and retweets from Twitter, one of the largest social network services. Third, we provide basic user information including the terms and characteristics of 'heavy fake news user' for presenting a better understanding of T/F claims in considerations of COVID-19. Our dataset has several significant contributions. The dataset can be useful to uncover potential propagation patterns with their relations to issues, authenticity of claims, traits of users who engaged in, and patterns of information diffusion. We provide suggestions on possible applications of the dataset with a few exploratory analyses to examine effectiveness of the approaches we used. 


## Overview of our Dataset.
Our repository consists of three datasets: News Claim, Claim Propagation, and User Information. News Claim was collected from two fact-checking sites, Politifact and Snopes. Claim Propagation and User Information about the News Claim data were collected from Twitter. In Claim Propagation and User Information, we pseudonymized the user screen name and marked them in numbers for a privacy policy. All the data were grouped as follows: 0 as COVID True claims, 1 as COVID Fake claims, 2 as Non-COVID True claims, and 3 as Non-COVID Fake claims.


## Data Collection Pipeline
![pipe](https://user-images.githubusercontent.com/18303573/104558729-99bf7580-5686-11eb-9207-8dc3b2bbc3ea.png)

In order to comprise the dataset from January 2020 to December 2020, we built the pipeline with three steps. First, we crawled the labeled claim data from Politifact and Snopes using our own crawler. With the claims, we extracted the keywords in order to make the search query. Second, the generated search query was deployed through our Twitter crawler to obtain the claim propagation features. Finally, we supplemented the user information using Twitter API, Tweepy.


## Requirement
* python >= 3.6.5


## Clone
git clone https://github.com/merry555/FibVID


## Dataset
The dataset for each result condition can be downloaded by running the file in the dataset.

* News claim
  * news_claim.csv : this file provides a list of news contents that include claim number, group, text, and news source.

 
* Claim Propagation
  * origin_tweet.csv : this file provides assurance that the correct origin tweets were collected in reference to claims collected from Politifact and Snopes. The dataset includes tweet user, tweet id, retweet count, post text, hashtag, like count, create date, group, and similarity.
  * claim_propagation.csv : this file provides the claim propagation that includes claim number, parent user, parent id, tweet user, tweet id, retweet count, post  text, hashtag, like count, create date, group, depth.
 
* User Information
  * user_information.csv : this file provides the user information that includes user id, create date, description, follower count, and the following count.


## Schematic diagram of network model
We provide a sample network model to calculate volume, depth, and virality for claims.

```
# output dataset : calculate_output.csv
cd network_model
python network_model_sample.py
```

