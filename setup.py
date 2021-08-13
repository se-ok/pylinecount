from setuptools import setup, find_packages

setup(
    name='pylinecount',
    version='0.1',
    description='Count number of .py code lines',
    author='Seongmin Ok',
    author_email='seongmin.ok@gmail.com',
    url='https://github.com/se-ok/pylinecount',
    download_url='https://github.com/se-ok/pylinecount/archive/refs/heads/main.zip',
    install_requires=[],
    packages=find_packages(exclude=[]),
    keywords=['line count'],
    python_requires='>=3',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)