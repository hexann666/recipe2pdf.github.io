---
title: "Architecture"
date: 2022-05-19T17:57:49+02:00
draft: true
summary: 
categories:
tags:
---

## Architecture

### Deployment

For implementation of UI we can not use Steamlit, as Streamlit apps aren't static. As Streamlit apps can not run on static-file host (eg. GitHub pages, where current recipe2PDF documentation website is running), we have to select another platform to host the functional part of the website. Most of them are paid, like AWS, Azure etc., but Heroku is an option, though it has a free tier.