## test cases for question model.

from django.test import TestCase
from questionnaire.models import Question, Teacher, Student
from django.db import models 

# create your tests here.

class QuestionTestCase(TestCase):
    """ 
     unit test on question model
    """ 
    def setUp(self) -> None:
        Question.objects.create( 
            question_number=1,
            text= "Empty test", 
            multiple_choice =True, 
            custom_answer =False), 
        
        Question.objects.create( 
            question_number=2,
            text= "Empty text", 
            multiple_choice =False, 
            custom_answer =True), 
                                
        
    
    def test_Question(self)-> None: 
        """ unit test Question model field"""
        questTest = Question.objects.get(question_number=1)
        questTest2 = Question.objects.get(question_number=2)

        # happy case : equal 
        self.assertEqual(questTest.question_number, '1')
        self.assertEqual(questTest.text, 'Empty test')
        self.assertEqual(questTest.multiple_choice, True)
        self.assertEqual(questTest.custom_answer, False)

        # happy case : not-equal
        self.assertNotEqual(questTest.question_number, '2')
        self.assertNotEqual(questTest.text, 'Empty text')
        self.assertNotEqual(questTest.multiple_choice, False)
        self.assertNotEqual(questTest.custom_answer, True) 

        # happy case : comparing [ Question ] objects data fields.
        self.assertNotEqual(questTest.question_number, questTest2.question_number)
        self.assertNotEqual(questTest.text, questTest2.text)
        self.assertNotEqual(questTest.multiple_choice, questTest2.multiple_choice)
        self.assertNotEqual(questTest.custom_answer, questTest2.custom_answer)

        # happy case : verification of object instances. 
        self.assertEqual(type(questTest), Question)
        self.assertEqual(type(questTest2), Question) 
        #
        


        



