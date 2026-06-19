from exceptions import Exception

ex = Exception()
class Decorators:
    def __init__(self,v_ratings):
        self.v_ratings = v_ratings
    @property
    def success_book(self):
        return "Successfully booked a ride."
    @property
    def ride_logger(self):
        self.success_book
        if 1 <= self.v_ratings <= 5:
            return self.v_ratings
        else:
            ex.rating_error()
