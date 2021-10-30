"""
This  file contains the main "mountains" dictionary, and also a
simple function used to output a string depending on difficulty rating
of each particular mountain to hike.
"""

def difficulty_check(intensity):
    if intensity == 1:
        return "A walk in the park"
    elif intensity == 2:
        return "For the weekend warriors"
    elif intensity == 3:
        return "Pack the aleve and the knee braces!"
    elif intensity == 4:
        return "You'll be paying for it!"

mountains = [
    {
        'name':'mount adams',
        'elevation':'5,774',
        'prominence':'804',
        "difficulty": difficulty_check(4)
    },
    {
        'name':'mount bond',
        'elevation':'4,698',
        'prominence':'299',
        'difficulty':difficulty_check(4)
    },
    {
        'name':'Bondcliff',
        'elevation':'4,265',
        'prominence':'299',
        'difficulty': difficulty_check(3)
    },
    {
        'name':'west bond',
        'elevation':'4,610',
        'prominence':'299',
        'difficulty':difficulty_check(3)
    },
    {
        'name':'mount cabot',
        'elevation':'4,170',
        'prominence':'2,674',
        'difficulty': difficulty_check(2)
    },
    {
        'name':'cannon mountain',
        'elevation':'4,100',
        'prominence':'740',
        'difficulty':difficulty_check(2)
    },
    {
        'name':'mount carrigain',
        'elevation':'4,700',
        'prominence':'2,240',
        "difficulty": difficulty_check(2)
    },
    {
        'name':'carter dome',
        'elevation':'4,832',
        'prominence':'2,830',
        'difficulty':difficulty_check(3)
    },
    {
        'name':'middle carter',
        'elevation':'4,610',
        'prominence':'720',
        'difficulty': difficulty_check(3)
    },
    {
        'name':'south carter',
        'elevation':'4,430',
        'prominence':'230',
        'difficulty':difficulty_check(3)
    },
    {
        'name':'mount eisenhower',
        'elevation':'4,780',
        'prominence':'350',
        'difficulty': difficulty_check(3)
    },
    {
        'name':'mount field',
        'elevation':'4,331',
        'prominence':'1,706',
        'difficulty':difficulty_check(2)
    }
]