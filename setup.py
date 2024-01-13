import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r', encoding="utf-8") as fp:
    contents = fp.read()
    requirements = list(map(str.strip, contents.split('\n')))

setuptools.setup(
    name='hyperbolic_numpy_ext',
    version='0.0.1',
    author='Inzamam Rahaman',
    author_email='inzamam.rahaman@outlook.com',
    description='An implementation of vector operations in different models of hyperbolic space',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/guardian-group-ti/mck_tooling/guardian-gcp-utils',
    project_urls={
        "Bug Tracker": "https://github.com/guardian-group-ti/mck_tooling/issues"
    },
    license='MIT',
    packages=['hyperbolic_numpy_ext'],
    install_requires=requirements
)