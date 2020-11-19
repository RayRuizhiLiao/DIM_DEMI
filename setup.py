from setuptools import setup

setup(name='cortex_DIM_DEMI_demi',
      version='0.15.4',
      description='The Deep InfoMax package (with DEMI)',
      author='Ruizhi Ray Liao; R Devon Hjelm',
      author_email='ruizhi@mit.edu; erroneus@gmail.com',
      packages=['cortex_DIM_DEMI_demi', 'cortex_DIM_DEMI_demi.configs', 'cortex_DIM_DEMI_demi.functions', 'cortex_DIM_DEMI_demi.nn_modules',
                'cortex_DIM_DEMI_demi.models', 'cortex_DIM_DEMI_demi.evaluation_models'],
      install_requires=['cortex==0.13a0'],
      zip_safe=False)
