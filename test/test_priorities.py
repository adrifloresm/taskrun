# Python 3 compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from .OrderCheckObserver import OrderCheckObserver
import unittest
import taskrun


class PrioritiesTestCase(unittest.TestCase):
  def test_pri1(self):
    ob = OrderCheckObserver(['+t1', '+t2', '-t1', '-t2'])
    tm = taskrun.TaskManager(observer=ob)
    t1 = taskrun.ProcessTask(tm, 't1', 'sleep 0.01')
    t2 = taskrun.ProcessTask(tm, 't2', 'sleep 0.02')
    t1.priority = 2
    t2.priority = 1
    tm.run_tasks()
    self.assertTrue(ob.ok())

  def test_pri2(self):
    ob = OrderCheckObserver(['+t2', '+t1', '-t1', '-t2'])
    tm = taskrun.TaskManager(observer=ob)
    t1 = taskrun.ProcessTask(tm, 't1', 'sleep 0.01')
    t2 = taskrun.ProcessTask(tm, 't2', 'sleep 0.02')
    t1.priority = 1
    t2.priority = 2
    tm.run_tasks()
    self.assertTrue(ob.ok())

  def test_pri3(self):
    ob = OrderCheckObserver('+t4 +t3 +t2 +t1 -t1 -t2 -t3 -t4'.split())
    tm = taskrun.TaskManager(observer=ob)
    t1 = taskrun.ProcessTask(tm, 't1', 'sleep 0.01')
    t2 = taskrun.ProcessTask(tm, 't2', 'sleep 0.02')
    t3 = taskrun.ProcessTask(tm, 't3', 'sleep 0.03')
    t4 = taskrun.ProcessTask(tm, 't4', 'sleep 0.04')
    t1.priority = 1
    t2.priority = 2
    t3.priority = 3
    t4.priority = 4
    tm.run_tasks()
    self.assertTrue(ob.ok())

  def test_pri4(self):
    ob = OrderCheckObserver('+t2 +t1 +t3 +t4 -t1 -t2 -t3 -t4'.split())
    tm = taskrun.TaskManager(observer=ob)
    t1 = taskrun.ProcessTask(tm, 't1', 'sleep 0.01')
    t2 = taskrun.ProcessTask(tm, 't2', 'sleep 0.02')
    t3 = taskrun.ProcessTask(tm, 't3', 'sleep 0.03')
    t4 = taskrun.ProcessTask(tm, 't4', 'sleep 0.04')
    t1.priority = 3
    t2.priority = 4
    t3.priority = 2
    t4.priority = 1
    tm.run_tasks()
    self.assertTrue(ob.ok())
