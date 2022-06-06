---
title: "Brainstorming about project flow"
date: 2022-05-01T14:22:01+02:00
draft: false
summary: Technical requirements
categories:
- 'blog'
tags:
- 'blog'
- 'miro'
- 'CRISP-DM'
---

As I want to deliver the product iteratively, I separated the desired functionality in 3 releases, that build-up on the previous state and after each deployment deliver a running product to the users.

Release 1 - generate PDF from a URL provided by user. 

Release 2 - save PDF and data to data base, if user gave consent.

Release 3 - provide a choice of 2 templates for PDF.

Release 4 - if user types is some ingredients, he should get a recipe recommendation from the recipes stored in data base.

*Note: it is visible from Miro board, that at the beginninge Release 1 and 2 were in one unit and next Release was 1.5. After some consideration I separated Release 1 in two parts, defining MVP as just delivering a PDF to the user and bringing non-behavioral functionality to the next iteration. Also for the sake of simplicity I swithced to integer numbers in release numeration.*

For the further definition of project flow I used CRISP-DM, here is the screenshot from the first phase of brainstorming:
![crisp_picture](https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/photo_protocol/recipe2pdf_-_CRISP-DM_.jpg)

Second phase of brainstorming:

![crisp_picture_2](https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/photo_protocol/recipe2pdf-CRISP-DM__2.jpg)

For detailed analysis of DS methodology and flow see [this post](https://hexann666.github.io/recipe2pdf.github.io/posts/ds_concept/).