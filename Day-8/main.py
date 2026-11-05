import numpy as np
import matplotlib.pyplot as plt

# Create Words adn Their Vectors
word_vectors = {
    "Apple": np.array([2,3]),
    "Dog": np.array([3,4]),
    "Car": np.array([9,1]),
    "Computer": np.array([8,2]),
    "Football": np.array([5,7])
}

# Display Words and Their Vectors
for word,vector in word_vectors.items():
    print("Word:", word)
    print("Vector:", vector)
    print("----------------")

# Display Vector Dimensions
for word, vector in word_vectors.items():
    print(word, "Dimensions:", len(vector))

# Compare Two Vectours
vector1 = word_vectors["Apple"]
vector2= word_vectors["Dog"]
print("Apple Vector:", vector1 )
print("Dog Vector:", vector2)
print("Are both vector equal?", np.array_equal(vector1,vector2))

# Calculate Euclidean Distance
distance = np.linalg.norm(vector1 - vector2)
print("Distance between Apple and Dog:", distance)

# Find Closest Words
words = list(word_vectors.keys())
minimum_distance = float("inf")
closest_word = ()
for i in range(len(word)):
     for j in range( i+1, len(words)):
         word1 = words[i]
         word2 = words[j]
         distance = np.linalg.norm(
              word_vectors[word1] - word_vectors[word2]   
         )
         if distance < minimum_distance:
             minimum_distance = distance
             closest_word = (word1, word2)
print("Closest Words:", closest_word)
print("Minimum Distance:", minimum_distance)

# Visualize Word Vectors
for word, vector in word_vectors.items():
    plt.scatter(vector[0], vector[1])
    plt.text(vector[0] + 0.1, vector[1] + 0.1, word)
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.title("Text-to-Vector Explorer")
plt.grid(True)
plt.show()      
            
    