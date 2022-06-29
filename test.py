import unittest, bank as bk, controller as ctrler

class TestATM(unittest.TestCase):
    def test_insert_card(self):
        bank = bk.Bank()
        bank.add_card(1234, 'password')
        
        controller = ctrler.Controller(bank)
        self.assertTrue(controller.insert_card(1234))
        self.assertFalse(controller.insert_card(5678))
        
    def test_enter_pin(self):
        bank = bk.Bank()
        bank.add_card(1234, 'password')
        
        controller = ctrler.Controller(bank)
        self.assertFalse(controller.enter_pin('password'))
        controller.insert_card(1234)
        self.assertFalse(controller.enter_pin('pass'))
        self.assertTrue(controller.enter_pin('password'))
        
    def test_select_account(self):
        bank = bk.Bank()
        bank.add_card(1234, 'password')
        bank.add_account(1234, 'password', 'Checking')
        bank.add_account(1234, 'password', 'Saving')
        
        controller = ctrler.Controller(bank)
        self.assertFalse(controller.select_account('Checking'))
        controller.insert_card(1234)
        controller.enter_pin('password')
        self.assertTrue(controller.select_account('Checking'))
        self.assertTrue(controller.select_account('Saving'))
        self.assertFalse(controller.select_account('Retirement'))
        
    def test_add_card(self):
        bank = bk.Bank()
        bank.add_card(1234, 'password')
        with self.assertRaises(ValueError):
            bank.add_card(1234, 'password')
    
    def test_add_account(self):
        bank = bk.Bank()
        bank.add_card(1234, 'password')

        with self.assertRaises(ValueError):
            bank.add_account(5678, 'password', 'Checking')
        with self.assertRaises(ValueError):
            bank.add_account(1234, 'pass', 'Checking')

    def test_balance_deposit_withdraw(self):
        bank = bk.Bank()
        bank.add_card(1234, 'password')
        bank.add_account(1234, 'password', 'Checking')
        
        with self.assertRaises(ValueError):
            bank.get_balance(5678, 'password', 'Saving')
        with self.assertRaises(ValueError):
            bank.deposit(5678, 'password', 'Checking', 100)
        with self.assertRaises(ValueError):
            bank.withdraw(1234, 'pass', 'Checking', 100)
            
        controller = ctrler.Controller(bank)
        self.assertTrue(controller.insert_card(1234))
        self.assertTrue(controller.enter_pin('password'))
        self.assertTrue(controller.select_account('Checking'))

        self.assertEqual(controller.get_balance(), 0)
        with self.assertRaises(ValueError):
            controller.deposit(-100)
        with self.assertRaises(TypeError):
            controller.deposit('100')
        controller.deposit(100)
        self.assertEqual(controller.get_balance(), 100)
        
        controller.withdraw(50)
        self.assertEqual(controller.get_balance(), 50)
        with self.assertRaises(ValueError):
            controller.withdraw(-100)
        with self.assertRaises(TypeError):
            controller.withdraw('100')
        with self.assertRaises(ValueError):
            controller.withdraw(60)

if __name__ == '__main__':
    unittest.main()
