def get_recommendation(subject, level):

    recommendations = {

        "Python": {
            "Beginner": [
                "Variables",
                "Data Types",
                "Loops",
                "Functions",
                "Lists"
            ],
            "Intermediate": [
                "OOP",
                "File Handling",
                "Modules",
                "Exception Handling",
                "Projects"
            ],
            "Advanced": [
                "Flask",
                "Django",
                "APIs",
                "Machine Learning",
                "Deployment"
            ]
        },

        "DBMS": {
            "Beginner": [
                "Database Basics",
                "ER Diagram",
                "SQL Basics"
            ],
            "Intermediate": [
                "Joins",
                "Normalization",
                "Views"
            ],
            "Advanced": [
                "Stored Procedures",
                "Triggers",
                "Transactions"
            ]
        }

    }

    return recommendations.get(subject, {}).get(level, ["No recommendation available"])