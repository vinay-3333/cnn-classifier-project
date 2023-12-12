#setup.py file use for install package and set enviroment for local

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
        description="This is my classification project",
        long_description=long_description,
        long_description_content="text/markdown",
        url=f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}'


        project_urls={
            '''if we have some bug in the packages those we can created
                if we can track that this particular url'''
            
            "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"

        },
        package_dir={"":"src"},
        packages=setuptools.findpackage(where='src')

)
