'''
The setup.py file is an essential part of packaging and distributing Python
code. It is a script that you write that tells Python how to install your 
package. It is also used to specify the dependencies that your package has.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return the list of requirements
    """

    requirement_list:List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            #read lines from the file
            lines = file.readlines()
            #process each line
            for line in lines:
                requirement = line.strip()
                #ignore the empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_list

# print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.0.1",
    author="Simarjeet Singh",
    author_email="simarjeetss509@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)