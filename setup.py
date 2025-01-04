from setuptools import find_packages,setup
from typing import List
def get_requirements()->List[str]:
    requirements_list : List[str]= []
    return requirements_list

setup(
    name ='Live Sensor',
    version = "0.0.1",
    author= 'Shashank Singh',
    author_email = 'shashanksinghmain@gmail.com',
    description = 'This is a live sensor project',
    packages= find_packages(),
    install_requires = get_requirements(),

)