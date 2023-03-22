from setuptools import find_packages,setup
from typing import List


hypen_e_dot="-e ."
def get_requirements(file_path:str) ->List[str]:
    "This will install all the packages "
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements


setup(
name="Machine Learning Project",
version="0.0.1",
author="Gajender",
author_email="Iamsanju0707@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt")

)