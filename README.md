# Static Site Generator

This is a project done for boot.dev. The object of the project was to build a site generator where, given a proper markdown file (.md), it would turn it into html code. 

## How to run

1. Pull the repository locally (either by cloning it, or by downloading the .zip).
2. *Important!* I am using python@3.11. I have to specify in ```main.sh``` this version. I have another version of python (3.9 I think) installed by default and have not figured out how to make 3.11 the default. Anyways, if you don't have 3.11 installed, this may not work as intended. So, you can update the python versions in main.sh by changing all of the **python3.11** instances to python3, or whatever version you prefer.
3. Once that is complete, you can type ```./main.sh``` and the script will take care of the rest:

*Removing all contents from the /public directory, copying files over, and finally staring a python server listening on port 8888.*

4. To see the generated webpage, open up your browser of choice, and navigate to ```localhost:8888```. You will see the html code generated there. :)

## How to add new pages
If you would like to add any markdown or pages, please do the following:

1. Move the **valid** markdown file (.md extension) under the content/ directory. 
2. Take the majesty/ directory as an example and make a separate directory for this markdown file (```content/my_new_file/index.md``` for example).*
3. Go back to step 2. under *How to Run*

