python_binary(
    name = 'WFTransactionGrabber',
    source = 'WFTransactionGrabber.py',
    dependencies = [
        '//:splinter',
        'src/splinterbot:splinterbot'
    ],
    compatibility = ['>=2.7','<3']
)

python_binary(
    name = 'EnrollmentChecker',
    source = 'EnrollmentChecker.py',
    dependencies = [
        '//:splinter',
        'src/splinterbot:splinterbot',
        'src:gmail'
    ],
    compatibility = ['>=2.7','<3']
)
