from django.test import TestCase
from questionnaire.models import Teacher
from questionnaire.models import *

from django.db import models 



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
    
        Teacher.objects.create( 
            first_name="string value_2",
            last_name="string value_2",
            school="school_name_2" 
        ), 
    
        # objects for boundary testing
        Teacher.objects.create( 
            first_name="",
            last_name="",
            school=""
        ), 
    
        Teacher.objects.create( 
            first_name="\n",
            last_name="\n",
            school="\n"
        ), 
    
    def test_Teacher(self) -> None: 

        """ unit test Teacher model field """
        teacherTest = Teacher.objects.get(first_name="string value")
        teacherTest2 = Teacher.objects.get(first_name="string value_2")

        # happy case : equal 
        self.assertEqual(teacherTest.first_name, 'string value')
        self.assertEqual(teacherTest.last_name , 'string value')
        self.assertEqual(teacherTest.school, "school_name")
        

        # happy case : not-equal
        self.assertNotEqual(teacherTest.first_name, '2')
        self.assertNotEqual(teacherTest.last_name, 'Empty text')
        self.assertNotEqual(teacherTest.school, 'Empty text')
        

        # happy case : test two [ Teacher ] data fields
        self.assertNotEqual(teacherTest.first_name, teacherTest2.first_name)
        self.assertNotEqual(teacherTest.last_name, teacherTest2.last_name)
        self.assertNotEqual(teacherTest.school, teacherTest2.school)

        # happy case : type checking of instance of object fields. 
        self.assertEqual ( type(teacherTest), Teacher)
        self.assertEqual ( type(teacherTest2), Teacher)
        self.assertNotEqual ( type(teacherTest), Student )
        self.assertNotEqual ( type(teacherTest2), Student )

        


    def test_TeacherBoundary(self) -> None: 

        """ boundary testing of Teacher model """
        teacherTestA = Teacher.objects.get(first_name="")
        teacherTestB = Teacher.objects.get(first_name="\n")

        # case : boundary test on empty string
        self.assertTrue(teacherTestA.first_name == "")
        self.assertTrue(teacherTestA.last_name == "" )
        self.assertTrue(teacherTestA.school == "")

        # case : boundary test on new line. 
        self.assertTrue( teacherTestB.first_name == "\n")
        self.assertTrue( teacherTestB.last_name == "\n")
        self.assertTrue( teacherTestB.school == "\n")

        # get more requirements on string stuff.
        #









