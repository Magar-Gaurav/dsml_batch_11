class Exception:
    def rating_error(self):
        raise ValueError("Invalid Ratings!!!\nRatings must be between 1 and 5.")
    def ride_distance(self):
        raise ValueError("Invalid distance!!!\nDistance cannot be negative.")
    def file_error(self):
        raise FileNotFoundError("Invalid File Name!!!.\nNo such file found.")
    def type_error(self):
        raise ValueError("Please enter a valid option!!!")