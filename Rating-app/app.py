class Rating:
    # def __init__(self):
    #     fivestar,fourstar,threestar,twostar,onestar= 0 # type: ignore

    def calculateRating(self):   
        self.fivestar = 3
        self.fourstar = 4
        self.threestar = 1
        self.twostar = 0
        self.onestar = 0

        Total_Rating = (5*self.fivestar + 4*self.fourstar + 3*self.threestar + 2*self.twostar + 1*self.onestar ) / (self.fivestar+self.fourstar+self.threestar+self.twostar+self.onestar)
        print((5*self.fivestar + 4*self.fourstar + 3*self.threestar + 2*self.twostar + 1*self.onestar ))
        print((self.fivestar+self.fourstar+self.threestar+self.twostar+self.onestar))
        print(f"The Total rating you get {Total_Rating} out of 5")
    @staticmethod
    def rating_ranks():
        ratings = []
        total_rates = 0
        for star in range(1, 6):
            one_rate = int(input(f"Enter number of {star} ratings: "))
            local_rate = one_rate * int(star)
            total_rates += int(one_rate)
            ratings.append(local_rate)
        print(sum(ratings))
        print(total_rates)
        print(sum(ratings)/total_rates)

        
# Sum of (weight * number of at that weight) / total number of
# (5*252 + 4*124 + 3*40 + 2*29 + 1*33) / 478 = 4.1

# rating1 = Rating()
# rating1.calculateRating()
# rating1.rating_ranks()

list_rating = [[int(input(f"Enter number of {rateing} ratings: ")) , rateing] for rateing in range(1, 6)]
# print(((list_rating[0][0]*list_rating[0][1])+(list_rating[1][0]*list_rating[1][1])+(list_rating[2][0]*list_rating[2][1])+(list_rating[3][0]*list_rating[3][1])+(list_rating[4][0]*list_rating[4][1]))/(list_rating[0][0]+list_rating[1][0]+list_rating[2][0]+list_rating[3][0]+list_rating[4][0]))
total, sumlist = 0, []
for lst in list_rating:
    total += lst[0]
    sumlist.append(lst[0]*lst[1])

print(sum(sumlist)/total)