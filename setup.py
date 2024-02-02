from setuptools import setup, find_packages

# Read dependencies from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='syngen', 
    version='0.1', 
    packages=find_packages(),
    install_requires = requirements, 
    author='Ananya Pathak',
    author_email='',
    description='Create finetuning/distillation data fast! Multi-model support for regularization against single model biases.',
    long_description="test",
    long_description_content_type='text/markdown',
    url='https://github.com/AnanyaP-WDW/syngen',  
    license='Apache 2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)