import unittest
from unittest.mock import patch
import sys
from io import StringIO
from pkb.cli import main

class TestPKBCLIBasica(unittest.TestCase):
    @patch('sys.argv', ['pkb', '--help'])
    def test_cli_help(self):
        """Verifica que el comando de ayuda imprima la descripción de la CLI sin lanzar excepciones."""
        stdout_simulado = StringIO()
        with patch('sys.stdout', stdout_simulado):
            try:
                main()
            except SystemExit as e:
                # Si llama a sys.exit(), verificamos que sea con código 0
                self.assertEqual(e.code, 0)
        
        self.assertIn("PKB CLI", stdout_simulado.getvalue())

    @patch('sys.argv', ['pkb', 'validate'])
    def test_cli_validate_stub(self):
        """Verifica el enrutamiento inicial hacia el subcomando validate."""
        stdout_simulado = StringIO()
        with patch('sys.stdout', stdout_simulado):
            try:
                main()
            except SystemExit as e:
                self.assertEqual(e.code, 0)
                
        self.assertIn("Motor de validación en desarrollo", stdout_simulado.getvalue())

if __name__ == "__main__":
    unittest.main()