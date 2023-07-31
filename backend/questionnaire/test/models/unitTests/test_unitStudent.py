from django.test import TestCase
from questionnaire.models import *
from django.db import models 

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
        Student.objects.create( 
            first_name="string value_2",
            last_name="string value_2",
            gender="Male", 
            IEP=False,
            grade="4"
        ),  

        # objects on boundary testing
        Student.objects.create( 
            first_name="",
            last_name="",
            gender="", # why dont you guys make that an enum.
            IEP=False,
            grade="" # this one should be an enum of typed grade. Will make testing better.
        ), 
        Student.objects.create( 
            first_name="\n",
            last_name="\n",
            gender="\n", # why dont you guys make that an enum.
            IEP=False,
            grade="\n" # this one should be an enum of typed grade. Will make testing better.
        ),
        

    
    
    def test_Student(self) -> None: 

        """ unit test Student model field """
        studentTestA = Student.objects.get(first_name="string value")
        studentTestB = Student.objects.get(first_name="string value_2")


        # happy case : equal 
        self.assertEqual(studentTestA.first_name, 'string value')
        self.assertEqual(studentTestA.last_name , 'string value')
        self.assertEqual(studentTestA.gender, "Female")
        self.assertEqual(studentTestA.grade, "5")
        self.assertEqual(studentTestA.IEP, True)
        

        # happy case : not-equal
        self.assertNotEqual(studentTestA.first_name, 'string')
        self.assertNotEqual(studentTestA.last_name , 'string')
        self.assertNotEqual(studentTestA.gender, "Male")
        self.assertNotEqual(studentTestA.grade, "4")
        self.assertNotEqual(studentTestA.IEP, False) 

        # boundary testing : 
        

        # happy case : comparing two [ Student ] data fields
        self.assertNotEqual(studentTestA.first_name, studentTestB.first_name)
        self.assertNotEqual(studentTestA.last_name, studentTestB.last_name)
        self.assertNotEqual(studentTestA.gender, studentTestB.gender)
        self.assertNotEqual(studentTestA.grade, studentTestB.grade)
        self.assertNotEqual(studentTestA.IEP, studentTestB.IEP) 

        # happy case : object instance verification
        self.assertEqual(type(studentTestA), Student)
        self.assertEqual(type(studentTestB), Student) 
        self.assertNotEqual( type(studentTestA), Teacher)
        self.assertNotEqual( type(studentTestB), Teacher)


    def test_StudentBoundary(self) -> None: 
         
        """ Boundary testing on Student model fields """
        studentTestA = Student.objects.get(first_name="")
        studentTestB = Student.objects.get(first_name="\n")

        self.assertEqual(studentTestA.first_name, "")
        self.assertEqual(studentTestA.last_name, "")
        self.assertEqual(studentTestA.gender, "")
        self.assertEqual(studentTestA.grade, "")
        self.assertEqual(studentTestA.IEP, False)

        self.assertEqual(studentTestB.first_name, "\n")
        self.assertEqual(studentTestB.last_name, "\n")
        self.assertEqual(studentTestB.gender, "\n")
        self.assertEqual(studentTestB.grade, "\n")
        self.assertEqual(studentTestB.IEP, False)
        #


        
        
        

        
        
