import json
import random
import os
import webbrowser
from datetime import datetime

class MentalSupportSystem:
    def __init__(self):
        self.resources_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'support', 'resources')
        self.quotes_file = os.path.join(self.resources_path, 'motivational_quotes.json')
        self.contacts_file = os.path.join(self.resources_path, 'crisis_contacts.json')
        
    def show_main_menu(self):
        """Основное меню психологической поддержки"""
        print("\n" + "="*50)
        print("🧠 IT COMPASS: ПСИХОЛОГИЧЕСКАЯ ПОДДЕРЖКА")
        print("="*50)
        print("1. 💬 Случайная мотивационная цитата")
        print("2. 🆘 Кризисные номера помощи")
        print("3. 🧘 Режим 'низкой энергии'")
        print("4. 👥 Руководство сообщества")
        print("5. 🏠 Вернуться в главное меню")
        print("="*50)
        
        choice = input("\nВыберите опцию (1-5): ")
        return choice
    
    def show_motivational_quote(self):
        """Показать случайную мотивационную цитату"""
        try:
            with open(self.quotes_file, 'r', encoding='utf-8') as f:
                quotes = json.load(f)
            
            quote = random.choice(quotes)
            print(f"\n🌟 {quote['quote']}")
            print(f"   — {quote['author']}")
            
            if quote['action']:
                print(f"\n💡 Действие: {quote['action']}")
                
        except Exception as e:
            print(f"❌ Ошибка загрузки цитат: {e}")
            print("💡 Попробуйте поработать над одним маленьким шагом сегодня")
    
    def show_crisis_contacts(self):
        """Показать кризисные номера помощи"""
        try:
            with open(self.contacts_file, 'r', encoding='utf-8') as f:
                contacts = json.load(f)
            
            print("\n" + "="*50)
            print("🆘 ЭКСТРЕННЫЕ КОНТАКТЫ ПОМОЩИ")
            print("="*50)
            
            for contact in contacts:
                print(f"\n📍 {contact['name']}")
                print(f"📞 {contact['phone']}")
                print(f"🌐 {contact['website']}")
                print(f"ℹ️ {contact['description']}")
            
            print("\n" + "="*50)
            print("❗ Если вы или кто-то рядом с вами в опасности - немедленно обратитесь за помощью")
            print("="*50)
            
        except Exception as e:
            print(f"❌ Ошибка загрузки контактов: {e}")
            print("\n🆘 Срочные номера для России:")
            print("   📞 112 - единая служба спасения")
            print("   📞 8-800-333-44-34 - доверенная служба для детей и подростков")
            print("   📞 8-800-2000-122 - детский телефон доверия")
    
    def activate_low_energy_mode(self):
        """Активировать режим 'низкой энергии'"""
        print("\n" + "="*50)
        print("😴 АКТИВИРОВАН РЕЖИМ 'НИЗКОЙ ЭНЕРГИИ'")
        print("="*50)
        print("В этом режиме доступны только базовые функции:")
        print("✅ Просмотр прогресса")
        print("✅ Простые упражнения")
        print("✅ Мотивационные цитаты")
        print("🚫 Сложные задачи")
        print("🚫 Анализ компетенций")
        print("🚫 Настройки")
        print("\n💡 Совет: Включите этот режим, когда чувствуете усталость или выгорание.")
        print("Сосредоточьтесь на маленьких победах и восстановлении ресурсов.")
        print("="*50)
        
        input("\nНажмите Enter, чтобы продолжить...")
    
    def show_community_guide(self):
        """Показать руководство сообщества"""
        guide_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'support', 'community_guide.md')
        
        try:
            with open(guide_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            print("\n" + "="*50)
            print("👥 РУКОВОДСТВО СООБЩЕСТВА IT COMPASS")
            print("="*50)
            print(content)
            print("="*50)
            
        except Exception as e:
            print(f"❌ Ошибка загрузки руководства: {e}")
            print("\n💡 Основные принципы поддержки:")
            print("1. Слушайте без осуждения")
            print("2. Предлагайте помощь, но не навязывайте")
            print("3. Уважайте границы других людей")
            print("4. Делитесь ресурсами, а не давайте советы")
    
    def run(self):
        """Запустить систему психологической поддержки"""
        while True:
            choice = self.show_main_menu()
            
            if choice == '1':
                self.show_motivational_quote()
                input("\nНажмите Enter, чтобы продолжить...")
                
            elif choice == '2':
                self.show_crisis_contacts()
                input("\nНажмите Enter, чтобы продолжить...")
                
            elif choice == '3':
                self.activate_low_energy_mode()
                
            elif choice == '4':
                self.show_community_guide()
                input("\nНажмите Enter, чтобы продолжить...")
                
            elif choice == '5':
                break
                
            else:
                print("❌ Неверный выбор. Пожалуйста, выберите опцию от 1 до 5.")
                input("\nНажмите Enter, чтобы продолжить...")

# Функции для интеграции в основной интерфейс
def show_random_quote_on_startup():
    """Показать случайную цитату при запуске"""
    try:
        resources_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'support', 'resources')
        quotes_file = os.path.join(resources_path, 'motivational_quotes.json')
        
        with open(quotes_file, 'r', encoding='utf-8') as f:
            quotes = json.load(f)
        
        quote = random.choice(quotes)
        print(f"\n{'='*60}")
        print(f"🌟 {quote['quote']}")
        print(f"   — {quote['author']}")
        print(f"{'='*60}")
        
    except Exception as e:
        pass  # Не показываем ошибку, чтобы не испортить пользовательский опыт

