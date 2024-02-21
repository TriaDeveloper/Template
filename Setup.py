from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='Template_RPA',
    version='0.0.17',
    license='MIT License',
    author='Joao Buso',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='developer@hypercoe.com',
    keywords='template rpa hypercoe tria software',
    description=u'Template para desenvolvimento RPA',
    packages=['Template_RPA'],
    install_requires=['requests','psutil','pyautogui','rpa_hypercoe_log'],)