---
title: "Pilot"
date: 2022-05-08T10:55:20+02:00
draft: false
summary: a try-out of technical implementation of the main functionality
categories:
- tech
- blog
tags:
- tech
- python
- code
---

To make sure, that the planned functionality can be implemented in Python, two pilots were built. They don't provide all features, that are defined as project requirements, but give an overview of main libraries, that are necessary for the implementation, and their functions, that will be used.

The notebooks are available in the directory [pilot_code](https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/tree/main/pilot_code), as well as some txt files, that are needed for the functions and PDFs, that were generated as samples.

[Pilot_web_scraping](https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/blob/main/pilot_code/pilot_web_scraping.ipynb) shows some try-outs for the data preparation for the main functionality of the project - finding the relevant text parts on the website and scraping this text for future use. It was shown, that there are two implementation pathes: scraping from Web and scraping from a full PDF of the page. Some funcitons from libraries BeautifulSoup in the first case and pdfquery in the second are provided with some simple functions written to prove, that these strategies could work for the project goal. The aim at the start of actual work on the project would be to extend these try-outs and to choose one of them.

[Pilot_PDF_templates](https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/blob/main/pilot_code/pilot_PDF_templates.ipynb) implements two templates for user to choose from in the release 3 with the functions from FPDF library. 
Functions generate_pdf_template_1 and generate_pdf_template_2 generate PDFs, that can be also found in the directory. Now these functions are taking the text data from txt-files in the directory, however for the full functionality they are supposed to use the scraped data.

Template 1           |  Template 2
:-------------------------:|:-------------------------:
![PDF1](https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/pilot_code/pdf_template_1.png) |  ![PDF2](https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/pilot_code/pdf_template_2.png)

