import requests
import json
from datetime import datetime

class CrisisAPIService:
    """Класс для интеграции с API сервисов психологической помощи"""
    
    def __init__(self):
        self.services = {
            "psyhelp_hotline": {
                "name": "Психологическая помощь",
                "api_url": "https://api.psyhelp.ru/v1/hotlines",
                "method": "GET"
            },
            "mindful_meditations": {
                "name": "Mindful",
                "api_url": "https://mindful.ru/api/meditations",
                "method": "GET"
            },
            "psyhelp_find": {
                "name": "Психологи России",
                "api_url": "https://api.psyhelp.ru/v1/find",
                "method": "POST",
                "headers": {"Content-Type": "application/json"}
            }
        }
    
    def get_hotlines(self):
        """Получить список горячих линий психологической помощи"""
        try:
            response = requests.get(self.services["psyhelp_hotline"]["api_url"], timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Ошибка API: {response.status_code}"}
        except Exception as e:
            return {"error": str(e)}
    
    def get_meditations(self):
        """Получить список медитаций для снятия стресса"""
        try:
            response = requests.get(self.services["mindful_meditations"]["api_url"], timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Ошибка API: {response.status_code}"}
        except Exception as e:
            return {"error": str(e)}
    
    def find_psychologists(self, city=None, specialization=None):
        """Найти психологов по городу и специализации"""
        try:
            payload = {}
            if city:
                payload["city"] = city
            if specialization:
                payload["specialization"] = specialization
            
            response = requests.post(
                self.services["psyhelp_find"]["api_url"],
                json=payload,
                headers=self.services["psyhelp_find"]["headers"],
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Ошибка API: {response.status_code}"}
        except Exception as e:
            return {"error": str(e)}
    
    def show_available_services(self):
        """Показать доступные сервисы"""
        print("\n" + "="*50)
        print("🌐 ДОСТУПНЫЕ СЕРВИСЫ ПОДДЕРЖКИ")
        print("="*50)
        
        for key, service in self.services.items():
            print(f"\n🔹 {service['name']}")
            print(f"   URL: {service['api_url']}")
            print(f"   Метод: {service['method']}")
        
        print("\n" + "="*50)
        print("💡 Как использовать: Выберите сервис и вызовите соответствующий метод")
        print("   Например: service.get_hotlines() для получения горячих линий")
        print("="*50)
        
        input("\nНажмите Enter, чтобы продолжить...")

# Пример использования
if __name__ == "__main__":
    service = CrisisAPIService()
    service.show_available_services()