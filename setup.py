from __future__ import absolute_import, print_function, with_statement

import sys
from glob import glob
from os.path import join

import numpy
from setuptools import Extension, find_packages, setup
from setuptools.command.build_ext import build_ext

_VERSION = "0.3.8"


world_src_top = join("lib", "World", "src")
world_sources = glob(join(world_src_top, "*.cpp"))

ext_modules = [
    Extension(
        name="pyworld.pyworld",
        include_dirs=[world_src_top, numpy.get_include()],
        sources=[join("pyworld", "pyworld.pyx")] + world_sources,
        language="c++",
    )
]

kwargs = {"encoding": "utf-8"} if int(sys.version[0]) > 2 else {}
setup(
    name="pyworld-fixed",
    description="PyWorld: a Python wrapper for WORLD vocoder -- Now supporting Python 3.12",
    long_description=open("README.md", "r", **kwargs).read(),
    long_description_content_type="text/markdown",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    version=_VERSION,
    packages=find_packages(),
    setup_requires=[
        "numpy",
    ],
    install_requires=[
        "numpy",
        "cython>=0.24",
    ],
    extras_require={
        "test": ["nose"],
        "sdist": ["numpy", "cython>=0.24"],
    },
    author="Pyworld Contributors",
    author_email="jackismyshephard@gmail.com",
    url="https://github.com/JackismyShephard/Python-Wrapper-for-World-Vocoder",
    keywords=["vocoder"],
    classifiers=[],
)
