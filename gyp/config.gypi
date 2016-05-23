# Copyright 2016 Nidium Inc. All rights reserved.
# Use of this source code is governed by a MIT license
# that can be found in the LICENSE file.

{
    'variables' : {
        'nidium_version': '0.1',
        'nidium_webgl%': 1,
        'nidium_audio%': 1,
        'nidium_embed_private%': 0,
        'nidium_private_dir': '../src/JS/',
        'nidium_private_bin_header': '../src/Native_private_bin.h',
        'nidium_private_bin': '../resources/private.bin',

        'nidium_src_path': '../src/',
        'nidium_av_path': '<(nidium_src_path)/AV/',
        'nidium_app_path': '<(nidium_src_path)/Frontend/app/',
        'nidium_interface_path': '../src/Interface/',
        'nidium_network_path': '../src/libapenetwork/',
        'nidium_resources_path': '../resources/',
        'nidium_tools_path': '../tools/',
        'nidium_tests_path': '../tests/gunittest/',
        'nidium_exec_name': 'nidium',
        'nidium_exec_path': '../bin/',

        'nidium_output%': '../out/',
        'nidium_tests_output%': 'tests/',
        'nidium_output_third_party%': '../out/third-party-libs/release/',
        'third_party_path': '../third-party/',

        # Hack to workaround two gyp issues : 
        # - Variables defined in command line are not relativized (at all)
        #   https://code.google.com/p/gyp/issues/detail?id=72
        #
        # - Variables named with a "%" at the end are not relativized
        #   https://code.google.com/p/gyp/issues/detail?id=444
        'variables': {
            'third_party%': 'third-party'
        },
        'third_party_path': '<(DEPTH)/<(third_party)',

        'asan%': 0,
        'jemalloc%': 0,
        'profiler%': 0,
        'target_os%': '<(OS)',
        'mac_deployment_target': '10.7',
        'mac_sdk_version%': '10.11',

        # Crash reporter settings
        'nidium_enable_breakpad%': 0,
        'nidium_crash_collector_host': 'crash.nidium.com',
        'nidium_crash_collector_port': 80,
        'nidium_crash_collector_endpoint': '/submit',

        # Linux build only
        'nidium_use_gtk': 1,

        # Nidium server specifics
        'nofork%': 0
    },
}