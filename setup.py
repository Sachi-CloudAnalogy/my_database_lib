from setuptools import setup, find_packages

setup(
    name='my_database_lib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'psycopg2-binary'
    ],
)
