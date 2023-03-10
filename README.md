# Article Summariser

Article Summariser is a streamline app which summarizes an article of your choice by simply providing an URL

## Installation

Step 1 : Clone the repository 

```bash
$ git clone https://github.com/vnaydenovaa/article-summarizer.git
```
for more info check [https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)



Step 2 : Create a subfolder in this repo, called .streamlit



Step 3 : Create a file at .streamlit/secrets.toml file with your opeanai api key:

```bash
<API_KEY>  
```


Step 4 : Install packages with pip

```bash
pip install -r requirements.txt 
```


Step 5 : Run in terminal

```bash
streamlit run app.py   
```

Your streamlit summariser is running.
