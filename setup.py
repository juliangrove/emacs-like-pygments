from setuptools import setup, find_packages

setup(name='emacs-like-pygments',
      description='Emacs-like pygments color schemes for use with minted.',
      packages=find_packages(),
      entry_points="""
                   [pygments.styles]
                   el-gruvbox-dark = el_gruvbox_dark.style:ELGruvboxDark
                   el-gruvbox-light = el_gruvbox_light.style:ELGruvboxLight
                   """
      )
