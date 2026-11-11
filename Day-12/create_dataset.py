import os

dataset = {
    "Python": [
        "Python is a high-level programming language used for software development.",
        "Python supports object-oriented programming and functional programming.",
        "Python variables store values such as integers, strings and Boolean data.",
        "Python lists store multiple items in an ordered collection.",
        "Python tuples are ordered collections that cannot be modified.",
        "Python dictionaries store data using key-value pairs.",
        "Python sets store unique elements without duplicates.",
        "Python functions help organize reusable blocks of code.",
        "Python classes are used to create objects.",
        "Python exception handling uses try and except blocks.",
        "Python supports file handling to read and write files.",
        "Python modules allow developers to organize reusable code.",
        "Python loops include for loops and while loops.",
        "Python conditional statements include if, elif and else.",
        "Python is widely used in artificial intelligence and data science."
    ],
    "NumPy": [
        "NumPy is a Python library for numerical and scientific computing.",
        "NumPy provides multidimensional array objects.",
        "NumPy arrays usually perform numerical operations faster than Python lists.",
        "The NumPy array is commonly created using the array function.",
        "NumPy supports mathematical operations on arrays.",
        "NumPy provides functions for matrix multiplication.",
        "NumPy supports linear algebra operations.",
        "NumPy can generate arrays containing random numbers.",
        "NumPy provides functions to calculate mean and median.",
        "NumPy supports reshaping arrays into different dimensions.",
        "NumPy slicing selects specific elements from arrays.",
        "NumPy broadcasting allows operations between compatible arrays.",
        "NumPy can calculate standard deviation.",
        "NumPy supports sorting and searching array elements.",
        "NumPy is commonly used in machine learning projects."
    ],
    "Pandas": [
        "Pandas is a Python library used for data analysis.",
        "Pandas provides Series and DataFrame data structures.",
        "A DataFrame stores information in rows and columns.",
        "A Series represents a one-dimensional labelled data structure.",
        "Pandas can read CSV files.",
        "Pandas can read Excel files.",
        "Pandas supports data cleaning and data manipulation.",
        "Pandas can identify missing values in datasets.",
        "The fillna function can replace missing values.",
        "The dropna function can remove missing values.",
        "Pandas supports filtering rows using conditions.",
        "Pandas can group data using the groupby function.",
        "Pandas supports merging multiple DataFrames.",
        "Pandas can sort data using column values.",
        "Pandas is widely used in data science."
    ],
    "Machine_Learning": [
        "Machine Learning is a branch of artificial intelligence.",
        "Machine Learning allows computers to learn patterns from data.",
        "Supervised learning uses labelled training data.",
        "Unsupervised learning finds patterns in unlabelled data.",
        "Reinforcement learning uses rewards and penalties.",
        "Classification predicts categories or class labels.",
        "Regression predicts continuous numerical values.",
        "Training data is used to build machine learning models.",
        "Testing data evaluates model performance.",
        "Overfitting occurs when a model learns training data too closely.",
        "Underfitting occurs when a model fails to learn important patterns.",
        "Decision trees are used for classification and regression.",
        "Random forests combine multiple decision trees.",
        "Linear regression predicts numerical values.",
        "Accuracy measures the proportion of correct predictions."
    ],
    "Deep_Learning": [
        "Deep Learning is a subset of Machine Learning.",
        "Deep Learning uses artificial neural networks.",
        "Neural networks are inspired by the human brain.",
        "Deep Learning models learn from large amounts of data.",
        "Convolutional Neural Networks are commonly used for image recognition.",
        "Recurrent Neural Networks process sequential information.",
        "Transformers are widely used in natural language processing.",
        "Deep Learning is used in speech recognition.",
        "Computer vision uses Deep Learning to analyse images.",
        "An artificial neuron receives inputs and produces an output.",
        "Activation functions introduce non-linearity into neural networks.",
        "Backpropagation helps train neural network models.",
        "Gradient descent updates model parameters during training.",
        "Deep Learning requires computational resources.",
        "Large datasets can improve Deep Learning performance."
    ],
    "Company_Policies": [
        "Employees must follow company rules and regulations.",
        "Company information must be kept confidential.",
        "Employees should use company equipment responsibly.",
        "Employees must protect passwords and login credentials.",
        "Personal data must be handled securely.",
        "Employees should report security incidents immediately.",
        "Employees must follow the attendance policy.",
        "Unauthorized sharing of company documents is prohibited.",
        "Employees should communicate professionally.",
        "Company resources should be used for authorized purposes.",
        "Employees must follow workplace safety guidelines.",
        "Visitors must follow company security procedures.",
        "Employees should respect the privacy of colleagues.",
        "Important company records must be stored securely.",
        "Employees should follow approved data protection procedures."
    ],
    "Training_Information": [
        "The company provides training programs for new employees.",
        "Technical training helps employees improve programming skills.",
        "Python is included in software development training.",
        "Employees can attend workshops and practical sessions.",
        "Training materials are available for learning and revision.",
        "Employees should complete assigned training activities.",
        "Regular assessments evaluate learning progress.",
        "Team members are encouraged to share knowledge.",
        "Software training includes practical coding exercises.",
        "Data science training introduces data analysis concepts.",
        "Machine Learning training covers model development.",
        "Employees can learn through online training sessions.",
        "Training attendance should be recorded.",
        "Mentors help trainees understand technical concepts.",
        "Training feedback helps improve future learning programs."
    ]
}

count = 0

for category, documents in dataset.items():
    folder = os.path.join(os.path.dirname(__file__), "dataset", category)
    os.makedirs(folder, exist_ok=True)

    for index, content in enumerate(documents, start=1):
        filename = f"{category.lower()}_{index:02d}.txt"
        file_path = os.path.join(folder, filename)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        count += 1

print(f"Successfully created {count} documents!")