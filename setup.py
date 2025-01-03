from setuptools import find_packages,setup

def get_requirements()->list[str]:
    requirements_list  = list[str]= []
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