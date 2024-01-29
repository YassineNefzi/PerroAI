# PerroAI

## Overview
PerroAI is a chatbot application designed to assist children with speech difficulties using the Mistral Large Language Model (LLM). The project provides two main endpoints: `/talk` for interactive chatbot sessions focusing on pronunciation and various speech exercises, and `/retrieve_from_pdf` for extracting information from PDF documents to aid in speech therapy.

## Features
- **/talk Endpoint:**
  - Engage in interactive conversations with the chatbot.
  - Pronunciation exercises to help children improve speech clarity.
  - Additional exercises and encouragement to support speech development.

- **/retrieve_from_pdf Endpoint:**
  - Utilize Mistral LLM to extract relevant information from provided PDF documents.
  - Facilitates efficient retrieval of data for personalized speech therapy.

- **Docker Integration:**
  - The project is containerized using Docker for easy deployment and scalability.
  - Simplified setup, ensuring consistency across different environments.

## Getting Started

### Prerequisites
- Docker installed on your machine.

### Installation and Deployment
1. Clone the repository:
   ```bash
   git clone https://github.com/YassineNefzi/PerroAI.git
   cd PerroAI
2. Build and run the Docker container:
  ```bash
  docker build -t perro-app .
  docker run -p 8080:8080 perro-app
  ```
3. Access the application:
  Chatbot endpoint: http://localhost:8080/talk
  PDF retrieval endpoint: http://localhost:8080/retrieve_from_pdf

## Usage
Open your preferred web browser and navigate to the provided endpoints.
Interact with the chatbot by accessing the /talk endpoint.
Upload PDF documents to the /retrieve_from_pdf endpoint to extract information.

## Contact
For any inquiries or support, please contact ynyassine7@gmail.com.


