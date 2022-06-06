---
title: "About"
date: 2022-05-08T10:21:59+02:00
draft: false
summary: About the project
---

The idea for the project came from following question: how would it be possible to keep recipes found online, originally scattered on different platforms and being visualised with different styles, in one place, structure them in the same manner, create own cook book and extend it on the fly every time a new inspiring recipe appears?

The planning phase of the project was structured according to following schedule and contained 7 topics. 

![time_UML](https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/photo_protocol/UML-time_diagram.png)

Planning activities were divided in sprints and progress was documented and tracked in [Scrum boards](https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/photo_protocol/scrum_epic_board_1.JPG)

To sum up the planning phase of this project a [website](https://hexann666.github.io/recipe2pdf.github.io/) was created, that contains planning documentation (section [Blog](https://hexann666.github.io/recipe2pdf.github.io/)) and [requirements](https://hexann666.github.io/recipe2pdf.github.io/page/requirements/). Website structure, contents and navigation are described in the blog article ["Web Technologies"](https://hexann666.github.io/recipe2pdf.github.io/posts/web_technologies.md)

During the planning phase multiple decisions were made, concerning the project setup: tools, that will be used for development and deployment, libraries, strategies for data preparation and analysis. Some proof of concept were made to ensure, that desired functionality can be implemented with selected tools. Also UX was thought through and a demo of UI was created.

The process flow of this project includes following steps: web scraping from a URL, provided by user in the UI; using NLP models to classify text and find the chunks, that are important for future cooking process; store them; create a PDF from these text pieces, arranging the elements on the page according to the templates. Second use case, which is independent from the first one in user's perspective, is generation of recipe recommendations based on typed in ingredients using another ML model. should be created, that will take in the ingredients, turn them into bag of words and compare with stored datasets, gained in the use case 1, choosing the one, that will have highest match of ingredients. In this way data, scraped, cleaned and classified in the UC1 can be used in UC2.

![user_journey](https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/photo_protocol/user_journey.png)

This project allowed to evaluate and simulate all activities, that are needed for an ML project, from an idea to a state, that is ready for actual implementation to start. Various topics, that were anlyzed, show, that code is just a small part of such project and much effort is needed to make it accesible to a user. It includes not only UI, but also elements of a workflow, that sty invisible for a user, hence contributing to stable work of the software: development environment,  storage space, tools and platforms to deploy the ready software state, tools for project organisation to make working process transparant and understandable for the team. It would be a mistake to expect, that only a good code can be enough for a good ML application. As long as it only exists in a Jupyter Notebook however progressive and useful the output is, it can't fully achieve it's goal, as nobody can use it's results. Providing solid stable infrastructure is what really allows to maximize the benefits to whole extent and practicing this process is a valuable contribution to my education as Data Scientist.