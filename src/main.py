#!/usr/bin/env python3
"""
IT Compass — объективная карта роста в IT через верифицируемые маркеры
Методология "Объективные маркеры компетенций"
© 2025 Ekaterina Kudelya. CC BY-ND 4.0
"""
import sys
import logging
from pathlib import Path

import sys
from pathlib import Path

# Add the project root to the path to allow imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from src.core.tracker import CareerTracker
    from src.utils.portfolio_gen import generate_portfolio
except ImportError as e:
    print(f"❌ Ошибка импорта модулей: {e}")
    print("Убедитесь, что вы находитесь в корневой директории проекта")
    sys.exit(1)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('it_compass.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

class ITCompassApp:
    def __init__(self):
        self.tracker = None
        self.running = True
    
    def initialize(self):
        try:
            self.tracker = CareerTracker()
            logger.info("IT Compass успешно инициализирован")
            return True
        except Exception as e:
            logger.error(f"Ошибка инициализации: {e}")
            print(f"❌ Ошибка при запуске приложения: {e}")
            return False
    
    def show_welcome(self):
        print("\n" + "="*50)
        print("🧭 IT Compass")
        print("Объективная карта твоего IT-роста")
        print("="*50)
        print("📊 Отслеживай прогресс • 🎯 Получай рекомендации")
        print("📄 Создавай портфолио • 🚀 Развивай карьеру")
        print("="*50)
        print("Методология: © 2025 Ekaterina Kudelya, CC BY-ND 4.0")
        print("Код: MIT License • Версия: 1.0.0")
        print("="*50)
    
    def show_menu(self):
        print("\n📋 ДОСТУПНЫЕ ДЕЙСТВИЯ:")
        print("1 — 📊 Показать прогресс")
        print("2 — ✅ Отметить выполненный маркер")
        print("3 — 🎯 Рекомендации по развитию")
        print("4 — 📄 Сгенерировать портфолио")
        print("5 — 📈 Статистика по навыкам")
        print("6 — ⚙️ Настройки и информация")
        print("7 — 🚪 Выход")
        print()
    
    def handle_choice(self, choice: str) -> bool:
        try:
            if choice == "1":
                self.show_progress()
            elif choice == "2":
                self.mark_completed()
            elif choice == "3":
                self.show_recommendations()
            elif choice == "4":
                self.generate_portfolio()
            elif choice == "5":
                self.show_statistics()
            elif choice == "6":
                self.show_settings()
            elif choice == "7":
                print("\n🎉 До новых встреч! Удачи в карьерном росте! 🚀")
                logger.info("Пользователь завершил работу")
                return False
            else:
                print("❌ Неверный выбор. Попробуйте снова.")
        except KeyboardInterrupt:
            print("\n\n👋 Прерывание пользователем. До свидания!")
            return False
        except Exception as e:
            logger.error(f"Ошибка при выполнении действия '{choice}': {e}")
            print(f"⚠️ Произошла ошибка: {e}")
            print("Попробуйте ещё раз или обратитесь к администратору")
            return True
    
    def show_progress(self):
        print("\n📊 ВАШ ПРОГРЕСС:")
        print("-" * 50)
        try:
            self.tracker.show_progress()
        except Exception as e:
            logger.error(f"Ошибка при отображении прогресса: {e}")
            print("❌ Не удалось загрузить прогресс.")
    
    def mark_completed(self):
        print("\n✅ ОТМЕТКА ВЫПОЛНЕННОГО МАРКЕРА")
        print("-" * 40)
        available_markers = self._get_available_markers()
        if not available_markers:
            print("❌ Нет доступных маркеров для отметки")
            return
        
        print("Доступные маркеры (первые 10):")
        for i, (marker_id, description) in enumerate(available_markers[:10], 1):
            print(f"{i:2d}. {marker_id}: {description}")
        
        if len(available_markers) > 10:
            print(f"... и ещё {len(available_markers) - 10} маркеров")
        
        print("\nВведите ID маркера (например: python_1_1)")
        print("Или нажмите Enter для отмены")
        marker_id = input("ID маркера: ").strip()
        
        if not marker_id:
            print("❌ Отмена операции")
            return
        
        success = self.tracker.mark_completed(marker_id)
        if success:
            self._show_motivation_message()
    
    def _get_available_markers(self) -> list:
        available = []
        completed = set(self.tracker.progress["completed_markers"])
        for skill_data in self.tracker.markers.values():
            for level_markers in skill_data.levels.values():
                for marker in level_markers:
                    if marker.id not in completed:
                        available.append((marker.id, marker.marker))
        return available
    
    def _show_motivation_message(self):
        import random
        messages = [
            "🎉 Отличная работа! Продолжайте в том же духе!",
            "💪 Каждый маркер приближает вас к цели!",
            "⭐ Вы на правильном пути к успеху!",
            "🚀 Отличный прогресс! Так держать!",
            "🏆 Ещё один шаг к карьерным высотам!",
            "🌟 Ваш рост впечатляет! Не останавливайтесь!"
        ]
        print(f"\n{random.choice(messages)}")
    
    def show_recommendations(self):
        try:
            self.tracker.show_recommendations()
        except Exception as e:
            logger.error(f"Ошибка при показе рекомендаций: {e}")
            print("❌ Не удалось загрузить рекомендации")
    
    def generate_portfolio(self):
        print("\n📄 ГЕНЕРАЦИЯ ПОРТФОЛИО")
        print("-" * 30)
        try:
            success = generate_portfolio()
            if success:
                print("✅ Портфолио успешно создано: docs/my_portfolio.md")
                print("💡 Используйте его для откликов на вакансии!")
            else:
                print("❌ Не удалось создать портфолио")
        except Exception as e:
            logger.error(f"Ошибка при генерации портфолио: {e}")
            print(f"❌ Ошибка: {e}")
    
    def show_statistics(self):
        print("\n📈 ДЕТАЛЬНАЯ СТАТИСТИКА")
        print("-" * 40)
        if not self.tracker.markers:
            print("❌ Нет данных о навыках")
            return
        
        total_completed = 0
        total_markers = 0
        
        for skill_name in sorted(self.tracker.markers.keys()):
            progress = self.tracker.get_skill_progress(skill_name)
            if progress:
                percentage = progress["percentage"]
                completed = progress["completed_count"]
                total = progress["total_count"]
                total_completed += completed
                total_markers += total
                
                print(f"\n{skill_name}:")
                print(f" Прогресс: {percentage:.1f}% ({completed}/{total})")
        
        if total_markers > 0:
            overall = (total_completed / total_markers) * 100
            print(f"\n📊 ОБЩАЯ СТАТИСТИКА:")
            print(f"Выполнено: {total_completed} из {total_markers} маркеров")
            print(f"Общий прогресс: {overall:.1f}%")
    
    def show_settings(self):
        print("\n⚙️ НАСТРОЙКИ И ИНФОРМАЦИЯ")
        print("-" * 35)
        print(f"📁 Директория маркеров: {self.tracker.markers_dir}")
        print(f"💾 Файл прогресса: {self.tracker.progress_file}")
        print(f"📊 Загружено навыков: {len(self.tracker.markers)}")
        
        completed = len(self.tracker.progress["completed_markers"])
        in_progress = len(self.tracker.progress["in_progress_markers"])
        print(f"✅ Выполнено маркеров: {completed}")
        print(f"🔄 В процессе: {in_progress}")
        
        print("\n📄 ЛИЦЕНЗИИ:")
        print("• Методология: © 2025 Ekaterina Kudelya, CC BY-ND 4.0")
        print("• Код: MIT License")
        print("• Версия: 1.0.0")
    
    def run(self):
        if not self.initialize():
            return
        
        self.show_welcome()
        
        while self.running:
            try:
                self.show_menu()
                choice = input("Выберите действие (1-7): ").strip()
                if not self.handle_choice(choice):
                    self.running = False
            except KeyboardInterrupt:
                print("\n\n👋 До свидания!")
                break
            except Exception as e:
                logger.error(f"Критическая ошибка в главном цикле: {e}")
                print(f"❌ Критическая ошибка: {e}")
                break

def main():
    try:
        app = ITCompassApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 До свидания!")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Критическая ошибка: {e}")
        print(f"❌ Критическая ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
