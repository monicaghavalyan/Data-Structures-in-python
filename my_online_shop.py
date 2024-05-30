from abc import ABC, abstractmethod
import my_collections as cl
from enum import Enum


class ProductType(Enum):
    AudioBook = 1
    PaperBook = 2
    Computer = 3
    Airpods = 4

class Product(ABC):
    def __init__(self, id, price, rating: float):
        self._id = id
        self._price = price
        self._rating = rating
        self._reviews = []   
        
    @abstractmethod
    def display(self):
        pass
    
    def rating_product(self, rating):
        self._rating = rating
        
    def get_rating(self):
        return self._rating
    
    def __lt__(self, other):
        return self._price < other._price
    
    def __le__(self, other):
        return self._price <= other._price
   
    def __ne__(self, other):
        return self._price != other._price
    
    def __gt__(self, other):
        return self._price > other._price
    
    def __ge__(self, other):
        return self._price >= other._price

      
class Book(Product):
    def __init__(self, id, price, rating, title, author):
        super().__init__(id, price, rating)
        self._title = title
        self._author = author
        
    def get_title(self) -> str:
        return self._title
    
    def get_author(self) -> str:
        return self._author
    
    def add_review(self, new_review: str) -> None:
        self._reviews.append(new_review)
        
    def rating_product(self, rating):
        self._rating = rating

class AudioBook(Book):
    def __init__(self, id, price, rating, title, author, format, reader):
        super().__init__(id, price, rating, title, author)
        self._format = format
        self._reader = reader
     
    def display(self) -> None:
        print(f'This is the audiobook {self._title} written by {self._author} in {self._format} format.')

    def rating_product(self, rating):
        self._rating = rating
        
class PaperBook(Book):
    def __init__(self, id, price, rating, title, author, num_of_panges, cover_type):
        super().__init__(id, price, rating,  title, author)
        self.number_of_panges = num_of_panges
        self._cover_type = cover_type
        self._preowned = False
        
    def change_preowned_status(self) -> None:
        self._preowned = not self._preowned
        
    def display(self) -> None:
        print(f'This is the book {self._title} written by {self._author} with {self._cover_type} cover.')
    
    def rating_product(self, rating):
        self._rating = rating
        
class Device(Product):
    def __init__(self, id, price, rating, model, brand):
        super().__init__(id, price, rating)
        self._model = model
        self._brand = brand
 
    def get_model(self):
        return self._model
    
    def get_brand(self):
        return self._brand
    
    def add_review(self, new_review: str) -> None:
        self._reviews.append(new_review)

    def rating_product(self, rating):
        self._rating = rating     

class Computer(Device):
    def __init__(self, id, price, rating, model, brand, size_of_screen):
        super().__init__(id, price, rating, model, brand)
        self._size_of_screen = size_of_screen
    
    def display(self):
        print(f'This is a computer of model {self._model} from brand {self._brand} with {self._size_of_screen}sms size of screen.')
    
    def get_size_of_screen(self):
        return self._size_of_screen

    def rating_product(self, rating):
        self._rating = rating      

class Airpods(Device):
    def __init__(self, id, price, rating: float, model, brand, color):
        super().__init__(id, price, rating, model, brand)
        self._color = color
    
    def display(self):
        print(f'This are {self._color} airpods of model {self._model} from brand {self._brand}.')
    
    def rating_product(self, rating):
        self._rating = rating        

class User:
    def __init__(self, id, nickname, name, surname, birthday):
        self._id = id
        self._nickname = nickname
        self._name = name
        self._surname = surname
        self._favourites = []
        self._birthday = birthday
        self._shopping_card = [None] * 2
   
    def rate_product(self, product):
        if 'excellent'in product._reviews:
            product.rating_product(10)   
        elif 'good' in product._reviews:
            product.rating_product(8)   
        elif 'normal' in product._reviews:
            product.rating_product(6.5)  
        elif 'bad' in product._reviews:
            product.rating_product(3)
        else:
            product.rating_product(0)

    def add_favourite(self, product):
        self.add_favourite.append(product)
        
    def rate_seller(self, seller):
        if seller.get_trust_score() >= 8:
            seller.update_trust_score(9)
        else:
            seller.update_trust_score(5)

    def add_product_to_card(self, product):
        if product in self._shopping_card:
            return False
        if None in self._shopping_card:
            self._shopping_card[self._shopping_card.index(None)] = product
            return True
        else:
            new_shopping_list = [product] + self._shopping_card
            self._shopping_card = new_shopping_list
            return True
            
    def remove_product_from_card(self, product):
        if product not in self._shopping_card:
            return False
        self._shopping_card[self._shopping_card.index(product)] = None
        return True  
    
    def get_shopping_card(self):
        return self._shopping_card
    

class ISeller(ABC):  
    @abstractmethod
    def list_product(self, product):
        pass
    
    @abstractmethod
    def sell_product(self):
        pass
    
    @abstractmethod
    def deliver_product(self):
        pass
    
    @abstractmethod
    def unlist_product(self):
        pass
    
class Seller(User, ISeller):
    def __init__(self, id, nickname, name, surname, favourites, birthday, shopping_card, trust_score):
        super().__init__(id, nickname, name, surname, favourites, birthday, shopping_card)
        self._trust_score = trust_score
        
    def get_trust_score(self):
        return self._trust_score
        
    def update_trust_score(self, new_score):
        self._trust_score = (self._trust_score + new_score) / 2
       
    def list_product(self, product):
        print(f'This is product with id {product._id}.')
    
    def sell_product(self):
        print('I am selling product.')
    
    def deliver_product(self):
        print('We can deliver the product.')
    
    def unlist_product(self):
        print('The product is unlisted.')

class MyOnlineShop:
    def __init__(self, name, address):
        self._name = name
        self._address = address
        self._products = cl.ArrayList()
        self._users = cl.LinkedList()
        self._top10 = cl.ArrayDeque()
        self._min_queue = cl.MinPriorityQueue()
        
    def add_new_product(self, type, id, price, rating = None, reviews = None, title = None, author = None, format = None, 
                        reader = None, num_of_panges = None, cover_type = None, model = None, brand = None, 
                        size_of_screen = None, color = None):
        if type == ProductType.AudioBook:
            product = AudioBook(id, price, rating, title, author, format, reader)
        elif type == ProductType.PaperBook:
            product = PaperBook(id, price, rating, title, author, num_of_panges, cover_type)
        elif type == ProductType.Computer:
            product = Computer(id, price, rating, model, brand, size_of_screen)
        elif type == ProductType.Airpods:
            product = Airpods(id, price, rating, model, brand, color)
        else:
            print('There is no such type.')
            return
        self._products.add(product)
            
    def get_most_popular_products(self) -> list:
        popular_products = cl.ArrayList()
        for product in self._products:
            if product._rating >= 9:
                popular_products.add(product)
        return popular_products
    
    def get_trusted_sellers(self) -> list:
        trusted_sellers = cl.LinkedList()
        for seller in self._users:
            if seller._trust_score and seller._trust_score >= 9:
                trusted_sellers.add(seller)
        return trusted_sellers
    
    def add_product_to_top10(self, product):
        if not self._top10.add(product):
            self._top10.dequeue()
        self._top10.add(product)
        
    def remove_product_from_top10(self, product):
        self._top10.remove(product)
    
    def add_product_to_min_queue(self, product):
        self._min_queue.add(product)
        
    def remove_product_from_min_queue(self):
        product = self._min_queue.dequeue()
        if product:
            print('id:', product._id, 'price:', product._price)
    
    
    
    
    