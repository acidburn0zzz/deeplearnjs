# Copyright 2018 Google Inc. All Rights Reserved.
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
# ==============================================================================

import unittest
from weights_writer import write_weights

class TestWeightsWrite(unittest.TestCase):
  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')
      with open('/tmp/test', 'w') as f:
        f.write('test')
      with open('/tmp/test', 'r') as f:
        print 'contents: ' + f.read()


if __name__ == '__main__':
    unittest.main()
