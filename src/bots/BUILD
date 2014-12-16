python_binary(
    name = 'TransactionDownloader',
    source = 'TransactionDownloader.py',
    dependencies = [
        '//:splinter',
        'src/splinterbot:splinterbot',
        'src/sites:sites.wells_fargo'
    ],
    compatibility = ['>=2.7','<3']
)

python_binary(
    name = 'EnrollmentChecker',
    source = 'EnrollmentChecker.py',
    dependencies = [
        '//:splinter',
        'src/splinterbot:splinterbot',
        'src:gmail',
        'src/sites:sites.myred'
    ],
    compatibility = ['>=2.7','<3']
)
