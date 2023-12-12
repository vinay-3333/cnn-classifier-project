#setup.py file use for install package and set enviroment for local
#setup.py its take a local package it install in local enviroment
 
import setuptools

__version__ ='0.0.1'

with open("README>md",'r',encoding='utf-8') as f :
    long_description = f.read()


REPO_NAME="cnn-classifier"
AUTHOR_NAME='vinay agrawal'
SRC_REPO="CNNClassifier"
AUTHOR_Email='vagrawal032@gmail.com'



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_Email,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    )

