# Basic Search Engine

Overview

This project involves building a simplified document search engine, similar in concept to major search engines like Google, Bing, and Yahoo. The search engine will be able to efficiently find web pages matching user queries, providing a foundation for understanding the underlying technology used in modern search engines.

Objectives

- Tokenization: Develop the ability to process text data and split it into individual words.
- Creating Forward and Inverted Index: Create data structures to map words in web page content to their respective URLs, enabling efficient search functionality.
- Search Engine Basics: Implement the fundamental components of a search engine, such as query processing.
- Practice Developing High-Performance Solutions: Build a search engine capable of fast response times.
- Theoretical and Empirical Complexity Analysis: Understand and analyze the computational and storage complexities, both theoretically and empirically.

Problem Specification

The project consists of several key tasks, including:

1. Tokenizing web page content to extract words.
2. Constructing a forward index that maps URLs to unique words in each page.
3. Building an inverted index, which maps words to the URLs of web pages containing those words.
4. Implementing a search function capable of handling single and compound queries.
5. Developing a console program for user interaction.

The search engine will support simple queries with optional modifiers (e.g., + for intersection, - for exclusion), providing search results quickly and efficiently.

Project Structure

- cleanToken(): A helper function to process and clean tokens, ensuring consistency and improving search effectiveness.
- readDocs(): Reads and processes a database file, building a forward index mapping URLs to unique words on each page.
- buildInvertedIndex(): Constructs the inverted index, mapping words to the URLs of pages where they appear.
- findQueryMatches(): Processes user queries and retrieves matching URLs based on the inverted index.
- mySearchEngine(): A console program that uses the above functions to build and interact with the search engine.

The project encourages a structured code approach, breaking tasks into smaller, manageable functions for better code organization and maintainability.

Usage

1. Run `mySearchEngine("sampleWebsiteData.txt")` to build the search engine and start the interactive console.
2. Enter search queries, including single and compound queries with optional modifiers.
3. Retrieve and display matching web page URLs.
4. Continue querying until you enter an empty string to exit the program.

The search engine is case-insensitive for queries.

Note

This project is an educational exercise to gain insights into search engine technology and is not meant to replicate the complexity of real-world search engines.

For detailed implementation and testing, please refer to the project code and documentation.

References
• Inverted Index on GeeksForGeeks
• Wikipedia article on Inverted Indexes
• Stanford Natural Processing Group on Tokenization
