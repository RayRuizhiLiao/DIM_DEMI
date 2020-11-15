from setuptools import setup

setup(name='cortex_DIM_DEMI',
      version='0.14',
      description='The Deep InfoMax package',
      author='R Devon Hjelm',
      author_email='erroneus@gmail.com',
      packages=['cortex_DIM_DEMI', 'cortex_DIM_DEMI.configs', 'cortex_DIM_DEMI.functions', 'cortex_DIM_DEMI.nn_modules',
                'cortex_DIM_DEMI.models', 'cortex_DIM_DEMI.evaluation_models'],
      install_requires=['cortex==0.13a0'],
      zip_safe=False)
