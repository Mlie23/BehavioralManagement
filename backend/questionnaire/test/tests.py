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
                                
        
    
    def test_Question(self)-> None: 
        """ unit test Question model field"""
        questTest = Question.objects.get(question_number=1)

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

        # happy case : assert false
        # self.assertFalse(questTest.question_number, 1)
        # self.assertFalse(questTest.text, 'Empty text')
        # self.assertFalse(questTest.multiple_choice, False)
        # self.assertFalse(questTest.custom_answer, True)




class TeacherTestCase(TestCase): 
    """
     unit test on teacher model
    """

    def setUp(self) -> None:
        Teacher.objects.create( 
            first_name="string value",
            last_name="string value",
            school="school_name"
        ), 
    


    def test_Teacher(self) -> None: 

        """ unit test Teacher model field """
        teacherTest = Teacher.objects.get(first_name="string value")

        # happy case : equal 
        self.assertEqual(teacherTest.first_name, 'string value')
        self.assertEqual(teacherTest.last_name , 'string value')
        self.assertEqual(teacherTest.school, "school_name")
        

        # happy case : not-equal
        self.assertNotEqual(teacherTest.first_name, '2')
        self.assertNotEqual(teacherTest.last_name, 'Empty text')
        self.assertNotEqual(teacherTest.school, 'Empty text')
        

        # happy case : assert false
        # self.assertFalse(questTest.question_number, 1)
        # self.assertFalse(questTest.text, 'Empty text')
        # self.assertFalse(questTest.multiple_choice, False)
        # self.assertFalse(questTest.custom_answer, True)


class StudentTestCase(TestCase): 
    """
     unit test on teacher model
    """

    def setUp(self) -> None:
        Student.objects.create( 
            first_name="string value",
            last_name="string value",
            gender="Female", 
            IEP=True,
            grade="5"
        ), 
    


    def test_Student(self) -> None: 

        """ unit test Teacher model field """
        studentTest = Student.objects.get(first_name="string value")

        # happy case : equal 
        self.assertEqual(studentTest.first_name, 'string value')
        self.assertEqual(studentTest.last_name , 'string value')
        self.assertEqual(studentTest.gender, "Female")
        self.assertEqual(studentTest.grade, "5")
        self.assertEqual(studentTest.IEP, True)
        

        # happy case : not-equal
        self.assertNotEqual(studentTest.first_name, 'string')
        self.assertNotEqual(studentTest.last_name , 'string')
        self.assertNotEqual(studentTest.gender, "Male")
        self.assertNotEqual(studentTest.grade, "4")
        self.assertNotEqual(studentTest.IEP, False)
        

        # happy case : assert false
        # self.assertFalse(questTest.question_number, 1)
        # self.assertFalse(questTest.text, 'Empty text')
        # self.assertFalse(questTest.multiple_choice, False)
        # self.assertFalse(questTest.custom_answer, True)
