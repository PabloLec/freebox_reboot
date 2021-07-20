from setuptools import setup, find_packages

with open("requirements.txt", "r") as req_fp:
    required_packages = req_fp.readlines()


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="freebox_reboot",
    version="1.0.1",
    author="Pablo Lecolinet",
    author_email="pablolec@pm.me",
    license="MIT License",
    keywords="free freebox reboot",
    description="Simple script pour redémarrer une Freebox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PabloLec/freebox_reboot",
    packages=find_packages(exclude=["tests", "docs"]),
    project_urls={
        "Bug Tracker": "https://github.com/PabloLec/freebox_reboot/issues",
    },
    entry_points={
            "console_scripts": [
                "freebox_reboot = freebox_reboot:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    package_data={"freebox_reboot": ["free.cert"]},
    include_package_data=True,
    install_requires=required_packages,
    python_requires=">=3.6",
)
