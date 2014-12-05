source_root('src', python_binary, python_library)

python_binary(
  name = 'WFTransactionGrabber',
  source = 'src/WFTransactionGrabber.py',
  dependencies = [
    'src:browsers',
    'src:driver_utils',
    ':splinter',
  ]
)

python_requirement_library(
    name='splinter',
    requirements=[
        python_requirement('splinter==0.7.0'),
    ]
)
