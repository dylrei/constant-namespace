from unittest import TestCase

from constant_namespace import ConstantNamespace


class SampleNamespace(ConstantNamespace):
    FOO = 'Foo'
    BAR = 'Bar'
    FLORB = '_Florb_'


class TestConstantNamespace(TestCase):
    def _run_test(self, method, expected):
        self.assertEqual(getattr(SampleNamespace, method)(), expected)

    def test_as_dict(self):
        self._run_test(
            method='as_dict',
            expected={
                'FOO': 'Foo',
                'BAR': 'Bar',
                'FLORB': '_Florb_'
            }
        )

    def test_keys(self):
        self._run_test(
            method='keys',
            expected=['BAR', 'FLORB', 'FOO']
        )

    def test_values(self):
        self._run_test(
            method='values',
            expected=['Bar', 'Foo', '_Florb_']
        )

    def test_items(self):
        self._run_test(
            method='items',
            expected=[
                ('BAR', 'Bar'),
                ('FLORB', '_Florb_'),
                ('FOO', 'Foo'),
            ]
        )

    def test_choices(self):
        self._run_test(
            method='choices',
            expected=[
                ('Bar', 'BAR'),
                ('Foo', 'FOO'),
                ('_Florb_', 'FLORB'),
            ]
        )

    def test_document(self):
        self._run_test(
            method='document',
            expected={
                'SampleNamespace': {
                    'FOO': 'Foo',
                    'BAR': 'Bar',
                    'FLORB': '_Florb_',
                }
            }
        )
