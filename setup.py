from setuptools import setup

from django_redis import __version__

description = """
Full featured redis cache backend for Django.
"""

setup(
    name="zh-pinyin",
    url="https://github.com/sunwenquan/zh-pinyin",
    author="Gavin",
    author_email="gavinsun@qq.com",
    version=__version__,
    packages=[
    ],
    description=description.strip(),
    python_requires=">=3.4",
    install_requires=[
    ],
    zip_safe=False,
    include_package_data=True,
    package_data={
        "": ["*.html"],
    },
    classifiers=[
        "Development Status :: 1 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)