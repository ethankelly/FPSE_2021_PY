from src.adapter_soln import Input
import unittest


class ConsoleInput(Input):

    def getString(self, message):
        return input(message)