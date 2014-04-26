{
  'target_defaults': {
      'default_configuration': 'Release',
      'configurations': {
          'Debug': {
              'cflags_cc!': ['-O3', '-Os', '-DNDEBUG'],
              'xcode_settings': {
                'OTHER_CPLUSPLUSFLAGS!':['-O3', '-Os', '-DNDEBUG'],
                'GCC_OPTIMIZATION_LEVEL': '0',
                'GCC_GENERATE_DEBUGGING_SYMBOLS': 'YES'
              },
              'msvs_settings': {
                  'VCCLCompilerTool': {
                      'ExceptionHandling': 1, # /EHsc
                      'RuntimeTypeInfo': 'true' # /GR
                  }
              }
          },
          'Release': {
              'xcode_settings': {
                'GCC_OPTIMIZATION_LEVEL': 's',
                'GCC_GENERATE_DEBUGGING_SYMBOLS': 'NO',
                'DEAD_CODE_STRIPPING':'YES',
                'GCC_INLINES_ARE_PRIVATE_EXTERN':'YES'
              },
              'ldflags': [
                    '-Wl,-s'
              ],
              'msvs_settings': {
                  'VCCLCompilerTool': {
                      'ExceptionHandling': 1, # /EHsc
                      'RuntimeTypeInfo': 'true' # /GR
                  }
              }
          }
      }
  }
}