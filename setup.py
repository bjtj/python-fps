import setuptools

long_description = 'python fps display utility'

setuptools.setup(name='pyfps',
                 version='1.0.3',
                 author='bjtj',
                 author_email='bjtj10@gmail.com',
                 description='python fps tool',
                 long_description=long_description,
                 long_description_content_type='text/markdown',
                 url='https://github.com/bjtj/python-fps',
                 packages=setuptools.find_packages(),
                 classifiers=[
                     'Programming Language :: Python :: 3',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: OS Independent',
                 ],
)
