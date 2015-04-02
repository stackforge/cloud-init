# Copyright (C) 2015 Canonical Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# vi: ts=4 expandtab

import pkg_resources

try:
    from pbr import version as pbr_version
    _version_info = pbr_version.VersionInfo('cloudinit')
    version_string = _version_info.version_string
except ImportError:
    _version_info = pkg_resources.get_distribution('cloudinit')
    version_string = lambda: _version_info.version
