from setuptools import setup

install_requires = ['click']

setup(
    name="wrap_si_units",
    version="0.1",
    long_description=__doc__,
    packages=['wrap_si_units'],
    install_requires=install_requires,
    package_data={'wrap_si_units': ['default-si-units.txt']},
    include_package_data=True,
    zip_safe=True,
    entry_points="""
        [console_scripts]
        wrap-si-units=wrap_si_units:cli
    """
)

