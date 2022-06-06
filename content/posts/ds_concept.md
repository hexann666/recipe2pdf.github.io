---
title: "Data Science methodology and concept"
date: 2022-05-01T16:41:56+02:00
draft: false
summary: Project planning according to CRISP-DM
categories:
- 'blog'
tags:
- 'miro'
- 'CRISP-DM'
- 'DS'
---

![crisp_scheme](https://www.datascience-pm.com/wp-content/uploads/2021/02/CRISP-DM.png)

<!--more-->

# Business understanding

To unify business requirements with functionality I formulated the simple acceptance test cases for the main functionality of each release.

### Release 1
#### Behavioral functionality:
**Description:** user provides a URL of a website with a recipe she wants to have as pdf.
**Instructions:**
- paste URL https://www.ambitiouskitchen.com/banana-oatmeal-pancakes/ into an input field.
- confirm URL as source with a click on a "Generate recipe pdf" button.

**Expected result:** a recipe PDF opens in a new tab

### Release 2
#### Behavioral functionality:
**Description:** user provides a URL of a website with a recipe she wants to have as pdf.
**Instructions:**
- paste URL https://www.ambitiouskitchen.com/banana-oatmeal-pancakes/ into an input field.
- tick a checkbox with text "Choosing this box you allow us to store this recipe in our data base.":
- confirm URL as source with a click on a "Generate recipe pdf" button.

**Expected result:** a recipe PDF opens in a new tab.

#### Non-behavioral functionality:
**Description:** if user gave permission to store the data, save pdf and scrpaed text in the data base.
**Instructions:**
- If user ticks a checkbox with text "May we store this recipe in our data base?":
  - store recipe title, ingredients, instructions and notes in database
  - store the recipe PDF in a database with a key=recipe_title

**Expected result:** for key 1 a PDF is stored in database and information from the website from df columns title, ingridients, instructions, note

### Release 3:
#### Behavioral functionality:
**Description:** user can choose a template for the pdf.
**Instructions:**
- paste URL https://www.ambitiouskitchen.com/banana-oatmeal-pancakes/ into an input field
- choose one of three templates.
- optional: tick a checkbox with text "May we store this recipe in our data base?":
- confirm URL as source with a click on a "Generate recipe pdf" button.
  
**Expected result:** PDF is generated with chosen PDF template, if step 2 was done.
*Note: If step 2 was skipped, pdf is generated with a default pdf.*


### Release 4:
#### Behavioral functionality:
**Description:** user can enter ingridients of her choice and get a recipe suggestion.
**Instructions:**
- type in ingridients separated by comma into input field
- confirm input by clicking "inspire me!"
  
**Expected result:** a recipe suggestion is shown below the "inspire me" button.

#### Non-behavioral functionality:
**Description:** user can enter ingridients of her choice and get a recipe suggestion.
**Instructions:**
- type in ingridients "banana, oatmeal, milk, eggs" into input field
- confirm input by clicking "inspire me!"
- run ML algorithm "recipe_prediction" with content of input field as input ariables
- show the result with highest score in a field below the "inspire me!" button
  
**Expected result:** a recipe suggestion is shown below the "inspire me!" button.

# Data understanding

![data_understanding](https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/photo_protocol/recipe2pdf-Data%20understanding.jpg)

I analysed the typical layout and content of some english speaking food blogs. Here are some overall rules on the example of [this recipe](https://www.ambitiouskitchen.com/banana-oatmeal-pancakes/):
- Usually the food blog article consists of an introduction part with some comments from author about the idea of the recipe and some optional suggestions to avoid/substitute/add some ingredients and multiple pictures.

- The next part is the one, that contains actual cooking informations. For the recipe2pdf algorithm this part is crucial. It has following parts, that we will use for PDF generation, storing the data and ML algorithm: title (1), ingredients (2), instructions (3) and some optional notes (4). 

- There is often a button "jump to recipe" at the top of the page, that brings the user to the second part. *Note: can it be used to find the part of the website, which is crucial for our project?*

# Data preparation

Data preparation technique depends on the modeling task. As we have two main technical cluster in the software, data preparation steps will be based on the main issue with data and are taylored to concrete Use Case.

![data_preparation](https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/photo_protocol/recipe2pdf-Data_preparation.jpg)

Detailed overview of solutions, that were chosen for the data preparation in the brainstorming session is displayed in the flow diagram in Modeling section.

# Modeling

On the first diagram entire process is shown from the current perspective with all 3 releases being included in this visualisation. Two use cases are shown from the ser perspective in two swim lanes on the top and the bottom, the swim lane in the middle shows the system operations, that the backend should perform to provide functionality.

![flow_diagram](https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/diagrams+process_flows/flow_diagram.jpeg)

The next process diagram shows the main technical steps and selected solutions for data mining, preparation and modeling. Also it is shown, which steps belong to which release.

![technical_steps](https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/diagrams+process_flows/diagram_technical_steps.png)

Main libraries, that will be used are BeautifulSoup, PDFQuery, FPDF, pdfkit, spacey, sklearn

# Evaluation

This phase will be repeated for every iteration, whereas following questions are to answer after each release:

**Evaluate results:** Do the models meet the business success criteria? The estimation will be conducted with the test results and compared to the acceptance criteria of the release, defined above.

**Review process:** Review the work accomplished. Summarize findings and correct anything if needed. The goal is to compare the expected results according to technical and businss requirement, set before the release and including the changes, that might come up during implementation, and the final product of this release. Lessons learned and process updates should be analysed and drawn for the next iteration.

**Determine next steps:** The decision should be made, if it is possible to deploy current state of the project or some changes are needed. It is possible, that concerning the release results there will be changes in the scope of next release(s).

# Deployment

**Deployment:** for this project deployment with Flask to the recipe2pdf website is planned.
Following diagram summs up the technologies, which were chosen in first phase of planning to support defined architecture:

![recipe2pdf architecture](https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/photo_protocol/recipe2pdf-Architecture.jpg)

More on UI and deployment see in [this post](https://hexann666.github.io/recipe2pdf.github.io/posts/web_technologies/)

**Review project:** Conduct a project retrospective about what went well, what could have been better, and how to improve in the future.


**Sources:**
https://www.datascience-pm.com/crisp-dm-2/
http://www.agilemodeling.com/essays/agileRequirements.htm