# Phase 4 Project - Sentiment Analysis of Depression in Tweets
![images/depression_social_media.jpg](https://github.com/jordanate/sentiment-analysis-phase-4-project/blob/main/images/depression_social_media.jpg)

**By:** Jordana Tepper

## Overview

This project utilizes a dataset containing various tweets from Twitter to conduct a sentiment analysis for depression. With both mental health disorders and social media use on the constant rise, it is common to see individuals expressing their inner feelings and struggles online. Therefore, this sentiment analysis aims to aid Twitter in classifying certain tweets as potential displays of depression and, as a result, use their targeted advertisements to provide mental health resources to the associated users (e.g., showing an advertisement for affordable online therapy). It is significant to note that this project does not act as a diagnostic tool, as depression cannot be formally diagnosed based on tweets. Rather, this sentiment analysis serves as a tool that can be used to detect potential signs of depression and provide support for Twitter users.

Using Natural Language Processing, I implement four different types of models to produce the highest recall score; such models include Random Forest with Count Vectorization, Random Forest with TF-IDF Vectorization, Multinomial Naive Bayes with Count Vectorization, and Multinomial Naive Bayes with TF-IDF Vectorization. Furthermore, each of the four models was subdivided into two, more specific models: one with basic stop words and one with curated stop words.

After reviewing the outputs from each of the models, the highest recall was 98.99%.

I decided to utilize recall as my primary metric because a false negative (classifying a tweet as NOT a potential display of depression when it is) is more costly than a false positive (classifying a tweet as a potential display of depression when it is NOT). In other words, missing an indication of potential depression and not providing the necessary resources can be more harmful than falsely indicating potential depression and providing such resources.

## Business Problem

## Data Understanding

## Modeling

## Evaluation

## Conclusion

### Recommendations

### Limitations

### Next Steps

## Mental Health Resources

**United States Suicide and Crisis Lifeline (24/7):** Call 988 (No data charges)

**NAMI HelpLine (M-F, 10am - 10pm, ET):** Call 1-800-950-NAMI (6264), Text "HelpLine" to 62640, or Email at <a href="mailto:helpline@nami.org">helpline@nami.org</a> 


**SAMHSA’s (Substance Abuse and Mental Health Services Administration) National Helpline (24/7):** Call 1-800-662-HELP (4357)

**Crisis Text Line (24/7):** Text HOME to 741741

**BetterHelp Teletherapy:** https://www.betterhelp.com/

## For More Information

For a full analysis, please look at my [Jupyter Notebook](./sentiment-analysis-phase-4-project.ipynb)

For a more concise summary, please review my [presentation]().


For any additional questions, please contact Jordana Tepper at <a href="mailto:jtepper724@gmail.com">jtepper724@gmail.com</a> 

## Repository Structure
```
├── data
├── images
├── .gitignore
├── README.md
├── model.py
├── model3a.pkl
├── presentation.pdf
└── sentiment-analysis-phase-4-project.ipynb
```
