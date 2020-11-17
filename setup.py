from setuptools import setup

setup(name='cortex_DIM_DEMI_dev',
      version='0.18',
      description='The Deep InfoMax package',
      author='R Devon Hjelm',
      author_email='erroneus@gmail.com',
      packages=['cortex_DIM_DEMI_dev', 'cortex_DIM_DEMI_dev.configs', 'cortex_DIM_DEMI_dev.functions', 'cortex_DIM_DEMI_dev.nn_modules',
                'cortex_DIM_DEMI_dev.models', 'cortex_DIM_DEMI_dev.evaluation_models'],
      install_requires=['cortex==0.13a0'],
      zip_safe=False)
