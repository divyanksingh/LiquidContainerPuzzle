#!/usr/bin/env python3

import unittest
from solution import MainEntry

class TestProcessData(unittest.TestCase):
    
    def setUp(self):
        self.processor = MainEntry()

    '''
        Below are the Testcases for different input configurations
    '''
    def test_forPossibleFinalConf1(self):
        input_data = [
                        (8,5,3), 
                        (8,0,0), 
                        (4,4,0)
                    ]
    
        expected_path = [
                            (8, 0, 0), 
                            (3, 5, 0), 
                            (3, 2, 3), 
                            (6, 2, 0), 
                            (6, 0, 2), 
                            (1, 5, 2), 
                            (1, 4, 3), 
                            (4, 4, 0)
                        ]
        

        actual_output  =  self.processor.process_input(input_data[0],\
                input_data[1], input_data[2])
        self.assertEqual(actual_output, expected_path)


    def test_forPossibleFinalConf2(self):
        input_data = [
                        (10,5,2), 
                        (6,3,0), 
                        (5,4,0)
                    ]
    
        expected_path = [
                            (6, 3, 0), 
                            (4, 5, 0), 
                            (2, 5, 2), 
                            (7, 0, 2), 
                            (7, 2, 0), 
                            (5, 2, 2), 
                            (5, 4, 0)
                        ]

        actual_output  =  self.processor.process_input(input_data[0],\
                input_data[1], input_data[2])
        self.assertEqual(actual_output, expected_path)



    def test_forImpossibleFinalConf(self):
        input_data = [
                        (10,5,2), 
                        (6,3,0), 
                        (4,4,1)
                    ]
    
        expected_path = "Not possible"
        

        actual_output  =  self.processor.process_input(input_data[0],\
                input_data[1], input_data[2])
        self.assertEqual(actual_output, expected_path)


    def test_forInvalidInput1(self):
        
        input_data = [
                        (10,5,2),
                        (5,2),
                        (4,1,1)
                    ] 

        with self.assertRaises(ValueError):

            self.processor.process_input(input_data[0],\
                input_data[1], input_data[2])

    def test_forInvalidInput2(self):
        
        input_data = [
                        (10,5,2),
                        (5,4,3),
                        (6,4,2)
                    ] 

        with self.assertRaises(ValueError):

            self.processor.process_input(input_data[0],\
                input_data[1], input_data[2])

    def test_forInvalidInput3(self):
        
        input_data = [
                        (10,5,2),
                        (5,-4,1),
                        (1,1,0)
                    ] 

        with self.assertRaises(ValueError):

            self.processor.process_input(input_data[0],\
                input_data[1], input_data[2])


    def test_forInvalidInput4(self):
        
        input_data = [
                        (10,5,2),
                        (5,4,1),
                        (6,1,0)
                    ] 

        with self.assertRaises(ValueError):

            self.processor.process_input(input_data[0],\
                input_data[1], input_data[2])


if __name__=="__main__":
    unittest.main()
