import media
import fresh_tomatoes

#Creating the instance of the Movie class
the_hurt_locker = media.Movie("The Hurt Locker",
                                "When SFC William James joins Bravo Company in Iraq, they have a month or so left in their tour of duty. He's a bomb disposal expert sent to replace Sgt. Matt Thompson, a long-standing member of the team recently killed while disposing of an improvised explosive device. To say that James loves what he does doesn't quite capture the emotional high he experiences when he gets to do what he does best. His fellow squad members (Sgt. JT Sanborn and Spc. Owen Eldridge) just want to survive the few days of duty they have left, but James' risk-taking drives them all to the edge. - Written by garykmcd / edited by statmanjeff (imdb.com)",
                                "War", "Jeremy Renner", "Kathryn Bigelow", "2008",
                                "https://upload.wikimedia.org/wikipedia/en/6/6c/HLposterUSA2.jpg",
                                "https://www.youtube.com/watch?v=2GxSDZc8etg")

the_great_gatsby = media.Movie("The Great Gatsby",
                                "An adaptation of F. Scott Fitzgerald's Long Island-set novel, where Midwesterner Nick Carraway is lured into the lavish world of his neighbor, Jay Gatsby. Soon enough, however, Carraway will see through the cracks of Gatsby's nouveau riche existence, where obsession, madness, and tragedy await. - Written by Anonymous (imdb.com)",
                                "Drama", "Leonaro DiCaprio", "Baz Luhrmann", "2013",
                                "https://upload.wikimedia.org/wikipedia/en/2/26/TheGreatGatsby2012Poster.jpg",
                                "https://www.youtube.com/watch?v=TaBVLhcHcc0" )

life_is_beautiful = media.Movie("Life is Beautiful",
                                "In 1930s Italy, a carefree Jewish book keeper named Guido starts a fairy tale life by courting and marrying a lovely woman from a nearby city. Guido and his wife have a son and live happily together until the occupation of Italy by German forces. In an attempt to hold his family together and help his son survive the horrors of a Jewish Concentration Camp, Guido imagines that the Holocaust is a game and that the grand prize for winning is a tank. - Written by Anthony Hughes (imbd.com)",
                                "Dramatic", "Roberto Benigni", "Roberto Benigni", "1997",
                                "https://upload.wikimedia.org/wikipedia/en/7/7c/Vitaebella.jpg",
                                "https://www.youtube.com/watch?v=pAYEQP8gx3w" )

#Creating a list containing the instances of the Movie just created
movies = [the_hurt_locker, the_great_gatsby, life_is_beautiful]

#calling the open_movies_page to create the page with the Movies
fresh_tomatoes.open_movies_page(movies, media.Movie.TOTAL_INSTANCES)
