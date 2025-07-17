from setuptools import setup, find_packages

setup(name='emacs-like-pygments',
      description='Some Emacs-like pygments color schemes.',
      packages=find_packages(),
      entry_points="""
                   [pygments.styles]
                   el-gruvbox-light = el-gruvbox-light.style:ELGruvboxLight
                   """
      )
