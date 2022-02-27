import pytest
import student 


def test_3(capsys):
    student.pyramid(3)
    out,err =  capsys.readouterr()
    assert out == "*\n**\n***" or out == "* \n* * \n* * *\n"

def test_1(capsys):
    student.pyramid(1)
    out,err =  capsys.readouterr()
    assert out == "*\n" or out == "*"

def test_5(capsys):
    student.pyramid(5)
    out,err =  capsys.readouterr()
    assert out == "*\n**\n***\n****\n******\n" or out == "* \n* * \n* * * \n* * * * \n* * * * * * \n"
