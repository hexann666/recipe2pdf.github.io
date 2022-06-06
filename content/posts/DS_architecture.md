---
title: "Data Science Architecture"
date: 2022-05-22T18:47:16+02:00
draft: false
summary: 
categories: 
- 'blog'
tags:
- "DS"
- "tools"
- "setup"
---

In the cycle of implementation, testing, deployment we want to follow CRISM-ML.

We will start in Release 1 with jupyter notebooks, as it offers an easy entry point to start implementing ML models and see first results. It is highly responsible, easy to make changes in code and there are tools to start documentation and sufficient repository structure from the beginning.

From current point of view our use case doesn't require dashboards, as we don't need visual presentation of trends/data/correlations. We might want to introduce it later, but only for external use, if we are interested in the user activity and want to evaluate eg. what websites are the most populat among users, how often is the website used, which function is more popular.

For the text classification we ar eplanning to use ptr-trained models from **Huggingface** as a starting point to speed up the training process keeping the compute cost low. Their models are effective, APIs are well described and there are many articles about their implementation, which should make the entry smooth. Also internationalization can be made simpler using Huggingface models, as many of their pre-trained models are already multilingual.

### MLOps Tools

We use **GitHub** as SCM. We can use GitHub pipelines to configure CI/CD and make sure the development runs iteratively, involves frequent merges and includes build and tests for each code iteration to quickly react, if a new portion of code should evoke any problems. 

Alternatively **Jenkins** can be a good solution for CI/CD. It also can automate all steps from pushing of software to tests and deployment and works well with GitHub. Also it works with docker container. As seting up Jenkins locally can be tricky, it is worth looking into different price models of cloud providers to see, if we can carry out development in a cloud service. All of the main providers have specific ML directed workspaces, that can make setup of the MLOps much faster.

Scraping the data from the web means working with big amount of text data, which might be a problem on a single computer. **Kubeflow** would allow us to work with external computing resources and not be limited by machine capacity of our own hardware. Alternatively it would be possible to use **Airflow** for the pipeline. However it is expected, that models and data flow are quite small, so the question is, whether the initial effort invested in setup of one of these tools will be worth the time. Using Cloud will offer the benefits of external machine power and allows to benefit from ML solutions of cloud providers.

### Data Warehouse

The app saves very limited number of information types: text data, scraped from web, that only comes from one source in the app, and generated PDFs. It means, there is no nedd for a complicated daa model. Also we can limit the number of potential data operations, that will be required in the future and we know, that it won't be required to upload big amounts of data in single queries. This low requirements don't require a high-scale Data Warehouse.

Implementing a Data Lake allows to store different types of data, including not-structured PDFs. It also gives us some room, in case that during implementation more Use Cases for data storage will be discovered. 

Depending on the budget we can use solutions from cloud providers to design a data lake and store the data. At the start to save costs and save time for implementation, we can store data in Notion. With time we can develop an image, how much storage space is required, how often are the data queried and how much is the load by transactions, and chosse a suitable alternative solution, if it is required.

Sources:
* https://towardsdatascience.com/from-devops-to-mlops-integrate-machine-learning-models-using-jenkins-and-docker-79034dbedf1
* https://github.blog/2022-02-02-build-ci-cd-pipeline-github-actions-four-steps/
* https://towardsdatascience.com/hugging-face-a-step-towards-democratizing-nlp-2c79f258c951