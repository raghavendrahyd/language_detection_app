## Language detection app

Developed a simple web app which classifies/predicts the language of a text input.

- Used randomForest classifier to train on a dataset with various languages ('English', 'Malayalam', 'Hindi', 'Tamil', 'Portugeese', 'French','Dutch', 'Spanish', 'Greek', 'Russian', 'Danish', 'Italian','Turkish', 'Sweedish', 'Arabic', 'German', 'Kannada'). Model building work can be found in notebooks/
- Used FastAPI for the API development
- Containerized through docker
- Deployed on Heroku 