import requests
import pytest

BASE_URL = "http://127.0.0.1:5000/tasks"

def setup_module(module):
    """Limpa todas as tarefas antes de executar os testes"""
    requests.delete(f"{BASE_URL}/clear")

def test_create_task():
    """Testa a criação de uma nova tarefa"""
    new_task = {
        "title": "Tarefa de teste",
        "description": "Descrição da tarefa de teste"
    }
    
    response = requests.post(BASE_URL, json=new_task)
    assert response.status_code == 201
    data = response.json()
    
    assert "message" in data
    assert "task" in data
    assert data["task"]["title"] == new_task["title"]
    assert data["task"]["description"] == new_task["description"]
    assert data["task"]["completed"] == False

def test_get_all_tasks():
    """Testa a listagem de todas as tarefas"""
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    data = response.json()
    
    assert "tasks" in data
    assert isinstance(data["tasks"], list)
    assert len(data["tasks"]) > 0

def test_get_single_task():
    """Testa a obtenção de uma tarefa específica"""
    new_task = {
        "title": "Tarefa para buscar",
        "description": "Descrição da tarefa para buscar"
    }
    create_response = requests.post(BASE_URL, json=new_task)
    task_id = create_response.json()["task"]["id"]
    
    response = requests.get(f"{BASE_URL}/{task_id}")
    assert response.status_code == 200
    data = response.json()
    
    assert data["id"] == task_id
    assert data["title"] == new_task["title"]
    assert data["description"] == new_task["description"]

def test_delete_task():
    """Testa a exclusão de uma tarefa"""
    new_task = {
        "title": "Tarefa para deletar",
        "description": "Descrição da tarefa para deletar"
    }
    create_response = requests.post(BASE_URL, json=new_task)
    task_id = create_response.json()["task"]["id"]
    
    delete_response = requests.delete(f"{BASE_URL}/{task_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Task deleted successfully"
    
    get_response = requests.get(f"{BASE_URL}/{task_id}")
    assert get_response.status_code == 404

def test_get_nonexistent_task():
    """Testa a busca por uma tarefa que não existe"""
    response = requests.get(f"{BASE_URL}/9999")
    assert response.status_code == 404
    assert "error" in response.json()

def test_update_nonexistent_task():
    """Testa a atualização de uma tarefa que não existe"""
    response = requests.put(f"{BASE_URL}/9999", json={"title": "Título atualizado"})
    assert response.status_code == 404
    assert "error" in response.json()

def test_delete_nonexistent_task():
    """Testa a exclusão de uma tarefa que não existe"""
    response = requests.delete(f"{BASE_URL}/9999")
    assert response.status_code == 404
    assert "error" in response.json()

def test_create_task_with_missing_fields():
    """Testa a criação de tarefa com campos faltantes"""
    response = requests.post(BASE_URL, json={"description": "Descrição sem título"})
    assert response.status_code == 400
    assert "error" in response.json()
    
    response = requests.post(BASE_URL, json={"title": "Título sem descrição"})
    assert response.status_code == 400
    assert "error" in response.json()