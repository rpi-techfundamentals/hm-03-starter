test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> int(sum(train.PredGenderAge13))
          351
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> int(sum(test.PredGenderAge13))
          168
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> int(sum(train.PredGenderAge18))
          385
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> int(sum(test.PredGenderAge18))
          182
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
