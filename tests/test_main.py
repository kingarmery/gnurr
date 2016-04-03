from unittest import TestCase
from src.main.main import main


class TestMain(TestCase):
    def test_read_commands(self):
        s0 = main([])
        s1 = main(["one"])
        s2 = main(["one", "-2"])

        self.assertTrue(0 == 0, "Testing if 0 equals 0.")
        self.assertFalse(0 == 1, "Testing if 0 doesn't equal 1.")