class Book:
    def __init__(self, title: str, author: str, price: float):
        self._title = title
        self._author = author
        self._price = price

    # --- TITLE PROPERTY ---
    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        if not value.strip():
            raise ValueError("Title cannot be empty.")
        self._title = value

    # --- AUTHOR PROPERTY ---
    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str):
        if not value.strip():
            raise ValueError("Author cannot be empty.")
        self._author = value

    # --- PRICE PROPERTY ---
    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    def get_description(self) -> str:
        """Returns basic information about the book."""
        return f"'{self.title}' by {self.author} (${self.price:.2f})"


class Novel(Book):
    def __init__(self, title: str, author: str, price: float, genre: str, pages: int):
        # Passes common fields to the parent Book constructor
        super().__init__(title, author, price)
        self._genre = genre
        self._pages = pages

    @property
    def genre(self) -> str:
        return self._genre

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if value <= 0:
            raise ValueError("Pages must be greater than zero.")
        self._pages = value

    # Overriding method to add specific Novel details
    def get_description(self) -> str:
        return f"[Novel] {super().get_description()} | Genre: {self.genre} ({self.pages} pages)"


class Comic(Book):
    def __init__(self, title: str, author: str, price: float, illustrator: str, issue_number: int):
        # Passes common fields to the parent Book constructor
        super().__init__(title, author, price)
        self._illustrator = illustrator
        self._issue_number = issue_number

    @property
    def illustrator(self) -> str:
        return self._illustrator

    @property
    def issue_number(self) -> int:
        return self._issue_number

    # Overriding method to add specific Comic details
    def get_description(self) -> str:
        return f"[Comic] {super().get_description()} | Issue #{self.issue_number} | Illustrated by: {self.illustrator}"


# ==========================================
# EXECUTION / TESTING
# ==========================================
if __name__ == "__main__":
    # 1. Instantiating Objects
    dune = Novel(title="Dune", author="Frank Herbert", price=14.99, genre="Sci-Fi", pages=617)
    spiderman = Comic(title="The Amazing Spider-Man", author="Stan Lee", price=3.99, illustrator="Steve Ditko", issue_number=1)

    # 2. Printing Descriptions
    print(dune.get_description())
    print(spiderman.get_description())

    # 3. Utilizing Setters and updating attributes
    print("\n--- Applying Discounts & Updates ---")
    dune.price = 11.99          # Using parent setter
    spiderman.price = 2.99      # Using parent setter
    
    print(dune.get_description())
    print(spiderman.get_description())
