from distutils.core import setup
setup(
    name='ter',
    packages=['ter'],
    version='0.0.1',
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    description='Ter is a simple CLI framework for Python App',
    author='Ming-doan',
    author_email='quangminh57dng@gmail.com',
    # Provide either the link to your github or to your website
    url='https://github.com/user/reponame',
    # I explain this later on
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    # Keywords that define your package best
    keywords=['Terminal', 'Python App',
              'Terminal App', 'CLI', 'CLI Framework'],
    install_requires=[],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.10',
    ],
)
