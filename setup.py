from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='cellcount',
    version='0.0.1',
    description='Count the number of contiguous regions in a binary array',
    py_modules=["cellcount"],
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_context_type='text/markdown',
    install_requires = [
        "numpy ~= 1.19"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English"
    ]
)