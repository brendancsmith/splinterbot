python_library(
  name = 'bots-lib',
  dependencies = [
    'src:browsers',
    'src:driver_utils',
    '//:splinter'
  ]
)

python_binary(
    name = 'WFTransactionGrabber',
    source = 'WFTransactionGrabber.py',
    dependencies = [
        'src/bots:bots-lib'
    ],
    compatibility = ['>=2.7','<3']
)

python_binary(
    name = 'SpanishEnrollmentChecker',
    source = 'SpanishEnrollmentChecker.py',
    dependencies = [
        'src/bots:bots-lib'
    ],
    compatibility = ['>=2.7','<3']
)
