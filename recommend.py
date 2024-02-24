# # # recommend.py
# # import test

# # emotion = test.label

# # def recommend_activities(emotion):
# #     if emotion == 'Angry':
# #         return ["Take deep breaths", "Practice mindfulness", "Listen to calming music"]

# #     elif emotion == 'Happy':
# #         return ["Celebrate with friends", "Watch a comedy movie", "Listen to upbeat music"]

# #     elif emotion == 'Neutral':
# #         return ["Take a break", "Read a book", "Try a new hobby"]

# #     elif emotion == 'Sad':
# #         return ["Talk to a friend", "Watch an uplifting movie", "Listen to comforting music"]

# #     elif emotion == 'Surprise':
# #         return ["Embrace the unexpected", "Try something new", "Watch a thrilling movie"]

# #     else:
# #         return ["No specific recommendation for this emotion"]

# # # Get recommendations based on the predicted emotion
# # recommendations = recommend_activities(emotion)
# # print("Recommendations:")
# # for recommendation in recommendations:
# #     print("- " + recommendation)

# # recommend.py
# import test

# emotion = test.label

# def recommend_activities(emotion):
#     if emotion == 'Angry':
#         return ["Take deep breaths", "Practice mindfulness", "Listen to calming music"]

#     elif emotion == 'Happy':
#         return ["Celebrate with friends", "Watch a comedy movie", "Listen to upbeat music"]

#     elif emotion == 'Neutral':
#         return ["Take a break", "Read a book", "Try a new hobby"]

#     elif emotion == 'Sad':
#         return ["Talk to a friend", "Watch an uplifting movie", "Listen to comforting music"]

#     elif emotion == 'Surprise':
#         return ["Embrace the unexpected", "Try something new", "Watch a thrilling movie"]

#     else:
#         return ["No specific recommendation for this emotion"]

# # Get recommendations based on the predicted emotion
# recommendations = recommend_activities(emotion)

# # Generate HTML content
# html_content = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Emotion Recommendations</title>
# </head>
# <body>
#     <h1>Emotion Recommendations</h1>
#     <h2>Emotion: {}</h2>
#     <h3>Recommendations:</h3>
#     <ul>
#         {}
#     </ul>
# </body>
# </html>
# """.format(emotion, "\n".join("<li>{}</li>".format(rec) for rec in recommendations))

# # Save HTML content to a file
# with open("recommendations.html", "w") as html_file:
#     html_file.write(html_content)

# print("HTML file 'recommendations.html' created.")

# recommend.py

# import test

# emotion = test.label
# recommend.py

# import test

# emotion = test.label

# recommend.py

import test

emotion = test.label

def recommend_activities(emotion):
    recommendations_dict = {
        'Angry': {
            'Movies': ["Inside Out", "The Pursuit of Happiness", "A Beautiful Mind"],
            'Precautions': ["Practice deep breathing exercises", "Take a walk to cool off", "Engage in physical activity to release energy"],
            'Songs': ["Eye of the Tiger - by Survivor" , "Lose Yourself - by Eminem", "Breaking the Habit  - by Linkin Park"],
            'Comics': ["Sad Sack", "Persepolis", "Blankets - by Craig Thompson"],
        },
        'Happy': {
            'Movies': ["The Secret Life of Walter Mitty", "La La Land", "Up"],
            'Precautions': ["Share your joy with friends and family", "Reflect on positive moments", "Practice gratitude"],
            'Songs': ["Happy - by Pharrell Williams" , "Don't Stop Believin - by Journey", "Good Vibrations - by The Beach Boys"],
            'Comics': ["Calvin and Hobbes", "Garfield", "Adventure Time comics"],
        },
        'Sad': {
            'Movies': ["The Fault in Our Stars", "Eternal Sunshine of the Spotless Mind", "A Walk to Remember"],
            'Precautions': ["Reach out to friends or a support system", "Allow yourself to grieve and express emotions", "Engage in activities that bring comfort"],
            'Songs': ["Someone Like You - by Adele", "Hallelujah - by Jeff Buckley", "Fix You - by Coldplay"],
            'Comics': ["Sad Sack", "Persepolis", "Blankets - by Craig Thompson"],
        },
        'Surprise': {
            'Movies': ["The Sixth Sense", "Inception", "The Prestige"],
            'Precautions': ["Embrace the unexpected with an open mind", "Try new activities or experiences", "Stay curious and adventurous"],
            'Songs': ["Thriller - by Michael Jackson", "Bohemian Rhapsody - by Queen", "Don't Stop Me Now - by Queen"],
            'Comics': ["The Twilight Zone comics", "Sandman - by Neil Gaiman", "Black Mirror comics"],
        },
    }

    return recommendations_dict.get(emotion, recommendations_dict.get('Default'))

# Get recommendations based on the predicted emotion
recommendations = recommend_activities(emotion)

# Generate HTML content
# html_content = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Emotion Recommendations:</title>
# </head>
# <body>
#     <h1>Emotion Recommendations</h1>
#     <h2>Emotion: {}</h2>
#     <h3>Recommendations:</h3>
#     <ul>
#         <li><h3>Movie: </h3>{}</li>
#         <br>
#         <li><h3>Precautions: </h3>{}</li>
#         <br>
#         <li><h3>Songs: </h3>{}</li>
#         <br>
#         <li><h3>Comics: </h3>{}</li>
#     </ul>
# </body>
# </html>
# """.format(emotion, "\n".join("<li>{}</li>".format(rec) for rec in recommendations['Movies']),
#            "\n".join("<li>{}</li>".format(rec) for rec in recommendations['Precautions']),
#            "\n".join("<li>{}</li>".format(rec) for rec in recommendations['Songs']),
#            "\n".join("<li>{}</li>".format(rec) for rec in recommendations['Comics']))

# # Save HTML content to a file
# with open("recommendations.html", "w") as html_file:
#     html_file.write(html_content)

# print("HTML file 'recommendations.html' created.")

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Emotion Recommendations:</title>
</head>
<body>
    <h1>Emotion Recommendations</h1>
    <h2>Emotion: {}</h2>
    <h3>Recommendations:</h3>
        <h3>Movie: </h3>{}
        <br>
        <h3>Precautions: </h3>{}
        <br>
        <h3>Songs: </h3>{}
        <br>
        <h3>Comics: </h3>{}
    </ul>
</body>
</html>
""".format(emotion, "\n".join("<li>{}</li>".format(rec) for rec in recommendations['Movies']),
           "\n".join("<li>{}</li>".format(rec) for rec in recommendations['Precautions']),
           "\n".join("<li>{}</li>".format(rec) for rec in recommendations['Songs']),
           "\n".join("<li>{}</li>".format(rec) for rec in recommendations['Comics']))

# Save HTML content to a file
with open("recommendations.html", "w") as html_file:
    html_file.write(html_content)

print("HTML file 'recommendations.html' created.")
