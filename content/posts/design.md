---
title: "Design"
date: 2022-05-19T17:57:37+02:00
draft: false
summary: Design of the web application
categories:
tags:
- 'setup'
- 'software'
---

Application will be developed as microservices, because 2 planned Use Cases (UC) are relatively independent of each other. Their dependency is, that the 2. UC generates recommendation based on the data collected in the first month of productive work of the 1. UC.
As we will develop the application iteratively, it should be easy to add a new microservice, as we will start implementing the recommendation engine.

![microservice_scheme](https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/diagrams+process_flows/microservices_architecture.drawio.png)

### Patterns

It is possible to use **Bridge** pattern for the template generation: we can specify the class "TextFormat" inside of the class PDF.
In this case, if at some point another format than A4 will be used, we can delegate text formatting of the elements to this class.
Implementing a class for specific format, eg. Arial 12 cursive and Times 14 bold underlyned, can be than applied without the need to specify a special object for A5 landscape with Times ... and A4 portrait with Times and A5 with Arial and A4 with Arial.

If we extend templates to A4 and A5 formats, different coordinates should be provided to place the text blocks. In this case we could write a wrapper, that would pass the x and y parameters to the class.

We can use a **Facade** pattern to hide the complicated model's framework (for scraping and labeling the text from cooking websites) behind simple interface.
In this case facade would reach to all methods, that we need to proceed with the ML algorithm. 
An application class would only reach to this facade class and it doesn't depend on classes provided by the complex framework. If at some point we would change our ML model, it won't demand update of application. 
It is also possible to make two facades for models of two use cases: generating recipe recommendation and recognition of text blocks.

### Tests

Tests will be written simultaneously with code and will be part of CI/CD pipeline. We will write tests for parts of application, testing the input/output of the functions as well as end-to-end tests to make sure the application is working in the desired way.

### Logging

Logging will be introduced to track user activity on the website. The log table should be extended with info messages every time, when:
- a user pastes an URL and confirms the input
- when a PDF is generated
- a new input to data base is written
- when user clicks on "inspire me"
- a new recommendation is generated.

Error messages shall be stored, if:
  
- PDF was not generated
- an attempt of writing to data base failed
- a recommendation could not be generated

### Internationalisation

The need of internationalisation depends on the algorithm, that we will choose to work with scraped text data. If we will use the function, that analyse the meaning of words, it will mean the need to re-write model for each new language we want to introduce as working language, as the library should contain the vocabulary in this language.
However, if we only train model without analysing the meaning of words, bit rather concentrating on a word as a sequence of string, we can extend the application to all languages, that use latin alphabet as long as we make sure, that special characters are either cleaned/substituted in the data preparation step or are familiar to the model.
Of course there still must be a training step for each new langugage, as the algorithm needs to create a "bag of words" and calculate the frequency of different words appearing in recipes in this particular language.

Even if we only take into account English speaking recipes, we have to adopt some strategy to work with both metric and imperial units, as imperial units are very frequent in the US-English recipes. At first it's enough to just use the original units in the source recipe. For later development stages we can plan a feature to transform units of one metric system into another.