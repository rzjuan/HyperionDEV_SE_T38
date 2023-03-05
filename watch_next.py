#  NLP library is imported
import spacy

#  English NLP model is loaded into the nlp variable 
nlp = spacy.load('en_core_web_md')

# Variables
movies_list = []
movies_list_full = []
file_name = "movies.txt"
seen_movie = ["""Will he save their world or destroy it? 
When the Hulk becomes too dangerous for the Earth, the Illuminati 
trick Hulk into a shuttle and launch him into space to a planet where 
the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar 
where he is sold into slavery and trained as a gladiator."""]

# External files is read to extract information
file = open(file_name, "r")
file_content = file.readlines()
file.close()

#  Lists are filled with movie's description and full details
for line in file_content:
    pre = line.strip("\n").split(" :")
    movies_list_full.append(pre)
    movies_list.append(pre[1])

#  Examine the like criteria against a list of movies and create a list of the probability of match
sim_list = []
for token in seen_movie:
    token = nlp(token)
    for token_ in movies_list:
        token_ = nlp(token_)
        sim_list.append(round((token.similarity(token_)),4))

#  Extraxt max similiraty/probability of like and conver to %
possible_favourite = round(max(sim_list)*100,2)

#  Depending on the most similar, find the movie title and description
movie_pos = 0
for simil in sim_list:
    if round(simil*100,2) == possible_favourite:
        movie = movies_list_full[movie_pos][0]
        movie_description = movies_list_full[movie_pos][1]
    else:
        movie_pos += 1

#  Print to user % of match and movie details
print("\n------------------------ Next Movie To Watch ------------------------")
print(f"\nThere is a {possible_favourite} % chance that {movie} should be your next movie, this is about:\n\n'{movie_description}'\n")