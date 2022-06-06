---
title: "Web technologies"
date: 2022-06-04T15:13:56+02:00
draft: false
summary: Description of web technologies used for recipe2PDF project
categories:
- 'blog'
tags: 
- 'web'
- 'website'
- 'practical'
---

### Recipe2PDF documentation blog

To present documentation for this project, a website was created with Hugo. Hugo is quite intuitive tool to create static websites without extensive prior khowledge of programming languages or HTML, which allows a very fast start into site building process. It still allows a lot of flexibility and provides various possibilities for self-expression and experiments with design for those, who feel secure with HTML.

The website map is presented on the scheme below. 

![website map]('https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/photo_protocol/recipe2pdf_-_Website_map.jpg')

Main sections of the website are Blog, About and Requirements. Blog contains articles, that describe future implementation of the project recipe2PDF from different perspectives:
- protocol of project planning ("Brainstorming about project flow")
- practical setup ("Scrum setup", "Data Science methodology and concept")
- choice of tools, that will be used ("Design", "DS architecture")
- proof of concept for the coding part ("Pilot")

Upon entry user sees the list of blog articles. From the panel above the website title user can navigate to "About" or "Requirements" sections. To come back to the list of blog entries user can choose "Blog" on the header panel. This panel is present on every page, so navigation to another point on the website is available at any time and independent on the current position of the user.

![]('https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/photo_protocol/recipe2pdf_website.jpg')

All images used on the website are stored in the Gitlab repository on FH Kufstein server. It creates a dependancy for the website content: if server is not available at the moment, images can't be displayed. Unfortunately, as experience of past 2 semesters shows, server is quite unstable.

### UI of recipe2PDF

To use the functionality of recipe2PDF app, user will interact with web interface. The main buttons to perform actions on the website are described in requirements. For better overview of UI functions a pilot of this interface was built with streamlit to visualize future UI.

After website has loaded, user sees following UI:
![website screenshot]('https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/photo_protocol/UI_pilot_1.JPG')

In the left sidebar user chooses the function she wants to use next: generate PDF or generate recommendation. The middle part of the page changes depending on the choice. Default choice is "Generate PDF".

If **"Generate PDF"** is chosen (or upon opening, as this choice is the default option):

User can insert or type in her weblink in the input field.

Also user can choose a template for her PDF. The samples of templates are shown, if user expands the element with the button "See templates". Templates can be seen in a bigger size, if user clicks on the standard button with two arrows on the right of the image. If image is expanded, user either clicks ESC or clicks on the same button to close the image.

Default setting is to use template 1 for the PDF and this option is preselected. User can change it to template 2.

User can select the checkbox "Choosing this..." and allow her recipe to be stored in the recipe2PDF data base for future use.

The button "Create PDF" starts the script, that extracts the data from provided link, and creates a recipe PDF using them.

If **"Generate recommendation"** is chosen:

![recommendation_screenshot]('https://gitlab.web.fh-kufstein.ac.at/anna.fedorova/recipe2pdf/-/raw/main/photo_protocol/UI_pilot_2.JPG')

User can paste or type in ingredients separated by comma to the input field. After click on "Inspire me!" button a script will run in the background to generate recipe recommendations based on user's input. If a match was found, the recipe title will be displayed below the button. This title is a hyperlink, that opens the source recipe (it's original URL) in the new tab. Also the PDF is downloaded from data base and is available, if user clicks "Download PDF" button.

### Deployment

Initially it was planned to have the UI pilot on a page in recipe2PDF documentation blog. Unfortunately it's not possible to combine Hugo and streamlit, as Hugo creates static websites and Streamlit apps aren't static. As Streamlit apps can not run on static-file host (eg. GitHub pages, where current recipe2PDF documentation website is running), we will have to select another platform to host the functional part of the website in the project. Most of them are paid, like AWS, Azure etc., but Heroku is an option, though it has a free tier.

It is planned to use streamlit only to create a pilot for demo purposes, as streamlit is easy to learn and gives an opportunity to create and deploy websites in minutes, if not seconds, which makes it perfect to create demos. Its disadvantages are some limitations in functionality, starting with inability to have more than one button pressed on the interface - if there are two buttons, both of which perform soem process, you only can have one running and showing results, which will be a big limitation in our context. For pilot we solvd this issue with a selectbox on the sidebar. Still it would be a problem to have "Inspire me!" and "Download PDF" buttons on one page. Also frontend elements are not very customizable with streamlit.

Taking this into consideration, it is currently planned to use Flask to create the web part for the project.

## Source

* https://theibbster.medium.com/how-to-build-a-blog-a-complete-beginners-guide-to-hugo-9f831b50aad
* https://docs.streamlit.io/
* https://towardsdatascience.com/deploying-models-to-flask-fb62155ca2c4