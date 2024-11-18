# Social Media Analysis Assignment

## Introduction

This project analyzes social media data to identify clusters of content, users, and directional trends using efficient data structures and algorithms. The document explains the approach and provides code implementations for the described algorithms.

---

## Data Representation

### Data Structure Choices

1. **Graph Representation**
   - **Nodes:** Represent users and posts.
   - **Edges:** Represent relationships like authorship, viewing, and connections.
   - **Implementation:** Adjacency list for efficient memory usage and traversal.

2. **Hash Tables**
   - Map user names to user objects (`username -> user object`).
   - Map post IDs to post objects (`post ID -> post object`).

3. **Priority Queues**
   - Used for trending post detection, sorted by attention gain rate.

4. **Word Frequency Map**
   - Efficient calculation of word frequencies for analysis and visualization.

---

## Algorithms

### Highlight Important Posts in a Graph

- **Description:**  
  Identify and highlight posts with high importance based on criteria like views and comments. 
- **Approach:**  
  1. Calculate importance using the formula: `importance = views + 2 * comments`.
  2. Represent the data as a graph with users and posts as nodes.
  3. Visualize important posts with distinct attributes (e.g., color, size).

---

### Highlight Interesting Users

- **Description:**  
  Identify users who meet criteria for "interestingness" based on attributes like the number of posts or reading level.
- **Approach:**  
  1. Compute a score for each user using their attributes.
  2. Filter and rank users dynamically based on the scores.
  3. Visualize interesting users in the graph using attributes like node size or color.

---

### Generate a Word Cloud

- **Description:**  
  Create a word cloud to visualize word frequencies in posts.
- **Approach:**  
  1. Parse selected posts and count word frequencies using a dictionary.
  2. Use a word cloud library (e.g., `WordCloud`) to generate and display the visualization.

---

### Identify Trending Posts

- **Description:**  
  Track posts gaining popularity based on views and comments over time.
- **Approach:**  
  1. Calculate attention rate: `(new views + new comments) / time period`.
  2. Use a max-heap (priority queue) to track and rank top trending posts.
  3. Optionally filter posts based on specific keywords or attributes.

---

### Handle Quoted or Referred Posts

- **Description:**  
  Extend the graph representation to include quoted or referred relationships as additional edges.
- **Approach:**  
  Dynamically include/exclude referred posts during analysis based on user-defined requirements.

---

## Code Files
- **`graph_analysis.py`**: Contains the implementation for graph representation and analysis of important posts.
- **`interesting_users.py`**: Highlights interesting users based on selected criteria.
- **`word_cloud.py`**: Generates word clouds from post data.
- **`trending_posts.py`**: Identifies trending posts using a priority queue.

## Libraries and Resources

- **NetworkX:** [https://networkx.org/](https://networkx.org/)
- **WordCloud Library:** [https://github.com/amueller/word_cloud](https://github.com/amueller/word_cloud)
- **Python Documentation:** [https://docs.python.org/](https://docs.python.org/)

---
