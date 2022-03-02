# -*- coding: utf-8 -*-
#
# K2hash Python Driver
#
# Copyright (c) 2022 Yahoo Japan Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
# AUTHOR:   Hirotaka Wakabayashi
# CREATE:   Tue Feb 08 2022
# REVISION:
#

import unittest
import k2hash
import logging
import time

class TestKeyQueue(unittest.TestCase):

    def test_KeyQueue_construct(self):
        db = k2hash.K2hash()
        q = k2hash.KeyQueue(db)
        self.assertTrue(isinstance(q, k2hash.KeyQueue))
        self.assertTrue(q.close(), True)
        db.close()

    def test_KeyQueue_put(self):
        db = k2hash.K2hash()
        db = k2hash.K2hash()
        q = k2hash.KeyQueue(db)
        self.assertTrue(isinstance(q, k2hash.KeyQueue))
        self.assertRaises(TypeError, q.put)
        self.assertTrue(q.close(), True)
        db.close()

    def test_KeyQueue_put_with_obj(self):
        db = k2hash.K2hash()
        q = k2hash.KeyQueue(db)
        self.assertTrue(isinstance(q, k2hash.KeyQueue))
        obj={"k1": "v1"}
        self.assertTrue(q.put(obj), True)
        self.assertTrue(q.get(), obj)
        self.assertTrue(q.close(), True)
        db.close()

    def test_KeyQueue_clear(self):
        db = k2hash.K2hash()
        q = k2hash.KeyQueue(db)
        self.assertTrue(isinstance(q, k2hash.KeyQueue))
        obj={"k1": "v1"}
        self.assertTrue(q.put(obj), True)
        self.assertTrue(q.qsize() == 1)
        self.assertTrue(q.clear(), True)
        self.assertTrue(q.qsize() == 0)
        self.assertTrue(q.close(), True)
        db.close()

    def test_KeyQueue_close(self):
        db = k2hash.K2hash()
        q = k2hash.KeyQueue(db)
        self.assertTrue(isinstance(q, k2hash.KeyQueue))
        self.assertTrue(q.close(), True)
        db.close()

    def test_KeyQueue_qsize(self):
        db = k2hash.K2hash()
        q = k2hash.KeyQueue(db)
        self.assertTrue(isinstance(q, k2hash.KeyQueue))
        obj={"k1": "v1"}
        self.assertTrue(q.put(obj), True)
        self.assertTrue(q.qsize() == 1)
        self.assertTrue(q.close(), True)
        db.close()

    def test_KeyQueue_element(self):
        db = k2hash.K2hash()
        q = k2hash.KeyQueue(db)
        obj={"k1": "v1"}
        self.assertTrue(q.put(obj), True)
        self.assertTrue(q.element(), obj)
        self.assertTrue(q.close(), True)
        db.close()

    def test_KeyQueue_element_with_position(self):
        db = k2hash.K2hash()
        q = k2hash.KeyQueue(db)
        self.assertTrue(isinstance(q, k2hash.KeyQueue))
        obj={"k1": "v1"}
        self.assertTrue(q.put(obj), True)
        self.assertTrue(q.element(1) == {})
        self.assertTrue(q.close(), True)
        db.close()

    def test_KeyQueue_handle(self):
        db = k2hash.K2hash()
        q = k2hash.KeyQueue(db)
        self.assertTrue(isinstance(q, k2hash.KeyQueue))
        self.assertFalse(q.handle == k2hash.K2hash.K2H_INVALID_HANDLE)
        self.assertTrue(q.close(), True)
        db.close()

    def test_KeyQueue_empty(self):
        db = k2hash.K2hash()
        q = k2hash.KeyQueue(db)
        self.assertTrue(isinstance(q, k2hash.KeyQueue))
        self.assertTrue(q.empty(), True)
        self.assertTrue(q.close(), True)
        db.close()

    def test_KeyQueue_get(self):
        db = k2hash.K2hash()
        q = k2hash.KeyQueue(db)
        self.assertTrue(isinstance(q, k2hash.KeyQueue))
        obj={"k1": "v1"}
        self.assertTrue(q.put(obj), True)
        self.assertTrue(q.get(), obj)
        self.assertTrue(q.close(), True)
        db.close()

    def test_KeyQueue_print(self):
        db = k2hash.K2hash()
        q = k2hash.KeyQueue(db)
        self.assertTrue(isinstance(q, k2hash.KeyQueue))
        self.assertTrue(q.print(), True)
        self.assertTrue(q.close(), True)
        db.close()

    def test_KeyQueue_remove(self):
        db = k2hash.K2hash()
        q = k2hash.KeyQueue(db)
        self.assertTrue(isinstance(q, k2hash.KeyQueue))
        obj={"k1": "v1"}
        self.assertTrue(q.put(obj), True)
        self.assertTrue(q.qsize() == 1)
        self.assertTrue(q.remove(), True)
        self.assertTrue(q.qsize() == 0)
        self.assertTrue(q.close(), True)
        db.close()

    def test_KeyQueue_remove_with_count(self):
        db = k2hash.K2hash()
        q = k2hash.KeyQueue(db)
        self.assertTrue(isinstance(q, k2hash.KeyQueue))
        obj={"k1": "v1"}
        self.assertTrue(q.put(obj), True)
        self.assertTrue(q.qsize() == 1)
        self.assertTrue(q.remove(1), True)
        self.assertTrue(q.qsize() == 0)
        self.assertTrue(q.close(), True)
        db.close()

    def test_KeyQueue_repr(self):
        db = k2hash.K2hash()
        q = k2hash.KeyQueue(db)
        self.assertTrue(isinstance(q, k2hash.KeyQueue))
        self.assertTrue(q.close(), True)
        db.close()

if __name__ == '__main__':
    unittest.main()

#
# Local variables:
# tab-width: 4
# c-basic-offset: 4
# End:
# vim600: expandtab sw=4 ts=4 fdm=marker
# vim<600: expandtab sw=4 ts=4
#
