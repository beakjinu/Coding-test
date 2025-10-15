def pick_top_two(genre_dict):
    for genre in genre_dict:
        genre_dict[genre].sort(key=lambda x: (-x[0], x[1]))
        genre_dict[genre] = genre_dict[genre][:2]
    return genre_dict


def solution(genres, plays):
    genre_dict = {}
    total_play = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in genre_dict:
            genre_dict[genre] = []
            total_play[genre] = 0
        genre_dict[genre].append((play, i))
        total_play[genre] += play

    pick_top_two(genre_dict)

    genres_sequence = sorted(total_play, key=total_play.get, reverse=True)

    answer = []
    for genre in genres_sequence:
        for song in genre_dict[genre]:
            answer.append(song[1])

    return answer
