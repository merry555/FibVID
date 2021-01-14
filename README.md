# FibVID
FibVID repository is to supplement the paper "Comprehensive Fake News Diffusion Dataset during COVID-19 Period". This repository (FibVID) is collected to address challenges in Fake News detection during the COVID-19 period. 

## Overview of our Dataset.
Our repository consists of three datasets: News Claim, Claim Propagation, and User Information. News Claim was collected from two fact-checking sites, Politifact and Snopes. Claim Propagation and User Information about the News Claim data were collected from Twitter. In Claim Propagation and User Information, we pseudonymized the user screen name and marked them in numbers for a privacy policy. All the data were grouped as follows: 0 as COVID True claims, 1 as COVID Fake claims, 2 as Non-COVID True claims, and 3 as Non-COVID Fake claims.

## Clone
git clone https://github.com/merry555/FibVID

## Dataset
The dataset for each result condition can be downloaded by running the file in the dataset.

* News claim
  * news_claim.csv : this file provides a list of news contents that include claim number, group, text, and news source.

 
* Claim Propagation
  * origin_tweet.csv : this file provides assurance that the correct origin tweets were collected in reference to claims collected from Politifact and Snopes. The dataset includes tweet user, tweet id, retweet count, post text, hashtag, like count, create date, group, and similarity.
 
* User Information
  * user_information.csv : this file provides the user information that includes user id, create date, description, follower count, and the following count.

## Schematic diagram of network model
We provide a sample network model to calculate volume, depth, and virality for claims.

```
# output dataset : calculate.csv
cd network_model
python network_model_sample.py
```

## Reference
