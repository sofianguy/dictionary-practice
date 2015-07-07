file_name = "scores.txt"

open_file = open(file_name)

def alpha_order_rest_rate(open_file):
    rest_rate_dict = {}
    for line in open_file:
        restaurant, rating = line.split(":")
        #add restaurant and rating to dictionary

    
        print restaurant + " is rated at " + rating



alpha_order_rest_rate(open_file)

 # if restaurant, rating not in rest_rate_dict:
        #     rest_rate_dict += restaurant
        # if rating not in rest_rate_dict:
        #     rest_rate_dict += rating


        #need .items()