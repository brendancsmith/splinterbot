python_library(
  name = 'bots-lib',
  dependencies = [
  ]
)

python_binary(
    name = 'WFTransactionGrabber',
    source = 'WFTransactionGrabber.py',
    dependencies = [
        '//:splinter',
        'src:browsers',
        'src:utils'
    ],
    compatibility = ['>=2.7','<3']
)

python_binary(
    name = 'EnrollmentChecker',
    source = 'EnrollmentChecker.py',
    dependencies = [
        '//:splinter',
        'src:browsers',
        'src:utils',
        'src:gmail'
    ],
    compatibility = ['>=2.7','<3']
)
