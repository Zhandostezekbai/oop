class Teacher:
    def __init__(self, name: str, subject: str):
        self.name = name
        self.subject = subject

    def conduct_lesson(self):
        print(f"Оқытушы {self.name} {self.subject} пәні бойынша сабақ өткізуде.")


class OnlineCourse:
    def __init__(self, course_name: str, teacher: Teacher):
        self.course_name = course_name
        self.teacher = teacher

    def conduct_lesson(self):
        print(f"'{self.course_name}' онлайн курсы басталуда.")
        self.teacher.conduct_lesson()


class Document:
    def __init__(self, title: str, page_count: int):
        self._title = title
        self.__page_count = page_count

    def get_page_count(self):
        return self.__page_count

    def display_info(self):
        print(f"Құжат атауы: {self._title}, Бет саны: {self.__page_count}")


class Report(Document):
    def prepare_document(self):
        time = self.get_page_count() * 5
        print(f"Report: Дайындалу уақыты = {time} минут.")
        return time

    def calculate_time(self):
        return self.prepare_document()


class Manual(Document):
    def prepare_document(self):
        time = self.get_page_count() / 2
        print(f"Manual: Дайындалу уақыты = {time} минут.")
        return time

    def calculate_time(self):
        return self.prepare_document()


class TechnicalDocument(Report, Manual):
    def __init__(self, title: str, page_count: int):
        super().__init__(title, page_count)

    def prepare_document(self):
        print("TechnicalDocument класындағы қайта анықталған prepare_document() әдісі:")
        report_time = super().prepare_document()
        return report_time


if __name__ == "__main__":
    print("--- 1-ТАПСЫРМА НӘТИЖЕСІ ---")
    teacher1 = Teacher("Айбек Қанатұлы", "Python бағдарламалау")
    course1 = OnlineCourse("Data Science негіздері", teacher1)
    course1.conduct_lesson()

    print("\n--- 2-ТАПСЫРМА НӘТИЖЕСІ ---")
    tech_doc = TechnicalDocument("Техникалық есеп", 20)
    tech_doc.display_info()
    tech_doc.prepare_document()