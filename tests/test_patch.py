#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2011-2013 Codernity (http://codernity.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from threading import RLock

from CodernityDB3 import lfu_cache, patch, rr_cache


class TestPatches:

    def test_lfu(self):
        orig_1lvl = lfu_cache.cache1lvl
        orig_2lvl = lfu_cache.cache2lvl
        try:
            patch.patch_cache_lfu(RLock)
            assert lfu_cache.cache1lvl is not orig_1lvl
            assert lfu_cache.cache2lvl is not orig_2lvl
        finally:
            lfu_cache.cache1lvl = orig_1lvl
            lfu_cache.cache2lvl = orig_2lvl

    def test_rr(self):
        orig_1lvl = rr_cache.cache1lvl
        orig_2lvl = rr_cache.cache2lvl
        try:
            patch.patch_cache_rr(RLock)
            assert rr_cache.cache1lvl is not orig_1lvl
            assert rr_cache.cache2lvl is not orig_2lvl
        finally:
            rr_cache.cache1lvl = orig_1lvl
            rr_cache.cache2lvl = orig_2lvl