def show_daily_motivation():
    """Показать ежедневную мотивацию"""
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    
    # Хэш-функция для определения цитаты на день
    day_hash = sum(ord(c) for c in today) % 100
    
    try:
        resources_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'support', 'resources')
        quotes_file = os.path.join(resources_path, 'motivational_quotes.json')
        
        with open(quotes_file, 'r', encoding='utf-8') as f:
            quotes = json.load(f)
        
        # Выбираем цитату, основанную на дате
        quote = quotes[day_hash % len(quotes)]
        print(f"\n{'='*60}")
        print(f"🌞 УТРЕННЯЯ МОТИВАЦИЯ НА {now.strftime('%d.%m.%Y')}")
        print(f"{'='*60}")
        print(f"💡 {quote['quote']}")
        print(f"   — {quote['author']}")
        print(f"\n🎯 {quote['action']}")
        print(f"{'='*60}")
        
    except Exception as e:
        print(f"\n💡 Не забывай делать маленькие шаги каждый день. Они ведут к большим результатам.")

def get_crisis_contacts():
    """Получить контакты кризисной помощи"""
    try:
        resources_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'support', 'resources')
        contacts_file = os.path.join(resources_path, 'crisis_contacts.json')
        
        with open(contacts_file, 'r', encoding='utf-8') as f:
            contacts = json.load(f)
        
        return contacts
    except Exception as e:
        return []

# Интеграция с API психологических сервисов
def integrate_crisis_api():
    """Интеграция с API сервисов психологической помощи"""
    print("\n" + "="*50)
    print("🌐 ПОДКЛЮЧЕНИЕ К СЕРВИСАМ ПОДДЕРЖКИ")
    print("="*50)
    
    services = [
        {
            "name": "Психологи России",
            "api_url": "https://api.psyhelp.ru/v1/find",
            "description": "Поиск психологов по вашему городу с возможностью онлайн-консультации"
        },
        {
            "name": "Mindful",
            "api_url": "https://mindful.ru/api/meditation",
            "description": "Гиды по медитации и осознанности для снятия стресса"
        },
        {
            "name": "Психологическая помощь",
            "api_url": "https://psyhelp.ru/api/hotline",
            "description": "Список горячих линий психологической помощи"
        }
    ]
    
    print("Доступные сервисы:")
    for i, service in enumerate(services, 1):
        print(f"\n{i}. {service['name']}")
        print(f"   🌐 {service['api_url']}")
        print(f"   ℹ️ {service['description']}")
    
    print("\n" + "="*50)
    print("💡 Совет: Для интеграции с этими сервисами можно использовать модуль requests.")
    print("Создайте отдельный файл `api_integration.py` с функциями для каждого сервиса.")
    print("="*50)
    
    input("\nНажмите Enter, чтобы продолжить...")

if __name__ == "__main__":
    # Пример запуска системы поддержки
    support_system = MentalSupportSystem()
    support_system.run()