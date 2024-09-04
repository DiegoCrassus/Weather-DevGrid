from setuptools import setup, find_packages

setup(
    name="ppa",
    version="1.0.0",
    description="Microservice architecture module.",
    url="-",
    author="Diego Crassus",
    classifiers=[
        "Development Status :: Developer/Alpha",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="Flasgger documentation",
    packages=find_packages(),
    install_requires=["flask-restx==0.9.2", "Flask-SQLAlchemy==2.1"],
)
