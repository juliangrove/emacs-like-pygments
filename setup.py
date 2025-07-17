from setuptools import setup, find_packages

setup(name='el-gruvbox-light',
      description='Emacs-like pygments color schemes for use with minted.',
      packages=find_packages(),
      entry_points="""
                   [pygments.styles]
                   el-gruvbox-light = el-gruvbox-light.style:ELGruvboxLight
                   """
      )
