import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='OS_Helper',  
     version='0.1',
     scripts=['OS_Helper'] ,
     author="Thomas Vaudescal",
     author_email="jeanchristophegaudreau@hotmail.com",
     description="A directory director package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/CoffeeBeans007/OSHelper.git",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )