from setuptools import setup, find_packages


setup(
    # include_package_data=True,
    name='helmcli',
    version='1.0.0',
    packages=find_packages(),
    package_data={
    },
    entry_points={
        'console_scripts': [
            ' helmcli = helm.main:cli'
        ]}
)
