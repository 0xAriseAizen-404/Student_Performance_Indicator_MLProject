from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
  requirements = []
  with open(file_path) as f:
    requirements = [req.replace('\n', '') for req in f.readlines()]
    if HYPEN_E_DOT in requirements:
      requirements.remove(HYPEN_E_DOT)
  return requirements

setup(
  name='Student_Performance_Indicator_MLProject',
  version='1.0.0.0',
  author='0xAriseAizen-404',
  author_email='maheshmahesh6336.6336@gmail.com',
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt'),
)