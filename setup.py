from setuptools import find_packages, setup



with open('README.md',"r") as f:
    long_description = f.read()

with open("requirements.txt","r") as f:
    install_deps = f.readlines()


setup(
    name='FreeTAKServer',
    packages=find_packages(include = ['FreeTAKServer', 'FreeTAKServer.*']),
    version='1.9.8',
    license='Eclipse License',
    description='An open source server for the TAK family of applications.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='FreeTAKTeam',
    author_email='your.email@domain.com',
    url='https://github.com/FreeTAKTeam/FreeTakServer',
    download_url='https://github.com/Tapawingo/FreeTakServer/archive/v0.8.4-Beta.tar.gz',
    keywords=['TAK', 'OPENSOURCE'],
    install_requires=install_deps,
    extras_require = {'ui': ['FreeTAKServer_UI']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
