import pytest
import uuid
from datetime import datetime

from api.domain.task.task_entity import Task



class TestTask:
    def test_title_string(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        task = Task("teste","testando a entidade", True, uuid.uuid4().hex, date_s)
        assert task.title == "teste"
        
    def test_title_empty(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        task = Task("","testando a entidade", True, uuid.uuid4().hex, date_s)
        with pytest.raises(ValueError, match=r"Title is required"):
            task.title
                   
    def test_title_blank(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        task = Task("   ","testando a entidade", True, uuid.uuid4().hex, date_s)
        with pytest.raises(ValueError, match=r"Title is required"):
            task.title
        
    def test_description_string(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        task = Task("teste","testando a entidade", True, uuid.uuid4().hex, date_s)
        assert task.description == "testando a entidade"   
    
    def test_description_empty(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        task = Task("teste","", True, uuid.uuid4().hex, date_s)
        with pytest.raises(ValueError, match=r"Description is required"):
            task.description
    
    def test_description_blank(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        task = Task("teste","   ", True, uuid.uuid4().hex, date_s)
        with pytest.raises(ValueError, match=r"Description is required"):
            task.description
    
    def test_listId_uuid(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        listId = uuid.uuid4().hex
        task = Task("teste","testando a entidade", True, listId, date_s)
        assert task.listId == listId
    
    def test_listId_empty(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        task = Task("teste","testando a entidade", True, "", date_s)
        with pytest.raises(ValueError, match=r"List id is required"):
            task.listId
        
    def test_listId_blank(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        task = Task("teste","testando a entidade", True, "  ", date_s)
        with pytest.raises(ValueError, match=r"List id is required"):
            task.listId
            
    def test_data_string(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        listId = uuid.uuid4().hex
        task = Task("teste","testando a entidade", True, listId, date_s)
        assert task.timeSelect == date_s

    def test_data_empty(self):
        listId = uuid.uuid4().hex
        task = Task("teste","testando a entidade", True, listId, "")
        with pytest.raises(ValueError, match=r"Data is required"):
            task.timeSelect
            
    def test_data_blank(self):
        listId = uuid.uuid4().hex
        task = Task("teste","testando a entidade", True, listId, "  ")
        with pytest.raises(ValueError, match=r"Data is required"):
            task.timeSelect
            