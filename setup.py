from setuptools import setup, find_packages
from titlecase import __version__

setup(
    name='titlecase',
    version=__version__,
    description="Stewart Colville's port of John Gruber's titlecase.pl",
    package_dir={'titlecase': 'titlecase'},
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
    ],
    zip_safe=False,
)
