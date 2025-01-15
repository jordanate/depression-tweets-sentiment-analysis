# Sentiment Analysis of Depression in Tweets
![images/depression_social_media.jpg](https://github.com/jordanate/sentiment-analysis-phase-4-project/blob/main/images/depression_social_media.jpg)

<!-- ### Deployed Model

https://jordanate-sentiment-analysis-phase-4-project-model-0ki2uu.streamlit.app/ -->

**By:** Jordana Tepper

## Overview

This project utilizes a dataset containing various tweets from Twitter to conduct a sentiment analysis for depression. With both mental health disorders and social media use on the constant rise, it is common to see individuals expressing their inner feelings and struggles online. Therefore, this sentiment analysis aims to aid Twitter in classifying certain tweets as potential displays of depression and, as a result, enable the company to use their targeted advertisements to provide mental health resources to the associated users (e.g., showing an advertisement for affordable online therapy). It is significant to note that this project does not act as a diagnostic tool, as depression cannot be formally diagnosed based on tweets. Rather, this sentiment analysis serves as a tool that can be used to detect potential signs of depression and provide support for Twitter users.

Using Natural Language Processing, I implement four different types of models to produce the highest recall score; such models include Random Forest with Count Vectorization, Random Forest with TF-IDF Vectorization, Multinomial Naive Bayes with Count Vectorization, and Multinomial Naive Bayes with TF-IDF Vectorization. Furthermore, each of the four models was subdivided into two, more specific models: one with basic stop words and one with curated stop words.

After reviewing the outputs from each model, the highest recall was 98.99%.

I decided to utilize recall as my primary metric because a false negative (classifying a tweet as NOT a potential display of depression when it is) is more costly than a false positive (classifying a tweet as a potential display of depression when it is NOT). In other words, missing an indication of potential depression and not providing the necessary resources can be more harmful than falsely indicating potential depression and providing such resources.

## Business Problem

As of 2021, approximately 280 million people suffer from depression worldwide [(WHO)](https://www.who.int/news-room/fact-sheets/detail/depression). Furthermore, within the first year of the COVID-19 pandemic, the global prevalence of anxiety and depression increased by 25% [(WHO)](https://www.who.int/news/item/02-03-2022-covid-19-pandemic-triggers-25-increase-in-prevalence-of-anxiety-and-depression-worldwide). In the United States specifically, studies have shown that 1 in 10 Americans suffer from depression [(USA News)](https://www.usnews.com/news/health-news/articles/2022-09-19/depression-affects-almost-1-in-10-americans). With such high rates of mental health disorders - depression, in particular - there is no question that action should be taken to aid individuals in receiving the support and care they need. One way that this can be done is through the utilization of social media. 

According to an analysis from [Kepios](https://datareportal.com/social-media-users#:~:text=Analysis%20from%20Kepios%20shows%20that,of%20the%20total%20global%20population.), over 59% of the world uses social media. Regarding the United States alone, this number rises to 70% [(Pew Research Center)](https://www.pewresearch.org/internet/fact-sheet/social-media/). Therefore, it is no surprise that, often, such areas overlap, and individuals display or provide an indication of their mental health struggles on social media. So, with the abundance of posts and data that social media outlets receive daily, it would be beneficial to society to use such information to detect potential indications of mental health disorders, such as depression, and generate targeted advertisements that provide support and resources for the users who may be in need of them.

For my project, Twitter is the stakeholder and has asked me to utilize existing tweets from their platform to create a model that detects potential signs of depression through language patterns. Twitter then plans to put this model into practice by distributing mental health resources using the process of targeted advertising.

## Data Understanding

The data that I used for this project comes from a dataset from [Kaggle](https://www.kaggle.com/datasets/gargmanas/sentimental-analysis-for-tweets) titled "Sentimental Analysis for Tweets." This source is comprised of 10,313 tweets taken from Twitter, with each entry classified as either an indication of depression (denoted by 1) or not an indication of depression (denoted by 0).

## Data Analysis

### Visualizing Word Frequency in the Dataset

**_Word Cloud_**
<p align = 'center'>
  <img width = '670' height = '580' src="https://github.com/jordanate/sentiment-analysis-phase-4-project/blob/main/images/word_cloud.png"> 
</p>

**_Bar Chart of Top 10 Words_**
![word_freq.png](https://github.com/jordanate/sentiment-analysis-phase-4-project/blob/main/images/word_freq.png)

## Modeling

After doing some data cleaning, I performed a 75%-25% Train-Test Split on the data with an indication of depression as the target variable and tweets as the predictor. Next, I created several classification models.

Recall was the main metric used to determine the accuracy of my model due to the fact that I was interested in using the model to detect potential depression, and therefore, a false negative is more costly than a false positive.

In this project, a false negative is a case where a tweet is classified as NOT being a potential display of depression when it truly is, and a false positive is a case where a tweet is classified as being a potential display of depression when it is not.

The following models were used on the testing set:

1a. Count Vectorizer and Random Forest (Basic Stemmed Stop Words)   
1b. Count Vectorizer and Random Forest (Amended Stemmed Stop Words)   
2a. TF-IDF Vectorizer and Random Forest (Basic Stemmed Stop Words)    
2b. TF-IDF Vectorizer and Random Forest (Amended Stemmed Stop Words)    
**3a. Count Vectorizer and Multinomial Naive Bayes (Basic Stemmed Stop Words) - Best Model**    
3b. Count Vectorizer and Multinomial Naive Bayes (Amended Stemmed Stop Words)   
4a. TF-IDF and Multinomial Naive Bayes (Basic Stemmed Stop Words)   
4b. TF-IDF and Multinomial Naive Bayes (Amended Stemmed Stop Words)

<p align = 'center'>
  <img width = '1500' height = '270' src="https://github.com/jordanate/sentiment-analysis-phase-4-project/blob/main/images/stats_graph.png"> 
</p>

## Evaluation

### Why Model 3a?

With recall being the primary metric, the best models are Models 2a and 3a. More specifically, Model 2a has a recall of 98.65% (8 false negatives), and Model 3a has a recall of 98.99% (6 false negatives). Despite Model 3a having 2 fewer false negatives, I contemplated making my final model Model 2a rather than Model 3a due to the fact that it has no false positives while Model 3a has 91 false positives. In other words, Model 2a minimizes both false negatives and false positives. Furthermore, there is not much difference in the recall percentages of the two models, and a difference of 2 false negatives does not seem too significant. Nevertheless, after doing some sample tweets, I decided that my final model is Model 3a. While both models were flawed with some of the sample tweets, the specific examples that led me to this decision are "I want to die," "Kill me," and "I need help." If anyone were to see these tweets, they would likely believe that the user is potentially struggling with depression or other mental health concerns, so when Model 2a did not pick up on such patterns, I decided that Model 3a was better.

### Final Model Confusion Matrix

<p align = 'center'>
  <img width = '720' height = '570' src="https://github.com/jordanate/sentiment-analysis-phase-4-project/blob/main/images/confusion_matrix.png"> 
</p>

### Final Model ROC-AUC

<p align = 'center'>
  <img width = '730' height = '550' src="https://github.com/jordanate/sentiment-analysis-phase-4-project/blob/main/images/roc_auc.png"> 
</p>

## Conclusions

### Limitations

- The model fails to understand slang words such as 'emo' and 'depro.'
- The model also fails to properly interpret negation in statements such as, "I am NOT depressed" or "I am NOT okay."
- These two limitations likely root from the fact that this dataset contains only 10,313 tweets meaning that the model is limited and cannot capture every pattern of text/language that exists online.

### Next Steps

If I had access to more data, I would do the following:

- Acquire a larger dataset
- Acquire more data that accounts for slang words
- Develop models that incorporate other languages

## Mental Health Resources

**United States Suicide and Crisis Lifeline (24/7):** Call 988 (No data charges)

**NAMI HelpLine (M-F, 10 am - 10 pm, ET):** Call 1-800-950-NAMI (6264), Text "HelpLine" to 62640, or Email at <a href="mailto:helpline@nami.org">helpline@nami.org</a> 


**SAMHSA’s (Substance Abuse and Mental Health Services Administration) National Helpline (24/7):** Call 1-800-662-HELP (4357)

**Crisis Text Line (24/7):** Text HOME to 741741

**BetterHelp Teletherapy:** https://www.betterhelp.com/

## For More Information

For a full analysis, please look at my [Jupyter Notebook](./sentiment-analysis-phase-4-project.ipynb)

For a more concise summary, please review my [presentation](https://github.com/jordanate/sentiment-analysis-phase-4-project/blob/main/presentation.pdf).

For any additional questions, please contact Jordana Tepper at <a href="mailto:jtepper724@gmail.com">jtepper724@gmail.com</a> 

## Repository Structure
```
├── data
├── images
├── .gitignore
├── .jovianrc
├── README.md
├── depression-tweets-sentiment-analysis.ipynb
├── model.py
├── model3a.pkl
├── presentation.pdf
└── requirements.txt
```
