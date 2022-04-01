import pytest
import student 


def test_3(capsys):
    student.pyramid(3,'oaks')
    out,err =  capsys.readouterr()
    assert out == "oaks\noaksoaks\noaksoaksoaks\n" or out == "oaks \noaks oaks \noaks oaks oaks \n"

def test_1(capsys):
    student.pyramid(1, 'magiscarps')
    out,err =  capsys.readouterr()
    assert out == "magiscarps\n" or out == "magiscarps \n" or out == 'magiscarps' or out == 'magiscarps '

def test_5(capsys):
    student.pyramid(5,'*')
    out,err =  capsys.readouterr()
    assert out == "*\n**\n***\n****\n*****\n" or out == "* \n* * \n* * * \n* * * * \n* * * * * \n"
