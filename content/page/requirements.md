---
title: "Requirements"
date: 2022-05-01T16:21:59+02:00
draft: false
summary: Technical requirements
tags:
- 'requirements'

---

## Requirements Release 1:

- System must show an input field.
- User should insert a web-link into this field.
- System scrapes web content from the provided link and should look for following informations: recipe_title, ingredients, instructions, notes.
- If recipe_title, ingredients, instructions were found, system must generate a pdf file with recipe_title, ingredients, instructions, notes (if found) according to the template specified in the model configurations after maximum 20 s.
- System must show pdf in a new tab.

## Requirements Release 2:

- User can tick a checkbox with text "Choosing this box you allow us to store your recipe in our data base." (consent checkbox), checkbox is optional for the flow.
- If user gave consent ticking the checkbox and if recipe_title, ingredients, instructions were found, system must store the generated pdf file and recipe_title, ingredients, instructions, notes (if found) and source URL in the data base with the same key.
- Information in the database shall be reachable, if user performs a search, and shall provide result with response time of maximum 30 s.

## Requirements Release 3:

- Provide a choice of templates (min. 2) as pictures (jpg-files) below the insert field.
- System should provide an option to zoom in the template example.
- If user doesn't choose a template, use a default template to generate PDF.

## Requirements Release 4:

- System must show an input field for ingridients.
- User should type in ingridients separated by comma.
- After typing in the ingridients, user shall press button "inspire me!" to confirm. 
- After user pressed "inspire me!" button, validate the input. Only following characters are allowed [A-Za-z, ]
- If any special characters are typed in, don't proceed to the next step and show the error message below the input field: "No special characters are allowed."
- If validation succeeded, use input as input in the ML script.
- ML script shall be ready in max 40 s.
- System should show a loading animation while ML script is running.
- As soon as ML script is ready, the system should show the title of the result with highest score below the "inspire me!" button. The title is a hyperlink to the PDF of the recipe.
- System should show a button "Download PDF".
- If user clicks on the button "Download PDF", system should show a PDF of this recipe in the new browser tab.