from django.test import TestCase 
from questionnaire.models import Answer, Question
from django.db import models 

class AnswerTestCase(TestCase): 
    """ 
     unit test on answer model
    """

    def setUp(self) -> None: 

        Question.objects.create(
            question_number=1, text= "cur_question", 
            multiple_choice =True, custom_answer =False
        ),  

        Question.objects.create( 
            question_number='a', text= "branch_question_A", 
            multiple_choice =True, custom_answer =False
        ), 

        Question.objects.create( 
            question_number='b', text= "branch_question_B", 
            multiple_choice =True, custom_answer =False
        ),


        Answer.objects.create(
            text="answer_text", 
            question = Question.objects.get(question_number=1),
            next_question =  Question.objects.get(question_number='b'), 
                            
                             
        )


    def test_Answer(self) -> None: 
        """ unit test Answer model field """

        answerTest = Answer.objects.get(text="answer_text")

        # happy case : equal 
        self.assertEqual(answerTest.text, 'answer_text')
        self.assertEqual(answerTest.question, Question.objects.get(question_number=1))
        self.assertEqual(answerTest.next_question, Question.objects.get(question_number='b') )

        

        # happy case : branching of-models

        # happy case : only unique values found.

        # happy case : instance validation. 
        self.assertIsInstance(answerTest.question, Question)
        self.assertIsInstance(answerTest.next_question, Question)
        self.assertIsInstance(answerTest, Answer)
        #


        


