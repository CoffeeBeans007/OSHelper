from setuptools import setup

setup(
    name='OSHelper',
    version='0.1.0',    
    description='A example Python package',
    url='https://github.com/CoffeeBeans007/OSHelper.git',
    author='Thomas Vaudescal',
    author_email='jeanchristophegaudreau@hotmail.com',
    license='BSD 2-clause',
    packages=['pyexample'],
    install_requires=['mpi4py>=2.0',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Working',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)