from distutils.core import setup

setup(
    name='kugdc',
    version='0.1',
    author=u'Isaac Cook',
    author_email='isaac@simpload.com',
    packages=['gdc_site', 'gdc'],
    requires=['django','south'],
    license='BSD licence, see LICENCE.txt',
    description='Simple website for University of Kansas Game Design Club',
    zip_safe=False,
)
