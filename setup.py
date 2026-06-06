'''
To build our project as a package, we need to create a setup.py file. 
This file will contain the necessary information about our package, 
such as its name, version, and dependencies.
'''


from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='examperformance',
version='0.0.1',
author='Pardhu',
author_email='pardhasaradhireddy00@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)