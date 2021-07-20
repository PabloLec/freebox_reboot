import setuptools

with open("requirements.txt", "r") as req_fp:
    required_packages = req_fp.readlines()


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="freebox_reboot",
    version="1.0.0",
    author="Pablo Lecolinet",
    author_email="pablolec@pm.me",
    description="Simple script pour redémarrer une Freebox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PabloLec/freebox_reboot",
    project_urls={
        "Bug Tracker": "https://github.com/PabloLec/freebox_reboot/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    package_data={"": ["free.cert"]},
    include_package_data=True,
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
